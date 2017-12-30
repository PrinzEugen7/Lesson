//オブザーバの設計
A=[1 0;0 2]; c=[1 1];
poles=[-4,-5];
gt=ppol(A',c',poles);
g=gt'
spec(A-g*c)

