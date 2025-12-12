---
title: "Inchworm Foldable Robotics"

excerpt: 
    "Oct 2025 – Dec 2025<br/>  
    Driven by the principles of foldable robotics, this compact inchworm robot demonstrates how far creativity, clever mechanisms, and a single sheet of material can go.
    <br/>
    <img src= 'https://inchworm-foldable-robotics.github.io/assets/01_Home/Inch_Worm.jpg'>"
    

collection: portfolio
---

<br/>


Check the website [here](https://inchworm-foldable-robotics.github.io/)

<br/>

# ArcFold 


<video width="700" controls>
  <source src="https://raw.githubusercontent.com/Inchworm-Foldable-Robotics/Inchworm-Foldable-Robotics.github.io/master/assets/04_Results/P4_Inchworm_Good.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

ArcFold is an inchworm‑inspired crawling robot based on the locomotion of [Manduca sexta larvae](https://en.wikipedia.org/wiki/Manduca_sexta). The robot uses rigid foldable linkages and friction‑modulated pads to realize a planar, two‑anchor lift‑and‑drag gait whose parameters can be modeled, fabricated, and systematically varied.  


The project team consists of:

- [Sai Srinivas Tatwik Meesala](https://tatwik19.github.io/)
- [Colin Fricke](https://www.linkedin.com/in/colin-fricke)
- Nathan Vairora  

## Simulation in MuJoCo

<img src= 'https://inchworm-foldable-robotics.github.io/assets/04_Results/inchworm_crawlP4.gif'>"



## Biological Inspiration

The primary biological inspiration is the Manduca sexta larva, a geometrid inchworm‑type crawler that uses a characteristic two‑anchor looping gait. Posterior prolegs anchor while the anterior body arches and extends; then the anterior prolegs anchor while the posterior body is pulled forward, generating large stride‑to‑body‑length ratios with relatively simple control [1]. Manduca’s crawling is driven by friction modulation between “anchored” and “sliding” contacts and by controlled body curvature rather than by discrete legs or wheels [1], [2].  

Biomechanics studies provide quantitative targets for the robot’s kinematics and contact conditions. Manduca exhibits nearly orientation‑invariant proleg timing, stride periods on the order of 2–3 s, and stride lengths of roughly 0.3–0.5 body lengths [1]. Multi‑contact ground‑reaction measurements show that anterior prolegs generate forward thrust while posterior prolegs often serve as high‑friction anchors, with effective friction ratios between anchored and sliding states of approximately 3:1 [2]. Beam‑bending models of inchworm locomotion relate curvature, arc length, and forward displacement, constraining the lift height and deformation envelope that the mechanical analog should reproduce [3].  

These insights motivate a foldable, rigid‑link crawler with two friction‑modulated pads and a controllable arching motion: a mechanism that abstracts the biological gait while remaining compatible with laminated fabrication and dynamic simulation.  




## References

Numbers correspond to the references used in the Assignment 1 report; full bibliographic details are provided there. 

[1] N. P. L. Griethuijsen and B. A. Trimmer, “Crawling kinematics of Manduca sexta larvae on horizontal and vertical substrates,” *J. Exp. Biol.*, 2009.

[2] H. T. Lin and B. A. Trimmer, “Multi‑contact ground reaction forces of crawling Manduca sexta,” *J. Exp. Biol.*, 2010 (with 2011 corrigendum).

[3] R. H. Plaut, “Large deflection model of inchworm locomotion using a flexible beam,” *Int. J. Non‑Linear Mech.*, 2015.

[4] X. Wang *et al.*, “A mini‑modular climbing caterpillar robot with inchworm‑like gait,” *Prog. Nat. Sci.*, 2009.

[5] Y. Li *et al.*, “An inchworm‑like climbing robot based on cable‑driven grippers,” 2024.

[6] M. Pan *et al.*, “Bio‑inspired soft crawling robots: mechanisms, actuation, and control,” *Adv. Sci.*, 2025.

[7] F. Wu, “Kinematic analysis of a line robot based on inchworm biomimicry,” 2024.  
