# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 13:20:38 2020

@author: Saffa Fatima
"""

#-------------------------------#

'''
Write a function to check whether two given strings are permutation of each other.
'''


## 1. Sorting the strings ##

def is_perm1(str1, str2):
    
    ''':type str1 & str 2: string
       :rtype: Boolean
    '''
    
    n1 = len(str1)
    n2 = len(str2)
    
    
    ## quick check ##
    if n1 != n2:
        return False
    
    str1 = sorted(str1)
    str2 = sorted(str2)
    
    for i in range(0, n1, 1):
        if str1[i] != str2[i]:
            return False
    return True
    

# =============================================================================
# ## Time complexity ##
# is O(n) as the no. of operations required increase in direct proportion to length of the input strings

## Space complexity ##
# Sorting algorithm takes up extra space then the length of the strings (need to check)  
# =============================================================================   



## 2. Comparing the ASCII characters in each string ##

def is_perm2(str1, str2):
    
    ''':type str1 & str 2: string
       :rtype: Boolean
    '''
     
    n1 = len(str1)
    n2 = len(str2)
    
    
    ## quick check ##
    if n1 != n2:
        return False
    
    
    ## Assuming that each item in the string is stored as 8 bits, the maximum ASCII value will be 2^8 = 256
    
    charArr_1 = [0] *256
    charArr_2 = [0] *256
    
    for i in str1:
        for j in range(256):
            if ord(i) == j:
                charArr_1[j] += 1
                
    for i in str2:
        for j in range(256):
            if ord(i) == j:
                charArr_2[j] += 1
                
    
    for i in range(256):
        if charArr_1[i] != charArr_2[i]:
            return False
    return True
                
        
# =============================================================================
# ## Time complexity ##
# is O(n) as the no. of operations required increase in direct proportion to length of the input strings

## Space complexity ##
# O(1) ?
# =============================================================================   
    
    
    
    


# =============================================================================
# checking 
# 
# is_perm('abcd', 'bacd') >> True
# is_perm('abcd', 'bacd') >> False 
# =============================================================================
    
