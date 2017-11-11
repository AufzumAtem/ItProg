from pylab import *
import xlrd

#wb = xlrd.open_workbook('C:/Users/stdm/Documents/Lehre/BSc_IT_PROG/it_prog/Lectures/code/v01_grades.xls')
wb = xlrd.open_workbook('v01_grades.xls')
sheet = wb.sheet_by_index(0)

grades = []
for i in range(sheet.nrows):
    grades.append(float(sheet.cell(i,0).value))

hist(grades, bins=30)
xlim([1,6])
xlabel('Grade')
ylabel('Number of students')
title('Exam - Grades')
show()

failed = 0
passed = 0
for grade in grades:
    if grade < 4:
        failed += 1
    else:
        passed += 1
pie([passed, failed], labels=["passed","failed"])
show()
