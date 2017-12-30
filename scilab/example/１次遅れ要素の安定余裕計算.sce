//‚PŽŸ’x‚ê—v‘f‚ÌˆÀ’è—]—TŒvŽZ
s=%s;
G=1/(s+1); H=1; GH=G*H;
sys=syslin('c',GH);
croots=roots(denom(GH)+numer(GH));
sys=syslin('c',GH);
gm=g_margin(sys)
pm=p_margin(sys)
xset("window",1);clf();bode(sys,0.01,10);
xset("window",2);clf();nyquist(sys);

