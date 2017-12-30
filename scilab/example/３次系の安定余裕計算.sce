//‚RŽŸŒn‚ÌˆÀ’è—]—TŒvŽZ
s=%s;
G=1/(s*(s^2+2*s+4));
H=20;
croots=roots(denom(G*H)+numer(G*H))
sys=syslin('c',G*H);
gm=g_margin(sys)
pm0=p_margin(sys);
if pm0 < 0 then 
  pm = pm0+180
else
  pm = pm0-180
end
xset("window",0);clf();bode(sys,0.1,1);

