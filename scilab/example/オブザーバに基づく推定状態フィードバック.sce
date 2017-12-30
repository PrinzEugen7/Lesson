//オブザーバに基づく推定状態フィードバック
A=[1 0;0 2]; b=[1;1]; c=[1 1];
k=[12 -20]; g=[-30;42];
Plant=syslin('c',A,b,c);
Cnt=obscont(Plant,k,-g); 
ExClosed = Plant/.(-Cnt);
spec(ExClosed('A'))
t=0:0.01:10; v=0*t; x0=[1;0;0;1]
[y,x]=csim(v,t,ExClosed,x0);
xset("window",0); clf(); 
plot2d(t',[x(1,:)',x(3,:)'])
xtitle("Extended closed loop response","time [s]","state variables x1 and hat x1")
xset("window",1); clf(); 
plot2d(t',[x(2,:)',x(4,:)'])
xtitle("Extended closed loop response","time [s]","state variables x2 and hat x2")

