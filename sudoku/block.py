#!/usr/bin/python

import cell as c

# There are three key structures: Block, Row, Column.
# Each has a set of nine cells and must contain each digit 1-9 only once each.
# Each is tracked using a simple list.


class Grid(object):

    rows = []
    cols = []
    blocks = []

    # create all the cells we need for the grid
    cells = []
    for x in range(0,9):
        for y in range(0,9):
            tc = c.Cell(x,y)
            #Which r/b/c?
            rows[y][x] = tc
            cols[x][y] = tc
            
            

    # Nice! Ok - got a full grid, what's next...
    # Need to put each cell into the right b/r/c

    
    
    # put them into the relevant row, col, blocks
    
    #rows
    #cols
    #blocks
    

class Row(object):

    cells = []

    # initialize with starting cell (0,0 top left) co-ordinates
    def __init__(self, xloc, yloc):
        



#Each Block has co-ordinates ( 1 <= x/y <= 3) and contains 9 Cells
# By default each Cell is set up 'open' (all 1-9 possibles in place)





class Block(object):

    


    uncertainCells = 9

    def __init__(self, xloc, yloc):
#        print("Initializing block with %d and %d" % (xloc, yloc))
        self.cells = [[c.Cell(0,0),c.Cell(1,0),c.Cell(2,0)],
                      [c.Cell(0,1),c.Cell(1,1),c.Cell(2,1)],
                      [c.Cell(0,2),c.Cell(1,2),c.Cell(2,2)]]
        self.x = xloc
        self.y = yloc

    def cell(self, x, y):
#        print("Getting cell %d,%d" % (x,y))
        #Intentional x/y flip...
#        print("Returning cell: %s" % self.cells[y][x])
        return self.cells[y][x]

    def row(self, y):
        return self.cells[y]

    #Have to create a new list here... :( TODO: optimize!
    def col(self, x):
        return [self.cells[0][x],self.cells[1][x],self.cells[2][x]]

    def dropCellNum(self, x, y, num):
        result = self.cell(x,y).drop(num)

#        print("Removed %d from %d,%d - got back: %d" % (num, x, y, result))

        # Fun bit: if we're down to a single possibility in a cell
        # we need to update the rest of the cells in this block to
        # remove this number
        if (result > 0):
            self.clearNum(result)

    def clearNum(self, num):
#        print("Clearing: %d" % num)
        for row in self.cells:
#            print("..clearing cells: %s" % row)
            for cell in row:
#                print("....clearing cell: %s" % cell)
                if not cell.isFixed():
#                    print("....dropping %d from %s" % (num, cell))
                    cell.drop(num)
#                    print("dropped!")
#                else:
#                    print("....cell fixed, not clearing")

    def isComplete(this):
        return this.uncertainCells == 0

    def print(self):
        for row in self.cells:
            for cell in row:
                cell.printCell()
            print("")


    def __repr__(self):
        return "block(%d,%d): %s" % (self.x, self.y, self.cells) 
        
    @staticmethod
    def testMe():
        print ("Testing Block")
        b1 = Block(0,1)
#        print ("Built: %s" % b1)
#        print("Block is complete: %s" % b1.isComplete())
#        b1.cell(1,1).drop(5)        
#        b1.dropCellNum(1,1,6)
#        print("Row %d: %s" % (1, b1.row(1)))
#        print("Col %d: %s" % (1, b1.col(1)))

        # Now fix all the cells in the grid but one, leaving 5
        # available so it should auto-select

        fixNum = 1
        for row in b1.cells:
            for cell in row:
                if fixNum != 5:
                    cell.fixAs(fixNum)
                    b1.clearNum(fixNum)
                fixNum = fixNum + 1

        b1.print()

        #should end up auto-selecting the middle cell to be 5

                    

                
        

Block.testMe()
