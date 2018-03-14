## Program : File Module
## Developer : Trevor Murphy
## Date : start(23/02/2017)
## Description : File module.

import time

def prnt_line(name, strtln = 0, endln = 'o', wait = 0):
    '''Takes name adds '.txt'''
    name += '.txt'
    '''if endln = 'a' prints to end of file'''
    if endln == 'a':
        '''set endln equal to the amount of lines in the file'''
        endln = len(open(name).readlines())
        '''if endln = 'o' prints next(one)line in file'''
    elif endln == 'o':
        endln = strtln + 1
    '''with the specified file opend as object f'''
    with open(name, 'r') as f:
        '''all lines in the file are written to ctnt(content)'''
        ctnt = f.readlines()
        '''While the strtln is less than the endln'''
        while strtln < endln:
            '''print ctnt in strtln index'''
            print(ctnt[strtln], end='')
            '''Increment strtln to print the next line'''
            strtln += 1
            time.sleep(wait)
            
## Find number of lines in a file
## return lif(linesInFile)
def lines_in(name):
    name += '.txt'
    linesInFile = len(open(name).readlines())
    return linesInFile

def get_ctnt(name):
    name += '.txt'
    with open(name, 'r')as f:
        ctnt = f.readlines()   
    return ctnt

def s_txt(x = 79):
    if x > 79:
##        print('Dont do that!')
        x = 79
    for i in range(x):
        if i == x - 1:
            print('-')
        else:
            print('-', end='')

def main():
    pass
main()
