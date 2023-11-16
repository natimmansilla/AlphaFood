![Esta es una imagen de ejemplo](https://github.com/natimmansilla/AlphaFood/blob/7698d81368fbd10462e1ea4056e618df0bef28d8/assets/img/Banner2.png)

# Trabajo Práctico - Frontend : HTML - CSS - JAVASCRIPT
![Badge en Desarollo](https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green)

## Descripción del Proyecto:
Este proyecto se basa en la construcción de una página web resposive para la empresa ficticia AlphaFood, la que se dedica a la venta de menus BARF 100% natural para perros. La página esta pensada para proyectar un entorno saludable y natural para el usuario, mientras se concientiza sobre la alimentación responsable y natural en la tenencia de perros.

## Contenido: 
  0. Navbar : Consta de un navegador de secciones responsive para desktop, tablet y mobile. 
  1. Home: Imagen ilustrativa de un perro saludable por comer dieta barf. Inspira calidad, vitalidad y confianza.
  2. Menús: Sección que exibirá los diferentes menús disponibles, son 6 en total
     * Cordero y Pavo
     * Pavo y Sardinas
     * Pollo
     * Pavo
     * Pollo y Vaca
     * Conejo y Caballo
  3. Instrucciones: Imagenes ilustrativas del proceso de compra de un menu Barf.
  4. Preguntas Frecuentes: 5 "cartas" encolumnadas con despliegue de movimiento, que le aclarará las posibles dudas al cliente. 
  5. Contacto: Se incluirá un formulario de contacto con tecnologia Javascrip.
  6. Footer con un ancla: Logo de la empresa y copyright.

### Seccion 0: Navbar
#### Colaborador: Natalia 
##### Detalles técnicos:
Consta de un navegador de secciones responsive para desktop, tablet y mobile. Tiene sus respectivas anclas a cada una de las secciones, desplieque de forma vertical encolumnado y centrado. Añade un efecto hover en color azul a los textos. Se utilizo Javascript para crear el menú de hamburguesa con una funcion "visible" para el despliegue y quitando ese atributo, el menu se contrae. Se añadio la imagen del logo de la empresa junto con el nav, que se alinearon de forma justify-content: space-between para abarcar la totalidad del espacio.Se utilizo 2 iconos de Bootstrap para hacer el menu, 3 lineas horizontales y un close X. Por último se añadió el cursor: pointer para hacer clickeable el menu.

### Seccion 1: Home
#### Colaborador: Natalia 
##### Detalles técnicos:
Imagen ilustrativa acorde al temario, editado con Photoshop para agregarle detalles usando la paleta de colores que rempresenta a la empresa. Ocupa el total de la pantanlla para todos los dispositivos. Adicionalmente se agregó una segunda imagen en alta calidad, promocionando el logo y la frase iconica de AlphaFood.Misma estética que la imagen anterior.

### Sección 2: Menús
#### Colaborador: Natalia 
##### Detalles técnicos:
La sección exibirá los diferentes menús disponibles en 6 cartas distribuidas de manera encolumnada, 3 elementos por fila. Las cartas estan centradas en todo aspecto, conteniendo en su interior una imagen descriptiva, el nombre del menú y un boton para más información.
Las cartas estan redondeadas en las esquinas, con una pequeña traslacion del eje Y cuando el cursor pasa por encima; tienen una sombra gris que proyecta profundidad a cada carta.
El boton de + info tiene los bordes redondeado en color azul y se le asigno un efecto de relleno al boton cuando el cursor pasa por encima del mismo.

### Sección 3: Instrucciones - (Posee una animación y una API)
#### Colaborador: Natalia y Franco
##### Detalles técnicos:
Esta sección contiene 4 cartas informativas sobre el proceso de compra de los menús. Cada carta posee un efecto de animación de bordes con movimiento circular. Este efecto se logro gracias varios estilos de css. En primer lugar se le dio el formato a la figura carta, añadiendole color, sobras, bordes redondeados, una posición relativa y la propiedad de overflow: hidden (para que la carta inconica quede dentro de la carta fondo); luego se utiliza ::before para darle el estilo a la carta que va a estar por encima del fondo original. A esta carta se le coloco un efecto inconico que va desde el color azul a transpartente en 120 grados, posicion absolute y contenido vacio.
Aqui se crea la animación en la carta before, con nombre "ROTAR", 2 segundos de demora, con efecto linear, y repeticion infinita. Luego use la propiedad keyframe para que rote en posición antihorario a -360 grados.
Por ultimo hice uso de ::after para modificar la última carta que va a estar por encima de todas, con posicion absolute, bordes redondeados y efecto de sobras al interior de la carta.Tambien se le agregaron estilos a los textos de su interior.

Descripción de la API:


### Sección 4:  Preguntas Frecuentes
#### Colaborador: Juan
##### Detalles técnicos:
La sección Preguntas Frecuentes ha sido desarrollada mediante HTML dentro de un contenedor padre section denominado "contenedor-preguntas" . Cada una de las preguntas, se encuentra compuesta por la pregunta propiamente dicha, identificada mediante la clase "question", seguido inmediatamente por un párrafo identificado mediante la clase "answer" el cual contiene la respuesta propiamente dicha, pero en principio se encuentra oculto debido a la propiedad "display:none" en el código css de su clase.

En cuanto a las interacciones, hay puntualmente dos de ellas, una se trata de un mero cambio de color frente al evento "hover", impelementado mediante css sobre las preguntas "question" en su estado sin desplegar, esto facilita al usuario el identificar que existe una interacción posible al hacer click en dicho contenedor. En cuanto a la segunda interacción, la misma se encuentra implementada mediante un event listener de JavaScript, el cual al recibir un click sobre una "question" en particular, detona el cambio de formato CSS tanto de la misma, ya que se utilizará el CSS "question:after" (el cual simplemente modifica el color y el ícono final) como de su answer subsiguiente, cambiando la propiedad display, del valor none, al valor block, volviendo la respuesta visible para el usuario, en su defecto, la misma función, de estar desplegada la respuesta, vuelve la misma al estado anterior, al clickear sobre la pregunta.


### Sección 5: Contacto
#### Colaborador: Franco 
##### Detalles técnicos:
El formulario de contacto se ha desarrollado con precisión utilizando el framework Bootstrap, en cumplimiento de los requisitos del TPO. Este formulario ofrece campos bien estructurados para que los usuarios ingresen su Nombre, Apellido, Correo Electrónico, Teléfono y un espacio dedicado para redactar sus mensajes. La funcionalidad del formulario se ha implementado de manera efectiva a través de formsubmit.co, lo que permite a los visitantes completar el formulario y enviar un correo electrónico directamente a la dirección de correo de la página.

La elección de Bootstrap no solo asegura una presentación visual atractiva sino también la capacidad de ser completamente responsive. Esto significa que el formulario se adapta de manera óptima a diversos dispositivos y tamaños de pantalla, incluyendo computadoras de escritorio, tablets y dispositivos móviles. Este enfoque garantiza una experiencia de usuario uniforme y accesible en todos los dispositivos, fusionando así un diseño atractivo con una funcionalidad efectiva.

### Sección 6: Footer
#### Colaborador: Franco 
##### Detalles técnicos:
El footer de la página web ha sido minuciosamente elaborado, destacándose por la atención al detalle en el diseño de los logos, cada uno enlazando directamente a las redes sociales de la marca. Se ha puesto un énfasis especial en la disposición de colores y la ubicación precisa de cada ícono, lo que contribuye a una estética armoniosa y atractiva en la parte inferior de la página. Además, se ha incluido un copyright de la marca, asegurando la protección de los derechos de propiedad intelectual.

Una característica esencial del footer es su total capacidad de respuesta (responsive design), lo que significa que se adapta de manera óptima a una variedad de tamaños de pantalla y dispositivos, desde computadoras de escritorio hasta dispositivos móviles. Esto garantiza que los visitantes experimenten una navegación fluida y una presentación consistente de la información, independientemente del dispositivo que utilicen, mejorando así la usabilidad y satisfacción del usuario.

## Tecnologias utilizadas: 
1.  HTML
2.  CSS
3.  Javascript
4.  Github y Git [control de versiones]
5.  Bootstrap [formulario]
6.  Photoshop
7.  FontAwesome y Flaticon [iconos]
8.  Google Fonts [fuentes]
9.  Flexbox y Grid [maquetación]
10. Uso de Api: [The dog Api - Implementada en la sección "Asi Funciona BARF"]

## Integrantes:
* Dominguez, Juan Cruz Elias - dominguez.juanelias@gmail.com
* Gomez, Franco - fe.gomez182@gmail.com
* Mansilla, Natalia Micaela - natimmansilla.sistemas@gmail.com

#### Trabajo Práctico Obligatorio Frontend - COMISION 23506 - Aprendizaje a lo Largo de la Vida - Codo a Codo - Segundo Semestre - 2023 - Buenos Aires - Argentina.
