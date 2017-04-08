var cvs;
var ctx;
var bx = 50;
var by = 50;
var vx = 10;
var vy = 4;

var score1p = 0;
var score2p = 0;
const WINNING_SCORE = 3;

var showingWinScreen = false;

var p1y = 250;
var p2y = 250;
const PADDLE_HEIGHT = 100;
const PADDLE_WIDTH = 10;



class Pone {
    constructor(name = '吹雪', arm1 = '10cm連装高角砲') {
        this.name = name;
        this.arm1 = arm1;
    }
    move() {
        if (showingWinScreen) {
            return;
        }

        computerMovement();

        bx += vx;
        by += vy;

        if (bx < 0) {
            if (by > p1y && by < p1y + PADDLE_HEIGHT) {
                vx = -vx;

                var dy = by - (p1y + PADDLE_HEIGHT / 2);
                vy = dy * 0.35;
            } else {
                score2p++; // Must come first for win checking
                ballReset();

            }
        }

        if (bx > cvs.width) {
            if (by > p2y && by < p2y + PADDLE_HEIGHT) {
                vx = -vx;

                var dy = by - (p2y + PADDLE_HEIGHT / 2);
                vy = dy * 0.35;
            } else {
                score1p++; // Must come first for win checking
                ballReset();

            }
        }

        if (by > cvs.height || by < 0) {
            vy = -vy;
        }
    }

    draw() {
        // next line blanks out the screen with black
        paddle(0, 0, cvs.width, cvs.height, 'black');

        if (showingWinScreen) {
            if (score1p >= WINNING_SCORE) {
                ctx.fillStyle = 'white';
                ctx.fillText("Left Player Won!!!", 350, 200);
            } else {
                ctx.fillStyle = 'white';
                ctx.fillText("Right Player Won!!!", 350, 200);
            }

            ctx.fillText("click to continue", 350, 500);
            return;
        }

        drawNet();

        paddle(0, p1y, PADDLE_WIDTH, PADDLE_HEIGHT, 'white');

        paddle(cvs.width - PADDLE_WIDTH, p2y, PADDLE_WIDTH, PADDLE_HEIGHT, 'white');

        // Next line draws the balls
        ball(bx, by, 10, 'white');

        ctx.fillText(score1p, 100, 100);
        ctx.fillText(score2p, cvs.width - 100, 100);
    }
}

function calculateMousePosition(evt) {
    var rect = cvs.getBoundingClientRect();
    var root = document.documentElement;
    var mousex = evt.clientx - rect.left - root.scrollLeft;
    var mouseY = evt.clientY - rect.top - root.scrollTop;
    return {
        x: mousex,
        y: mouseY
    };
}

function handleMouseClick(evt) {
    if (showingWinScreen) {
        score1p = 0;
        score2p = 0;
        showingWinScreen = false;
    }
}

window.onclick = function () {
    cvs = document.getElementById('pone');
    ctx = cvs.getContext('2d');
    const pone = new Pone();
    var fps = 30;
    setInterval(function () {
        pone.move();
        pone.draw();
    }, 1000 / fps);

    cvs.addEventListener('mousemove', function (evt) {
        var mousePos = calculateMousePosition(evt);
        p1y = mousePos.y - (PADDLE_HEIGHT / 2);
    });

    cvs.addEventListener('mousedown', handleMouseClick);
}

function computerMovement() {
    var p2yCentre = p2y + (PADDLE_HEIGHT / 2);
    if (p2yCentre < by - 35) {
        p2y += 6;
    } else if (p2yCentre > by + 35) {
        p2y -= 6;
    }
}

function ballReset() {
    if (score1p >= WINNING_SCORE || score2p >= WINNING_SCORE) {
        showingWinScreen = true;
    }

    bx = cvs.width / 2;
    by = cvs.height / 2;
    vx = -vx;
}

function drawNet() {
    for (var i = 0; i < cvs.height; i += 40) {
        paddle(cvs.width / 2 - 1, i, 2, 20, 'white');
    }
}

function paddle(x, y, w, h, color) {
    ctx.fillStyle = color;
    ctx.fillRect(x, y, w, h);
}

function ball(x, y, r, color) {
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.arc(x, y, r, 0, Math.PI * 2, true);
    ctx.fill();
}
