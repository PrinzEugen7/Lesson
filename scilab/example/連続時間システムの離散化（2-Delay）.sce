//状態方程式
Ac=[0 1;-1 0];
Bc=[0;1];
Cc=[1 1];
x0=[1;0;0;1];

//サンプリング周期
T=0.01;
//m=0.2

//線形システムを定義(cは連続，dは離散)
sc=syslin("c",Ac,Bc,Cc,0);

//連続時間線形システムの離散化
sd=dscr(sc,T);
//sd2=dscr(sc,T+m*T);

//状態方程式の係数行列の表示
[Ad,Bd,Cd,Dd]=abcd(sd);
//[Ad2,Bd2,Cd2,Dd2]=abcd(sd2);

//離散時間システムの定義
Plant=syslin('d',Ad,Bd,Cd,Dd);

//オブザーバに基づく推定状態フィードバック

//オブザーバゲインを求める
poles=[0.1,0.3];
gt=ppol(Ad',Cd',poles);
g=gt';
//spec(Ad-g*Cd)

//フィードバックゲインを求める
poles=[0.8,0.9];
kt=ppol(Ad,Bd,poles);
k=-kt;
//spec(Ad+Bd*lk)

//オブザーバの設計
Cnt=obscont(Plant,k,-g); 
ExClosed = Plant/.(-Cnt);

//グラフの表示
//シミュレーション時間
t=0:10; v=0*t;
//離散時間系のシミュレーション
x=ltitr(ExClosed(2),ExClosed(3),v,x0);
xset("window",0); clf(); 
plot2d(t',[x(1,:)',x(3,:)'])
xtitle("Extended closed loop response","time [s]","state variables x1 and hat x1")
xset("window",1); clf(); 
plot2d(t',[x(2,:)',x(4,:)'])
xtitle("Extended closed loop response","time [s]","state variables x2 and hat x2")


