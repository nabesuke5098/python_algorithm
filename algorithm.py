list = [17, 11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]

def sort(array):
  sorted_array = []
  length = len(array)
  i = 0

  while i < length:
    if len(sorted_array) == 0:
      sorted_array.append(array[i])
      i + 1
    elif sorted_array[0] > array[i]:
      sorted_array[0] = array[i]
      i + 1
    i + 1

  print(sorted_array)


sort(list)

def selected_sort(array):
  for i in range(0, len(array) - 1):
    select_min(array, i)

def select_min(array, i):
  min = i
  for j in range(i + 1, len(array)):
    if array[min] > array[j]:
      min = j
  array[i], array[min] = array[min], array[i]


selected_sort(list)
print(list)


def insert_sort(array):
  for i in range(1, len(array)):
    insert(array, i)

def insert(array, i):
  tmp = array[i]
  for j in range(i - 1, -1, -1):
    if tmp < array[j]:
      array[j + 1] = array[j]
    else:
      array[j + 1] = tmp
      break
  else:
    array[0] = tmp

insert_sort(list)
print(list)


def bubble_sort(array):
  for i in range(0, len(array) - 1):
    exchange(array, i)

def exchange(array, i):
  for j in range(len(array) - 1, i, -1):
    if array[j - 1] > array[j]:
      array[j - 1], array[j] = array[j], array[j - 1]

bubble_sort(list)
print(list)

def method(num):
  arr = []

  for i in range(0, num):
    if i == 0 or i == 1:
      arr.append(1)
    else:
      arr.append(arr[i-1] + arr[i-2])

  return arr

print(method(35))

def fib(n):
  if n == 0 or n == 1:
    return 1
  return fib(n-1) + fib(n-2)

for i in range(35):
  print(fib(i))

def fib_memo(n):
  memo = [None] * (n+1)

  def _fib(n):
    if n == 0 or n == 1:
      return 1
    if memo[n] != None:
      return memo[n]
    memo[n] = _fib(n-1) + _fib(n-2)
    return memo[n]
    
  return _fib(n)

for i in range(35):
  print(fib_memo(i))


def merge_sort(array):
  if len(array) < 2:
    return array
  mid = len(array) // 2
  return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))

def merge(arrf, arrb):
  if len(arrf) < 1:
    return arrb
  if len(arrb) < 1:
    return arrf
  if arrf[0] <= arrb[0]:
    return [arrf[0]] + merge(arrf[1:], arrb)
  else:
    return [arrb[0]] + merge(arrf, arrb[1:])
  
print(merge_sort(list))

def quick_sort(array):
  if len(array) < 2:
    return array
  p = array[0]
  arrf, arrb = divide(p, array[1:])
  return quick_sort(arrf) + [p] + quick_sort(arrb)

def divide(p, array):
  left = []
  right = []
  for i in array:
    if i < p:
      left.append(i)
    else:
      right.append(i)
  return left, right

print(quick_sort(list))

def bucket_sort(array):
  arrc = [0] * (max(array) + 1)

  for i in array:
    array[i] += 1

  for j in range(1, len(arrc)):
    arrc[j] = arrc[j] + arrc[j-1]
  arrs = [0] * len(array)
  for i in reversed(array):
    arrs[arrc[i] - 1] = i
    arrc[i] -= 1
  return arrs

print(bucket_sort(list))