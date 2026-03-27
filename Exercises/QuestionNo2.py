# Question No. 2: Calculate the average age of the students.

from QuestionData import data
import numpy as np

avg = np.average(data, axis=0)
age = avg[0]

print("Average Age:", age)