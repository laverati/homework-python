# Классная работа 20.09.2021

student_1 = {
"group": "9.26",
"age": "18",
}
student_2 = {
"group": "9.21",
"age": "20",
}
students = {
"Liza": student_1,
"Sasha": student_2
}

print(students)


# первое задание
import string

def cont_letters(text):
    d = {}
    for ch in string.ascii_letters:
        d [ch] = text.count(ch)
    return d

print(cont_letters('sgfltsgdjspafhcs'))



# второе задание
def delaem_goroda(p, s):
    goroda = {}
    goroda[p] = s
    return goroda


print(delaem_goroda(18, 20))



# третье задание
def aria_dicti(names, znach):
    n = names
    z = znach
    aria = {}
    for i, j in zip (n,z):
        aria[i] = j
    return aria

print(aria_dicti(['Maldives', 'Sochi', 'Tokio'], [{'a':1},{'b':2},{'c':3}]))



# ДЗ 20.09.2021
# функция unique и функция intersection

set_01 = {1, 2, 3, 4, 5, 6, 7, 6, 6, 0, 5}
set_02 = {5, 6, 7, 8, 9, 0}
set_03 = [1, 2, 3, 4, 5, 6]
set_04 = [1, 6, 7, 8, 9, 0]

def unique(spis):
    return list(set(spis))
print(unique(set_01))

def intersection(set_01, set_02):
    return list(set(set_01).intersection(set(set_02)))

print(intersection(set_03, set_04))