class ChecksumException(Exception):
  def __init__(self, point, actual, expected):
    message = "Checksum failed at %s. Expected '%c' (0x%02x) but got '%c' (0x%02x)." % (
        str(point), chr(expected), expected, chr(actual), actual)
    super(ChecksumException, self).__init__(message)

class BadResponse(Exception):
  def __init__(self, actual, expected):
    message = "Bad response from server. Expected '%s' but got '%s'" % (expected, actual)
    super(BadResponse, self).__init__(message)

class TestFailure(Exception):
  def __init__(self, actual, expected):
    message = "Test failed: expected '%s' but got '%s'" % (str(expected), str(actual))
    super(TestFailure, self).__init__(message)

class InternalError(Exception):
  def __init__(self, message):
    super(InternalError, self).__init__(message)

class KnownBug(Exception):
  def __init__(self, reason):
    super(KnownBug, self).__init__(reason)

class BrokenTest(Exception):
  def __init__(self, reason):
    super(BrokenTest, self).__init__(reason)

class Point(object):
  def __init__(self, x, y):
    self._x = x
    self._y = y

  def __str__(self):
    return "Point(x=%d, y=%d)" % (self._x, self._y)

  def x(self):
    return self._x

  def y(self):
    return self._y


class Size(object):
  def __init__(self, width, height):
    self._width = width
    self._height = height

  def __str__(self):
    return "Size(width=%d, height=%d)" % (self._width, self._height)

  def width(self):
    return self._width

  def height(self):
    return self._height


class Rect(object):
  def __init__(self, left, top, right, bottom):
    self._left = left
    self._top = top
    self._right = right
    self._bottom = bottom

  def __str__(self):
    return "Rect(left=%d, top=%d, right=%d, bottom=%d)" % (
        self._left, self._top, self._right, self._bottom)

  def left(self):
    return self._left

  def top(self):
    return self._top

  def right(self):
    return self._right

  def bottom(self):
    return self._bottom

  def width(self):
    return self._right - self._left + 1

  def height(self):
    return self._bottom - self._top + 1

  def params(self):
    return [ self._top, self._left, self._bottom, self._right ]

  def points(self):
    y = self._top
    while y <= self._bottom:
      x = self._left
      while x <= self._right:
        yield Point(x, y)
        x += 1
      y += 1


