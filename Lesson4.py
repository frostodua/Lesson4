# 1. Користувач вводить рядок з клавіатури. Порахуйте кількість літер,
#    цифр у рядку. Виведіть обидві кількості на екран. (використовувати цикл)

# 2. Користувач вводить з клавіатури рядок та символ для пошуку.
#    Порахуйте скільки разів у рядку зустрічається потрібний символ.
#    Отримане число виведіть на екран.

# 3. Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни.
#    Зробіть у рядку заміну одного слова на інше. Отриманий рядок на екрані.

# 4. Дано рядок. (зробити зрізи)
#  - Спершу виведіть третій символ цього рядка.
#  - У другому рядку виведіть передостанній символ цього рядка.
#  - У третьому рядку виведіть перші п'ять символів цього рядка.
#  - У четвертому рядку виведіть весь рядок, крім двох останніх символів.
#  - У п'ятому рядку виведіть усі символи з парними індексами (вважаючи, що
#    індексація починається з 0, тому символи виводяться з першого).
#  - У шостому рядку виведіть усі символи з непарними індексами, тобто,
#    починаючи з другого символу рядка.
#  - У сьомому рядку виведіть усі символи у зворотному порядку.
#  - У восьмому рядку виведіть усі символи рядка через один у зворотному порядку,
#    починаючи з останнього.
#  - У дев'ятому рядку виведіть довжину цього рядка.
#
# Додатково:
# # Є певний текст. Реалізуйте наступну функціональність:
# # ■ Змінити текст таким чином, щоб кожне речення починалися з великої літери;
# # ■ Порахуйте скільки разів цифри зустрічаються у тексті;
# # ■ Порахуйте скільки разів розділові знаки зустрічаються в тексті;
# # ■ Порахуйте кількість знаків оклику в тексті.

#1
str=(input("Введіть будь який рядок "))
letters_count = 0
numbers_count = 0

for symbol in str:
    if symbol.isalpha():
        letters_count+=1
    elif symbol.isdigit():
        numbers_count +=1
print("Кількість букв ", letters_count)
print("Кількість цифр ", numbers_count)

#2
string=(input("Введіть будь який рядок "))
symbol=(input("Введіть будь який символ "))
symbol_count=0

for char in string:
    if char == symbol:
        symbol_count+=1
print("Кількість символів у рядку", symbol_count)

#3
text = input("Введіть будь який рядок: ")
search_word = input("Введіть слово для пошуку: ")
replace_word = input("Введіть слово для заміни: ")
text = text.replace(search_word, replace_word)
print(text)

#4
sentence = input("Введіть будь який рядок ")
print(sentence[2:3])
print(sentence[-2])
print(sentence[0:5])
print(sentence[0:-2])
print(sentence[1::2])
print(sentence[0::2])
print(sentence[::-1])
print(sentence[::-2])
print(len(sentence))

# additional task
sentence1 = input("Введіть будь який рядок ")
# Верхній регістр початкових букв
print(sentence1.title())
# Кількість цифр
numbers_count = 0
for symbol in sentence1:
    if symbol.isdigit():
        numbers_count +=1
print("Кількість цифр ", numbers_count)

# Кількість розділових знаків
countsym = 0
for letter in sentence1:
    if letter == ",":
        countsym+=1
    elif letter == ";":
        countsym += 1
    elif letter == "-":
        countsym += 1
    elif letter == ":":
        countsym += 1
print("Кількість розділових знаків ",countsym)

# Кількість !
count = 0
for symbol in sentence1:
    if symbol =="!":
        count +=1
print("Кількість ! ", count)


















