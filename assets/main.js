const nav = document.querySelector("#nav");
const abrir = document.querySelector("#abrir");
const cerrar = document.querySelector("#cerrar");


/*Menú Hamburguesa*/

abrir.addEventListener("click", () => {
    nav.classList.add("visible");
})

cerrar.addEventListener("click", () => {
    nav.classList.remove("visible");
})


/*Preguntas Frecuentes Colapsable */

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


var map;

function getmap(){
    map.entities.clear
    map = New.Microsoft.Map(document.getelemntbyid("map"), {
        credentials:'Amst3HQKXPmTU8-EHBCSri7fBKM8JE5RT3JXWWxtthGlLLct7GGrOQWYOig5VtwP',
        center: new Microsoft.Maps.Location(-34.61315, -58.37723),
        mapTypeId: Microsoft.Maps.MapTypeId.aerial,
        zoom: 10,
    });
};
