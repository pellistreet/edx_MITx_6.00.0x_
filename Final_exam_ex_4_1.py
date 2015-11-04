# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:02:00 2015

@author: EPellichero
"""
'''PROBLEM 4 PART 1 - EDX  MITx 6.00.01.X FINAL EXAM

Write a function called getSublists, which takes as parameters a list of integers named L and an integer named n. 
•assume L is not empty
•assume 0 < n <= len(L)

This function returns a list of all possible sublists in L of length n without skipping elements in L. The sublists in the returned list should be ordered in the way they appear in L, with those sublists starting from a smaller index being at the front of the list.

Example 1, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] and n = 4 then your function should return the list [[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]

Example 2, if L = [1, 1, 1, 1, 4] and n = 2 then your function should return the list [[1, 1], [1, 1], [1, 1], [1, 4]]'''


#iteratvie

def getSublists(L,n):
    finallist=[]
    for i in range(len(L)):
        if len(L[i:(i+n)])==n:
            finallist.append(L[i:(i+n)])
    return finallist


#recursvie code

def getSublists2(L,n):
    if len(L)==n:
        return L
    else:
        return [L[:n]] + getSublists(L[1:],n)
        
print getSublists([10, 4, 6, 8, 3, 4, 5, 7, 7, 2],n=4)
print getSublists2([10, 4, 6, 8, 3, 4, 5, 7, 7, 2],n=1)

    
    