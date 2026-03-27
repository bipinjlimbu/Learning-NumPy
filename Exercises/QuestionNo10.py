# Question No. 10: Replace all Science scores less than 75 with 0 and print the updated data.

from QuestionData import data

science = data[:, 2]
for i in range(len(science)):
    if science[i] < 75:
        data[i][2] = 0
        
print("Data after replacing Science scores less than 75 with 0:\n", data)