document.addEventListener('DOMContentLoaded', function () {
    new Splide('.splide', {
        arrows: 'false',
        type: 'loop',
        perPage: 1,
        autoplay: true,
        cover: false,
    }).mount();
});

document.querySelector("#sistema").addEventListener('click', function (e) {
    e.preventDefault();// impede comportamento padrão


    let sub01 = document.querySelector("#sub01");
    let sub02 = document.querySelector("#sub02");

    if (sub01.style.display != 'block') {

        sub01.style.display = "block";
    }
    else 
    {
        sub01.style.display = "none";
    }

   

});