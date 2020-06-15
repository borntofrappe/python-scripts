class Rectangle:
    def __str__(self):
        w = str(self.width)
        h = str(self.height)
        return 'Rectangle(width=' + w + ', height=' + h + ')'

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape):
        width_inside = self.width // shape.width
        height_inside = self.height // shape.height
        return width_inside * height_inside


class Square(Rectangle):
    def __str__(self):
        # additional check to guarantee that the width and height match
        w = str(self.width)
        h = str(self.height)
        if w == h:
            return 'Square(side=' + w + ')'
        else:
            return 'Mis-shaped Square(width=' + w + ',height=' + h + ')'

    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    # modify the width and height setters to guarantee the two measures are updated together
    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)
