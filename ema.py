#!/usr/bin/env python2.4
def ema(list, alpha=None):
    ema_data = []
    # reversed order for the whole list (big->small)
    rev_list = sorted(list,reverse=True)

    if not alpha:
       alpha = 2/(len(rev_list)+1) # defaults
    if (alpha<0) or (alpha>1):
       raise ValueError("0 < smoothing factor <= 1")
    alpha_bar = float(1-alpha)
    print "alpha: %s, alpha_bar: %s" % (alpha, alpha_bar)
    num_terms_list = [rev_list[:i] for i in range(1,len(rev_list)+1)]
    for nterms in num_terms_list:
        # calculate 1st~(t-1)-th terms corresponding exponential factor
        pre_exp_factor = [float(alpha_bar**(i-1)) for i in range(1,len(nterms))]
        print "pre_alpha: %s" % pre_exp_factor
        # calculate the ema at the next time periods
        ema = alpha*sum(map(lambda a,b: a*b, pre_exp_factor, nterms[:-1])) + (alpha_bar**(len(nterms)-1))*nterms[-1]
        print ema
        ema_data.append(ema)    
    return ema_data

if __name__ == "__main__":
     # this is your code
     ober = [97.6, 95.1, 90.3, 92,5, 89.8, 92.7, 94.4, 96.2]
     print "random_num=%s" % ober
     print "ema=%s" % ema(ober)
