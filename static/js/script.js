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
        console.log(filterClose,filterList)
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
    checklink();
    let closeElement = (all) =>{
        let close = document.querySelectorAll('.'+all);
        for(let i = 0; i < close.length; i++){
            close[i].classList.remove('active')
        }
    }
    let listDetail = (id) => {
        let listOpen = document.querySelector('#'+ id +'list');
        if (!document.querySelector('#' + id + 'list .list-btn-close')){
            let listBtnClose = document.createElement('div');
            listBtnClose.classList.add('list-btn-close');
            listBtnClose.innerHTML = '&#10006;';
            listOpen.prepend(listBtnClose);
        }

            let listBtnClose = document.querySelector('#' + id + 'list .list-btn-close');
        
        closeElement(listOpen.className);
        listOpen.classList.add('active')
        listBtnClose.addEventListener('click', () =>{
            listOpen.classList.remove('active');
        })
    }
    let btnDetail = document.querySelectorAll('.detail__list-btn')
    for(let i = 0; i < btnDetail.length; i++){
        btnDetail[i].addEventListener('click', e => {
            listDetail(btnDetail[i].id)
        });
    }


    let addActiveList = (list) =>{
        for(let i = 0; i < list.length; i++){
            list[i].classList.remove('active');
        }
           
    }
    if (document.querySelectorAll('.problem-item')){
        let listQuestion = document.querySelectorAll('.problem-item');
        for(let i = 0; i < listQuestion.length; i++){
            listQuestion[i].addEventListener('click', () => {
                addActiveList(listQuestion)
                listQuestion[i].classList.add('active');
            })
        }
    };

    

}) 
