def lerp(a, b, t):
    return a + t * (b - a)


class BBox:
    def __init__(self, x: float, y: float, w: float, h: float) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __repr__(self) -> str:
        return f"BBox({self.x}, {self.y}, {self.w}, {self.h})"
