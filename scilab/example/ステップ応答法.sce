//ステップ応答法
s=%s;
t=0:0.01:15;
L=0.5;
G0=1/((s+1)*(s+4));
DelayN=1-(L/2)*s+(1/10)*(L*s)^2-(1/120)*(L*s)^3;
DelayD=1+(L/2)*s+(1/10)*(L*s)^2+(1/120)*(L*s)^3;
Delay=DelayN/DelayD;
G=Delay*G0;
Le=0.6;Re=0.156;
//P
C=1/(Re*Le)
//PI
//C=0.9/(Re*Le)*(1+1/(3.3*Le*s));
//PID
//C=1.2/(Re*Le)*(1+1/(2*Le*s)+0.5*Le*s)
Tc=G*C/(1+G*C);
sys=syslin('c',Tc);
y=csim("step",t,sys);
clf(); plot2d(t,y)

