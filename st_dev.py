import csv
import math

with open('data.csv',newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

def mean(data):
    n=len(data)
    total= 0
    for x in data :
        total += int(x[1])
    
    mean = total / n
    return mean

squared_list = []
for number in file_data:
    a = int(number[1]) - mean(file_data)
    a = a ** 2
    squared_list.append(a)
sum = 0
for i in squared_list:
    sum = sum + i
result = sum / (len(file_data) - 1)
st_dev = math.sqrt(result)
print("The standard deviation is : " + str(st_dev))