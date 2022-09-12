from typing import List

def insertionSort(array) -> List[int]:
  # Write your code here
  for i in range(len(array)):
    min_index = i
    for j in range(i+1,0,-1):
      if array[min_index]>array[j]:
        array[min_index], array[j] = array[j], array[min_index] 
        min_index = j - 1
  return array

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
