clear,clc
global A B D S xi Xt Xbox Tbox i h hit
A = [-1 -1;-0 -2];
B = [0;1];
D = [1 0;0.4 1];
R = 1;
Q = [0.79552 -0.0077911;-0.0077911 1.2702];
E = D*inv(R)*D';
P = ricc(A,E,Q,'cont')

S = inv(R)*B'*P
