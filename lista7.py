# 1
a = 5
b = 9
print('Wartość a:', a, 'b:', b)
c = a
a = b
b = c
print('Wartość a:', a, 'b:', b)

print('\n')
# 2
def zmien(a, b):
    c = a
    a = b
    b = c
    print('[WEWNĄTRZ FUNKCJI] Wartość a:', a, 'b:', b)

a = 5
b = 9
zmien(a, b)
print('[POZA FUNKCJĄ] Wartość a:', a, 'b:', b)

print('\n')
# 3
def zmien(l):
    c = l[0]
    l[0] = l[1]
    l[1] = c
    print('[WEWNĄTRZ FUNKCJI] Wartość lista[0]:', l[0], 'lista[1]:', l[1])


lista = [5, 9]
zmien(lista)
print('[POZA FUNKCJĄ] Wartość lista[0]:', lista[0], 'lista[1]:', lista[1] )


print('\n')
# 4
def odwroc(lista):
    save = []
    for i in range(0,4):
        save.append(lista[i])
    for i in range(0, 4):
        lista[i] = save[(i+1)*(-1)]


l = [1, 5, 4, 3]
odwroc(l)
print(l)

print('\n')
# 5
import random
def sortuj(lista):
     leng = len(lista)
     for i in range(leng):
         for j in range(0, leng - i - 1):
             if lista[j] > lista[j + 1]:
                 c = lista[j]
                 lista[j] = lista[j + 1]
                 lista[j + 1] = c


l = []
for i in range(0, 10):
    l.append(random.randrange(1, 100))
print('Lista przed sortowaniem:', l)
sortuj(l)
print('Lista po sortowaniu:', l)
l = ['baron', 'jeniec', 'rycerz', 'krasnolud', 'elf', 'niziołek']
print('Lista przed sortowaniem:', l)
sortuj(l)
print('Lista po sortowaniu:', l)

print('\n')
# 6
def sortuj(lista):

    leng = len(lista)
    for i in range(leng):
        for j in range(0, leng - i - 1):
            if lista[j].lower() > lista[j + 1].lower():
                c = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = c
def sortujdlugosc(lista):

    leng = len(lista)
    for i in range(leng):
        for j in range(0, leng - i - 1):
            if len(lista[j]) > len(lista[j + 1]):
                c = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = c

zmienna = input('Podaj zdanie ze spacjami: ')
list = zmienna.split(' ')
sortuj(list)
dlugosc = len(list)
for i in range(dlugosc):
    print(list[i], end=' ')
print('\n')
sortujdlugosc(list)
for i in range(dlugosc):
    print(list[i], end=' ')