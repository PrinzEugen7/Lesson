//離散時間状態方程式
Ad=[0 1;-1 0];
Bd=[0;1];
Cd=[1 1];
x0=[1;0;0;1];

//離散時間システムの定義
Plant=syslin('d',Ad,Bd,Cd);

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

