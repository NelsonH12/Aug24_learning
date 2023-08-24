#Binary search algo repeatedly splits data in half until target value is found
#For example, a list of integers 1-10.  Binary search is targeting 3.  It will split the
#data in half, 1-5, 6-10.  It knows the middle value is 5, and checks if 3 is > or <
#It then knows to stay on the less than side, and continues splitting as needed.
#first, make a function that takes a list and target parameter
#multiple variables, middle, start, end, amount of steps
#recursion or while loop to repeatedly split data
#increase steps each time a split is done conditions to locate target and discard others
#Binary search is far quicker than linear search

def binary_search(list, target):
  middle = 0
  start = 0
  end = len(list)
  steps = 0

  while(start<=end): #this prevents the program from running past list length.
    print("Step",steps, ":" ,str(list[start:end+1]))

    steps = steps+1
    middle = (start + end) // 2

    if target == list[middle]:
      return middle
    if target < list[middle]:
      end = middle - 1
      #if the target is less than the middle, the end of the new list is the middle -1
    
    else:
      start = middle + 1

  return -1

mylist = [1,2,3,4,5,6,7,8,9,10,11,12]
secret_number = 12

binary_search(mylist, secret_number)