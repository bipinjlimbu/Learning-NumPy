# Question No. 7: Count the number of students whose age is less than 19.

from QuestionData import data

count = 0
age = data[:, 0] < 19
print("Number of students with age less than 19:", len(data[age]))