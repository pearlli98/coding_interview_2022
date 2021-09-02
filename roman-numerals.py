题目：https://www.hackerrank.com/contests/projecteuler/challenges/euler089/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT

l = int(input())
strings = [input() for i in range(l)]

d = {
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000
}

def roman2num(roman):
    if len(roman) == 0:
        return 0
    i = 0
    res = 0
    while i < len(roman):
        if i + 1 < len(roman) and d[roman[i+1]] > d[roman[i]]:
            res += d[roman[i+1]] - d[roman[i]]
            i += 2
        else:
            res += d[roman[i]]
            i += 1
    return res

def num2roman(num):
    out = ''
    for val, c in sorted(d.items(), key = lambda x:x[-1], reverse = True):
        if num >= c:
            repeat, num = divmod(num, c)
            out += repeat * val
    return out
    
for i in strings:
    num = roman2num(i)
    rom = num2roman(num)
    print(rom)
        
    
        

