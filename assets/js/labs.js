(function () {
  "use strict";

  function slugify(text) {
    return text
      .toLowerCase()
      .trim()
      .replace(/[^a-z0-9\s-]/g, "")
      .replace(/\s+/g, "-")
      .replace(/-+/g, "-");
  }

  function buildLabToc() {
    var content = document.querySelector("[data-lab-content]");
    var list = document.querySelector("[data-lab-toc-list]");
    var toc = document.querySelector("[data-lab-toc]");

    if (!content || !list || !toc) return;

    var headings = Array.prototype.slice.call(content.querySelectorAll("h1, h2, h3"));
    var usedIds = {};

    headings.forEach(function (heading) {
      var id = heading.id || slugify(heading.textContent);
      var baseId = id || "section";
      var suffix = 2;

      var existingHeading = document.getElementById(id);
      while (usedIds[id] || (existingHeading && existingHeading !== heading)) {
        id = baseId + "-" + suffix;
        suffix += 1;
        existingHeading = document.getElementById(id);
      }

      heading.id = id;
      usedIds[id] = true;

      var item = document.createElement("li");
      item.className = "lab-toc__item lab-toc__item--" + heading.tagName.toLowerCase();
      var link = document.createElement("a");
      link.href = "#" + id;
      link.textContent = heading.textContent;
      item.appendChild(link);
      list.appendChild(item);
    });

    if (!headings.length) {
      toc.hidden = true;
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", buildLabToc);
  } else {
    buildLabToc();
  }
}());
