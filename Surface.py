from Rectangle import Rectangle

class Surface:
  
  def __init__(self, filename, x, y, h, w):
    """
    Initializes the values.
    Takes integers and a string
    Returns none
    """
    self.image = filename
    self.rect = Rectangle(x,y,h,w)

  def getRect(self):
    """
    Returns the rectangle.
    Takes self and uses integer attributes
    Returns none
    """
    return self.rect