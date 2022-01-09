import math

#a class is like a template
#calling the class can give us new instances
class Coordinate:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def print_coordinate(self):
        return "({0}, {1})".format(self.x, self.y)

class Spline:
    def __init__(self, coordinate_list):
        self.coordinates = coordinate_list

    def get_slope(self):
        first = self.coordinates[0]
        last = self.coordinates[-1]

        return (last.x - first.x) / (last.y - first.y)

    def offset_x(self, offset):
        slope = self.get_slope()

        for point in self.coordinates: 
            point.x = (offset / math.sqrt(point.x))

    def offset_y(self, offset):
        slope = self.get_slope()

        for point in self.coordinates: 
            point.y = (offset * math.sqrt(point.y))

    def print_spline(self):
        output = []
        for coordinate in self.coordinates:
                output.append(coordinate.print_coordinate())    

        return ", ".join(output)


if __name__ == '__main__':
    
    #creating a coordinate list
    coordinate_list = []
    coordinate_list.append(Coordinate(1,2))
    coordinate_list.append(Coordinate(2,3))
    coordinate_list.append(Coordinate(3,4))

    #creating a spline
    spline = Spline(coordinate_list)
    print("spline coordinate:", spline.print_spline())
    print("spline slope:", spline.get_slope())

    #translate spline
    print("Translating the spline")
    spline.offset_x(5)
    spline.offset_y(12)
    print("new coordinate:", spline.print_spline())
    print("new slope:", spline.get_slope())
    
