$(document).ready(function () {
    const apiUrl = 'https://foodish-api.com/api/';
    
    $('.platillos').each(function () {
        const imgElement = $(this);
        
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => imgElement.attr('src', data.image));
    });
    
    $('.platillo').each(function () {
        const imgElement = $(this);
        
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => imgElement.attr('src', data.image));
    });
});