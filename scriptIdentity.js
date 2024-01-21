// Use const or let for variable declaration
const form = document.getElementById('crimeForm');
const nextBtn = document.querySelector('.nextBtn');
const backBtn = document.querySelector('.backBtn');

// Use a function for moving the form
function moveForm(direction) {
    const moveAmount = direction === 'left' ? '450px' : '-450px';
    form.style.left = moveAmount;
}
