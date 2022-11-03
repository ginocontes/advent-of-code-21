import re

class Plane(object):
    def __init__(self, max_x, max_y, lines):
        self.max_x = max_x
        self.max_y = max_y
        self.lines = lines
        self.res = self.build_plane()
        self.check_plane()

    def build_plane(self):
        res = []
        for x in range(self.max_x):
            col = []
            for y in range(self.max_y):
                col += ["0"]
            res += [col]
        return res
    
    def print_plane(self):
        # for x in range(self.max_x):
        #     for y in range(self.max_y):
        #         print(f"{self.res[x][y]}", end = " ")
        #     print()
        print(self.res)

    def check_plane(self):
        """Here we define the logic for modifying the plane with the lines"""
        for line in self.lines:
            points_to_check = line.intersect()
            for point in points_to_check:
                self.res[point[0]][point[1]] = str(int(self.res[point[0]][point[1]]) + 1)

    def check_overlaps(self):
        counter = 0
        for row in self.res:
            for col in row:
                if int(col) > 1:
                    counter += 1
        return counter


            
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def check_vertical_or_horizontal(self):
        return self.p1.x == self.p2.x or self.p1.y == self.p2.y
    
    def check_vertical_or_horizontal_or_diagonal(self):
        return self.check_vertical_or_horizontal() or self.is_diagonal()
    
    def is_diagonal(self):
        return abs(self.p1.x - self.p2.x) == abs(self.p1.y - self.p2.y)


    def intersect(self):
        """gets the range of numbers as [(0,0), (0,1) that need to be checked in the plane"""
        res = []
        if self.p1.y == self.p2.y:
            for i in range(min(self.p1.x, self.p2.x), max(self.p1.x, self.p2.x)+1):
                res += [(self.p1.y, i)]
            return res
        elif self.p1.x == self.p2.x:
            for j in range(min(self.p1.y, self.p2.y), max(self.p1.y, self.p2.y)+1):
                res += [(j, self.p1.x)]
            return res
        elif self.is_diagonal():
            # logic to handle diagonal lines in here.
            if( self.p1.x < self.p2.x and self.p1.y > self.p2.y )or (self.p1.x > self.p2.x and self.p1.y < self.p2.y):
                for i in range(abs(self.p1.x - self.p2.x)+1):
                    for j in range(abs(self.p1.x - self.p2.x) +1):
                        if i + j == (abs(self.p1.x - self.p2.x)):
                            res += [(min(self.p1.y, self.p2.y) + i, min(self.p1.x, self.p2.x) + j)]
            else:
                if self.p1.x < self.p2.x:
                    for i in range(abs(self.p1.x - self.p2.x)+1):
                        res += [(self.p1.y + i, self.p1.x + i)]
                else:
                    for i in range(abs(self.p1.x - self.p2.x)+1):
                        res += [(self.p2.y + i, self.p2.x + i)] 
            # print(res)
            return res
                # res += [(self.p1.x+i, self.p1.y+i)]
                # produce all possible pairs (x,y) that sum up to the absolute difference between x and y
        
        return None



def parse_lines(lines):
    res = []
    for line in lines:
        rexp = re.search("(\d+,\d+) -> (\d+,\d+)", line)
        parr = rexp.group(1).split(",")
        p2arr = rexp.group(2).split(",")
        p1 = Point(int(parr[0]), int(parr[1]))
        p2 = Point(int(p2arr[0]), int(p2arr[1]))
        l = Line(p1, p2)
        if l.check_vertical_or_horizontal_or_diagonal(): #first exercise
            res += [l]
            if l.is_diagonal(): 
              diag = l.intersect()
            #   print(l.intersect(), " = ", f"({l.p1.x},{l.p1.y}) -> ({l.p2.x},{l.p2.y})")
              
    plane = Plane(1000, 1000, res)
    # plane.print_plane()
    print(plane.check_overlaps())
    return res


def solve_problem(lines): 
    points = parse_lines(lines)
    # print(points)

def parse_input():
    with open("./day5-input.txt") as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
        solve_problem(lines)

def main():
    parse_input()


if __name__ == '__main__': 
    main()