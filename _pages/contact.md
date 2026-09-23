---
layout: archive
title: Contact Me
description: "Contact Tatwik Meesala about robotics research, engineering projects, teaching, and collaboration."
permalink: /contact/
author_profile: false
contact_page: true
---

<section class="contact-hero" aria-labelledby="contact-intro-title">
  <div class="contact-hero__content">
    <p class="contact-eyebrow"><i class="fas fa-satellite-dish" aria-hidden="true"></i> Hello there</p>
    <h2 id="contact-intro-title">Have an idea worth building?</h2>
    <p>Whether it is a robotics project, research collaboration, teaching opportunity, or simply an interesting technical conversation, I would be happy to hear from you.</p>
    <div class="contact-interests" aria-label="Topics I welcome">
      <span>Robotics research</span>
      <span>Engineering projects</span>
      <span>Teaching</span>
      <span>Collaboration</span>
    </div>
  </div>
  <div class="contact-hero__graphic" aria-hidden="true">
    <div class="contact-orbit contact-orbit--outer"></div>
    <div class="contact-orbit contact-orbit--inner"></div>
    <i class="fas fa-robot"></i>
  </div>
</section>

<div class="contact-layout">
  <aside class="contact-sidebar" aria-labelledby="contact-channels-title">
    <div>
      <p class="contact-section-label">Find me online</p>
      <h2 id="contact-channels-title">Choose a channel</h2>
      <p>For a quick introduction, send the form. For profiles, projects, and professional updates, use one of these links.</p>
    </div>

    <nav class="contact-channels" aria-label="External contact profiles">
      <a class="contact-channel contact-channel--linkedin" href="https://www.linkedin.com/in/Sai-Srinivas-Tatwik-Meesala" target="_blank" rel="noopener noreferrer">
        <span class="contact-channel__icon"><i class="fab fa-linkedin-in" aria-hidden="true"></i></span>
        <span><strong>LinkedIn</strong><small>Professional updates and messages</small></span>
        <i class="fas fa-external-link-alt contact-channel__arrow" aria-hidden="true"></i>
      </a>

      <a class="contact-channel contact-channel--github" href="https://github.com/Tatwik19" target="_blank" rel="noopener noreferrer">
        <span class="contact-channel__icon"><i class="fab fa-github" aria-hidden="true"></i></span>
        <span><strong>GitHub</strong><small>Code, projects, and technical work</small></span>
        <i class="fas fa-external-link-alt contact-channel__arrow" aria-hidden="true"></i>
      </a>

      <a class="contact-channel contact-channel--orcid" href="https://orcid.org/0009-0008-4787-9741" target="_blank" rel="noopener noreferrer">
        <span class="contact-channel__icon"><i class="fab fa-orcid" aria-hidden="true"></i></span>
        <span><strong>ORCID</strong><small>Research identity and scholarly record</small></span>
        <i class="fas fa-external-link-alt contact-channel__arrow" aria-hidden="true"></i>
      </a>
    </nav>

    <div class="contact-note">
      <i class="fas fa-lightbulb" aria-hidden="true"></i>
      <p><strong>A useful first message</strong><br>Tell me what you are working on, where I might help, and the best way to continue the conversation.</p>
    </div>
  </aside>

  <section class="contact-form-card" aria-labelledby="contact-form-title">
    <div class="contact-form-card__header">
      <span class="contact-form-card__icon"><i class="fas fa-paper-plane" aria-hidden="true"></i></span>
      <div>
        <p class="contact-section-label">Start a conversation</p>
        <h2 id="contact-form-title">Send me a message</h2>
        <p>Complete the fields below and your message will be delivered through Formspree.</p>
      </div>
    </div>

    <form class="contact-form" action="https://formspree.io/f/xeoebqlb" method="POST">
      <div class="contact-form__row">
        <div class="contact-field">
          <label for="contact-name">Your name <span aria-hidden="true">*</span></label>
          <div class="contact-control">
            <i class="fas fa-user" aria-hidden="true"></i>
            <input type="text" id="contact-name" name="name" autocomplete="name" placeholder="First and last name" required>
          </div>
        </div>

        <div class="contact-field">
          <label for="contact-email">Email address <span aria-hidden="true">*</span></label>
          <div class="contact-control">
            <i class="fas fa-envelope" aria-hidden="true"></i>
            <input type="email" id="contact-email" name="email" autocomplete="email" inputmode="email" placeholder="you@example.com" required>
          </div>
        </div>
      </div>

      <div class="contact-field">
        <label for="contact-topic">What would you like to discuss? <span aria-hidden="true">*</span></label>
        <div class="contact-control contact-control--select">
          <i class="fas fa-compass" aria-hidden="true"></i>
          <select id="contact-topic" name="topic" required>
            <option value="" selected disabled>Select a topic</option>
            <option value="Research collaboration">Research collaboration</option>
            <option value="Robotics or engineering project">Robotics or engineering project</option>
            <option value="Teaching or laboratory material">Teaching or laboratory material</option>
            <option value="Speaking or mentoring">Speaking or mentoring</option>
            <option value="Other">Something else</option>
          </select>
        </div>
      </div>

      <div class="contact-field">
        <label for="contact-message">Your message <span aria-hidden="true">*</span></label>
        <textarea id="contact-message" name="message" rows="7" maxlength="3000" placeholder="Share a little context, your goal, and how I can help..." required></textarea>
        <small class="contact-field__hint">Please avoid including confidential or sensitive information.</small>
      </div>

      <input type="hidden" name="_subject" value="New message from tatwik19.github.io">
      <div class="contact-honeypot" aria-hidden="true">
        <label for="contact-company">Leave this field empty</label>
        <input type="text" id="contact-company" name="_gotcha" tabindex="-1" autocomplete="off">
      </div>

      <div class="contact-form__footer">
        <button type="submit" class="contact-submit">
          <span>Send message</span>
          <i class="fas fa-arrow-right" aria-hidden="true"></i>
        </button>
        <p><i class="fas fa-lock" aria-hidden="true"></i> Your details are used only to respond to your message.</p>
      </div>
    </form>
  </section>
</div>
