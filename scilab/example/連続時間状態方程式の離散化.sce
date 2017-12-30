//˜A‘±ŠÔó‘Ô•û’ö®‚Ì—£U‰»
A=[0 1;0 0]; b=[0;1]; c=[1 0]; d=0; T=0.2;
cont=syslin('c',A,b,c);
disc=dscr(cont,T);
[A_d,b_d,c_d,d_d]=abcd(disc)

