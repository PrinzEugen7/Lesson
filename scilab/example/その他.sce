s=%s;
G=200/(s^2+4*s+100);
H1=1.5/(s+2);
H2=2.5/(s+2);
rth1=routh_t(G*H1,1)
rth2=routh_t(G*H2,1)
root1=roots(denom(G*H1)+numer(G*H1))
root2=roots(denom(G*H2)+numer(G*H2))
DenomGH2=denom(G*H2)+numer(G*H2)

