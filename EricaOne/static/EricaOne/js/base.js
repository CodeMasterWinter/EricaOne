const left = document.getElementById('nav-prev')
const right = document.getElementById('nav-next')
const boxes = document.getElementsByClassName('nav-item')
var boxwidth = 18;
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