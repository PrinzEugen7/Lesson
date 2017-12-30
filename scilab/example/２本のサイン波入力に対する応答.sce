//‚Q–{‚ÌƒTƒCƒ“”g“ü—Í‚É‘Î‚·‚é‰ž“š
s=%s;
G=1/(1+0.5*s);
t=0:0.01:10;
u1=[3*sin(2*t)];
sys=syslin('c',G);
y1=csim(u1,t,sys);
xset("window",0);clf();plot2d(t',[u1',y1'])
u2=[4*sin(2*sqrt(3)*t)];
y2=csim(u2,t,sys);
xset("window",1);clf();plot2d(t',[u2',y2'])
u12=u1+u2;
y12=csim(u12,t,sys);;
xset("window",2);clf();plot2d(t',[y1',y2',y12'])

