"""
Complexities:

Depth D

Time: O(D) = 4*O(D-1)
=> O(D) = 4^D

Space:
Recursive calls add overhead since we store them in the execution stack.
The space occupied in the stack will be then O(D), in the worst case scenario.
The stack space occupied will be no more than O(D) at any given point since a sibling
drawHTree will not be called before the current one being executed returns (i.e. finishes its execution).

"""

import numpy as np
import matplotlib.pyplot as plt

def draw_line(x, y):
  """
  x = [x0, x1]
  y = [y0, y1]
  """
  plt.plot(x, y, c='k')


def drawHTree(x, y, length, depth):
  if depth == 0:
    return
  
  x_lo, x_hi = x - length / 2., x + length / 2.
  y_lo, y_hi = y - length / 2., y + length / 2.
  
  # Draw lines for the current depth
  draw_line([x_lo, x_lo], [y_lo, y_hi])     # Vertical (left)
  draw_line([x_lo, x_hi], [y, y])           # Horizontal
  draw_line([x_hi, x_hi], [y_lo, y_hi])     # Vertical (right)
  
  # Now the recursion
  new_length = length / 2.
  
  # Upper left
  drawHTree(x=x_lo, y=y_hi, length=new_length, depth=depth-1)
  # Lower left
  drawHTree(x=x_lo, y=y_lo, length=new_length, depth=depth-1)
  # Upper right
  drawHTree(x=x_hi, y=y_hi, length=new_length, depth=depth-1)
  # Lower right
  drawHTree(x=x_hi, y=y_lo, length=new_length, depth=depth-1)


if __name__ == '__main__':
  drawHTree(0, 0, 1, depth=2)
  plt.show() 
  
