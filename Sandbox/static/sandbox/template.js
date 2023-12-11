var navItems = document.getElementsByClassName('nav-item')

for (const navItem of navItems) {
    var navwidth =  92/5;
    navItem.style.transform = `translateX(${navwidth}vw);`
    console.log("ight done");
}