//Å“KƒŒƒMƒ…ƒŒ[ƒ^
A=[0 1;0 -1]; b=[0;1]; c=[1 0]; x0=[1;0]; 
r=1; Q=diag([4 1]);
k=lqr(syslin('c',A,b,[sqrtm(Q);[0 0]],[0;0;sqrt(r)]))
Ak_sys=syslin('c',A+b*k,b,c);
t=0:0.01:10; v=0*t;
[y,x]=csim(v,t,Ak_sys,x0); u=k*x;
xset("window",0); clf(); 
plot2d(t',x')
xtitle("Optimal regulator response","time [s]","state variables x1 and x2")
xset("window",1); clf(); 
plot2d(t',u')
xtitle("Optimal regulator input","time [s]","control input u")

