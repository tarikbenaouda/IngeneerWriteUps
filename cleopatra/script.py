from pwn import *
from collections import defaultdict, deque
import ast
def tri_to_matrix(triangle):
    length = len(triangle)
    width = len(triangle[-1])
    matrix = []
    for i in range(length):
        matrix.append([0] * width)
        for j in range(len(triangle[i])):
            matrix[i][j] = triangle[i][j]
    return matrix

def largest_rectangle_with_number(matrix, target):
  max_area = 0
  max_length = 0
  max_width = 0

  # Iterate over each cell in the matrix
  for row in range(len(matrix)):
    # Keep track of consecutive target values for each column in this row
    consecutive = [0] * len(matrix[row])

    # Initialize consecutive for the first column
    consecutive[0] = 1 if matrix[row][0] == target else 0

    # Calculate consecutive values for other columns based on previous row (if exists)
    for col in range(1, len(matrix[row])):
      consecutive[col] = consecutive[col - 1] + 1 if matrix[row][col] == target else 0

    # Use a stack to find the maximum rectangle area based on consecutive values
    stack = []
    for col in range(len(matrix[row])):
      # Pop elements from the stack while the current consecutive value is less than the element on top
      while stack and consecutive[stack[-1]] > consecutive[col]:
        height = consecutive[stack.pop()]
        width = col - (stack[-1] if stack else 0) - 1  # Consider edge case of empty stack
        area = height * width
        if area > max_area:
          max_area = area
          max_length = height
          max_width = width
      stack.append(col)  # Push current column index onto the stack

  return max_length, max_width
io = remote('ingeneer-2k24.ingeniums.club',14005)
# Define the matrix
for i in range(50):
    b = io.recvuntil(b'pyramid> ')
    print(b)
    b = io.recvuntil(b'\n')[:-1]
    triangle = ast.literal_eval(b.decode())
    for row in triangle:
        print(row)
    matrix = tri_to_matrix(triangle)
    new_matrix = []
    for i,row in enumerate(matrix):
        fill = row[:2*i+1]
        pad = [0]*((len(row)-len(fill))//2)
        new_matrix.append(pad + fill + pad) 

    matrix = new_matrix
    for row in matrix:
        print(row)
    dic = {}
    for i in range(1,10):
        dimensions = largest_rectangle_with_number(matrix, i)
        # Calculate the area of the largest rectangle
        area = dimensions[0] * dimensions[1] * i
        dic[i] = area
    max_area_target = max(dic, key=dic.get)
    max_area = dic[max_area_target]
    print(dic)
    print(max_area_target, max_area)
    io.sendline(str(max_area).encode())
    io.sendline(str(max_area_target).encode())
