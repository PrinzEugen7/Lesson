//ステップ応答シミュレーション
A=[-1 0;1 -2]; b=[0;1]; c=[1 1]; x0=[1;0];
sys=syslin('c',A,b,c);
t=0:0.01:10;
y=csim('step',t,sys,x0);
clf(); plot2d(t,y,rect=[0,0,10,1.5])
xtitle("Step responce","time [s]","output y")

