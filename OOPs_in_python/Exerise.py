"""Write OOP classes to handle the following scenarios:

A user can create and view 2D coordinates.
A user can find the distance between two coordinates.
A user can find the distance of a coordinate from the origin.
A user can check whether a point lies on a given line.
A user can find the distance between a given 2D point and a given line."""

class Point:

    def __init__(self,x,y):
        self.x_cod=x
        self.y_cod=y
    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)
    def euclidean_distance(self,other):
        return ((self.x_cod-other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    def distance_from_origin(self):
        return self.euclidean_distance(Point(0,0))
class Line:
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C
    def __str__(self):
        return '{}x+{}y+{}=0'.format(self.A,self.B,self.C)
    def point_on_line(line,point):
        if line.A*point.x_cod+line.B*point.y_cod+line.C==0:
            return "Point lies on the line"
        else:
            return "does not lie on the line"
p1=Point(1,2)
l=Line(1,1,-2)
print(l)
print(l.point_on_line(p1))
 