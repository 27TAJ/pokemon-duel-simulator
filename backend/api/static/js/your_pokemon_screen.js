

document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('your_pokemon_screen');
    const context = canvas.getContext('2d');

    const img = new Image();

    img.src = "../images/pokeball.png";

    img.onload = function() {
        context.drawImage(img, 50, 50, img.width/3, img.height/2);
    }

});