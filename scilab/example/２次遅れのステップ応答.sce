//
s=%s;
t=0:0.01:50;
G=0.1/((s+0.5)^3);
//C=5; //P
//C=4.5*(1+1/(6.081*s));     //PI
C=6.0*(1+1/(3.65*s)+0.913*s); //PID
Tc=G*C/(1+G*C);
sys=syslin("c",Tc);
y=csim("step",t,sys);
clf(); plot2d(t,y)
