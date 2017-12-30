//------------------------------------------------
//■2013.12.14 秋山殿
// 比例到達則+対称化
//------------------------------------------------

//▼2自由度機械システムの定義
L=[1 0; 0 2];    //アクチュエータに加わる力を表す行列(正則行列)
//L=[1 3; 0 0];    //アクチュエータに加わる力を表す行列(正則でない正方行列)
m1=1; m2=1;      //質量
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
//S1=[4 0; 0 3];  //(対称1)
S1=[3 0; 0 4];  //(対称2)
//S1=[1 2; -3 6];  //(非対称1)
//S1=[2 2; -1 5];  //(非対称2)
S2=[eye(2,2)]
S = [S1 S2];

//▼マッチング条件を満たさない不確かさ
//D = [0.2 0.4;0.1 0.2;0.1 0.15;0.3 0.2]; //マッチングを満たさない
D = [zeros(2,2); L ]; //マッチングを満たす
F=[1 1 1 1;1 1 1 1];
dA=D*F
disp(dA)
AF=AF+dA //不確かさをAに加える
// 離散化システムの定義
h = 0.02; // サンプリング時間
cont = syslin('c',AF,BF,S);
disc = dscr(cont,h);

//▼状態変数の初期値
X=[5.5 7.0 8.5 10.0]';

// ▼コンソールでLG_d, LG_vが対称行列になっているか確認
F={L*inv(S*BF)*S*AF};
//F = L*pinv(L)*inv(S2)*(S*AF)
disp(F);
[A,B,Sd] = abcd(disc);

// ▼シミュレーション
lines(0)
for i = 1:250;
  // 切換関数
  sigma = S*X;
  // 等価制御入力(通常)  
  U = -inv(S*BF)*{(S*AF*X)+Q*sign(sigma)+R*sigma};
  // 等価制御入力(擬似逆行列)
  //U = -pinv(L)*inv(S2)*{(S*AF*X)+Q*sign(sigma)+R*sigma};
  
  dX =A*X+B*U;
  // データの保存
  Xh1(:,i) = X;
  Uh1(:,i) = U; // 弄った
  Sh1(:,i) = sigma;// 弄った
  X = dX;
end

clf()

// ▼グラフの描画
tt =0:h:(i-1)*h;


//▼第1象限：制御入力
scf(0);
xset("wdim",850,600)
xset("thickness",2)
xset("font",1,4)
plot(tt,Uh1(1,:),tt,Uh1(2,:)),xgrid(2)
l=legend(["$u_1$";"$u_2$"],4);
l.font_size = 5;
xset("thickness",1)
xlabel('Time','fontsize',5,'fontname','Times')
ylabel('Control Input','fontsize',5,'fontname','Times')

//▼第2象限：状態変数
scf(1);
xset("wdim",850,600)
xset("thickness",2)
xset("font",1,4)
plot(tt,Xh1(1,:),tt,Xh1(2,:),tt,Xh1(3,:),tt,Xh1(4,:)),xgrid(2)
l=legend(["$x_1$";"$x_2$";"$x_3$";"$x_4$"],1);
l.font_size = 5;
xset("thickness",1)
xlabel('Time','fontsize',5,'fontname','Times')
ylabel('State Variable','fontsize',5,'fontname','Times')

//▼第3象限：切換関数
scf(2);
xset("wdim",850,600)
xset("thickness",2)
xset("font",1,4)
plot(tt,Sh1),xgrid(2)
l=legend(["$\sigma_1$";"$\sigma_2$"],1);
l.font_size = 5;
xset("thickness",1)
xlabel('Time','fontsize',5,'fontname','Times')
ylabel('Swiching Function','fontsize',5,'fontname','Times')

//▼第4象限：位相平面
scf(3);
xset("wdim",850,600)
xset("thickness",2)
xset("font",1,4)
plot(Xh1(1,:),Xh1(3,:),Xh1(2,:),Xh1(4,:)),xgrid(2)
l=legend(["$x_1, x_3$";"$x_2, x_4$"],2);
l.font_size = 5;
xset("thickness",1)
xlabel('$x_1, x_2$','fontsize',6,'fontname','Times')
ylabel('$x_3, x_4$','fontsize',6,'fontname','Times')

clear tt Uh1 Xh1 Sh1;
