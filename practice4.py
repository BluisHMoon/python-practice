# Import modules
        
# Practice4: list
# a = [1, 3, 5, 7, 9]
# count = 0
# for i in a:
#     print(i * i)
#     a[count] = i * i
#     count += 1    

# print(a)   

# for i in range(0, len(a)):
#     print(a[i], a[i])
#     a[i] = a[i], a[i]
# print(a)   

# score = [10, 30, 50, 70, 90]
# totalScore = 0

# print("五次成績：", end='')
# for i in range(0, len(score)):
#     totalScore += score[i]
#     print(score[i], end=' ')
# print(end='\n')

# print("平均成績：", totalScore / 5)

# totalScore = 0

# print("五次新成績：", end='')
# for i in range(0, len(score)):
#     score[i] = (score[i] ** 0.5 * 10)
#     totalScore += score[i]
#     print(score[i], end=' ')
# print(end='\n')

# print("新平均成績：", totalScore / 5)

people = []

for i in range(0, 10):
    num = int(input("請輸入宴客人數："))
    people.append(num)
print(people)

for questions in range(0, 5):
    start = int(input("請選擇起始點："))
    end = int(input("請選擇結束點："))
    checkList = people[start:end]
    print(sum(checkList))