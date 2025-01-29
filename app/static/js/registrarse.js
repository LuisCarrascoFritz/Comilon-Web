document.getElementById('registrarse').addEventListener('submit', function(event) {

    const nombre = document.getElementById('nombre').value;
    const correo = document.getElementById('correo').value;
    const contraseña = document.getElementById('contraseña').value;
    const contraseña2 = document.getElementById('contraseña').value;

    if (!nombre || !correo || !contraseña || !contraseña2) {
        alert("Por favor, completa todos los campos.");
        return;
    }
});