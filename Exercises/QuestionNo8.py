# Question No. 8: Calculate the average marks in each subject (column-wise mean).

from QuestionData import data
import numpy as np

sub = data[:, 1:]
avg = np.mean(sub, axis=0)
print("Average Subject Marks (Math, Science):", avg)