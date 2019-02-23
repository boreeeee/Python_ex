# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def fib(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        result = [0, 1]
        while True:
            num = result[len(result)-1] + result[len(result)-2]
            if num > n:
                break
            else:
                result.append(num)
        
        real_result = ''
        for i in result:
            real_result += str(i) + ' '
            
        return real_result

            
