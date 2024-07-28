

document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('your_pokemon_screen');
    const context = canvas.getContext('2d');

    const img = new Image();

    img.src = "/static/images/pokeball.png";

    img.onload = function() {
       
        const rows = 2;
        const columns = 3;
        
        const pokeballWidth = canvas.width / columns * 0.8; 
        const pokeballHeight = pokeballWidth; 

        const xPadding = (canvas.width - (pokeballWidth * columns)) / (columns + 1);
        const yPadding = (canvas.height - (pokeballHeight * rows)) / (rows + 1);

        for (let row = 0; row < rows; row++) {
            for (let col = 0; col < columns; col++) {
                const x = xPadding + col * (pokeballWidth + xPadding);
                const y = yPadding + row * (pokeballHeight + yPadding);
                context.drawImage(img, x, y, pokeballWidth, pokeballHeight);
            }
        }
    }
});