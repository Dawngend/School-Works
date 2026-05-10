document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('length-conversion-form');
    const resultDiv = document.getElementById('conversion-result');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const fromUnit = form.fromUnit.value;
        const toUnit = form.toUnit.value;
        const inputValue = parseFloat(form.inputValue.value);

        if (isNaN(inputValue)) {
            resultDiv.innerHTML = 'Please enter a valid number.';
            return;
        }

        fetch('api/convert.php', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                fromUnit: fromUnit,
                toUnit: toUnit,
                inputValue: inputValue
            }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                resultDiv.innerHTML = `Result: ${data.result} ${toUnit}`;
            } else {
                resultDiv.innerHTML = 'Conversion failed. Please try again.';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            resultDiv.innerHTML = 'An error occurred. Please try again later.';
        });
    });
});