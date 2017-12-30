A=[1 9;6 9];
B=[5 7;9 5];
M=[0 9;2 8];
R=[1 0;0 6];
P=[2 0;0 9];
spec(M);
spec(R)
spec(P)
A'*R*B*M;
spec(A'*R*B*M);
(B*M)'*R*A;
spec((B*M)'*R*A);
2*inv((R+B'*P*B))
inv((2*R+2*B'*P*B))