#!/usr/bin/env python

def ema(list, alpha=None):
    """
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

         where alpha: smoothing factor
               X(t-1) is observation value at time (t-1) period
               EMA(t-1) is prediction value at time (t-1) periods
               EMA(t) is prediction value at time t periods
    """
    ema_data = []

    # reversed order for the whole list (big->small)
    rev_list = sorted(list,reverse=True)

    if not alpha:
       alpha = 1/len(rev_list) # defaults
    if (alpha<0) or (alpha>1):
       raise ValueError("0 < smoothing factor <= 1")
    alpha_bar = float(1-alpha)

    num_terms_list = [rev_list[:i] for i in range(1,len(rev_list)+1)]
    #print num_terms_list
    for nterms in num_terms_list:
        # calculate 1st~(t-1)-th terms corresponding exponential factor
        pre_exp_factor = [alpha_bar**(i-1) for i in range(1,len(nterms))]
        #print pre_exp_factor

        # calculate the ema at the next time periods
        ema_data.append(alpha*sum(map(lambda a,b: a*b, pre_exp_factor, nterms[:-1])) + \
                         (alpha_bar**len(nterms))*nterms[-1])
                         
    return sorted(ema_data)

if __name__ == "__main__":
     # this is your code
     print ema(range(1,5000))
     
     
