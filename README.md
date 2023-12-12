![Esta es una imagen de ejemplo](https://github.com/natimmansilla/AlphaFood/blob/7698d81368fbd10462e1ea4056e618df0bef28d8/assets/img/Banner2.png)

# Trabajo Práctico Fullstack : HTML - CSS - JAVASCRIPT - Python - MySQL - Django
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
  7. Mascotas_app: para registro de usuarios.

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

### Sección 3: Instrucciones - (Posee una animación, una API y una app)
#### Colaborador: Natalia y Franco
##### Detalles técnicos:
Esta sección contiene 4 cartas informativas sobre el proceso de compra de los menús. Cada carta posee un efecto de animación de bordes con movimiento circular. Este efecto se logro gracias varios estilos de css. En primer lugar se le dio el formato a la figura carta, añadiendole color, sobras, bordes redondeados, una posición relativa y la propiedad de overflow: hidden (para que la carta inconica quede dentro de la carta fondo); luego se utiliza ::before para darle el estilo a la carta que va a estar por encima del fondo original. A esta carta se le coloco un efecto inconico que va desde el color azul a transpartente en 120 grados, posicion absolute y contenido vacio.
Aqui se crea la animación en la carta before, con nombre "ROTAR", 2 segundos de demora, con efecto linear, y repeticion infinita. Luego use la propiedad keyframe para que rote en posición antihorario a -360 grados.
Por ultimo hice uso de ::after para modificar la última carta que va a estar por encima de todas, con posicion absolute, bordes redondeados y efecto de sobras al interior de la carta.Tambien se le agregaron estilos a los textos de su interior.

### Dog_API
#### Colaborador: Natalia, Franco y Juan
##### Detalles técnicos:
Dog API Explorer es una pequeña aplicación web que  permite explorar información sobre razas de perros de manera aleatoria. La aplicación utiliza la API de The Dog API para obtener datos detallados sobre diferentes razas, incluyendo nombres, alturas, pesos y imágenes representativas. Tecnologías Utilizadas: HTML, CSS, JavaScript, Fetch API.

### mascotas_app
#### Colaborador: Natalia, Franco y Paola
##### Detalles técnicos:
La funcionalidad principal de mascotas-app ofrece una experiencia intuitiva y amigable para el  usuario. A través de una interfaz cuidadosamente diseñada, puede realizar acciones la creación de nuevos registros, la visualización detallada de información existente, la actualización de datos y la eliminación de registros obsoletos. 

Se fundamenta en el modelo MTV de Django,  implementa el protocolo HTTP, ofreciendo soporte completo para los métodos GET, POST, PUT y DELETE. Proporciona un sistema integral de CRUD (Create, Read, Update, Delete), permitiendo a los usuarios realizar operaciones con sus datos de manera eficiente. Al interactuar con una base de datos integrada, tienen la capacidad de registrar información relevante sobre sus mascotas y garantizar la persistencia de estos registros.

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
11. Python [backend]
12. Django [backend]
13. PythonAnywhere [backend]

## Estructura del proyecto backend:

├── README.md
├── alphafood_project
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── __init__.cpython-311.pyc
│   │   ├── settings.cpython-310.pyc
│   │   ├── settings.cpython-311.pyc
│   │   ├── urls.cpython-310.pyc
│   │   ├── urls.cpython-311.pyc
│   │   ├── views.cpython-310.pyc
│   │   ├── views.cpython-311.pyc
│   │   ├── wsgi.cpython-310.pyc
│   │   └── wsgi.cpython-311.pyc
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── db.sqlite3
├── estructura_del_repositorio.txt
├── manage.py
├── mascotas_app
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── __init__.cpython-311.pyc
│   │   ├── admin.cpython-310.pyc
│   │   ├── admin.cpython-311.pyc
│   │   ├── apps.cpython-310.pyc
│   │   ├── apps.cpython-311.pyc
│   │   ├── forms.cpython-310.pyc
│   │   ├── models.cpython-310.pyc
│   │   ├── models.cpython-311.pyc
│   │   ├── urls.cpython-310.pyc
│   │   ├── urls.cpython-311.pyc
│   │   ├── views.cpython-310.pyc
│   │   └── views.cpython-311.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-310.pyc
│   │       ├── 0001_initial.cpython-311.pyc
│   │       ├── __init__.cpython-310.pyc
│   │       └── __init__.cpython-311.pyc
│   ├── models.py
│   ├── static
│   │   └── mascotas
│   │       ├── css
│   │       │   ├── style.css
│   │       │   └── styles2.css
│   │       ├── img
│   │       │   ├── 0.0_logo.png
│   │       │   └── icono.ico
│   │       └── js
│   │           └── main.js
│   ├── templates
│   │   ├── base.html
│   │   ├── mascotas
│   │   │   ├── editar.html
│   │   │   ├── form.html
│   │   │   ├── index.html
│   │   │   └── registrar.html
│   │   └── paginas
│   │       └── uno.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static
│   ├── css
│   │   └── styles.css
│   ├── img
│   │   ├── 0.0_logo.png
│   │   ├── 0.1_hero.png
│   │   ├── 0.3_baner_hero.png
│   │   ├── 1.1_CorderoPavo.webp
│   │   ├── 1.2_PavoSardinas.webp
│   │   ├── 1.3_Pollo.webp
│   │   ├── 1.4_Pavo.webp
│   │   ├── 1.5_PolloVaca.webp
│   │   ├── 1.6_ConejoCaballo.webp
│   │   ├── 1.7_CorderoPavoTrozos.webp
│   │   ├── Banner2.png
│   │   ├── S0-Logo.png
│   │   ├── foteer.png
│   │   ├── hero.png
│   │   ├── icono.ico
│   │   └── info-nutricional.png
│   └── js
│       ├── api.js
│       └── main.js
└── templates
    └── index.html

## Integrantes:
* Basualdo, Paola Ivana - paoladeembalse@gmail.com 
* Gomez, Franco - fe.gomez182@gmail.com
* Mansilla, Natalia Micaela - natimmansilla.sistemas@gmail.com
  

#### Trabajo Práctico Final - COMISION 23506 - Aprendizaje a lo Largo de la Vida - Codo a Codo - Segundo Semestre - 2023 - Buenos Aires - Argentina.
