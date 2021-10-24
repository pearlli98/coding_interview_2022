from impl_v1 import *
from impl_v2 import *

# test partitions:
# input: list of tuples of (description, amount, timestamp)
# where timestamp is positive integer; sorted in ascending order based on timestamp

# output: list of recurring description 

# partition on input length: =0, >0
# partition on output length: =0, >0
# parititon on sequence pattern: same description come in clumps, not

test1 = []

#output is not empty
test2 = [
  ("Netflix", 9.99, 10),
  ("Netflix", 9.99, 20),
  ("Netflix", 9.99, 30),
  ("Amazon", 27.12, 32),
  ("Sprint", 50.11, 45),
  ("Sprint", 50.11, 55),
  ("Sprint", 50.11, 65),
  ("Sprint", 60.13, 77),
]

test3 = [
  ("Netflix", 9.99, 10),
  ("Netflix", 9.99, 20),
  ("Amazon", 27.12, 32),
  ("Sprint", 50.11, 45),
  ("Sprint", 50.11, 55),
  ("Sprint", 60.13, 77),
]

test4 = [
  ("Netflix", 9.99, 10),
  ("Netflix", 9.99, 20),
  ("Netflix", 9.99, 30),
  ("Sprint", 50.11, 45),
  ("Sprint", 50.11, 55),
  ("Sprint", 50.11, 65),
]

# test for orders come in separate chunks
test5 = [
  ("Netflix", 9.99, 10),
  ("Sprint", 50.11, 25),
  ("Netflix", 9.99, 30),
  ("Sprint", 50.11, 45),
  ("Amazon", 0.01, 46),
  ("Netflix", 9.99, 50),
  ("Sprint", 50.11, 65),
]

print(getRecurringTransactions(test1))
print(getRecurringTransactions(test2))
print(getRecurringTransactions(test3))
print(getRecurringTransactions(test4))
print(getRecurringTransactions(test5))
print('----------------------------------')
print(getRecurringTransactionsWithinThreshold(test1))
print(getRecurringTransactionsWithinThreshold(test2))
print(getRecurringTransactionsWithinThreshold(test3))
print(getRecurringTransactionsWithinThreshold(test4))
print(getRecurringTransactionsWithinThreshold(test5))