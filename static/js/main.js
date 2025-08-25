document.addEventListener('DOMContentLoaded', () => {
    // Select the delete button
    const deleteButton = document.querySelector('.delete-btn');

    if (deleteButton) {
        // Add a click listener to the button
        deleteButton.addEventListener('click', (event) => {
            // Add the pulse animation class
            deleteButton.style.animation = 'pulse-once 0.5s ease-in-out';

            // Remove the animation class after the animation ends to allow it to be re-triggered
            setTimeout(() => {
                deleteButton.style.animation = '';
            }, 500);
        });
    }
});