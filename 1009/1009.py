import string
def Gera():
    alphabets_in_lowercase=[]
    for i in string.ascii_lowercase:
        alphabets_in_lowercase.append(i)
    return alphabets_in_lowercase


s = string.ascii_lowercase
a = list(string.ascii_lowercase)
print(a)
b = list(s)
print(b)


l = [i for i in s ]
print(l)


def Liza(l):
    for l in l:
        print(l)

Liza(l)


def Liza_while (l):
    i = 0
    while i < len(l):
        print (l[i])
        i += 1