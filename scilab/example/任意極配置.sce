//”CˆÓ‹É”z’u
A=[1 0;0 2]; b=[1;1];
poles=[-2,-3];
k_=ppol(A,b,poles);
k=-k_
spec(A+b*k)

