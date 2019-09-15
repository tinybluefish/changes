import time

class MyTimer:

    isActive = false

    def __init__(self, name, time) :
        self.name = name
        self.timeLeft = time
        print("Created timer: " + name)

    def display() :
        update()
        print(name + ": " + timeLeft)

    def stop() :
        update()
        isActive = false
        self.timeLeft = self.timeLeft

    def start() :
        update()
        isActive = true
        lastStarted = int(round(time.time() * 1000))

    def update() :
        

t = MyTimer("Bob", 123)

t1 = Timer(


