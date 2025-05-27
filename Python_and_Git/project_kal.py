print("Вітаю у обліку особистих фінансів!")
name = input("Давайте знайомитися. Як Вас зовуть? ")
print(name,", будь ласка, оберить тип валюти: EUR, $, ГРН, PLN, або напишить іншу ")
val = input("Валюта: ")
print("Будь ласка, оберить номер калькулятор:")
print("1 - Калькулятор заощаджень")
print("2 - Калькулятор чайових")
print("3 - Інструмент розподілу бюджету")
kal = int(input("Номер калькулятора: "))
kal1 = int(1)
kal2 = int(2)
kal3 = int(3)
#kal_sav = 0.0
#kat_tip = 0.0
#kat_totl = 0.0
# for i in range(kal):
if kal == kal1: #and (i != kal2 and i != kal3):
    sav = float(input("Введить суму заощаджень: "))
    proc = float(input("Введить % ставку: "))
    term = int(input("Введить розрахунковій час в місяцях: "))
    #kal_sav = 0.0
    kal_sav = sav * proc * term / 100
    print(name,", загальна сума заощаджень: ", round(kal_sav, 2), val)
#else:
    #print(name, ", дякуємо, що скористалися нашим калькулятором!")
if kal == kal2: # and (i != kal1 and i != kal3):
    pay = float(input("Введить суму розрахунку: "))
    tips = float(input("Введить відсоток чайових: "))
    #kat_tip = 0.0
    kat_tip = pay * tips / 100
    print(name, ", сума для сплати чайових складає: ", round(kat_tip, 2), val)
#else:
    #print(name, ", дякуємо, що скористалися нашим калькулятором!")
if kal == kal3: # and (i != kal2 and i != kal1):
    kat1 = float(input("Введить доходи отримані з оплати праці: "))
    kat2 = float(input("Введить доходи отримані від предприємницької : "))
    kat3 = float(input("Введить доходи отримані від долевої участі: "))
    kat4 = float(input("Введить доходи отримані у вигляді відсотків банку: "))
    kat5 = float(input("Введить доходи отримані з операціями з цінними паперами: "))
    kat6 = float(input("Введить доходи отримані з криптовалютних операцій: "))
    kat7 = float(input("Введить інши доходи: "))
    #kat_totl = 0.0
    kat_totl = kat1+kat2+kat3+kat4+kat5+kat6+kat7
    print(name, " Ваш загальний доход складає: ", round(kat_totl, 2), val)
    print(name, ", дякуємо, що скористалися нашим калькулятором!")
else: # kal != kal3 and i != kal2 and i != kal1
    #print("Щось не вийшло. Спробуйте ще раз") 
    print(name, ", дякуємо, що скористалися нашим калькулятором!")
if kal != kal3 and kal != kal2 and kal != kal1:
    print("Щось не вийшло. Спробуйте ще раз")
print("Завжди раді Вам допомогти!")
