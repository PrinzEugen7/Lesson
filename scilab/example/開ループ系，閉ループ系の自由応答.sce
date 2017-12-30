//開ループ系，閉ループ系の自由応答
A=[1 0;0 2]; b=[1;1]; c=[1 1]; x0=[1;0.1];
k=stabil(A,b,[-2,-3]);
A_sys=syslin('c',A,b,c); Ak_sys=syslin('c',A+b*k,b,c);
t=0:0.01:5; u=0*t; v=0*t;
[yop,xop]=csim(u,t,A_sys,x0);
xset("window",0); clf(); 
plot2d(t',xop')
xtitle("Open loop response","time [s]","state variables x1 and x2")
[ycl,xcl]=csim(v,t,Ak_sys,x0);
xset("window",1); clf(); 
plot2d(t',xcl')
xtitle("Closed loop response","time [s]","state variables x1 and x2")

