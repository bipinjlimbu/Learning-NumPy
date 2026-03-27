# Question No. 5: Print the details of students whose Math score is greater than 90.

from QuestionData import data

math = data[:, 1]
for i in range(len(math)):
    if math[i] > 90:
        print("Math score greater than 90:", data[i])