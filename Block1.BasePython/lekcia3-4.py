#lekcia 2
a =int(input("Введіть а ="))
res = ((a+2)**3 / 4) - 5
print (res)

#lekcia 3
x = float(input("Введіть число:"))
print("Чи більше воно 0:", str(x>0))
print("Чи менше воно 0:", str(x<0))

#lekcia 3.1
N = int(input("Введіть число:"))
if ( 0<N<100):
    print("Число входить від 0 до 100")

if (0>N>100):
    print("Число не входить в проміжок від 0 до 100")
#lekcia 3.2

N2 = int(input("Введіть число:"))
if ( -33<=N2<150 or 151):
    print("Число входить від -33 до 150 або є числом 151")

else:
    print("Число не входить в проміжок від -33 до 150 і не є числом 151")

#lekcia 3.34
N3 = int(input("Введіть число:"))
negative = (-100 < N3 < 0)
positive= (0 < N3 < 100)
if negative or positive:
    print("Число входить в проміжок (-100; 0) or (0; 100)")
else:
    print("Число не входить в проміжок")

#lekcia 4
M = int(input("Введіть число"))
while M<=100:
    M = M +5
    print(f"Дорівнює: {M}")
print("Цикл завершено бо число стало більше 100")

#lekcia 4.1
player1 = int(input("Загадай число 1-10:"))
if 1>player1 or player1>10:
    print("Введіть вірне число від 1 до 10")
    exit()
else:
    print("Число прийнято")

number2 = int(input("Вгадайте число від 1-10:"))

while player1 != number2:
    print(f"Число: {number2} не є загаденим")
    number2 = int(input("Спробуй ще раз:"))


print(f"Перемога гравець 2 вгадав цисло гравця 1 і це число: {player1}")

#lekcia 4.2 
p = 1000
r = 0.25
n =(float(input("Введіть кількість років:")))
S = p*(1+ r)**n
S = round (S, 2)
print(f"Відповідь: {S} грн")

#lekcia 4.3 
a = float(input("К-ть першого елементу:"))
b = float(input("К-ть загальноъ суми"))
number = a
sum = 0 
for i in range(b):
    sum += number
    print(number, end="," if i < b -1 else "")
    number += 5 
print(f"Загальна сума {b} чисел: {sum}")

#lekcia 4.3
k = int(input("Введіть число якого хочете дізнатись факторіал:"))
factorial = 1
for i in range(1, k + 1 ):
    factorial *= 1
print(f"Факторіал числа {k} дорівнює {factorial}")
