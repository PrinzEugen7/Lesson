A=[2 0 3;0 0 1];
GA=A'*inv(A*A');
Ans=A*GA;
disp(A)
disp(GA)
disp(Ans)


//A=[2 0;1 0;1 1];
//GA=inv(A'*A)*A';
//Ans=A*GA;
//disp(A)
//disp(GA)
//disp(Ans)
