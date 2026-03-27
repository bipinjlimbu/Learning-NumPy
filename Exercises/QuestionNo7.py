# Question No. 7: Count the number of students whose age is less than 19.

from QuestionData import data

count = 0
age = data[:, 0]
for i in range(len(age)):
    if age[i] < 19:
        count += 1
        
print("Number of students under 19:", count)