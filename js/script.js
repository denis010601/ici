window.addEventListener('DOMContentLoaded',() =>{
    let video = document.querySelector('#myVideo');
    let textvideo = document.querySelector('.video-placeholder');
    let logovideo = document.querySelector('.video-logo');
    let viewVideo = document.createElement('source');
    viewVideo.src = textvideo.alt
  
    video.classList.add('z50');
    logovideo.classList.add('z100');
    video.append(viewVideo)
    let noPrev = (e) => {
        e.preventDefault();
    }
    let checklink = e => {
        if(window.innerWidth <= 768 && !document.querySelector('.nav-burger')){
            let gNav = document.querySelectorAll('.header__nav-link')
            let bNav = document.querySelector('.burger-menu')
            let nBurger = document.createElement('nav')
            nBurger.classList.add('nav-burger')
            bNav.append(nBurger)
            for(let i = 0; i < gNav.length; i++){
                let linkBurger = document.createElement('a')
                linkBurger.classList.add('burger-link')
                linkBurger.href = gNav[i]
                linkBurger.innerText = gNav[i].innerText
                console.log(linkBurger)
                nBurger.appendChild(linkBurger)
            }
            }
        else{
            let bNav = document.querySelector('.burger-menu')
            let nBurger = document.querySelector('.nav-burger')
            nBurger.classList.add('disabled')
            nBurger.classList.remove('active')
            bNav.classList.add('disabled')
            bNav.classList.remove('active') 
        }
    }
    if(window.innerWidth <= 768 && !document.querySelector('.nav-burger')){
        checklink()
    }
    window.addEventListener('resize', checklink) 

    let burger = document.querySelector('.burger')
    let closeBurger = document.querySelector('.close')
    burger.addEventListener('click', e => {
        let bNav = document.querySelector('.burger-menu')
        let nBurger = document.querySelector('.nav-burger')
        nBurger.classList.remove('disabled')
        nBurger.classList.add('active')
        bNav.classList.remove('disabled')
        bNav.classList.add('active')
        burger.classList.add('disabled')
    })
    closeBurger.addEventListener('click', e => {
        let bNav = document.querySelector('.burger-menu')
        let nBurger = document.querySelector('.nav-burger')
        nBurger.classList.add('disabled')
        nBurger.classList.remove('active')
        bNav.classList.add('disabled')
        bNav.classList.remove('active')
        burger.classList.remove('disabled')
    })
}) 
