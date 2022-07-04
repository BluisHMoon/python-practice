# Import modules
    
# Practice3: for loop
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end=' ')
#     print(end='\n')
    
# for i in range(1, 10, 2):
#     print(i, end=' ')
# print(end='\n')
    
# for i in range(10, 1, -1):
#     print(i, end=' ')
# print(end='\n')

bingo = 7

for i in range(0, 3):
    guess = int(input('請輸入您要猜的數字：'))
    if guess == bingo:
        print('恭喜您猜對')
        break
    elif i == 2:
        print('次數已用完！')
    else:
        print('請再接再厲')