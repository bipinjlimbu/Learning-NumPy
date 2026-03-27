# Question No. 9: Print the details of students whose Math and Science scores are both at least 80.

from QuestionData import data

sub = data[:, 1:]
print("Students with Math and Science scores at least 80:")
for i in range(len(sub)):
    if sub[i][0] >= 80 and sub[i][1] >= 80:
        print(data[i])