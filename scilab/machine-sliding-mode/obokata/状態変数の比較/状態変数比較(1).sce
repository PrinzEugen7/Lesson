//------------------------------------------------
//■2013.12.14 秋山殿
// 比例到達則+対称化
//------------------------------------------------

//▼2自由度機械システムの定義
L=[1 0; 0 1];    //アクチュエータに加わる力を表す行列(正則行列)
m1=1; m2=2;      //質量
k1=1; k2=2;  //ばね定数
d1=1; d2=2;  //減衰定数
M=[m1 0; 0 m2];  //
K = [k1 -k1; -k1 k1+k2];
D = [d1 -d1; -d1 d1+d2];
AF = [zeros(2,2) eye(2,2); -M*K -M*D];
BF = [zeros(2,2); L ];
//▼比例到達速のパラメータ
R=[6 0; 0 6];
Q=[0.5 0; 0 0.5];
//▼切換超平面Sの定義（設計済）
S1=[4 0; 0 3];  //(対称1)
//S1=[3 0; 0 4];  //(対称2)
//S1=[1 2; -3 6];  //(非対称1)
//S1=[2 2; -1 5];  //(非対称2)
S2=[eye(2,2)]
S = [S1 S2];

//▼状態変数の初期値
X=[0.5 1.0 3.5 4.0]';
//▼マッチング条件を満たさない不確かさ
D = [0.2 0.4;0.1 0.2;0.1 0.15;0.3 0.2]; //マッチングを満たさない
//D = [zeros(2,2); L ]; //マッチングを満たす
F=[1.4 0.8 1.1 1.2;0.7 1.1 0.9 1.3];
dA=D*F
disp(dA)
AF=AF+dA //不確かさをAに加える

//AF=AF+dA //不確かさをAに加える
// 離散化システムの定義
h = 0.02; // サンプリング時間
cont = syslin('c',AF,BF,S);
disc = dscr(cont,h);
[A,B,Sd] = abcd(disc);

lines(0)
// ▼シミュレーション1
for i = 1:250;
  // 切換関数
  sigma = S*X;
  // 等価制御入力(通常)  
  U = -inv(S*BF)*{(S*AF*X)+Q*sign(sigma)+R*sigma};
  dX =A*X+B*U;
  // データの保存
  Xh1(:,i) = X;
  Uh1(:,i) = U; // 弄った
  Sh1(:,i) = sigma;// 弄った
  X = dX;
end


// ▼ 対称でないスライディングモード制御系
X=[0.5 1.0 3.5 4.0]';
S1=[1 2; -3 6];
S = [S1 S2];

for i = 1:250;
  sigma = S*X;
  // 等価制御入力(通常)  
  U = -inv(S*BF)*{(S*AF*X)+Q*sign(sigma)+R*sigma};
  dX =A*X+B*U;
  // データの保存
  Xh3(:,i) = X;
  Uh3(:,i) = U; // 弄った
  Sh3(:,i) = sigma;// 弄った
  X = dX;
end

clf()

// ▼グラフの描画
tt =0:h:(i-1)*h;

//▼グラフ1
scf(0);
xset("wdim",800,700)
xset("thickness",3)
xset("font",1,5)
plot(tt,Xh1(1,:),tt,Xh3(1,:),'r'),xgrid(2)
l=legend(["${\rm Symmetrical\hspace{7pt}SMC}$";"${\rm Asymmetrical\hspace{7pt}SMC}$"],1);
l.font_size = 6;
xset("thickness",1)
xlabel('${\rm Time\hspace{4pt}[s]}$','fontsize',6,'fontname','Times')
ylabel('$x_1$','fontsize',7,'fontname','Times')

//▼グラフ2
scf(1);
xset("wdim",800,700)
xset("thickness",3)
xset("font",1,5)
plot(tt,Xh1(2,:),tt,Xh3(2,:),'r'),xgrid(2)
l=legend(["${\rm Symmetrical\hspace{7pt}SMC}$";"${\rm Asymmetrical\hspace{7pt}SMC}$"],1);
l.font_size = 6;
xset("thickness",1)
xlabel('${\rm Time\hspace{4pt}[s]}$','fontsize',6,'fontname','Times')
ylabel('$x_2$','fontsize',7,'fontname','Times')


//▼グラフ3
scf(2);
xset("wdim",800,700)
xset("thickness",2)
xset("font",1,5)
plot(tt,Xh1(3,:),tt,Xh3(3,:),'--'),xgrid(2)
l=legend(["${\rm Symmetrical\hspace{7pt}SMC}$";"${\rm Asymmetrical\hspace{7pt}SMC}$"],1);
l.font_size = 6;
xset("thickness",1)
xlabel('${\rm Time\hspace{4pt}[s]}$','fontsize',6,'fontname','Times')
ylabel('$x_3$','fontsize',7,'fontname','Times')

//▼グラフ4
scf(3);
xset("wdim",800,700)
xset("thickness",2)
xset("font",1,5)
plot(tt,Xh1(4,:),tt,Xh3(4,:),'--'),xgrid(2)
l=legend(["${\rm Symmetrical\hspace{7pt}SMC}$";"${\rm Asymmetrical\hspace{7pt}SMC}$"],1);
l.font_size = 6;
xset("thickness",1)
xlabel('${\rm Time\hspace{4pt}[s]}$','fontsize',6,'fontname','Times')
ylabel('$x_4$','fontsize',7,'fontname','Times')

clear tt Uh1 Xh1 Sh1;
