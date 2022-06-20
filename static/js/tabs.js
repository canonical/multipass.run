function setupTabs() {
  var tabs = document.querySelectorAll(".js-tab");

  tabs.forEach((tab) => {
    const tabSelector = tab.getAttribute("href");
    const tabContent = document.querySelector(tabSelector);

    if (tabContent) {
      if (tabContent.id !== "tab-one__content") {
        tabContent.classList.add("u-hide");
        tab.setAttribute("aria-selected", "false");
      } else {
        tab.setAttribute("aria-selected", "true");
      }

      tab.addEventListener("click", function (e) {
        e.preventDefault();
        e.stopPropagation();
        toggleTab(e.currentTarget);
      });
    } else {
      console.warn("Tab content does not exist");
    }
  });

  function toggleTab(tab) {
    var tabSelector = tab.getAttribute("href");
    var tabContent = document.querySelector(tabSelector);

    for (var i = 0; i < tabs.length; i += 1) {
      if (tabs[i] !== tab) {
        var otherTabSelector = tabs[i].getAttribute("href");
        var otherTabContent = document.querySelector(otherTabSelector);

        tabs[i].setAttribute("aria-selected", "false");
        tabs[i].classList.remove("active");
        otherTabContent.classList.add("u-hide");
      }
    }

    if (tab.getAttribute("aria-selected") !== "true") {
      tab.setAttribute("aria-selected", "true");
      tab.classList.toggle("active");
      tabContent.classList.toggle("u-hide");
    }

    if (tab.classList.contains("active")) {
      var breakpoint = 620;
      var yOffset = 200;
      var rect = tabContent.getBoundingClientRect();
      var inView = window.innerHeight - yOffset > rect.top;
      var scrollTarget = window.scrollY + yOffset;

      if (window.innerWidth <= breakpoint) {
        scrollTarget = pageYOffset + rect.top - 10;
      }

      if (!inView) {
        window.scroll({
          behavior: "smooth",
          top: scrollTarget,
        });
      }
    }
  }
}

setupTabs();
