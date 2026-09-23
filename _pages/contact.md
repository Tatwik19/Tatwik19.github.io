---
layout: archive
title: Contact Me
description: "Contact Tatwik Meesala about robotics, research, teaching, and collaboration."
permalink: /contact/
author_profile: false
contact_page: true
---

<div class="contact-intro">
  <h2>Let's connect</h2>
  <p>Send me a message about robotics, research, teaching, or collaboration.</p>

  <nav class="contact-links" aria-label="Professional profiles">
    <a class="contact-link contact-link--linkedin" href="https://www.linkedin.com/in/Sai-Srinivas-Tatwik-Meesala" target="_blank" rel="noopener noreferrer">
      <i class="fab fa-linkedin-in" aria-hidden="true"></i>
      <span>LinkedIn</span>
    </a>
    <a class="contact-link contact-link--github" href="https://github.com/Tatwik19" target="_blank" rel="noopener noreferrer">
      <i class="fab fa-github" aria-hidden="true"></i>
      <span>GitHub</span>
    </a>
    <a class="contact-link contact-link--orcid" href="https://orcid.org/0009-0008-4787-9741" target="_blank" rel="noopener noreferrer">
      <i class="fab fa-orcid" aria-hidden="true"></i>
      <span>ORCID</span>
    </a>
  </nav>
</div>

<section class="contact-form-card" aria-labelledby="contact-form-title">
  <h2 id="contact-form-title">Send a message</h2>

  <form class="contact-form" action="https://formspree.io/f/xeoebqlb" method="POST">
    <div class="contact-form__row">
      <div class="contact-field">
        <label for="contact-name">Name</label>
        <input type="text" id="contact-name" name="name" autocomplete="name" placeholder="Your name" required>
      </div>

      <div class="contact-field">
        <label for="contact-email">Email</label>
        <input type="email" id="contact-email" name="email" autocomplete="email" inputmode="email" placeholder="you@example.com" required>
      </div>
    </div>

    <div class="contact-field">
      <label for="contact-topic">Topic</label>
      <select id="contact-topic" name="topic" required>
        <option value="" selected disabled>Select a topic</option>
        <option value="Research collaboration">Research collaboration</option>
        <option value="Robotics or engineering project">Robotics or engineering project</option>
        <option value="Teaching or laboratory material">Teaching or laboratory material</option>
        <option value="Speaking or mentoring">Speaking or mentoring</option>
        <option value="Other">Other</option>
      </select>
    </div>

    <div class="contact-field">
      <label for="contact-message">Message</label>
      <textarea id="contact-message" name="message" rows="7" maxlength="3000" placeholder="How can I help?" required></textarea>
    </div>

    <input type="hidden" name="_subject" value="New message from tatwik19.github.io">
    <div class="contact-honeypot" aria-hidden="true">
      <label for="contact-company">Leave this field empty</label>
      <input type="text" id="contact-company" name="_gotcha" tabindex="-1" autocomplete="off">
    </div>

    <button type="submit" class="contact-submit">
      Send message <i class="fas fa-paper-plane" aria-hidden="true"></i>
    </button>
  </form>
</section>
