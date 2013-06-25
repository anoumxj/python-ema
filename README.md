python-ema
==========
for exponiential moving average calculation


  here we use 'exponential moving average' to predict the next time period data value
    # EMA Formula:

         X(0),X(1),X(2),...,X(t-1) : data-sets total with "t" time-period-points

         EMA(1) = X(0) // initial point            -> 1 terms
         EMA(2) = EMA(1) + alpha*(X(1)-EMA(1))
                = alpha*[X(1)] + (1-alpha)*X(0)    -> 2 terms
         EMA(3) = EMA(2) + alpha*[X(2)-EMA(2)]
                = [alpha*X(1)+(1-alpha)*X(0)] + alpha*[X(2)-(alpha*X(1)+(1-alpha)*X(0))]
                = alpha*[X(2)+(1-alpha)*X(1)] + (1-alpha-alpha-alpha^2)*X(0)
                = alph*[X(2)+(1-alpha)*X(1)] + (1-alpha)^2*X(0)     -> 3 terms
           .
           .
         EMA(t) = alpha*X(t-1) + (1-alpha)*EMA(t-1) = EMA(t-1) + alpha*[X(t-1) - EMA(t-1)]
                  = ...
                                    1st               2nd                     3rd                            (t-1)-th
                  = alpha*[ (1-alpha)^(0)*X(t-1) + (1-alpha)^(1)*X(t-2) + (1-alpha)^(2)*X(t-3) + ...+ (1-alpha)^(t-2)*X(t-(t-1)) ]
                            t-th
                    + (1-alpha)^(t)*X(0)

         where alpha: smoothing factor, alpha=1/len(list)
               X(t-1) is observation value at time (t-1) period
               EMA(t-1) is prediction value at time (t-1) periods
               EMA(t) is prediction value at time t periods
