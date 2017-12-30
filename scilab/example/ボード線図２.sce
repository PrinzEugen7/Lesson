s=%s;
G1=(1+s)/(s^2+s+1);
G2=(1-s)/(s^2+s+1);
t=0:0.1:10;
sys1=syslin("c",G1);
sys2=syslin("c",G2);
y1=csim("step",t,sys1);
y2=csim("step",t,sys2);
xset("window",0);
clf();plot2d(t',[y1',y2'],[1,-9],axesflag=5);
xset("window",1);clf();
bode(sys1,0.01,10);
bode(sys2,0.01,10);

