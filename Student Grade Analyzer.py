
# ⿣ Student Grade Analyzer
# Ask for 4 scores.
# Calculate average and assign grade:
# A = 70–100
# B = 60–69
# C = 50–59
# F = below 50
# Also print highest and lowest.


print("Student Grade Analyzer\n")

English = float(input('English Score: '))
Maths = float(input('Maths Score: '))
Chemistry = float(input('Chemistry Score: '))
Biology = float(input('Biology Score: '))

 #get average score

average = (English + Maths + Chemistry + Biology) / 4

if 70 <= average <= 100:
    grade = 'A'
elif 60 <= average <= 69:
    grade = 'B'
elif 50 <= average <= 59:
    grade = 'C'
else:
    grade = 'F'

#get to print the highest grade and lowest grade
highest = max(English, Maths, Chemistry, Biology)
lowest = min(English, Maths, Chemistry, Biology)

#Displaying the results
print('\n ===The Results===')
print(f'The average is {average:.3f}')
print(f'grade = {grade}')
print(f'The highest score is {highest}')
print(f'The lowest score is {lowest}')
