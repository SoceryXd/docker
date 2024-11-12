document.addEventListener('DOMContentLoaded', function () {
    new Splide('.splide', {
        arrows: 'false',
        type: 'loop',
        perPage: 1,
        autoplay: true,
        cover: false,
    }).mount();
});

// mouseover, click, mousedown, mouseout
document.querySelector("#sistema").addEventListener('click', function (e) {
    e.preventDefault();// impede o comportamento padrão

    let sub01 = document.querySelector("#sub01");

    if (sub01.style.display != 'block')
    {
        sub01.style.display = "block";
    }
    else {
        sub01.style.display = "none";
    }


});




