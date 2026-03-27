# Question No. 6: Add 5 marks to all students' Math scores and print the updated data.

from QuestionData import data
import numpy as np

data[:, 1] += 5
print("Data after adding 5 in Math scores:\n", data)