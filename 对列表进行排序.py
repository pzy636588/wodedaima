grade=[36,69,68,59,98,96,95,98,92,93]
total=sum(grade)
print("原来的成绩：",grade)
grade.sort()
print("升序排列:",grade)
grade.sort(reverse=True)
print("降序排列:",grade)