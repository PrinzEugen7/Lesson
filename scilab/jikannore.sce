clear all
s = %s/2/%pi;
j = %i;
L = 1;
frq = logspace(-4,3,1000);
for i = 1:1000;
  G = exp(-j*frq(i)*L)-1;
  g_G(i) = 20*log10(abs(G));
end
cl = 1;
plot2d(frq,g_G,cl,logflag = "ln"...
,rect = [1e-3,-60,1e2,20]);
G2 = (2.1*s)/(1+s);
sysG2 = syslin('c',G2);
[frq1,rep] = repfreq(sysG2,frq);
[db,phi] = dbphi(rep);
plot2d(frq,db,2,logflag = "ln",rect = [1e-3,-60,1e2,20]);