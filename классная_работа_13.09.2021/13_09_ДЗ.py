def zadanie_1(stroka):
    if stroka == stroka[::-1]:
        return True
    else:
        return False
print(zadanie_1('stroka'))



def zadanie_2(fname):
    l = fname.split('.')
    if len(l) < 2:
       return 'Invalid'
    else:
        return l[-1]
print(zadanie_2('fname'))



def zadanie_so_vremerem_3(seconds):
    sec = seconds
    time = ['12', '12', '12', '12']
    if sec // 86400:
        time[0] = str(sec // 86400)
        sec -= 86400 * (sec // 86400)
    if sec // 3600:
        time[1] = str(sec // 3600)
        sec -= (3600 * (sec // 3600))
    if sec // 60:
        time[2] = str(sec // 60)
        sec -= (60 * (sec // 60))
        time[-1] = str(sec)
    return time[0] + ':' + time[1] + ':' + time[2] + ':' + time[-1]
print(zadanie_so_vremerem_3(86400))



def zadanie_4(numbers):
    n = str(numbers)
    a = n + ' + ' + n * 4 + ' + ' + n * 6 + ' = '
    b = int(n) + int(n * 4) + int(n * 6)
    return a, b
print(zadanie_4(2))


 
def delayu_spisok_1(dz_1):
    a = dz_1
    a.sort()
    return a
print(delayu_spisok_1([56, 5, 40, 93, 24, 888]))



def delayu_spisok_2(dz_2):
    a = dz_2
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
print(delayu_spisok_2([12, 8, 34, 54, 264, 98,]))













