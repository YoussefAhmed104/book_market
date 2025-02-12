document.querySelectorAll('.close').forEach(closeBtn => {
    closeBtn.addEventListener('click', (event) => {
        event.preventDefault();
        const liElement = event.target.parentNode;
        liElement.style.opacity = '0';
        setTimeout(() => liElement.remove(), 300); // Smooth removal
    });
});