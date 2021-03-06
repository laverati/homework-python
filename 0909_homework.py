import random

big_names = ['Сазонова Анастасия Александровна', 'Тихонов Андрей Егорович', 'Зимин Всеволод Егорович',
             'Галкина Аврора Артемьевна', 'Иванов Артём Александрович', 'Чернов Демид Русланович',
             'Полякова Елизавета Григорьевна', 'Жуков Егор Михайлович', 'Миронова Милана Ильинична',
             'Морозова Елизавета Михайловна', 'Чистякова Варвара Степановна', 'Филиппов Александр Дмитриевич',
             'Максимов Максим Григорьевич', 'Фомичев Сергей Семёнович', 'Сорокина Анастасия Марковна',
             'Исаков Егор Маркович', 'Малышев Лев Макарович', 'Волков Андрей Дмитриевич', 'Зимин Артём Максимович',
             'Аксенов Андрей Матвеевич', ]

name = 'Mamrenko Elizaveta Vitalievna'

def show(func):
    def new_func(*args,**kwarg):
        print('Name of funcion - ' , func.__name__)
        print('args - ' , args)
        print('Kwargs - ' , kwarg)
        result = func(*args, **kwarg)
        return result
    return new_func

def initials(name):
    result = name.split()
    return result[0] + ' ' + result[1][0:1] + '. ' + result [2] [0:1] + '.'
#print (initials(name))

def initials_more(names):
    result = []
    for name in names:
        new_name = initials (name)
        result.append (new_name)
    return result


def gen_names(name, num):
     return [name for i in range(num)] 


def range_1(last=5):
    i = 0
    while i < last:
        yield big_names[random.randint(0, 19)]
        i = i + 1


ranger = range_1()

for x in ranger:
    print(x)


names = ['Mamrenko Elizaveta Vitalievna', 'Mamrenko Elizaveta Vitalievna']

print(gen_names('Mamrenko Elizaveta Vitalievna', 5))


@show
def get_elements_for(list_): # функция вывода элементов массива с буквами через for
    for k in list_:
        print(k)


print (get_elements_for(['Волков Андрей Дмитриевич', 'Исаков Егор Маркович']))


def get_elements_while(list_):
    k = 0
    while k < len(list_):
        print(list_[k])
        k += 1

