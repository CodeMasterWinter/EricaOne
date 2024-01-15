document.addEventListener('DOMContentLoaded', function () {
    var darkLightCheckbox = document.getElementById('dark-light');
    const navLinks = document.getElementsByClassName('nav-link')
    mode = "light";
    
    darkLightCheckbox.addEventListener('change', function () {
        document.body.classList.toggle('dark-mode', darkLightCheckbox.checked);

        if (mode == "light") {
            for (i=0; i<navLinks.length; i++){
                navLinks[i].style.color = '#ffffff';
                navLinks[i].style.fontWeight = '500';
                mode = "dark";
            }
        } 
        else {
            for (i=0; i<navLinks.length; i++){
                navLinks[i].style.color = '#131313';
                navLinks[i].style.fontWeight = '600';
                mode = "light";
            }
        }
    });
});