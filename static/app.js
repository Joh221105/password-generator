document.addEventListener('DOMContentLoaded', () => {
    const generate_password_button = document.getElementById('generate-password-button');
    const password_display = document.getElementById('password-container');
    const copy_button = document.getElementById('copy-button')

    generate_password_button.addEventListener("click", () => {
        const length_of_password = document.getElementById('length-input').value;
        const boolean_lower = document.getElementById('lower-checkbox').checked;
        const boolean_upper = document.getElementById('upper-checkbox').checked;
        const boolean_symbols = document.getElementById('symbols-checkbox').checked;
        const boolean_numbers = document.getElementById('numbers-checkbox').checked;
        const userInput = {
            length: length_of_password,
            lower: boolean_lower,
            upper: boolean_upper,
            symbols: boolean_symbols,
            numbers: boolean_numbers
        };

        fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(userInput)
        })
        .then(response => response.json())
        .then(data => {
            password_display.innerHTML = data.password;
        })
        .catch(error => console.error('Error:', error))
    })

    copy_button.addEventListener('click', () => {
        const passwordText = password_display.innerText;
        navigator.clipboard.writeText(passwordText)
    })
    
})