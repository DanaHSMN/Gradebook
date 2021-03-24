last_semester_gradebook = [["Politics", 80], ["Latin", 96], ["Dance", 97], ["Architecture", 65]]

#Create two separate lists for subjects and grades
subjects = ["Physics", "Calculus", "Poetry", "History"]
grades = [98, 97, 85, 88]

#Create a new two-dimensional list combining the previous lists
gradebook = [["Physics", 98], ["Calculus", 97], ["Poetry", 85], ["History", 88]]

#Append gradebook with a new subject and grade
gradebook.append(["Computer Science", 100])

#Append gradebook with another new subject and grade
gradebook.append(["Visual Arts", 93])

#Modify the grade for Visual Arts
gradebook[-1][-1] = 98

#Switch the numerical grade value from Poetry to a Pass/Fail option
gradebook[2].remove(85)
gradebook[2].append("Pass")

#Combine gradebooks
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)