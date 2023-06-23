const apiKey = 'db029b7eabe74dd0992ad7688e47d693';
const apiUrl = ''

const formulario = document.getElementById('formulario_log');
const inputs = document.querySelectorAll('#formulario_log inputs')

const expresiones = {
    usuario: /^[a-zA-Z0-9\_\-]{4,16}$/,
    nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/,    
    password: /^[a-zA-z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$/,
    telefono: /^\d{7,14}$/
} 

const validarFormulario = () => {
    console.log('Se ejecuto');
}

inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);    
    input.addEventListener('blur', validarFormulario);
});

formulario.addEventListener('submit', (e) => {
    e.preventDefault();
})

