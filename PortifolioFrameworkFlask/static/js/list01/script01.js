const canvas = document.getElementById('meuCanvas');
const ctx = canvas.getContext('2d');

const img = new Image();
img.src = '/static/img/car.png';  

let imgX = 250;
let imgY = 250;
const step = 10;

img.onload = () => {
    drawImage(); // Desenha a imagem inicialmente
};

function drawImage() {
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Limpa o canvas
    ctx.drawImage(img, imgX, imgY, 50, 50); // Ajuste as dimensões da imagem conforme necessário
}

// Detecta as teclas para mover a imagem
document.addEventListener('keydown', (event) => {
    switch (event.key) {
        case 'ArrowUp':
            imgY -= step;
            break;
        case 'ArrowDown':
            imgY += step;
            break;
        case 'ArrowLeft':
            imgX -= step;
            break;
        case 'ArrowRight':
            imgX += step;
            break;
    }
    drawImage();
});