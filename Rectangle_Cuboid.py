
# Define class rectangle
class rectangle(object):

    area = 0 
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return 'length = {} \nwidth = {}'.format(self.length, self.width)

    def area(self):
        return self.length * self.width

    def increase_size(self, l, w):
        self.length += l
        self.width += w

class cuboid(rectangle):

    def __init__(self, length, width, depth):
        super().__init__(length, width)
        self.depth = depth

    def __str__(self):
        return 'length = {} \nwidth = {} \ndepth = {}'.format(self.length, self.width, self.depth)
        # OR - return f"{super().__str__()}\ndepth = {self.depth}"
        
    def volume(self):
        return self.length * self.width * self.depth

    def increase_size(self, l, w, d):
        super().increase_size(l, w)
        self.depth += d


        

# ------------------------------------------
# Test Code
# ------------------------------------------

r1 = rectangle(1, 2)

print(r1)
print('Initial area of r1 is' ,r1.area())
r1.increase_size(1,1)
print(r1)
print('New area of r1 is', r1.area())

c1 = cuboid(1, 2, 3)
print(c1)
print('Initial volume of c1 is', c1.volume())
c1.increase_size(1,1,1)
print('New area of c1 is', c1.volume())
