clear all
s = %s/2/%pi;
Ks = [2 2.5 3];
colors = [1 2 3];
for i = 1:3;
  K = Ks(i)
  G = K/(1+s);
  sysG = syslin('c',G);
  frq = logspace(-4,2,100);
  [frq1,rep] = repfreq(sysG,frq);
  [db,phi] = dbphi(rep);
  scf(1)
  cl = colors(i);
  subplot(2,1,1)
  plot2d(frq1,db,cl,logflag="ln",rect=[1e-3,-80,1e2,10]);
  xgrid()
  subplot(2,1,2)
  plot2d(frq1,phi,cl,logflag="ln",rect=[1e-3,-100,1e2,10]);
  xgrid()
  scf(2)
  nyquist(sysG,0,100);
  end