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
#
# (description, amount, timestamp(positive integer)) 
# 
# recurring transaction:
# 1. at least 3 times
# 2. same description
# 3. same amount
# 4. same interval 
#
# output a list of recurring 

def getRecurringTransactions(array):
    amount_dict = {}
    time_dict = {}
    recurring_transactions = []
    
    for description, amount, time in array:
        amount_dict[description] = amount_dict.get(description, []) + [amount]
        time_dict[description] = time_dict.get(description, []) + [time]
    
    for description in amount_dict.keys():
        #check at least 3 times
        if len(amount_dict[description]) < 3:
            continue
        
        #check for same amount
        if len(set(amount_dict[description])) != 1:
            continue
        
        #check for same interval
        current_time_dict = time_dict[description]
        interval = current_time_dict[1] - current_time_dict[0]
        index = 2
        recurring = True
        
        while index < len(current_time_dict):
            if current_time_dict[index] - current_time_dict[index - 1] != interval:
                recurring = False
                break
            index += 1
            
        if recurring:
            recurring_transactions.append(description)
            
    return recurring_transactions