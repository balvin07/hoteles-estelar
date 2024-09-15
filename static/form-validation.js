document.addEventListener('DOMContentLoaded', function() {
    const emailField = document.getElementById('id_email');
    if (emailField) {
        emailField.addEventListener('input', function() {
            const value = emailField.value;
            if (value && !value.includes('@')) {
                emailField.setCustomValidity('Por favor, ingrese una dirección de correo electrónico válida.');
            } else {
                emailField.setCustomValidity('');
            }
        });
    }
});
