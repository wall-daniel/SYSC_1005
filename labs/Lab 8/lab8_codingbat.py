def array_count9(nums):
    count = 0
    for item in nums:
        if item == 9:
            count = count + 1
    return count

def first_last6(nums):
    if nums[0] == 6 or nums[len(nums)-1] == 6:
        return True
    return False

def common_end(a, b):
  if (a[0] == b[0]) or (a[len(a) - 1] == b[len(b)-1]):
    return True
  return False


def sum3(nums):
  sum = 0
  for n in nums:
    sum += n
    
  return sum

def rotate_left3(nums):
  first_num = nums[0]
  
  for x in range(len(nums) - 1):
    nums[x] = nums[x+1]
    
  nums[len(nums) - 1] = first_num
  
  return nums

def reverse3(nums):
  for x in range(len(nums) // 2):
    a = nums[x]
    nums[x] = nums[len(nums)-x - 1]
    nums[len(nums)-x - 1] = a
    
  return nums

def max_end3(nums):
  if nums[0] > nums[len(nums) - 1]:
    new_number = nums[0]
  else:
    new_number = nums[len(nums) - 1]
    
  for n in range(len(nums)):
    nums[n] = new_number
    
  return nums

def sum2(nums):
  if len(nums) > 1:
    return nums[0] + nums[1]
  elif len(nums) == 1:
    return nums[0]
  return 0

def middle_way(a, b):
  return [a[1], b[1]]

def make_ends(nums):
  return [nums[0], nums[len(nums) - 1]]

def has23(nums):
  if nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3:
    return True
  return False

def same_first_last(nums):
  if len(nums) > 0 and nums[0] == nums[len(nums) - 1]:
    return True
    
  return False

def make_pi():
  return [3,1,4]

def count_evens(nums):
  count = 0
  for n in nums:
    if n % 2 == 0:
      count += 1
      
  return count

def big_diff(nums):
  biggest = nums[0]
  smallest = nums[0]
  
  for n in nums:
    if n > biggest:
      biggest = n
    if n < smallest:
      smallest = n
      
  return biggest - smallest

def centered_average(nums):
  biggest = 0
  smallest = nums[0]
  
  sum = 0
  for x in range(len(nums)):
    sum += nums[x]
    
    if nums[x] > biggest:
      biggest = nums[x]
    if nums[x] < smallest:
      smallest = nums[x]
    
  return (sum - biggest - smallest) // (len(nums) - 2)

def sum13(nums):
  after_thirteen = False
  
  sum = 0
  for n in nums:
    if after_thirteen:
      after_thirteen = False
    elif n == 13:
      after_thirteen = True
    else:
      sum += n
      
  return sum

def list_front9(nums):
    for n in range(0, len(nums)):
        if n > 3:
            return False
        if nums[n] == 9:
            return True
    return False
    
def sum67(nums):
  is_six = False
  
  sum = 0
  
  for n in nums:
    if is_six:
      if n == 7:
        is_six = False
    elif n == 6:
      is_six = True
    else:
      sum += n
      
  return sum
    
def has22(nums):
  previous_too = False
  
  for n in nums:
    if previous_too and n == 2:
      return True
    if n == 2:
      previous_too = True
    else:
      previous_too = False
      
  return False
