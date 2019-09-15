#!/usr/bin/python

# Each cell is part of a Block, a Row and a Column
class Cell(object):

    possibles = []
    Block block
    Row row
    Col col

    def __init__(self, xloc, yloc, b, r, c):
#        print("Initializing cell with %d and %d" % (xloc, yloc))
        self.possibles = [1,2,3,4,5,6,7,8,9]
        self.x = xloc
        self.y = yloc
        self.block = b
        self.row = r
        self.col = c

    # Drop the specified number from the list of possibles and then return
    # either 0 if there are multiple possibilities left OR the one
    # remaining possibility
    def drop(this, number):
#        print("Before: %s" % this.possibles)
        if number in this.possibles:
            this.possibles.remove(number)
#        print("After: %s" % this.possibles)

        # Now...if we managed to get down to one possible, update the
        # b/c/r

        if (this.isFixed(number)):
            block.
            
        return this.isFixed()

    def isFixed(this):
#        print("There are %d possibles in %s" % (len(this.possibles), this.possibles))
        if (len(this.possibles) == 1):
            return this.possibles[0]
        else:
            return 0

    def fixAs(this, num):
        this.possibles = [num]
#        print("Fixed: %s" % this)
        
    def couldBe(this, number):
#        print(this.possibles)
#        print("Num to check: %d" % number)
        if (number in this.possibles):
            return True
        else:
            return False

    def printCell(self):
        outList = ['[']
        
        for i in range(1,10):
            if self.couldBe(i):
                outList.append(i.__str__())
            else:
                outList.append('-')
            if i != 9:
                outList.append(',')
                
        outList.append(']')
        
        print(''.join(outList), end="")

    def __repr__(self):
        return "cell(%d,%d): %s" % (self.x, self.y, self.possibles) 

    @staticmethod
    def testMe():
        print ("Testing Cell")
        c1 = Cell(1,2)
        print ("Built cell: %s" % c1)
        print("Cell might be 10...%s" % c1.couldBe(10))
        print("Cell might be 1...%s" % c1.couldBe(1))
        print("Cell might be 5...%s" % c1.couldBe(5))
        print("Removing 5...")
        c1.drop(5)
        print("Cell might be 5...%s" % c1.couldBe(5))
        print("Removing 5...again...")
        print("Cell might be 5...%s" % c1.couldBe(5))
        c1.drop(1)
        print("Cell fixed?: %s" % c1.isFixed())
        c1.drop(2)
        print("Cell fixed?: %s" % c1.isFixed())
        c1.drop(3)
        print("Cell fixed?: %s" % c1.isFixed())
        c1.drop(4)
        print("Cell fixed?: %s" % c1.isFixed())
        c1.drop(6)
        print("Cell fixed?: %s" % c1.isFixed())
        c1.drop(8)
        print("Cell fixed?: %s" % c1.isFixed())
        c1.drop(9)
        print("Cell fixed?: %s" % c1.isFixed())
        c1.printCell()

        
Cell.testMe()
