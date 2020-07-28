# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:14:13 2020

@author: Saffa Fatima
"""

## 1. Brute force solution with two loops ##

def is_unique1(string):
    
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
            
    return True
    
    
    
# =============================================================================
# ## check code ##
# 
# is_unique("GeeksforGeeks") >> False
# is_unique('unique') >> False
# is_unique('sad') >> True

## Time complexity ##

#O(n^2)

# =============================================================================
  
## 2. Sorting algorithm ##

def is_unique2(string):
    string = sorted(string)
    
    for i in range(len(string)):
        for j in range(i+1, len(string)):
           if string[i] == string[j]:
              return False
    return True
    
# =============================================================================
# Time complexity is O(nlogn) for the sorting algorithm used in Python's sorted() function
# =============================================================================


## 2. Using ASCII ##

def is_unique3(string):
    max_char = 256        #for extended ASCII, will be more if we use Unicode
    check_array = [False]*256
    
    ## quick check method for sstring length can't be greater than no. of unique chars available
    
    if len(string) > max_char:
        return False
    
    for s in string:
        for i in range(len(check_array)):
            if ord(s) == i and check_array[i] == False:
                check_array[i] = True
    
    cnt = 0
    for i in range(len(check_array)):
        if check_array[i] == True:
            cnt +=1

    if cnt < len(string):
        return False
    else:
        return True            
            
                
   # =============================================================================
# Time complexity is O(n) as the no. of operations required increase in direct proportion to length of the input string 
# =============================================================================             
