#!/usr/bin/env python

def problem01(inp):
    """
    Shop prices example
    """
    pass

def problem02(inp):
    """

    Write a program which will convert the given RGB input values 
    into the corresponding hexadecimal values preceded with a # sign.

    A single input sequence will be provided, consisting of RGB values 
    separated by "-". Each RGB combination will be separated by ",". 
    The outputs should be comma separated and in uppercase. Also, it 
    should be checked if a color value is greater than 255. In such a 
    case, the output for the corresponding combination should be given 
    as INVALID.

    Note: Number 10, which has a hexadecimal value of A, must be 
    represented as "0A" and not as "A". The same rule applies to 
    other single digit hexadecimal numbers.

    Example

    Suppose the following input sequence is supplied to the 
    program:

    12-13-14,45-156-23,234-234-256

    The output of the program should be:

    #0C0D0E,#2D9C17,INVALID
    """
    seq = inp.split(',')
    hex_list = []
    for rgb in seq:
        nmbrs = rgb.split('-')
        nmbrs = [int(i) for i in nmbrs]
        if sum(nmbrs) > 255:
            hex_list.append('INVALID')
        else:
            hex_rep = '#'
            for h in nmbrs:
                h = hex(h).upper()
                h = h.replace('0X', '')
                if len(h) < 2:
                    h = '0' + h
                hex_rep += h
            hex_list.append(hex_rep)
    return ','.join(hex_list)

def problem03(lo, hi):
    """
    Write a program which will find all such numbers which are 
    divisible by 7 but are not a multiple of 5, between 1000 and 
    1200 (both included). The numbers obtained should be printed 
    in a comma separated sequence on a single line.
    """
    pass_number = []
    for num in xrange(lo, hi + 1):
        if num % 7 == 0 and num % 5 != 0:
            pass_number.append(str(num))
    return ','.join(pass_number)

def problem04(inp):
    """
    Write a program that accepts a comma separated sequence of words 
    as input and prints the words in a comma separated sequence after 
    sorting them alphabetically.

    Suppose the following input is supplied to the program: 

    order,hello,would,test

    Then, the output should be:

    hello,order,test,would
    """
    work_list = inp.split(',')
    work_list = sorted(work_list)
    return ','.join(work_list)

def problem05(inp):
    """
    Write a program to calculate the bill amount, in cents, for the 
    units of power consumed. Following are the rates applicable:

    1. First 0-100 units: 60 cents per unit
    2. Next 200 units: 70 cents per unit
    3. Beyond 300 units: 80 cents per unit

    The program should accept three different usage unit readings.

    Example

    If the following inputs are supplied:

    305
    180
    120

    Then, the output should be:

    20400
    11600
    7400
    """
    amt = int(inp)
    if amt < 100:
        return amt * 60
    else:
        amt -= 100
        charge = 60 * 100
        if amt < 200:
            return charge + (amt * 70)
        else:
            amt -= 200
            charge += 200 * 70
        return charge + amt * 80
    


def problem06(inp):
    """
    Write a program which will accept 4 digit binary numbers each 
    separated by a comma as its input and then check whether they 
    are divisible by 3 or not. The numbers that are divisible by 
    3 are to be printed, separated by a comma.

    Example

    Suppose the following input is given to the program:

    0011,0100,0101,1001

    Then, the output of the program should be:

    0011, 1001
    """
    inp_list = inp.split(',')
    out_list = [i for i in inp_list if int(i, 2) % 3 == 0]
    return ','.join(out_list)

def problem07(inp):
    """
    Write a program which takes 4 inputs, where each input consists of 2 
    numbers in the format x,y. You are required to print a two dimensional 
    array having x rows and y columns for each input. The elements of the 
    arrays should be whole numbers starting from 1 and incrementing by 1. 

    Example

    Suppose the following 4 inputs are given to the program:

    2,2
    2,3
    3,3
    3,4

    Then, the output of the program should be:

    [[1, 2], [3, 4]]
    [[1, 2, 3], [4, 5, 6]]
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    """
    dims = inp.split(',')
    dims = [int(i) for i in dims]
    outlist = []
    counter = 1
    for x in range(dims[0]):
        inlist = []
        for y in range(dims[1]):
            inlist.append(counter)
            counter += 1
        outlist.append(inlist)
    return outlist
            
def problem08(inp):
    """
    Write a program which will receive a comma separated sequence 
    of numbers. Suppose a particular input number is represented by "n". 
    The program should find the greatest "n" digit number which is 
    divisible by "n" itself. The output should be comma separated.

    The greatest n digit number is denoted by "n" number of 9's occurring, 
    like, the greatest 6 digit number is 999999 or the greatest 4 digit 
    number is 9999. Note that although the greatest 4 digit number is 
    9999, it is not divisible by 4, but 9996 is divisible by 4.

    Examples

    If the following input is supplied to program:

    2,5,8

    Then, the output should be:

    98,99995,99999992
    """
    num = inp.split(',')
    num = [int(i) for i in num]
    outlist = []
    for digit in num:
        max_num = int('9' * digit)
        outlist.append(str(max_num - (max_num % digit)))
    return ','.join(outlist)

from math import sqrt

def problem09(inp):
    """
    Write a Program which calculates and prints the Optimal Order Quantity 
    for the production of LCD sets. Following is the formula to calculate 
    Optimal Order Quantity:

    Q = Square root of [(2 * C * D)/H]

    Following are the fixed values of C and H:

    Fixed cost per order, denoted by C, is $50.
    Annual holding cost per unit, denoted by H, is $30.

    Only the Annual Demand Quantity (D) of the product varies. The values of 
    D are supplied as input to your program in a comma separated sequence.

    Example

    Let us assume the following comma separated input sequence is given to 
    the program:

    100,150,180

    The output of the program should be:

    18,22,24

    Note: If the output received is in decimal form, it should be rounded off to
    its nearest value (for example, if the output received is 26.0, it should be
    printed as 26)
    """
    C = 50
    H = 30

    d = inp.split(',')
    d = [int(i) for i in d]
    Q_list = []
    for D in d:
        Q_list.append( str(int(sqrt( (2 * C * D) / H))) )       
    return ','.join(Q_list)
import re

def problem10(inp):
    '''
    A bank has implemented criteria for determining whether the transaction 
    passwords typed by customers of the bank are valid or not.

    Following are the criteria for checking the transaction password:

    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    1. At least 1 letter between [A-Z]
    3. At least 1 character from [*#+@]
    4. Minimum length of transaction password: 4
    5. Maximum length of transaction password: 6
    6. No space is allowed

    Write a program which will accept a sequence of comma separated transaction 
    passwords and will check them according to the bank's criteria. Passwords 
    that match the criteria are to be printed, each separated by a comma.

    Example

    If the following passwords are given as input to the program:

    Abc@1,a B1#,2w3E*,2We#3345

    Then, the output of the program should be:

    Abc@1,2w3E*
    '''
    test_list = inp.split(',')
    r = re.compile('[a-zA-Z0-9\*#\+@]')
    passed = []
    for element in test_list:
        if len(element) < 4 or len(element) > 6:
            continue
        test_string = ''
        for ch in element:
            if r.match(ch):
                test_string += ch
        if len(test_string) == len(element):
            passed.append(element)
    return ','.join(passed)

if __name__ == '__main__':
    print 'Problem 02'
    print '----------'
    l = 1000
    inparm = ('12-13-14,45-156-23,234-234-256')
    print 'input: ', inparm
    print 'output: ', problem02(inparm)
    print
        
    print 'Problem 03'
    print '----------'
    l = 1000
    h = 1200
    print 'input: low=', l, 'high=', h 
    print 'output: ', problem03(l, h)
    print
        
    print 'Problem 04'
    print '----------'
    inparm = 'order,hello,would,test'
    print 'input: ', inparm
    print 'output: ', problem04(inparm)
    print
        
    parms = (305,180,120)
    print 'Problem 05'
    print '----------'
    for inparm in parms:
        print 'input: ', inparm
        print 'output: ', problem05(inparm)
    print
        
    print 'Problem 06'
    print '----------'
    inparm = '0011,0100,0101,1001'
    print 'input: ', inparm
    print 'output: ', problem06(inparm)
    print
        
    parms = ( '2,2', '2,3', '3,3', '3,4')
    print 'Problem 07'
    print '----------'
    for inparm in parms:
        print 'input: ', inparm
        print 'output: ', problem07(inparm)
    print
        
    print 'Problem 08'
    print '----------'
    inparm = '2,5,8'
    print 'input: ', inparm
    print 'output: ', problem08(inparm)
    print
        
    print 'Problem 09'
    print '----------'
    inparm = '100,150,180'
    print 'input: ', inparm
    print 'output: ', problem09(inparm)
    print
        
    print 'Problem 10'
    print '----------'
    inparm = 'Abc@1,a B1#,2w3E*,2We#3345'
    print 'input: ', inparm
    print 'output: ', problem10(inparm)
        
