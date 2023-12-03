import { scrollToTarget } from './scroll.js';
/*const nav = document.querySelector("#nav");
const abrir = document.querySelector("#abrir");
const cerrar = document.querySelector("#cerrar");

abrir.addEventListener("click", () => {
    nav.classList.add("visible");
})

cerrar.addEventListener("click", () => {
    nav.classList.remove("visible");
})

var faq = document.getElementsByClassName("question");
var i;

for (i = 0; i < faq.length; i++) {
    faq[i].addEventListener("click", function () {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
} 

document.addEventListener('DOMContentLoaded', function() {
    scrollToTarget('menus');

    
});*/

const nav = document.querySelector("#nav");
const abrir = document.querySelector("#abrir");
const cerrar = document.querySelector("#cerrar");

abrir.addEventListener("click", () => {
    nav.classList.add("visible");
})

cerrar.addEventListener("click", () => {
    nav.classList.remove("visible");
})

var faq = document.getElementsByClassName("question");
var i;

for (i = 0; i < faq.length; i++) {
    faq[i].addEventListener("click", function () {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
} 


const links = document.querySelectorAll('.nav-link');

links.forEach(link => {
    link.addEventListener('click', function (e) {
        e.preventDefault(); 
        const targetId = this.getAttribute('href').substring(1); 
        const targetElement = document.getElementById(targetId); 
        if (targetElement) {
            targetElement.scrollIntoView({ behavior: 'smooth' }); 
        }
    });
});
