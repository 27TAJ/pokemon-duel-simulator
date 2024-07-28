document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('game_screen');
    if (canvas) {
        const context = canvas.getContext('2d');
    } else {
        console.error("Canvas element not found");
    }
});
