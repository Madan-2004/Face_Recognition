/*===== SHOW NAVBAR  =====*/ 
const showNavbar = (toggleId, navId, bodyId, headerId) =>{
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId),
    bodypd = document.getElementById(bodyId),
    headerpd = document.getElementById(headerId)

    // Validate that all variables exist
    if(toggle && nav && bodypd && headerpd){
        toggle.addEventListener('click', ()=>{
            // show navbar
            nav.classList.toggle('show')
            // change icon
            toggle.classList.toggle('bx-x')
            // add padding to body
            bodypd.classList.toggle('body-pd')
            // add padding to header
            headerpd.classList.toggle('body-pd')
        })
    }
}

showNavbar('header-toggle','nav-bar','body-pd','header')

/*===== LINK ACTIVE  =====*/ 
const linkColor = document.querySelectorAll('.nav__link')

function colorLink(){
    if(linkColor){
        linkColor.forEach(l=> l.classList.remove('active'))
        this.classList.add('active')
    }
}
linkColor.forEach(l=> l.addEventListener('click', colorLink))

// window.addEventListener('load', function () {
//     const currentBackgroundPosition = getComputedStyle(document.body).backgroundPosition;
//     const [x, y] = currentBackgroundPosition.split(' ');
    
//     const currentX = parseInt(x);
//     const currentY = parseInt(y);
    
//     // Move the background by 20% (adjust as needed)
//     const newX = currentX + 2000;
    
//     // Set the new background position
//     document.body.style.backgroundPosition = `${newX}% ${currentY}`;
//   });
// gsap.from('body',1.2,{opacity: 0,y: 2, delay: .1})