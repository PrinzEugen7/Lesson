//------------------------------------------------
//■2013.9.29 秋山殿
// 対称化された最終SMC(極配置)+チャタリング除去
//
//------------------------------------------------

// ▼定数の定義
K=10;//最終SMCのK
k1=1.1; k2=2.2; d1=1.2; d2=2.1;//ばね定数・減衰係数
s11=2; s12=0; s21=0; s22=1;//S1(対称)
L=[1 2; 3 2;]
//s11=3; s12=2; s21=-1; s22=0;//S1(非対称1)

// ▼行列の定義
AF = [0 0 1 0; 0 0 0 1; -k1  k1 -d1 d1; k1 -(k1+k2) d1 -(d1+d2)];
BF = [0 0;0 0;1 2;3 2];
S = [s11 s12 1 0; s21 s22 0 1]; //切換超平面
F={L*inv(S*BF)*S*AF};
Ct=F;
disp(F);
disp(Ct);

// ▼離散化システム //
h = 0.02; // サンプリング時間
cont = syslin('c',AF,BF,S);
disc = dscr(cont,h); // Discretized system //
[A,B,Sd] = abcd(disc);

// ▼初期値 //
X=[0.5 1.0 1.5 2.0]';//初期状態

// --------- ▼シミュレーション計算 ----------
lines(0)
for i = 1:250;
  sigma = S*X; // switching function //
  U = -inv(S*BF)*(S*AF*X)-K*sigma/{norm(sigma)};//等価制御入力
  dX =A*X+B*U;
  
  // ▼データの保存 //
  Xh1(:,i) = X;
  Uh1(:,i) = U; // 弄った
  Sh1(:,i) = sigma;// 弄った
  X = dX;
end

// ▼プロット //
clf()
tt =0:h:(i-1)*h;

// ------ ▼グラフ描画 ------
//▼第1象限
subplot(222),plot(tt,Uh1(1,:),tt,Uh1(2,:)),xgrid(2)
title('制御入力')
xlabel('Time   [s]')
ylabel('Control Input   [N]')
//▼第2象限
//subplot(221),plot(tt,Xh1(3,:),tt,Xh1(4,:)),xgrid(2)
subplot(221),plot(tt,Xh1(1,:),tt,Xh1(2,:),tt,Xh1(3,:),tt,Xh1(4,:)),xgrid(2)
title('変数')
xlabel('Time   [s]')
ylabel('Displacement   [m]')
//▼第3象限
subplot(223),plot(tt,Sh1),xgrid(2)
title('切換関数')
xlabel('Time   [s]')
ylabel('Swiching Function')
// ▼クリア
clear tt Uh1 Xh1 Sh1;
