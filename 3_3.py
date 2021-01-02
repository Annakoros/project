def my_func(var1, var2, var3):
    """Функция принимает три числа и возвращает сумму двух наибольших"""
    newvar=[]
    newvar.extend([var1, var2, var3])
    newvar.sort()
    return newvar[1] + newvar[2]
mystr = input('Введите три числа через пробел: ')
mylist = mystr.split()
mynewlist = []
for myvar in mylist:
    mynewlist.append(float(myvar))
print(my_func(mynewlist[0], mynewlist[1], mynewlist[2]))