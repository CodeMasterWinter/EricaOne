const left = document.getElementById('left')
const right = document.getElementById('right')
const boxes = document.getElementsByClassName('nav-item')
var boxwidth = 18;

right.addEventListener('click', () => {
    for (i=0; i < boxes.length; i++) {
        boxes[i].style.transform = `translateX(${boxwidth}vw)`;
        console.log("functional");
    }
    boxwidth += 18;
});

left.addEventListener('click', () => {
    for (i=0; i < boxes.length; i++) {
        boxes[i].style.transform = `translateX(${boxwidth}vw)`;
        console.log("functional");
    }
    boxwidth -= 18;
});