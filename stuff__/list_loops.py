last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

subjects = ["physics","calculus","poetry","history"]


grades = [98, 97, 85, 88]

gradebook = []

for i in range(len(subjects)):
  gradebook.append([subjects[i], grades[i]])

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

for grade in gradebook:
  if grade[0] == "visual arts":
    print("Test")
    grade.remove(93)
    grade.append(98)

for grade in gradebook:
  if grade[0] == "poetry":
    grade.remove(85)
    grade.append("Pass")

print(gradebook)

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)
