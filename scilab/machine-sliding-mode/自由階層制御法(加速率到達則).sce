// ▼定数行列
AF = [-2 1 0;0 0 1;0 0 1];
BF = [0;0;1];
S = [1 2 1]; //切換超平面

// ▼離散化システム
h = 0.02; // サンプリング時間
cont = syslin('c',AF,BF,S);
disc = dscr(cont,h); // 離散化
[A,B,Sd] = abcd(disc);

// ▼初期条件
X=[0.5 1.0 1.5]'; // 初期値
K=15;
a=0.7;

// ▼ ----- スライディングモード制御 -----
lines(0)
for i = 1:250;
  sigma = S*X; // 切換関数
  U = -inv(S*BF)*{(S*AF*X)+K*(abs(sigma)^a)*sign(sigma)}; //制御入力
  dX =A*X+B*U; 
  
  // ▼データを保存
  Xh1(:,i) = X;
  Uh1(1,i) = U;
  Sh1(1,i) = sigma;
  X = dX;
  // ▲データを保存
end
// ▲ ----- スライディングモード制御 -----

clf()
tt =0:h:(i-1)*h;

// ▼ ----- グラフ作成 -----

//▼ 第2象限
subplot(222),plot(tt,Uh1),xgrid(2)
title('制御入力')
xlabel('Time   [s]')
ylabel('Control Input   [N]')

//▼ 第1象限
subplot(221),plot(tt,Xh1(1,:),tt,Xh1(2,:),tt,Xh1(3,:)),xgrid(2)
title('変数')
xlabel('Time   [s]')
ylabel('Displacement   [m]')

//▼ 第3象限
subplot(223),plot(tt,Sh1),xgrid(2)
title('切換関数')
xlabel('Time   [s]')
ylabel('Swiching Function')
// ▲ ----- グラフ作成 -----

clear tt Uh1 Xh1 Sh1;
