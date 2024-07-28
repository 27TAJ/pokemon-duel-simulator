

document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('myCanvas');
    const context = canvas.getContext('2d');

    const img = new Image();

    img.src = "../../../../backend/api/static/images/pokeball.png";

    img.onload = function() {
        context.drawImage(img, 50, 50, img.width/3, img.height/2);
    }
});