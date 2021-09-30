def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()

#You recieve data from an exchange in the form of a stream of timestamps and position deltas in order.

#1. Aggregate the position deltas to find the overall position at each timestamp

#e.g.
#[(1, 5), (2, -7), (3, 23)] => [(1, 5), (2, -2), (3, 21)]

# 2. Now suppose you recieve data from N exchanges in the same format. Aggregate all streams of trades to find the overall position

#e.g.
#[(1, 5), (2, -7), (5, 23)]
#[(3, -10), (4, 10), (6, -20)]

#=> [(1, 5), (2, -2), (3, -12), (4, -2), (5, 21), (6, 1)]

def aggregateDeltas(array):
    current = 0
    result = []
    for timestamp, delta in array:
        current += delta
        result.append((timestamp, current))
    return result

print(aggregateDeltas([(1, 5), (2, -7), (3, 23)]))

def aggregateTwoExchanges(a, b):
    c = a + b
    c = sorted(c, key = lambda x:x[0])
    return aggregateDeltas(c)

print(aggregateTwoExchanges([(1, 5), (2, -7), (5, 23)], [(3, -10), (4, 10), (6, -20)]))


"""
N: number of exchanges
k: number of items per exchange
"""

import heapq

def aggregateNExchanges(exchanges):
    """
    exchanges:[[],[]]
    Runtime: O(N*k*logN)
    """
    result = []
    currentHeads = []
    heapq.heapify(currentHeads)
    currentDelta = 0
    
    for exchangeIndex in range(len(exchanges)):
        exchange = exchanges[exchangeIndex]
        time, delta = exchange.pop(0)
        currentHeads.append((time, delta, exchangeIndex))
    
    while exchanges:
        minTime, minDelta, minExchangeIndex = heapq.heappop(0) #O(1)
        if not exchanges[exchangeIndex]:
            exchanges.pop(exchangeIndex) 
        else:
            newTime, newDelta = exchanges[minExchangeIndex].pop(0)
            heapq.heappush(currentHeads, (newTime, newDelta, minExchangeIndex))
                
        currentDelta += minDelta
        result.append((minTime, currentDelta))
        
        
    return result


                
        
        
    
        
    
