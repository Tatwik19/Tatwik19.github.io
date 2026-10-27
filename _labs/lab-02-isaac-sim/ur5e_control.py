"""Simple UR5e control functions for the Isaac Sim Script Editor.

Use this file only while Isaac Sim is open. The stage must contain:

    /World/ur5e
    /World/ur5e/base_link
    /World/ur5e/wrist_3_link/flange

The flange must have Robot Site API applied and must be included in the
UR5e Robot Links list.

Available operations:

1. move_joints(...)       - Move using absolute joint angles in degrees.
2. move_tcp_to(...)       - Move TCP to an absolute XYZ position in meters.
3. move_tcp_delta(...)    - Move TCP by delta X, Y and Z in meters.
4. rotate_tcp(...)        - Set the TCP roll, pitch and yaw in degrees.
5. get_robot_status()     - Read current robot, joint and TCP information.

This file uses inverse kinematics for TCP commands. It does not perform
collision-aware motion planning or guarantee a straight Cartesian path.
"""

import numpy as np
import omni.timeline
import omni.usd

from pxr import Usd, UsdGeom

from isaacsim.core.experimental.prims import Articulation
from isaacsim.core.experimental.utils import transform as transform_utils
from isaacsim.robot.poser import RobotPoser, Transform, validate_robot_schema


class UR5eController:
    """Simple controller for the UR5e already present on the open stage."""

    def __init__(self):
        self.robot_path = "/World/ur5e"
        self.base_path = "/World/ur5e/base_link"
        self.tcp_path = "/World/ur5e/wrist_3_link/flange"

        self.stage = omni.usd.get_context().get_stage()

        self.robot_prim = self.stage.GetPrimAtPath(self.robot_path)
        self.base_prim = self.stage.GetPrimAtPath(self.base_path)
        self.tcp_prim = self.stage.GetPrimAtPath(self.tcp_path)

        if not self.robot_prim.IsValid():
            raise RuntimeError(f"Robot not found: {self.robot_path}")
        if not self.base_prim.IsValid():
            raise RuntimeError(f"Base link not found: {self.base_path}")
        if not self.tcp_prim.IsValid():
            raise RuntimeError(f"TCP not found: {self.tcp_path}")
        if not validate_robot_schema(self.robot_prim):
            raise RuntimeError("The UR5e does not have a valid Robot Schema.")

        self.articulation = Articulation(self.robot_path)
        self.poser = RobotPoser(
            self.stage,
            self.robot_prim,
            self.base_prim,
            self.tcp_prim,
        )

    def move_joints(self, joint_angles_degrees):
        """Move to absolute joint angles in degrees.

        Supply either six angles in the robot DOF order:

            robot.move_joints([0, -30, 30, -20, 10, 0])

        or selected joints by name:

            robot.move_joints({"shoulder_pan_joint": 15,
                               "elbow_joint": 30})

        Joints omitted from a dictionary remain at their current positions.
        """
        joint_names = list(self.articulation.dof_names)
        current_angles = np.asarray(
            self.articulation.get_dof_positions().numpy(),
            dtype=np.float64,
        ).reshape(-1)

        if isinstance(joint_angles_degrees, dict):
            target_angles = current_angles.copy()

            for joint_name, angle_degrees in joint_angles_degrees.items():
                if joint_name not in joint_names:
                    raise ValueError(f"Unknown joint name: {joint_name}")

                joint_index = joint_names.index(joint_name)
                target_angles[joint_index] = np.radians(angle_degrees)
        else:
            if len(joint_angles_degrees) != len(joint_names):
                raise ValueError(
                    f"Expected {len(joint_names)} angles in this order: "
                    f"{joint_names}"
                )

            target_angles = np.radians(
                np.asarray(joint_angles_degrees, dtype=np.float64)
            )

        self.articulation.set_dof_position_targets(target_angles)

        return {
            "applied": True,
            "joint_order": joint_names,
            "target_angles_degrees": {
                name: float(angle)
                for name, angle in zip(joint_names, np.degrees(target_angles))
            },
        }

    def move_tcp_to(self, x, y, z):
        """Move the TCP to absolute XYZ coordinates in the robot frame.

        X, Y and Z are in meters. The current TCP rotation is preserved.
        """
        transform_cache = UsdGeom.XformCache(Usd.TimeCode.Default())
        tcp_transform, _ = transform_cache.ComputeRelativeTransform(
            self.tcp_prim,
            self.robot_prim,
        )

        current_rotation = tcp_transform.ExtractRotationQuat()
        imaginary = current_rotation.GetImaginary()
        current_rotation = np.array(
            [
                current_rotation.GetReal(),
                imaginary[0],
                imaginary[1],
                imaginary[2],
            ],
            dtype=np.float64,
        )

        target_position = np.array([x, y, z], dtype=np.float64)
        target = Transform(t=target_position, q=current_rotation)
        result = self.poser.solve_ik(target)

        if result.success:
            self.poser.apply_pose(result)

        return {
            "success": bool(result.success),
            "target_position_m": target_position.tolist(),
        }

    def move_tcp_delta(self, delta_x=0.0, delta_y=0.0, delta_z=0.0):
        """Move the TCP by delta X, Y and Z in the robot frame.

        Delta values are in meters. The current TCP rotation is preserved.
        """
        transform_cache = UsdGeom.XformCache(Usd.TimeCode.Default())
        tcp_transform, _ = transform_cache.ComputeRelativeTransform(
            self.tcp_prim,
            self.robot_prim,
        )

        current_position = tcp_transform.ExtractTranslation()
        target_position = np.array(
            [
                current_position[0] + delta_x,
                current_position[1] + delta_y,
                current_position[2] + delta_z,
            ],
            dtype=np.float64,
        )

        current_rotation = tcp_transform.ExtractRotationQuat()
        imaginary = current_rotation.GetImaginary()
        current_rotation = np.array(
            [
                current_rotation.GetReal(),
                imaginary[0],
                imaginary[1],
                imaginary[2],
            ],
            dtype=np.float64,
        )

        target = Transform(t=target_position, q=current_rotation)
        result = self.poser.solve_ik(target)

        if result.success:
            self.poser.apply_pose(result)

        return {
            "success": bool(result.success),
            "delta_m": [delta_x, delta_y, delta_z],
            "target_position_m": target_position.tolist(),
        }

    def rotate_tcp(self, roll_x, pitch_y, yaw_z):
        """Set the absolute TCP rotation while preserving its position.

        Rotation is supplied in degrees as roll X, pitch Y and yaw Z.
        """
        transform_cache = UsdGeom.XformCache(Usd.TimeCode.Default())
        tcp_transform, _ = transform_cache.ComputeRelativeTransform(
            self.tcp_prim,
            self.robot_prim,
        )

        current_position = tcp_transform.ExtractTranslation()
        target_position = np.array(
            [current_position[0], current_position[1], current_position[2]],
            dtype=np.float64,
        )

        target_rotation = transform_utils.euler_angles_to_quaternion(
            [roll_x, pitch_y, yaw_z],
            degrees=True,
            extrinsic=True,
        ).numpy().reshape(-1)

        target = Transform(t=target_position, q=target_rotation)
        result = self.poser.solve_ik(target)

        if result.success:
            self.poser.apply_pose(result)

        return {
            "success": bool(result.success),
            "target_rotation_degrees": [roll_x, pitch_y, yaw_z],
        }

    def get_robot_status(self):
        """Return the current joint positions and TCP pose."""
        joint_names = list(self.articulation.dof_names)
        joint_positions = np.asarray(
            self.articulation.get_dof_positions().numpy(),
            dtype=np.float64,
        ).reshape(-1)
        joint_velocities = np.asarray(
            self.articulation.get_dof_velocities().numpy(),
            dtype=np.float64,
        ).reshape(-1)

        transform_cache = UsdGeom.XformCache(Usd.TimeCode.Default())
        tcp_transform, _ = transform_cache.ComputeRelativeTransform(
            self.tcp_prim,
            self.robot_prim,
        )

        tcp_position = tcp_transform.ExtractTranslation()
        tcp_rotation = tcp_transform.ExtractRotationQuat()
        imaginary = tcp_rotation.GetImaginary()
        tcp_rotation = np.array(
            [
                tcp_rotation.GetReal(),
                imaginary[0],
                imaginary[1],
                imaginary[2],
            ],
            dtype=np.float64,
        )

        tcp_euler_degrees = transform_utils.quaternion_to_euler_angles(
            tcp_rotation,
            degrees=True,
            extrinsic=True,
        ).numpy().reshape(-1)

        timeline = omni.timeline.get_timeline_interface()

        return {
            "robot_path": self.robot_path,
            "base_path": self.base_path,
            "tcp_path": self.tcp_path,
            "timeline_playing": bool(timeline.is_playing()),
            "joint_names": joint_names,
            "joint_positions_degrees": {
                name: float(angle)
                for name, angle in zip(joint_names, np.degrees(joint_positions))
            },
            "joint_velocities_radians_per_second": {
                name: float(velocity)
                for name, velocity in zip(joint_names, joint_velocities)
            },
            "tcp_position_m": [
                float(tcp_position[0]),
                float(tcp_position[1]),
                float(tcp_position[2]),
            ],
            "tcp_rotation_degrees": {
                "roll_x": float(tcp_euler_degrees[0]),
                "pitch_y": float(tcp_euler_degrees[1]),
                "yaw_z": float(tcp_euler_degrees[2]),
            },
        }
