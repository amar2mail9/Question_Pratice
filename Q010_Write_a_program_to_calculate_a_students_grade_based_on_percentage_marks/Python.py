# Write a program to calculate a student's grade based on percentage marks.

# user marks enter
hindiMarks = int(input("Enter Hindi Total Marks: "))
hindiObtained = int(input("Enter Hindi Obtained Marks: "))

englishMarks = int(input("Enter English Total Marks: "))
englishObtained = int(input("Enter English Obtained Marks: "))

mathMarks = int(input("Enter Math Total Marks: "))
mathObtained = int(input("Enter Math Obtained Marks: "))

scienceMarks = int(input("Enter Science Total Marks: "))
scienceObtained = int(input("Enter Science Obtained Marks: "))

socialScienceMarks = int(input("Enter Social Science Total Marks: "))
socialScienceObtained = int(input("Enter Social Science Obtained Marks: "))

passingPercentage = int(input("Enter Passing Percentage: "))

totalMarks = hindiMarks + englishMarks + mathMarks + scienceMarks + socialScienceMarks
obtainedMarks = hindiObtained + englishObtained + mathObtained + scienceObtained + socialScienceObtained

percentageGain = round((obtainedMarks / totalMarks) * 100, 2)

grade = "None"
status = "None"

if (
    (hindiObtained / hindiMarks * 100) >= passingPercentage and
    (englishObtained / englishMarks * 100) >= passingPercentage and
    (mathObtained / mathMarks * 100) >= passingPercentage and
    (scienceObtained / scienceMarks * 100) >= passingPercentage and
    (socialScienceObtained / socialScienceMarks * 100) >= passingPercentage
):

    if percentageGain >= 90:
        grade = "A+"
    elif percentageGain >= 80:
        grade = "A"
    elif percentageGain >= 70:
        grade = "B+"
    elif percentageGain >= 60:
        grade = "B"
    elif percentageGain >= 50:
        grade = "C+"
    elif percentageGain >= 40:
        grade = "C"
    else:
        grade = "D"

    status = "Pass"
else:
    status = "Fail"

print("\nSubject Name\tTotal Marks\tObtained Marks")
print(f"Hindi\t\t{hindiMarks}\t\t{hindiObtained}")
print(f"English\t\t{englishMarks}\t\t{englishObtained}")
print(f"Maths\t\t{mathMarks}\t\t{mathObtained}")
print(f"Science\t\t{scienceMarks}\t\t{scienceObtained}")
print(f"Social Science\t{socialScienceMarks}\t\t{socialScienceObtained}")
print('------------------------------------------')
print(f'Total Marks : {totalMarks}')
print(f'Obtained Marks : {obtainedMarks}')
print(f'Percentage : {percentageGain}%')
print(f'Grade : {grade}')
print(f'Status : {status}')
