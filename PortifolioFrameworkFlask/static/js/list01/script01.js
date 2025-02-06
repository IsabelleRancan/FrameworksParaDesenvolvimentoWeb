const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');

const img = new Image();
img.src = '/static/img/app/car.png';  

let imgX = 250;
let imgY = 250;
const step = 10;

img.onload = () => {
    drawImage(); 
};

function drawImage() {
    ctx.clearRect(0, 0, canvas.width, canvas.height); 
    ctx.drawImage(img, imgX, imgY, 50, 50); 
}

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