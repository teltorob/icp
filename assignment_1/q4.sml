  
fun indSqrt(n)=
let 
  val m = n div 4
   fun isqrt(i)=
     if (i < 2) then i
     else
       if ((i * i) <= m) andalso m < (i + 1) * (i + 1) then i
       else isqrt(i - 1)
in n = isqrt(n)
end;
