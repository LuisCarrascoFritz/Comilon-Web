$(document).ready(function () {
    // URL base de la API
    const apiUrl = 'https://foodish-api.com/api/';

    // Seleccionar todas las imágenes con la clase "platillos"
    $('.platillos').each(function () {
        const imgElement = $(this); // Obtener el elemento <img>

        // Solicitar una nueva imagen de la API
        $.ajax({
            url: apiUrl,
            method: 'GET',
            success: function (data) {
                // Verifica si el atributo 'image' existe en la respuesta
                if (data.image) {
                    // Reemplazar el atributo src del <img> con la nueva imagen
                    imgElement.attr('src', data.image);
                } else {
                    console.error('No se encontró el atributo "image" en la respuesta.');
                }
            },
            error: function (xhr, status, error) {
                console.error('Error al realizar la solicitud a la API:', error);
            }
        });
    });
});
