# Question No. 9: Print the details of students whose Math and Science scores are both at least 80.

from QuestionData import data

sub = (data[:, 1] >= 80) & (data[:, 2] >= 80)
print("Students with Math and Science scores both at least 80:")
print(data[sub])