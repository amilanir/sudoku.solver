#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 17:58:28 2020

@author: amilaperera
"""
import numpy as np

Sudoku = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

#print(np.matrix(Sudoku))

def possible(y,x,n):
    global Sudoku
    for i in range(0,9):
        if Sudoku[y][i] == n:
            return False
    for i in range(0,9):
        if Sudoku[i][x] == n:
            return False   
    x0 = (x//3)*3
    y0 = (y//3)*3    
    for i in range(0,3):
        for j in range (0,3):
            if Sudoku[y0+i][x0+j] == n:
                return False          
    return True
    
def solver():
    global Sudoku
    for y in range(9):
        for x in range(9):
            if Sudoku[y][x] == 0:
                for n in range (1,10):
                    if possible(y,x,n):
                        Sudoku[y][x] = n
                        solver()
                        Sudoku[y][x] = 0
                return
    print("The solution : \n")
    print(np.matrix(Sudoku))
    input("Any other Soulutions?")
                    
solver()                   