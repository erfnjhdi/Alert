const container = document.querySelector('.container');
const signUpBTN = document.querySelector('.green-bg button');

signUpBTN.addEventListener('click', () => {
    const serverURL = 'http://localhost:3000/api/users';

    // Example: Making a GET request to the server URL
    fetch(serverURL)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Network response was not ok: ${response.statusText}`);
            }
            return response.json();
        })
        .then(data => {
            // Handle the data received from the server
            console.log(data);
        })
        .catch(error => {
            // Handle errors
            console.error('Error:', error);
        });

    // Toggle the 'change' class on the container
    container.classList.toggle('change');
});
