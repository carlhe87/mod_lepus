#! /usr/bin/python
# -*- coding: utf-8 -*-

"""Module Intro: 

This Module is used for
"""
import sys
import os
from mod_input_mtd import input_seq #just temporary use for debug

def permutation(nk, mode="p"):
    """
    permutation and combination calculator
       
    input:
        nk:   (n, k) n>=k, both <int>
        mode:  "p"->permutation, "c"->combination 
    output: 
        type <int>
    Errormessage:
        n<k error
        unexpected error 
    """
    n, k = nk
    if n < k:
        return "Error: n < k"
    if mode == "c":
        return factorial(n)/factorial(n-k)/factorial(k)
    elif mode == "p":
        return factorial(n)/factorial(n-k)
    else: 
        return "Error: unexpected"


def factorial2(n):
    # 0!=1!=1, also n<0 error proof 
    if n < 2: return 1
    else: return n * factorial(n-1)
        
def factorial(n):
    a=1
    for i in range(1,n+1): a*=i
    return a

def binominal_item(nkab=(1,1,"a","b")):
    """generate kth binomial item
       
        According to binominal theorem:
            (a+b)^n = sum(binominal_item|k), k in [0,n]
                    binominal_item|k = c(n,k) * a^(n-k) * b^k
    """
    n, k, a, b = nkab
    print "{} {}^{} {}^{}".format(permutation((n, k), mode="c"),a,n-k,b,k)
    return permutation((n, k), mode="c"),a,n-k,b,k
    
def binominal_item_test(nkab):
    n, k, a, b = nkab
    sum = 0
    for k in range(n+1):
        arg=n,k,a,b
        print type(arg), arg
        coefficient,a,a_factor,b,b_factor = binominal_item(arg)
        sum += coefficient * a**a_factor * b**b_factor
    print "test:{}, ref:{}".format(sum, (a+b)**n)

#main
def _main(*argv): pass

if __name__ == "__main__": 
    #sys.exit(_main(*sys.argv))
    from timeit import timeit as t
    from guppy import hpy
    h= hpy()

    f1=factorial
    f2=factorial2
    print t("f1(100)", setup ="from __main__ import f1", number = 10000)
    print t("f2(100)", setup ="from __main__ import f2", number = 10000)
    print h.iso(f1)
    print h.iso(f2)
    print h.heap()
    print h.heap().more
    print h.heap().more
    #with open("temp.txt","r+") as doc:
    #    doc.write(str(h.heap())) 
