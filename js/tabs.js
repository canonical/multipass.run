var tabs = document.querySelectorAll('[role="tab"]');
var os = 'linux';
if (navigator.appVersion.indexOf('Win') != -1) { os = 'windows' };
if (navigator.appVersion.indexOf('MacOS') != -1) { os = 'macos' };
if (navigator.appVersion.indexOf('Mac OS') != -1) { os = 'macos' };
if (navigator.appVersion.indexOf('Macintosh') != -1) { os = 'macos' };

// Add a click listener to all tabs
for (var i = 0; i < tabs.length; i++) {
  tabs[i].addEventListener('click', function(e) {
    var control = this.getAttribute("aria-controls");
    toogleHandler(control);
  });
};

function toogleHandler(control) {
  var tabpanels = document.querySelectorAll('[role="tabpanel"]');
  var selectedTab = document.querySelector('[aria-controls="' + control + '"]');
  var selectedPanel = document.getElementById(control);

  // Hide all panels
  for (var i = 0; i < tabpanels.length; i++) {
    tabpanels[i].setAttribute('aria-hidden', 'true');
  }

  // Remove tab highlight
  for (var i = 0; i < tabs.length; i++) {
    tabs[i].setAttribute('aria-selected', 'false');
  }

  // Select the current tab to selected
  selectedTab.setAttribute('aria-selected', 'true');

  // Reveal the assosiated tabpanel
  selectedPanel.setAttribute('aria-hidden', 'false');
}

var hash = window.location.hash;
if (hash) {
  toogleHandler(hash.replace('#', ''));
} else {
  if (os !== 'linux') {
    toogleHandler(`${os}-install`);
  }
}