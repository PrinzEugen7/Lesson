// Poneゲームのクラス
class Pone {
    // 初期化
    init() {
        this.mouseX = 0; // マウスのx座標
        this.mouseY = 0; // マウスのy座標
        this.paddleW = 10; // パドルの幅
        this.paddleH = 100; // パドルの高さ
        this.vx = 10; // ボールの速さ(x方向)
        this.vy = 4; // ボールの速さ(y方向)
        this.cvs = null;
        this.ctx = null;
        this.score1p = 0; // 1P(プレイヤー)のスコア
        this.score2p = 0; // 2P(CPU)のスコア
        this.scoreMax = 3; // スコアの最大値
        this.gameSet = false; // ゲームセットフラグ
        this.bx = 50; // ボールのx座標
        this.by = 50; // ボールのy座標
        this.p2y = 250; // 2Pのy座標
        this.p1y = 250; // 1Pのy座標
        this.fps = 60; // フレームレート
    }
    // 各物体の動きを計算
    move() {
        if (this.gameSet) {
            return;
        }

        this.cpu();

        this.bx += this.vx;
        this.by += this.vy;

        if (this.bx < 0) {
            if (this.by > this.p1y && this.by < this.p1y + this.paddleH) {
                this.vx = -this.vx;

                var dy = this.by - (p1y + this.paddleH / 2);
                this.vy = dy * 0.35;
            } else {
                this.score2p++;
                this.resetBall();

            }
        }

        if (this.bx > this.cvs.width) {
            if (this.by > this.p2y && this.by < this.p2y + this.paddleH) {
                this.vx = -this.vx;

                var dy = this.by - (this.p2y + this.paddleH / 2);
                this.vy = dy * 0.35;
            } else {
                this.score1p++;
                this.resetBall();

            }
        }

        if (this.by > this.cvs.height || this.by < 0) {
            this.vy = -this.vy;
        }
    }
    // 各物体の描画
    draw() {
        this.screen(0, 0, this.cvs.width, this.cvs.height, '#111');
        this.line(this.cvs.width / 2, 0, this.cvs.width / 2, this.cvs.height, '#333');
        if (this.gameSet) {
            this.gameSetWindow();
            return;
        }
        this.paddle(0, this.p1y, this.paddleW, this.paddleH, '#22aa22');
        this.paddle(this.cvs.width - this.paddleW, this.p2y, this.paddleW, this.paddleH, '#aa2222');
        this.ball(this.bx, this.by, 10, '#ddd');
        this.ctx.font = "50px Georgia";
        this.ctx.fillText(this.score1p, 100, 100);
        this.ctx.fillText(this.score2p, this.cvs.width - 100, 100);
    }

    ball(x, y, r, color) {
        this.ctx.fillStyle = color;
        this.ctx.beginPath();
        this.ctx.arc(x, y, r, 0, Math.PI * 2, true);
        this.ctx.fill();
    }

    paddle(x, y, w, h, color) {
        this.ctx.fillStyle = color;
        this.ctx.fillRect(x, y, w, h);
    }

    screen(x, y, w, h, color) {
        this.ctx.fillStyle = color;
        this.ctx.fillRect(x, y, w, h);
    }

    line(x1, y1, x2, y2, color) {
        this.ctx.beginPath();
        this.ctx.strokeStyle = color;
        this.ctx.moveTo(x1, y1);
        this.ctx.lineTo(x2, y2);
        this.ctx.closePath();
        this.ctx.stroke();
    }
    resetBall() {
        if (this.score1p >= this.scoreMax || this.score2p >= this.scoreMax) {
            this.gameSet = true;
        }

        this.bx = this.cvs.width / 2;
        this.by = this.cvs.height / 2;
        this.vx = -this.vx;
    }
    // CPUの動き
    cpu() {
        var p2yCentre = this.p2y + (this.paddleH / 2);
        if (p2yCentre < this.by - 35) {
            this.p2y += 6;
        } else if (p2yCentre > this.by + 35) {
            this.p2y -= 6;
        }
    }
    gameSetWindow() {
        if (this.score1p >= this.scoreMax) {
            this.ctx.fillStyle = '#aa2222';
            this.ctx.fillText("You're WINNER!", 150, 200);
        } else {
            this.ctx.fillStyle = '#2222aa';
            this.ctx.fillText("You're LOSEER!", 200, 200);
        }
        this.ctx.font = "25px Georgia";
        this.ctx.fillText("Continue? [Yes:click window]", 350, 500);
    }
    // マウスの位置
    mousePos(evt) {
        var rect = this.cvs.getBoundingClientRect();
        var root = document.documentElement;
        this.mouseX = evt.clientx - rect.left - root.scrollLeft;
        this.mouseY = evt.clientY - rect.top - root.scrollTop;
    }
    // マウスクリック時の処理
    mouseClick(evt) {
        // ゲームセット状態なら再スタート
        if (this.gameSet) {
            this.cvs.clearRect(0, 0, this.cvs.width, this.cvs.height);
            this.gameSet = false;
            this.init();
            this.play();
        }
    }

    play(pone) {
        this.cvs = document.getElementById('pone');
        this.ctx = this.cvs.getContext('2d');
        setInterval(function () {
            pone.move();
            pone.draw();
        }, 1000 / this.fps);
        // マウスポインタ移動イベント
        document.addEventListener('mousemove', function (evt) {
            pone.mousePos(evt);
            pone.p1y = pone.mouseY - (pone.paddleH / 2);
        });
        // マウスクリックイベント
        document.addEventListener('mousedown', pone.mouseClick);
    }
}

// ゲーム開始ボタン押されたら開始
window.onclick = function () {
    var pone = new Pone();
    pone.init();
    pone.play(pone);
}
