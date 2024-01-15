#!/usr/bin/python3
"""Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines Square instances"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialise"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return string representation of a square"""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y,
                   self.width)

    @property
    def size(self):
        """return square size"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """assigns attributes"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """updates instance attributes using args or keywords"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """return dictionary representation of a square"""
        return {'id': self.id, 'size': self.width,
                'x': self.x, 'y': self.y}
