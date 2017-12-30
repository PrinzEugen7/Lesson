s=%s;
L=0.5;
G0=1/((s+1)*(s+4));
DelayN=1-(L/2)*s+(1/10)*(L*s)^2-(1/120)*(L*s)^3;
DelayD=1+(L/2)*s+(1/10)*(L*s)^2+(1/120)*(L*s)^3;
Delay=DelayN/DelayD