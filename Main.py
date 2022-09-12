from typing import List

def insertionSort(array) -> List[int]:
  # Write your code here
  for i in range(len(array)-1):
    min = array[i]
    for j in range(i-1,-1,-1):
        if min<array[j]:
          array[j + 1] = array[j]
    array[j + 1] = min
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
