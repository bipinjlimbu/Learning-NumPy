# Question No. 5: Print the details of students whose Math score is greater than 90.

from QuestionData import data

math = data[:, 1] > 90
print("Students with Math score greater than 90:")
print(data[math])