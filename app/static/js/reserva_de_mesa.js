document.getElementById('reservarMesa').addEventListener('click', function(event) {
    event.preventDefault(); // Evita el envío del formulario por defecto

    const rut = document.getElementById('rut').value.trim();
    const fecha = document.getElementById('fecha').value;
    const hora = document.getElementById('hora').value;
    const comensales = document.getElementById('comensales').value;

    if (!rut || !fecha || !hora || !comensales) {
        alert("Por favor, completa todos los campos.");
        return;
    }

    const reservaDetalle = `Reserva confirmada para el ${fecha} a las ${hora} para ${comensales} comensales.`;
    alert(reservaDetalle);
});
