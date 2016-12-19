# encoding: utf-8

'''
Created on 2016年12月19日

@author: merk
'''

import fileinput
if __name__ == '__main__':
    
    for line in fileinput.input(inplace=True):
        line=line.rstrip()
        num=fileinput.lineno()
        print '%-40s # %2i' %(line,num)
    