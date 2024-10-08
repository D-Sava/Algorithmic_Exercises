#Python je interpretirani programski jezik visokog nivoa. Podržava različite programske paradigme (objektno orijentisane, proceduralne, funkcionalne, itd). Glavna karakteristika je jednostavnost u smislu da u malom broju čitljivih linija mogu da se iskažu veoma zahtevne ideje. Još jedna vazna karakteristika je proširljivost.
#Bazični tipovi podataka: integer, float, boolean, string

#Ispisivanje varijable i tipa varijable na terminal
x = 5

print(type(x))
print(x)

#Osnovne operacije
print(x+5)
print(x-10)
print(x*25)
print(x/3)
print(x**2)#stepenovanje

#Skraceni oblik operacije i dodele nove vrednosti
x+=1
x-=2
x*=5
x/=2

#Tip podatka: float(decimalni broj)
y = 3.5

print(type(y))
print(y, y+1, y-3.234, y**3, y/2.5)

#Tip podatka: boolean
t = True
f = False

print(type(t)) # ispisuje "<class 'bool'>"
print(t and f) # logicko AND
print(t or f)  # logicko OR
print(not t)   # logicko NOT
print(t != f)  # logicko XOR

#Tip podatka: string
string1 = "Hello "
string2 = 'World'

print(string1 + string2)
print(type(string1), type(string2))

#fore sa stringovima
print(len(string1))
hw = string1 + ' ' + string2
print(hw)
hw12 = '%s %s %d' % (string1, string2, 12)  # c++ sprintf stil
print(hw12)

s = 'hello'
print(s.capitalize())  #Pravi veliko prvo slovo
print(s.upper()) #Konvertuje ceo string u velika slova
print(s.rjust(7)) #ravnanje na desno, popunjavanje razmacima
print(s.center(5)) #postavlja na centar, popunjava razmacima
print(s.replace('l', '(ell)')) #Zamenjuje sva pojavljivanja odredjenog stringa
print('  world '.strip())  #uklanja pocetne i krajnje razmake

# Kolekcije: lists, dictionaries, sets, and tuples
xs = [5,7,2]
print(xs[0],xs[1],xs[2])
print(xs[-1])
xs[1]='abc'
print(xs)

xs.append('efg')
print(xs)
x = xs.pop()
print(x, xs)

# isečci liste
nums = list(range(5))

print(nums)
print(nums[2:4])  # isecak od 2 do 4 (ne ukljucuje poslednji element)
print(nums[:2])   # od 2. do kraja
print(nums[2:])   # od pocetka do 2. (ne ukljucujuci ga)
print(nums[:])    # cela lista
print(nums[:-1])  # od prvog do poslednjeg (ne ukljucujuci poslednji)

nums[2:4] = [8,9]
print(nums)

# Petlje
zivotinje = ['pas', 'macka', 'konj']
for zivotinja in zivotinje:
    print(zivotinja)

# enumerate - korisna funkcija
for idx, z in enumerate(zivotinje):
    print('#%d: %s' % (idx + 1, z))

# koriscenje naredbe for u jednoj liniji koda
b = [0, 1, 2, 3, 4]
b2 = []
for x in b:
    b2.append(x ** 2)
print(b2)

b = [0, 1, 2, 3, 4]
b2 = [x ** 2 for x in b]
print(b2)
b3 = [x ** 2 for x in b2 if x % 2 == 0]

#Dictionary
d = {'macka':'bela', 'pas':'saren'}#kljuc:vrednost
print(d['macka']) #uzima se samo vrednost iz recnika

d2 = dict(one=1, two=2, info='neka informacija')
print(d2)

print('macka' in d)     # Proverava da li recnik ima kljuc macka
d['riba'] = 'siva'     # Dodavanje elementa
print(d['riba'])

print(d.get('majmun','Ne postoji.'))
print(d.get('riba', 'Ne postoji.'))
del d['riba']

# SKUPOVI
# Skup je kolekcija elemenata, u kojoj raspored nije bitan
#elementi mogu da budu razlicitog tipa
z = {'macka', 'pas'}
print('macka' in z)
print('macka' in z)
z.add('riba')
print('riba' in z)
print(len(z))

set([1,2,3,2])
A = {1,2,3}
A.remove(3)
A.discard(4)
A.discard(3)
print(A)

# dodavanje elemenata u skup
A = set()
A.update({0,10})
print(A)

A.update({1,10})
print(A)

# for sa skupovima
from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}
print(nums)