#!/usr/bin/python3
"""Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle properities"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initiates the attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y,
                   self.width, self.height)

    @property
    def width(self):
        """return the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of the width"""
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """return the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of the height"""
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """return the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """return the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y"""
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        """validates if integer or not"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """returns the area value of the Rectangle"""
        return self.width * self.height

    def display(self):
        """prints in stdout the rectangle with #"""
        print('\n' * self.y, end='')
        for i in range(self.height):
            if self.x != 0:
                print(' ' * self.x, end='')
            print('#' * self.width)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """assigns an argument to each attribute"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """updates arguments to each attribute with and without keywords"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)
