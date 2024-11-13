# 집계 알고리즘 : 1등급이 몇개있는지, 빈도수 체크
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]

#방법 1: 리스트를 통한 구조화
grades = [0,0,0,0]
for gem in gems:
    grades[gem] += 1

print(grades)

#방법 2: 딕셔너리를 통한 구조화
grades = {1:0, 2:0, 3:0}
for gem in gems:
    grades[gem] += 1
print(grades)
