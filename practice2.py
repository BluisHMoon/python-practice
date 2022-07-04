# Import modules

# Practice2: if else
count = input('請輸入您想做的運算，限定+, -, *, /：')
num1 = int(input('請輸入第一個整數：'))
num2 = int(input('請輸入第二個整數：'))

if count == '+':
    print('a + b = ', num1 + num2)
elif count == '-':
    print('a - b = ', num1 - num2)
elif count == '*':
    print('a * b = ', num1 * num2)
elif count == '/':
    print('a / b = ', num1 / num2)
else:
    print('您輸入的運算符有誤')