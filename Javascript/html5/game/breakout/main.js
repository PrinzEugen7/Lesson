

// ゲームシステム変数
var game = {
        ctx: null,
        time: 0,
        status: 'play',
        pos: {x: 0, y: 0},
        fps: 30,
        cvs: {width: 640,height: 480},                                                                                                          // キャンバス：サイズ
        paddle: {size: 50, color: '#00dd00'},                                                                                           // パドル：サイズ, 色
        ball: {size: 5, speed: 5, color: '#dd0000'},                                                                            // ボール：サイズ, 速さ, 色
        block: {size: 5, speed: 5, color: '#00aa00', strokeColor: '#003300'},   // ブロック：サイズ, 速さ, 色(内部), 色(外枠)
        background: {color: '#001100'},                                                                                                 // 背景: 色
        score: {point: 0, color: '#00aa00'}
};

// パドル管理用のクラス
function Paddle() { this.initialize.apply(this, arguments); }
Paddle.prototype = {
        size: 0, x: 0, y: 0,
        // コンストラクタ
        initialize: function(option) { this.size = option.size; },
        // 移動
        move: function(x, y) {
                this.x = x;
                this.y = y;
                if (this.x < 0) {
                        this.x = 0;
                }
                if (this.x > game.cvs.width) {
                        this.x = game.cvs.width;
                }
        },
        // 描画
        draw: function() {
                game.ctx.fillStyle = game.paddle.color;
                game.ctx.fillRect(this.x - (this.size / 2), this.y, this.size, 10);
        }
};

// ボール管理用のクラス
function Ball() { this.initialize.apply(this, arguments); }
Ball.prototype = {
        size: 0, x: 0, y: 0, dx: 0, dy: 0,
        // コンストラクタ
        initialize: function(option) {
                this.size = option.size;
                this.x = option.x;
                this.y = option.y;
                this.dx = option.speed;
                this.dy = option.speed;
        },
        // 移動テスト
        moveTest: function() {
                return {
                        x: this.x + this.dx,
                        y: this.y + this.dy
                };
        },
        // 移動
        move: function() {
                var pos = this.moveTest();
                if (pos.x < this.size || pos.x > game.cvs.width - this.size) {
                        this.dx *= -1;
                }
                if (pos.y < this.size || pos.y > game.cvs.height - this.size) {
                        this.dy *= -1;
                }
                this.x += this.dx;
                this.y += this.dy;
        },
        // 描画
        draw: function() {
                game.ctx.fillStyle = game.ball.color;
                game.ctx.beginPath();
                game.ctx.arc(this.x, this.y, this.size, 0, 2 * Math.PI, false);
                game.ctx.fill();
                game.ctx.closePath();
        }
};

// ブロック管理用のクラス
function Block() { this.initialize.apply(this, arguments); }
Block.prototype = {
        x: 0, y: 0, w: 0, h: 0, flag: true,
        // コンストラクタ
        initialize: function(option) {
                this.x = option.x;
                this.y = option.y;
                this.w  = option.w;
                this.h = option.h;
        },
        // 描画
        draw: function() {
                if (this.flag) {
                        game.ctx.fillStyle = game.block.color;
                        game.ctx.fillRect(this.x, this.y, this.w, this.h);
                        game.ctx.strokeStyle = game.block.strokeColor;
                        game.ctx.strokeRect(this.x, this.y, this.w, this.h);
                }
        }
};

// マウスイベント
window.addEventListener('mousedown', function(e) {}, false);
window.addEventListener('mousemove', function(e) {
        var rect = e.target.getBoundingClientRect();
        game.pos.x = e.clientX - rect.left;
        game.pos.y = e.clientY - rect.top;
}, false);

function main() {
        var cvs = document.getElementById('sample');
        game.ctx = cvs.getContext('2d');
        // ボール初期化
        var ball = new Ball({size: game.ball.size, x: 0, y: 0,speed: game.ball.speed});
        ball.x = 320;
        ball.y = 400;
        ball.dx = game.ball.speed;
        ball.dy = game.ball.speed * -1;
        // パドル初期化
        var paddle = new Paddle({size: game.paddle.size});
        // ブロック初期化
        var blocks = [];
        var col = 14;           // ブロックの列数
        var row = 10;           // ブロックの行数
        for (var i = 0; i < row; i++) {
                for (var j = 0; j < col; j++) {
                        blocks[i * col + j] = new Block({x: 40 + j * 40,　y: 40 + i * 20,　w: 40,　h: 20});
                }
        }
        // アニメーション
        setInterval(function() {
                if (game.status != 'play') {
                        game.ctx.fillStyle = game.background.color;
                        game.ctx.fillRect(0, 0, game.cvs.width, game.cvs.height);
                        game.ctx.fillStyle = '#aa0000';
                        game.ctx.font = '60px "Arial Black"';
                        if (game.status == 'gameover') {
                                game.ctx.fillText('Game Over', 160, 230);
                                game.ctx.fillText('Score : ' + game.score.point, 160, 320);
                        } 
                        else if (game.status == 'clear') {
                                game.ctx.fillText('Game Clear', 160, 230);
                                game.ctx.fillText('Score : ' + game.score.point, 160, 320);
                        }
                        return;
                }
                game.time++;                                                                                                                            // 時間加算
                game.ctx.clearRect(0, 0, game.cvs.width, game.cvs.height);      // キャンバスクリア
                game.ctx.fillStyle = '#001100';                                                                         // キャンバスを塗りつぶす
                game.ctx.fillRect(0, 0, game.cvs.width, game.cvs.height);
                paddle.move(game.pos.x, game.cvs.height - 40);                                  // パドル移動
                // パドル当たり判定
                if (ball.y >= paddle.y - ball.size && ball.y <= paddle.y + ball.size && ball.x >= paddle.x - (paddle.size / 2) && ball.x <= paddle.x + (paddle.size / 2)) {
                        ball.dy *= -1;
                }
                // ボール移動テスト
                var pos = ball.moveTest();
                // ブロック当たり判定
                for (var i = 0; i < row; i++) {
                        for (var j = 0; j < col; j++) {
                                if (blocks[i * col + j].flag) {
                                        // 左からヒット
                                        if ( ball.x <= blocks[i * col + j].x && blocks[i * col + j].x <= pos.x && pos.y >= blocks[i * col + j].y && pos.y <= blocks[i * col + j].y + blocks[i * col + j].h ) {
                                                ball.dx *= -1;
                                                blocks[i * col + j].flag = false;
                                                game.score.point += 5;
                                        }
                                        // 右からヒット
                                        if (pos.x <= blocks[i * col + j].x + blocks[i * col + j].w && blocks[i * col + j].x + blocks[i * col + j].w <= ball.x && pos.y >= blocks[i * col + j].y && pos.y <= blocks[i * col + j].y + blocks[i * col + j].h) {
                                                ball.dx *= -1;
                                                blocks[i * col + j].flag = false;
                                                game.score.point += 5;
                                        }
                                        // 上からヒット
                                        if (ball.y <= blocks[i * col + j].y && blocks[i * col + j].y <= pos.y && pos.x >= blocks[i * col + j].x && pos.x <= blocks[i * col + j].x + blocks[i * col + j].w) {
                                                ball.dy *= -1;
                                                blocks[i * col + j].flag = false;
                                                game.score.point += 10;
                                        }
                                        // 下からヒット
                                        if (pos.y <= blocks[i * col + j].y + blocks[i * col + j].h && blocks[i * col + j].y + blocks[i * col + j].h <= ball.y && pos.x >= blocks[i * col + j].x && pos.x <= blocks[i * col + j].x + blocks[i * col + j].w) {
                                                ball.dy *= -1;
                                                blocks[i * col + j].flag = false;
                                                game.score.point += 1;
                                        }
                                }
                        }
                }
                ball.move();            // ボール移動
                // アウト判定
                if (ball.y >= game.cvs.height - ball.size) { game.status = 'gameover'; }
                var flag = true;                // クリア判定
                for (var i = 0; i < row; i++) {
                        for (var j = 0; j < col; j++) {
                                if (blocks[i * col + j].flag) {
                                        flag = false;
                                }
                        }
                }
                if (flag) { game.status = 'clear'; }  // クリア状態に
                paddle.draw();                                                  //バドル描画
                ball.draw();                                                            //ボール描画
                // ブロック描画
                for (var i = 0; i < row; i++) {
                        for (var j = 0; j < col; j++) {
                                blocks[i * col + j].draw();
                        }
                }
        // スコア描画
        game.ctx.fillStyle = game.score.color;
        game.ctx.font = '30px "Arial Black"';
        game.ctx.fillText('score : ' + game.score.point, 10, game.cvs.height - 10);
        }, parseInt(1000 / game.fps));
}

