s=%s;
G=1/(s*(s+10)*(s+2));
K=poly(0,'K');
CharEq=denom(G)+numer(G)
rth=routh_t(G,K)


