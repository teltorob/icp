fun sub(a, b) =
        let
                fun subhelper([], [], carry) =
                        if (carry=0) then [] else [] 
                  | subhelper(xs,[],carry) =
                  if carry = 0 
                  then xs
                  else subhelper(xs,[carry],0)

                  | subhelper([],ys,carry) = subhelper(ys,[carry],0)
                  | subhelper(x::xs,y::ys,carry) =
                          let
                                val z = x-y-carry
                          in
                          if (z >= 0)
                          then
                                (z)::subhelper(xs,ys,0)
                            else
                            (z + 10)::subhelper(xs,ys,1)
                          end
        in
                subhelper(a,b,0)
        end;