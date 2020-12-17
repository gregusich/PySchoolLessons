# 111309
def extract_digits(s):
    s = input()  # ввод строки
    s = "".join(i for i in s if i.isdigit())  # добавляем в строку s все элементы, которые являются числами,
    # а знаки заменяем пробелами
    print(s)


extract_digits(s=str)
