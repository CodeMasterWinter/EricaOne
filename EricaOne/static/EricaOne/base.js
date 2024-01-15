document.addEventListener('DOMContentLoaded', function () {
    var darkLightCheckbox = document.getElementById('dark-light');
    const navLinks = document.getElementsByClassName('nav-link')
    mode = "light";
    const left = document.getElementById('nav-prev')
    const right = document.getElementById('nav-next')
    const boxes = document.getElementsByClassName('nav-item')
    var boxwidth = 18.4;
    var boxpos = 0;

    right.addEventListener('click', () => {
        for (i=0; i < boxes.length; i++) {
            boxes[i].style.transform = `translateX(${boxpos+boxwidth}vw)`;
            console.log("functional");
        }
        boxpos += boxwidth;
    });
    
    left.addEventListener('click', () => {
        for (i=0; i < boxes.length; i++) {
            boxes[i].style.transform = `translateX(${boxpos-boxwidth}vw)`;
            console.log("functional");
        }
        boxpos -= boxwidth;
    });
    
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