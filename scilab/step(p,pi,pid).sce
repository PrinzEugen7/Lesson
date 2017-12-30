s = %s;
t = 0:0.01:15;
L = 0.5;
G0 = 1/((s+1)*(s+4));
DelayN = 1-(L/2)*s+(1/10)*(L*s)^2-(1/120)*(L*s)^3;
DelayD = 1+(L/2)*s+(1/10)*(L*s)^2+(1/120)*(L*s)^3;
Delay = DelayN/DelayD;
G = Delay*G0;
Le = 0.6;Re = 1.56;
Cp = 1/(Re*Le);
Tcp = G*Cp/(1+G*Cp);
sysp = syslin('c',Tcp);
yp = csim("step",t,sysp);
Cpi = 0.9/(Re*Le)*(1+1/(3.3*Le*s));
Tcpi = G*Cpi/(1+G*Cpi);
syspi = syslin('c',Tcpi);
ypi = csim("step",t,syspi);
Cpid = 1.2/(Re*Le)*(1+1/(2*Le*s)+0.5*Le*s);
Tcpid = G*Cpid/(1+G*Cpid);
syspid = syslin('c',Tcpid);
ypid = csim("step",t,syspid);
clf();plot2d(t,yp)
plot2d(t,ypi)
plot2d(t,ypid)