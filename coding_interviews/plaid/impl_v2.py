# [
#   ("Netflix", 9.99, 10),
#   ("Netflix", 9.99, 20),
#   ("Netflix", 9.99, 30),
#   ("Amazon", 27.12, 32),
#   ("Sprint", 50.11, 45),
#   ("Sprint", 50.11, 55),
#   ("Sprint", 50.11, 65),
#   ("Sprint", 60.13, 77),
# ]
# maximum amount within 20% of minimum amount
# (description, amount, timestamp(positive integer)) 

def getRecurringTransactionsWithinThreshold(array):
    max_amount = {}
    min_amount = {}
    max_interval = {}
    min_interval = {}
    last_time = {}
    counter = {}
    recurring_transactions = []
    
    for description, amount, time in array:
        
        max_amount[description] = max(max_amount.get(description, 0), amount)
        min_amount[description] = min(min_amount.get(description, float('infinity')), amount)
        
        if description not in last_time:
            last_time[description] = time
        else:
            max_interval[description] = max(max_interval.get(description, 0), abs(last_time[description] - time))
            min_interval[description] = min(min_interval.get(description, float('infinity')), abs(last_time[description] - time))
            last_time[description] = time
        
        counter[description] = counter.get(description, 0) + 1
    
    for description in max_amount.keys():
        #check at least 3 times
        if counter[description] < 3:
            continue
        
        #check for same amount
        if min_amount[description] * 1.2 < max_amount[description]:
            continue
        
        #check for same interval
        if min_interval[description] * 1.2 < max_interval[description]:
            continue
            
        recurring_transactions.append(description)
            
    return recurring_transactions