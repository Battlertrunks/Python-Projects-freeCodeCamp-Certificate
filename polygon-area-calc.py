class Rectangle:
    width: int
    height: int

    # Assign the width and height of the rectangle
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)

    # Output what the user will view in the terminal
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    # Set the width
    def set_width(self, width):
        self.width = width

        # If sqare, match height's value with width
        if self.__class__.__name__ == 'Square':
            self.height = width

    # Set the height
    def set_height(self, height):
        self.height = height

        # If sqare, match width's value with height
        if self.__class__.__name__ == 'Square':
            self.width = height

    # Get the area by multiplying width and height
    def get_area(self):
        return self.width * self.height
    
    # Get the perimeter value
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    # Get the diagonal value
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    # Make a picture of the shape by following the width and height with each space filled with '*'
    def get_picture(self):
        # If either width or height is out of bounds, return restriction to user
        if self.width > 50 or self.height > 50:
          return "Too big for picture."
      
        picture = ""
        for _ in range(self.height):
            for _ in range(self.width):
              picture += "*"
            picture += "\n"
        return picture

    # return how many squares fit in rectangle
    def get_amount_inside(self, sq):
        return self.get_area() // sq.get_area()

class Square(Rectangle):  
    # Set sides for square
    def __init__(self, length):
        self.set_side(length)
    
    # Output what the user will view in the terminal
    # This could be set as 'width' as well, but height and width would be the same for a square,
    # can be either or...
    def __str__(self):
        return f'Square(side={self.height})'

    # Set height and width, again doesn't matter like the description above
    def set_side(self, length):
        self.set_width(length)
