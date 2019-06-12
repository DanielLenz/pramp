def num_of_paths_to_dest(n):
  """
  n = 1: 1
  n = 2: 1
  n = 3: 2
  n = 4: 5
  n = 5: 14
  
  X X X X 14
  X X X 5 14
  X X 2 5 9
  X 1 2 3 4 
  1 1 1 1 1
  """
  
  route = [[0 for _ in range(n)] for _ in range(n)]

  for row in range(n):
    for col in range(n):
#      print(row, col)
      if (row == 0) and (col == 0):
        route[row][col] = 1
        continue

      if (row == 0):
        route[row][col] = 1
        continue
        
      # Ignore lower left triangle
      if row > col:
        route[row][col] = 0
        continue
         
      route[row][col] = route[row][col-1] + route[row-1][col]

  return route[-1][-1]

if __name__ == '__main__':
  """
  Can also use the Catalan number of n-1 to solve this
  https://en.wikipedia.org/wiki/Catalan_number
  Take 2n, n steps up
  C_n = 1/(n+1) (2n,n)
  """
  
  for i in range(1, 7):
    print(num_of_paths_to_dest(i))
  
  