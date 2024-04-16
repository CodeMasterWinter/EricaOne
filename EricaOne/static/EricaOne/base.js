const DarkLightSwitch = document.getElementById("dark-light-switch");
var imgElement = document.querySelector(".nav-logo-img");
let isDarkMode = false

    DarkLightSwitch.addEventListener("click", function() {
        var elements = document.querySelectorAll("*");
        elements.forEach(function(element) {
            element.classList.toggle("dark-mode");
    });
});