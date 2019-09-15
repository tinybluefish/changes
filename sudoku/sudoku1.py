#!/usr/bin/python

import cell as c
import block as b

# initialize a full, open grid
# stick a bunch of numbers in based on the puzzle
# cycle through all the cells, trying to figure out what the thing looks like (the tricky bit)

class Grid(object):

    blocks = [[b.Block(0,0),b.Block(1,0),b.Block(2,0)],
              [b.Block(0,1),b.Block(1,1),b.Block(2,1)],
              [b.Block(0,2),b.Block(1,2),b.Block(2,2)]]

    def solve(this):
        return 1
        # start loop until solved
            # iterate over all the cells in order (initially...)
            # for each cell, check block, column, row and remove possibilities
            # if we get down to one, update the block, row, col accordingly
            
        
    
            

# Next step
def makeChecklist():
    return [0,0,0,0,0,0,0,0,0]
        

def checkBox(box):
    print ("Checking box")
    checkList = makeChecklist()
    row = 1
    for row in grid :
        cell = 1
        for cell in row :
            print (cell)



#checkBox(grid)

#print(makeChecklist())


