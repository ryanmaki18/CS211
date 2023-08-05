'''Python 3.10.7 (v3.10.7:6cc6b13308, Sep  5 2022, 14:02:52) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.'''
from numbers import Number

class Point:
    def __init__(self, x: Number, y: Number):
        """method that takes two integers, x and y, and stores them as instance variables self.x and self.y"""
        self.x = x
        self.y = y

    def move(self, dx: int, dy: int):
        """Move to (x+dx, y+dy)"""
        self.x += dx
        self.y += dy

    def __eq__(self, other: "Point") -> bool:
        """If the x and y fields of the self object and the other Point object are equal, __eq__ should return True"""
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        canvas.plot_point(self.x, self.y)


class Rect:
    def __init__(self, ll: Point, ur: Point):
        self.ll = ll
        self.ur = ur

    def __add__(self, other: "Rect") -> "Rect":
        """Union of two rectangles is a rectangle that covers both of them"""
        assert isinstance(other, Rect)
        return Rect(Point(min(self.ll.x, other.ll.x), min(self.ll.y, other.ll.y)),
                    Point(max(self.ur.x, other.ur.x), max(self.ur.y, other.ur.y)))

#    def overlaps(self, other: "Rect") -> bool:
#        if

    def draw(self, color="white"):
        canvas.plot_rect(self.ll.x, self.ll.y, self.ur.x, self.ur.y, color=color)


def main():
    print("In main")
    p = Point(300, 200)
    r = p + Point(50,75)
    print(p)
    print(r)
    s = Rect(p, r)

    r2 = Rect(Point(325, 225), Point(400, 400))

    r3 = s + r2
    r3.draw()
    s.draw(color="red")
    r2.draw("blue")
    canvas.finish()

if __name__ == "__main__":
    main()