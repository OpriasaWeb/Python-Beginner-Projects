
# list of numbers here
list_of_numbers = [
  3, 6, 7, 9, 10, 11, 15, 16, 20, 32, 42, 44, 52, 89, 100, 102, 105, 110, 140,
  284, 433, 543, 588, 894,
]

def binary_search(list, element):
  low = 0
  high = len(list)
  steps = 0
  while low <= high:
    print(f"Step: {steps} : {str(list[low:high+1])}")

    # Get the middle every iteration of loop
    mid = (low + high) // 2

    # Increment the step per iteration
    steps += 1

    if element == list[mid]:
      return mid
    elif element < list[mid]:
      high = mid - 1
    elif element > list[mid]:
      low = mid + 1

target = 101
binary_search(list_of_numbers, target)