# here we can aggregate by frequency
from collections import Counter
file = 'desolation_row.txt'
f = open(file, 'r')
data = f.read()
# print(data)
cleanup = '.,!?"'.split()
for mark in cleanup:
    data = data.replace(mark, '')
    
data = data.lower().split()
# print(data)

counts = Counter(data)
# print(counts)
# print(counts.most_common(10))
print(counts.most_common(len(counts)))