function xdot = subfile(t,X)
  global A B D S xi Xt Xbox Tbox i h hit
  n = i;
  i = i+1;
  sigma = S*X;
  if sigma < 0
    v = 1;
  end
  if sigma > 0
    v = -1;
  end
  if sigma == 0
    v = 0;
  end
  if t > h
    delay = t-h;
    for j = hit:n
      if Tbox(1,j) > delay
        Xt = Xbox(:,j-1);
        hit = j-1;
        break;
      end
    end
  end
    Xbox(:,i) = X;
  Tbox(1,i) = t;
  u = (S*B)*((S*A*X)+(S*D*Xt)-xi*v)

  xdot = A*X+D*Xt+B*u
endfunction