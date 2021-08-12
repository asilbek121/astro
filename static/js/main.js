$(function () {
  $('.rev_slider').slick({
    dots: true,
    arrows: false,
    infinite: true,
    speed: 300,
    slidesToShow: 1,
    adaptiveHeight: true,
    autoplay: true,
    autoplaySpeed: 3000,
  });
  $('.header-ham').click(function () {
    $('.header-mob-parent').fadeIn()
  })

  function closeSearchMob(e) {
    var target = $(e.target)
    if (target.is('.header-mob-parent')) {
      target.fadeOut()
    }
  }

  $('.header-mob-parent').click(closeSearchMob)
})

$(function () {
  $('.slider-user').slick({
    dots: true,
    infinite: true,
    slidesToShow: 3,
    prevArrow: '.arrow-prev',
    nextArrow: '.arrow-next',
    speed: 300,
    autoplay: true,
    autoplaySpeed: 2000,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
          infinite: true,
          dots: true
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ]
  });
  $('.course-slider').slick({
    dots: false,
    arrows: true,
    slidesToShow: 4,
    prevArrow: `<button class="course-slider-arrow arrow-right">
    <img src="img/img-slider/left.svg" alt="">
            </button>`,
    nextArrow: `<button class="course-slider-arrow arrow-left">
    <img src="img/img-slider/reght.svg" alt="">
    </button>`,
    speed: 300,
    // autoplay: true,
    // autoplaySpeed: 2000,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
          dots: false,
          prevArrow: false,
          nextArrow: false,
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ]
  });
})






let perPage = 6;
let idPage = 1;
let start = 0;
let end = perPage;

const product = [
    { id: 1, image: "img/news-img/sl1.png", title: "2 августа 2018", h4: "Польза Интернет продвижения для вашего бизнеса", p:"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do"},
    { id: 2, image: "img/news-img/sl2.png", title: "6 августа 2018", h4: "15 катастрофических ошибок в SEO продвижении", p: "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris " },
    { id: 3, image: "img/news-img/sl3.png", title: "2 августа 2018", h4: "Польза Интернет продвижения для вашего", p: "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore " },
    { id: 4, image: "img/news-img/sl4.png", title: "2 августа 2018", h4: "Польза Интернет продвижения для вашего бизнеса", p:"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do" },
    { id: 5, image:  "img/news-img/sl5.png", title: "6 августа 2018", h4: "15 катастрофических ошибок в SEO продвижении", p: "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris " },
    { id: 6, image: "img/news-img/sl6.png", title: "2 августа 2018", h4: "Польза Интернет продвижения для вашего", p: "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore " },
    { id: 7, image: "img/news-img/sl4.png", title: "2 августа 2018", h4: "Польза Интернет продвижения для вашего бизнеса", p:"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do" },
    { id: 8, image:  "img/news-img/sl5.png", title: "6 августа 2018", h4: "15 катастрофических ошибок в SEO продвижении", p: "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris " },
    { id: 9, image: "img/news-img/sl6.png", title: "2 августа 2018", h4: "Польза Интернет продвижения для вашего", p: "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore " },
    { id: 10, image: "img/news-img/sl5.png", title: "2 августа 2018", h4: "Польза Интернет продвижения для вашего бизнеса", p:"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do" },
    { id: 11, image:  "img/news-img/sl4.png", title: "6 августа 2018", h4: "15 катастрофических ошибок в SEO продвижении", p: "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris " },
    { id: 12, image: "img/news-img/sl6.png", title: "2 августа 2018", h4: "Польза Интернет продвижения для вашего", p: "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore " },
    { id: 13, image: "img/news-img/sl4.png", title: "2 августа 2018", h4: "Польза Интернет продвижения для вашего", p: "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore " },
]

let productArr = [];
let showAdd = false;

const addBookBtn = document.getElementById('add');
const name = document.getElementById('name');
const imgLink = document.getElementById('imgLink');
const addBook = document.getElementById('add-book');
addBook.addEventListener('click', () => {
    if (imgLink.value !== '' && name.value !== '') {
        productArr.push({
            id: product.length + 1,
            image: imgLink.value,
            title: name.value,
            h3: name.value,
            p: name.value,
        })
    }
});


function highlightText() {
    const title = document.querySelectorAll('.content__product__item h3');
    title.forEach((title, index) => {
        let titleText = title.innerHTML;
        let indexOf = Number(titleText.toLocaleLowerCase().indexOf(searchText.value.toLocaleLowerCase()));
        let searchTextLength = searchText.value.length;
        titleText = titleText.substring(0, indexOf) + "<span class='highlight'>" + titleText.substring(indexOf, indexOf + searchTextLength) + "</span>" + titleText.substring(indexOf + searchTextLength, titleText.length);
        title.innerHTML = titleText;
        console.log(titleText);
    })
}


productArr = product;


const pageConfig = document.querySelector('.page-config select');
const mySelect = document.getElementById('mySelect');
const countTotalPage = document.querySelector('.total-page');
const countTotalProduct = document.querySelector('.total-item');

let totalPages = Math.ceil(productArr.length / perPage);
const searchText = document.querySelector('.content__search input');
const searchBtn = document.getElementById('search');


function initRender(productAr, totalPage) {
    renderProduct(productAr);
    renderListPage(totalPage);
}

initRender(productArr, totalPages);

function getCurrentPage(indexPage) {
    start = (indexPage - 1) * perPage;
    end = indexPage * perPage;
    totalPages = Math.ceil(productArr.length / perPage);
    countTotalPage.innerHTML = `Total pages: ${totalPages}`;
    countTotalProduct.innerHTML = `Total Product:  ${productArr.length}`
}

const deleteBtn = document.querySelectorAll('.content__product__item .delete');

deleteBtn.forEach((item, index) => {
    deleteBtn[index].addEventListener('click', () => {
        product.splice(index, 1);
        productArr = product;
        renderProduct(productArr)
    });
});

getCurrentPage(1);

searchBtn.addEventListener('click', () => {
    idPage = 1;
    productArr = [];
    product.forEach((item, index) => {
        if (item.title.toLocaleLowerCase().indexOf(searchText.value.toLocaleLowerCase()) != -1) {
            productArr.push(item);
        }
    });
    if (productArr.length === 0) {
        $('.no-result').css('display', 'block')
    } else {
        $('.no-result').css('display', 'none')
    }
    getCurrentPage(idPage);
    initRender(productArr, totalPages);
    changePage();
    if (totalPages <= 1) {
        $('.btn-prev').addClass('btn-active');
        $('.btn-next').addClass('btn-active');
    } else {
        $('.btn-next').removeClass('btn-active');
    }
});

searchText.addEventListener("keyup", (event) => {
    if (event.keyCode === 13) {
        event.preventDefault();
        searchBtn.click();
    }
});

addBookBtn.addEventListener('click', () => {
    showAdd = !showAdd;
    if (showAdd) {
        $('.add-book').css('display', 'flex');
    } else {
        $('.add-book').css('display', 'none');
    }
})


pageConfig.addEventListener('change', () => {
    idPage = 1;
    perPage = Number(pageConfig.value);
    getCurrentPage(idPage);
    initRender(productArr, totalPages);
    if (totalPages == 1) {
        $('.btn-prev').addClass('btn-active');
        $('.btn-next').addClass('btn-active');
    } else {
        $('.btn-next').removeClass('btn-active');
    }
    changePage();
});



function renderProduct(product) {
    html = '';
    const content = product.map((item, index) => {
        if (index >= start && index < end) {
            html += '<div class="content__product__item">';
            html += '<a>';
            html += '<img src=' + item.image + '>';
            html += '</a>';
            html += '<h3>' + item.title + '</h3>';
            html += '<h4>' + item.h4 + '</h4>';
            html += '<p>' + item.p + '</p>';
            html += '</div>';
            return html;
        }
    });
    document.getElementById('product').innerHTML = html;
    highlightText();
}

function renderListPage(totalPages) {
    let html = '';
    html += `<li class="current-page active"><a>${1}</a></li>`;
    for (let i = 2; i <= totalPages; i++) {
        html += `<li><a>${i}</a></li>`;
    }
    if (totalPages === 0) {
        html = ''
    }
    document.getElementById('number-page').innerHTML = html;
}

function changePage() {
    const idPages = document.querySelectorAll('.number-page li');
    const a = document.querySelectorAll('.number-page li a');
    for (let i = 0; i < idPages.length; i++) {
        idPages[i].onclick = function () {
            let value = i + 1;
            const current = document.getElementsByClassName('active');
            current[0].className = current[0].className.replace('active', '');
            this.classList.add('active');
            if (value > 1 && value < idPages.length) {
                $('.btn-prev').removeClass('btn-active');
                $('.btn-next').removeClass('btn-active');
            }
            if (value == 1) {
                $('.btn-prev').addClass('btn-active');
                $('.btn-next').removeClass('btn-active');
            }
            if (value == idPages.length) {
                $('.btn-next').addClass('btn-active');
                $('.btn-prev').removeClass('btn-active');
            }
            idPage = value;
            getCurrentPage(idPage);
            renderProduct(productArr);
        };
    }
}

changePage();

$('.btn-next').on('click', () => {
    idPage++;
    if (idPage > totalPages) {
        idPage = totalPages;
    }
    if (idPage == totalPages) {
        $('.btn-next').addClass('btn-active');
    } else {
        $('.btn-next').removeClass('btn-active');
    }
    console.log(idPage);
    const btnPrev = document.querySelector('.btn-prev');
    btnPrev.classList.remove('btn-active');
    $('.number-page li').removeClass('active');
    $(`.number-page li:eq(${idPage - 1})`).addClass('active');
    getCurrentPage(idPage);
    renderProduct(productArr);
});

$('.btn-prev').on('click', () => {
    idPage--;
    if (idPage <= 0) {
        idPage = 1;
    }
    if (idPage == 1) {
        $('.btn-prev').addClass('btn-active');
    } else {
        $('.btn-prev').removeClass('btn-active');
    }
    const btnNext = document.querySelector('.btn-next');
    btnNext.classList.remove('btn-active');
    $('.number-page li').removeClass('active');
    $(`.number-page li:eq(${idPage - 1})`).addClass('active');
    getCurrentPage(idPage);
    renderProduct(productArr);
});



