//ナイキスト線図
s=%s;
H=1; G=(s+2)^2/((s+1)*(s^2-2*s+4));
GH=G*H;
sys=syslin("c",GH);
clf();
nyquist(sys)
CharEq=denom(GH)+numer(GH)
roots(CharEq)

