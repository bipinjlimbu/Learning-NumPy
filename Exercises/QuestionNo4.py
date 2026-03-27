# Question No. 4: Find the highest Science score among the students.

from QuestionData import data
import numpy as np

science = data[:, 2]
highest = np.max(science)
print("Maximum Science score:", highest)