// app.js

document.getElementById('obtenerRazaBtn').addEventListener('click', obtenerRazaAleatoria);

function obtenerRazaAleatoria() {
    const url = "https://api.thedogapi.com/v1/breeds";

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error en la solicitud. Código de estado: ${response.status}`);
            }
            return response.json();
        })
        .then(razas => {
            if (razas.length === 0) {
                throw new Error("La lista de razas está vacía.");
            }

            const razaAleatoria = razas[0];
            mostrarInformacion(razaAleatoria);
        })
        .catch(error => {
            console.error("Error al obtener la raza aleatoria:", error);
        });
}

function mostrarInformacion(raza) {
    const urlImagen = `https://api.thedogapi.com/v1/images/search?breed_id=${raza.id}`;

    fetch(urlImagen)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error en la solicitud de la imagen. Código de estado: ${response.status}`);
            }
            return response.json();
        })
        .then(imagenData => {
            if (imagenData.length === 0) {
                throw new Error("La lista de imágenes está vacía.");
            }

            const imagenUrl = imagenData[0].url;

            // Mostrar información de la raza en el contenedor
            const informacionRazaElement = document.getElementById('informacionRaza');
            informacionRazaElement.innerHTML = `
                <p>Raza: ${raza.name}</p>
                <p>Altura: ${raza.height.metric} cm</p>
                <p>Peso: ${raza.weight.metric} kg</p>
                <p>Imagen:</p>
                <img src="${imagenUrl}" alt="Imagen de la raza">
            `;
        })
        .catch(error => {
            console.error("Error al obtener la imagen:", error);
        });
}
