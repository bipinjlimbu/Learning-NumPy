# Question No. 5: Print the details of students whose Math score is greater than 90.

from QuestionData import data

math = data[:, 1]
print("Students with Math score greater than 90:")
for i in range(len(math)):
    if math[i] > 90:
        print(data[i])