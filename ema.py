#!/usr/bin/env python

def ema(list, alpha=None):
    ema_data = []

    # reversed order for the whole list (big->small)
    rev_list = sorted(list,reverse=True)

    if not alpha:
       alpha = 1/len(rev_list) # defaults
    if (alpha<0) or (alpha>1):
       raise ValueError("0 < smoothing factor <= 1")
    alpha_bar = float(1-alpha)

    num_terms_list = [rev_list[:i] for i in range(1,len(rev_list)+1)]
    for nterms in num_terms_list:
        # calculate 1st~(t-1)-th terms corresponding exponential factor
        pre_exp_factor = [alpha_bar**(i-1) for i in range(1,len(nterms))]
        # calculate the ema at the next time periods
        ema_data.append(alpha*sum(map(lambda a,b: a*b, pre_exp_factor, nterms[:-1])) + \
                         (alpha_bar**len(nterms))*nterms[-1])                  
    return sorted(ema_data)

if __name__ == "__main__":
     # this is your code
     print ema(range(1,5000))
