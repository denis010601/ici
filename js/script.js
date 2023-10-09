window.addEventListener('DOMContentLoaded',() =>{

    if(document.querySelector('.video-section')){
        let video = document.querySelector('#myVideo');
        let textvideo = document.querySelector('.video-placeholder');
        let logovideo = document.querySelector('.video-logo');
        let viewVideo = document.createElement('source');
        viewVideo.src = textvideo.alt
      
        video.classList.add('z50');
        logovideo.classList.add('z100');
        video.append(viewVideo)

    }

    if(document.querySelector('.filter')){
        let filterOpen = document.querySelector('.filter-text');
        let filterClose = document.querySelector('.closeFilter');
        let filterList = document.querySelector('.filter-popup');
        filterOpen.addEventListener('click', e => {
            filterList.classList.add('active');
            filterList.classList.remove('disabled');
        })
        filterClose.addEventListener('click', e => {
            filterList.classList.add('disabled');
            filterList.classList.remove('active');
        })
    }

    let noPrev = (e) => {
        e.preventDefault();
    }
    let checklink = e => {
        if(!document.querySelector('.nav-burger')){
            let gNav = document.querySelectorAll('.header__nav-link')
            let subNav = document.querySelector('.submenu').cloneNode(true)
            console.log(subNav)
            let bNav = document.querySelector('.burger-menu')
            let nBurger = document.createElement('nav')
            nBurger.classList.add('nav-burger')
            bNav.append(nBurger)
            nBurger.append(subNav)
            
            for(let i = 0; i < gNav.length; i++){
                let linkBurger = document.createElement('a')
                linkBurger.classList.add('burger-link')
                linkBurger.href = gNav[i]
                linkBurger.innerText = gNav[i].innerText
                console.log(linkBurger)
                nBurger.appendChild(linkBurger)
            }
      
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
    
          }
          
    }
    if(window.innerWidth <= 768 && !document.querySelector('.nav-burger')){
        checklink()
    }
    checklink()

        
   if(document.querySelectorAll('.detail__size-list-item')){
        let size = document.querySelectorAll('.detail__size-list-item');
        let sizeList = document.querySelector('.detail__size-list');
        sizeList.addEventListener('click', (e)=>{
            sizeList.classList.add('active') 
            for(let i = 0; i < size.length; i++){
                
                size[i].addEventListener('click', e => {
                    for(let j = 0; j < size.length; j++){
                        size[j].classList.remove('active')
                    }
                    if(!size[i].classList.contains('active')){
                        
                    }
                    sizeList.classList.remove('active') 
                })
            }
            e.target.classList.add('active')
      
        })
       
   }
}) 
