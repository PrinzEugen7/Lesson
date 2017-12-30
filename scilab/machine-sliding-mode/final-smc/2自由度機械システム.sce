//------------------------------------------------
//■2013.10.09 秋山殿
// 対称化された最終SMC(極配置)+チャタリング除去
//------------------------------------------------

// ▼2自由度機械システムの定義
L=[1 0; 0 1];    //アクチュエータに加わる力を表す行列
k=10;            //到達則のスカラ関数
m1=1; m2=1;      //質量
k1=1; k2=2;  //ばね定数
d1=1; d2=2;  //減衰定数
M=[m1 0; 0 m2];  //
K = [k1 -k1; -k1 k1+k2];
D = [d1 -d1; -d1 d1+d2];
AF = [zeros(2,2) eye(2,2); -M*K -M*D];
BF = [zeros(2,2); L ];

P=4;
Q=1;

// ▼切換超平面Sの定義（設計済）
S1=[4 0; 0 3];  //(対称)
//S1=[1 2; -3 6];  //(非対称1)
//S1=[2 2; -1 5];  //(非対称2)
S2=[eye(2,2)]
S = [S1 S2]; //切換超平面

// ▼コンソールでフィードバックゲインの値を確認
F={L*inv(S*BF)*S*AF};
Ct=F;
disp(F);
disp(Ct);
// ▼離散化システム
h = 0.02; // サンプリング時間
cont = syslin('c',AF,BF,S);
disc = dscr(cont,h); // Discretized system //
[A,B,Sd] = abcd(disc);

// ▼初期値
X=[0.5 1.0 1.5 2.0]';//初期状態

//=========== シミュレーション ==============
lines(0)
for i = 1:250;
  //▼外乱パラメータ
  w=1;t=i;
  //▼SMCの切換関数・制御入力・状態方程式
  sigma = S*X; // switching function //
  U = -inv(S*BF)*{(S*AF*X)+Q*sign(sigma)+P*sigma};//等価制御入力
  dX =A*X+B*U;//+[0; 0; 1 ; 1 ]*0.1*sin(w*t); //状態方程式 
  // ▼データの保存（グラフ用）
  Xh1(:,i) = X;
  Uh1(:,i) = U; // 弄った
  Sh1(:,i) = sigma;// 弄った
  X = dX;
end

// ▼プロット
clf()
tt =0:h:(i-1)*h;

//=========== グラフ描画 ==============
//▼第1象限：制御入力
subplot(222),plot(tt,Uh1(1,:),tt,Uh1(2,:)),xgrid(2)
title('制御入力')
xlabel('Time   [s]')
ylabel('Control Input   [N]')
//▼第2象限：状態変数
//subplot(221),plot(tt,Xh1(3,:),tt,Xh1(4,:)),xgrid(2)
subplot(221),plot(tt,Xh1(1,:),tt,Xh1(2,:),tt,Xh1(3,:),tt,Xh1(4,:)),xgrid(2)
title('状態変数')
xlabel('Time   [s]')
ylabel('Displacement   [m]')
//▼第3象限：切換関数
subplot(223),plot(tt,Sh1),xgrid(2)
title('切換関数')
xlabel('Time   [s]')
ylabel('Swiching Function')
//▼第4象限：位相平面
subplot(224),plot(Xh1(1,:),Xh1(3,:),Xh1(2,:),Xh1(4,:)),xgrid(2)
title('位相平面')
xlabel('x1')
ylabel('x2')
// ▼クリア
clear tt Uh1 Xh1 Sh1;
