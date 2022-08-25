import datetime
import math
import time

import pip

'''
message = "Hello There. My name is Sadik Turan"
#message = message.upper()
#message = message.lower()
#message = message.title()
#message = message.capitalize()

#message = message.strip()
#message = message.split()
#message = message.split(".")
#message="---".join(message)
#print(message)
#print(message[1])

#index = message.find("Sadik")
#isFound = message.startswith('H')
#isFound = message.endswith('H')

#message=message.replace("Sadik","Cinar")
message=message.center(50,"*")
print(message)'''

#website = "http://www.sadikturan.com"
#course = "Python Kursu: Bastan Sona Python Programlama Rehberiniz (40 saat)"
#1
#a = " Hello World ".strip()
#a = " Hello World ".lstrip()
#a = " Hello World".rstrip()
#b = website.lstrip("/:pth")
'''website = "www.sadikturan.com"
c = "www.sadikturan.com".strip()
c = website.lstrip("w")
c = website.rstrip(".com"),("w")

print(c)
result = "www.sadikturan.com".strip("w.moc")
print(result)'''

#course = course.lower()

#print(course)

#print(website.count("a"))
#print(website.count("www",0,10))

#result = website.startswith("www")
#result = website.startswith("http")
#result = website.endswith("com")
#result = website.find("com",0,10)
#result = course.find("Python")
#result = course.find("Python")

#result = course.isalpha()
#result = "Hello".isalpha()
#result = "123".isdigit()

#result = "Contents".ljust(50,"*")
#result = "Contents".rjust(50,"*")

#result = course.replace(" ","-",5)
#result = course.replace(" ","")

#result = "Hello World".replace("World", "There")

#result = course.split(" ")
#result = result[2]
#result = result[5]
#print(result)

#message = "Hello There. My name is Sadik Turan"
#print(message[0])
'''
my_list = [1,2,3]
my_list=["bir,2,True,5.6"]
print(my_list)
message = "Hello There. My name is Sadik Turan"
list1 = ["one","two", "three"]
list2 = ["four","five","six"]
numbers=list1 + list2
print(numbers)
print(len(numbers))
print(message)
print(numbers[2])

userA= ["Sadik",36]
userB = ["Cinar",2]
users = [userA,userB]
print(userA)
print(userB)
print(users)
a = users[1]
print(a[0])
print(users[0][0])'''

#names = ["Ali","Yagmur","Hakan","Deniz"]
#years = [1998,2000,1998,1987]

#names.append("Cenk")
#names.insert(0,"Sena")
#names.insert(len(names),"Sena")

#names.remove("Deniz")
#names.pop()
#names.pop(1)

#index = names.index("Deniz")
#print(index)
#names.pop(3)

#result = "Ali" in names
#result =names.index("Ali")
#print(result)

#names.reverse()

#names.sort()
#years.sort()

#print(years)

#str = "Chevrolet,Dacia"
#result = str.split(",")
#print(result)

#min = min(years)
#max = max(years)

#print(min,max)

#result = years.count(1998)
#print(result)

#years.clear()
#print(years)
'''
markalar = []
marka = input("marka: ")
markalar.append(marka)
marka = input("marka: ")
markalar.append(marka)
marka = input("marka: ")
markalar.append(marka)

print(markalar)'''

'''list = [1,2,3]

tuple = (1, "iki", 3)

print(type(list[2]))
print((list[2]))
print(type(tuple))
print((tuple[2]))'''

'''list = ["ali", "veli"]
tuple = ("damla","ayse","ayse")
names = ("demet","emel","ayse")+tuple
list[0]="ahmet"


print(names)
print(tuple.count("ayse"))
print(tuple.index("ayse"))'''

#key - value

# 41 => kocaeli 34 => Istanbul

'''sehirler = ["kocaeli","istanbul"]
plakalar = [41,34]
print(plakalar[sehirler.index("istanbul")])

# print(plakalar["kocaeli"]) ==> 41
# print(plakalar["istanbul"]) ==> 34

plakalar = {"kocaeli":41,"istanbul":34}
print(plakalar["kocaeli"])

plakalar["ankara"] = 6
plakalar["kocaeli"] = "new value"

print(plakalar)'''

'''users = {"sadikturan": {
    "age":36,
    "email":"sadikturan@gmail.com",
    "address":"kocaeli"},
    "cinarturan":{
     "age":2,
     "email":"cinar@gmail.com"}}



print(users)
print(users["sadikturan"])
print(users["cinarturan"])
print(users["cinarturan"]["age"])
#print(users["cinarturan"]["email"])
x=(users["cinarturan"]["email"])
print(x)'''

'''ogrenciler = {}

number = input("ogrenci no: ")
name = input("ogrenci adi: ")
surname = input("ogrenci soyad: ")
phone = input("ogrenci telefon: ")

ogrenciler [number] = {
    "ad": name,
    "soyad": surname,
    "telefon": phone

}'''

'''ogrenciler.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": phone,
    }
})

number = input("ogrenci no: ")
name = input("ogrenci adi: ")
surname = input("ogrenci soyad: ")
phone = input("ogrenci telefon: ")

ogrenciler.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": phone,
    }
})
number = input("ogrenci no: ")
name = input("ogrenci adi: ")
surname = input("ogrenci soyad: ")
phone = input("ogrenci telefon: ")

ogrenciler.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": phone,
    }
})

print("*"*50)
ogrNo = input("ogrenci no: ")
ogrenci= ogrenciler[ogrNo]
print(ogrenci)
print(f"Aradiginiz {ogrNo} nolu ogrencinin adi: {ogrenci['ad']} soyadi {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")
'''
'''fruits = { "orange","apple","banana"}

#print(fruits[0]) indexlenemez

for x in fruits:
    print(x)

fruits.add("cherry")
print(fruits)
fruits.update(["mango","grape","apple"])
fruits.remove("mango")
fruits.pop()
fruits.clear()

print(fruits)

myList = [1,2,5,4,4,2,1]
print(set(myList))
print((myList))'''

'''x = 5
y = 25
x = y
y = 10
#print(x,y)

a = ["apple","banana"]
b = ["apple","banana"]

a=b
b[0] = "grape"

print(a, b)'''

'''x = 5
y = 10
z = 20'''

'''x,y, z = 5, 16 ,20

#x, y = y, x

#x = x + 5
x += 5
x -=5
x *= 5
y //= 5
y **=z

print(x,y,z)'''

'''values = 1, 2, 3 ,4 ,5
print(values)
print(type(values))

x, y ,*z = values
print(x,y,z[1])'''

x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

#1
'''a = x+y+z
print(a)
b = int(input("1. sayi:" ))
c = int(input("2. sayi: "))
result =(b*c) - (a)
print(result'''
#2
'''a = y // x
print(a)
#3

toplam = (x+y+z)
result = toplam %3
print(result)
#4
result = y ** x
#5
x, *y, z = numbers
print(x, y, z)
print(z)
result = (z**3)
#6
x, *y, z = numbers
print(x, y, z)
print(y)
result = sum(y)

print(result)'''

# username, password => database
#"sadikturan", "123456"

'''a, b, c, d = 5,5,10,4
password = "1234"
username = "sadikturan"
result = a==b # true
result = a == c
result = ("sadikturan"==username)
result = (a!=b)
result = (a!=c)
result = (a>b)
result = (a>c)
result = a<c
result = a>=b
result = False + True + 40



print(result)'''

#1
'''a = input("a: ")
b = input("b: ")
result = a>b
print(f"a {a} b {b} den buyuktur:{result}")'''

#2

'''vize1 = int(input("1. vize notunu giriniz: "))
vize2 = int(input("2. vize notunu giriniz: "))
Final = int(input("Final notunu giriniz: "))
result = (vize1*0.3)+(vize2*0.3)+(Final*0.4)

print(f"Yil sonu ortalamaniz :{result}")
if result >= 50:
    print("Sinifi gectiniz!")
else:
        print("Caktin!!!")'''

#3

'''sayi = int(input("sayi: "))

tekcift = (sayi %2 == 0 )

print(f"girilen sayi cift olma durumu: {tekcift}")'''

#4

'''sayi = int(input("sayi: "))
pozitifmi = sayi >0
print(f"girilen sayinin pozitif olma durumu: {pozitifmi}")'''

#5

'''email = "email@cc.com"
password = "abc123"

girilenEmail = input("email:")
girilenpassword = input("parola:")
isEmail = (email == girilenEmail.lower().strip())
isPassword = (password == girilenpassword.lower().strip())

print(f"Email bilgisi dogru mu : {isEmail} ve Paroladogrumu: {isPassword}")'''

'''x = 7
hak = 0
devam = "e"

#result = 5<x<10

result = (x >5) and (x < 10)
result = (hak>0) and (devam == "e")

result = (x > 0) or ( x % 2 == 0)

print(result)

result = not(x > 0)

result = ((x>5) and (x<10)) and (x%2==0)

print(result)

x = float(input("Bir sayi giriniz: "))

result = ((x>0) and (x<100))


print(f'sayi 0-100 arasinda mi: {result}')

x = float(input("Bir sayi giriniz: "))

result = (x>0 and x%2 == 0)

print(f'sayi 0 cift  mi: {result}')

email = "email@sadikturan.com"
password = "abc123"

girilenEmail = input ("email:")
girilenPassword = input("password:")

result = (girilenEmail == email ) and (girilenPassword == password)
print(f'uygulamaya giris basarili mi: {result}')

x = int(input("Birinci sayiyi giriniz:"))
y = int(input("Ikinci sayiyi giriniz:"))
z = int(input("Ucuncu sayiyi giriniz:"))

result = (x>y) and  (x>y)
print(f'x en buyuk sayidir: {result}')

result = (y>z) and (y>x)

print(f'y en buyuk sayidir: {result}')

vize1 = int(input("1. vize sonucunu gir: "))
vize2 = int(input("2. vize sonucunu gir: "))
final = int(input("Final sonucunu gir: "))
ortalama = ((vize1+vize2)*0.3) + (final*0.4)
son = ortalama < 50
#x = (ortalama >= 50) and (final >=50)
x = (ortalama >= 50) or (final >=70)
print(f'final 50 alti: caktin :{x}')
print(f"Ortalama 50 nin altinda, caktin {son}")

print(ortalama)

x = y = [1,2,3]
z = [1,2,3]

print(x==y)
print(x==z)
print(x is y)
print(x is z)

x = [1,2,3]
y = [2, 4]

del x[2]
y[1] = 1
y.reverse()
print(x)
print(y)
print(x==y)
print(x is y)
print(x is not y)

x = ["apple","banana"]
print("banana" in x)

name = "Cinar"
print("a" in name)
print("a" not in name)


isLoggedin = True

if isLoggedin:
    print("hos geldiniz")

isim = input("isim giriniz: ")
yas = int(input("yas giriniz: "))

if (yas>=18):
    egitim = input("en son diploma: ")
    if (egitim == "lise" or egitim == "universite"):
        print(f"{isim} Ehliyet alabilirsin")
    else:
        print(f"{isim} ehliyet senin neyine cahil")
else:
    print(f"{isim} babayi alirsin, bebek")

yazili1 = int(input("1. Yazili notunu gir "))
yazili2 = int(input("2. Yazili notunu gir "))
sozlu = int(input("Sozlu notunu gir "))

ort = int((yazili1+yazili2+sozlu)/3)

print(f"Ortalaman {ort}")

if 24>=ort>0:
    print("Mal degneyi seni !!!")
elif 25 <=ort<=44:
        print("Az malsin")
elif 45<=ort<=54:
        print("2 aldin")
elif 55<=ort<=69:
        print("anca 3")
elif 70<=ort<=84:
        print("fena degil")
elif 85<=ort<=100:
        print("aferin")

tarih = input("araciniz hangi tarihte trafige cikti (2022/07/09): ")
tarih = tarih.split('/')
print(tarih[0])
print(tarih[1])
print(tarih[2])
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days =fark.days

if days <= 365:
    print("1. servis araligi")
elif days > 365 and days<= 365*2:
    print("2. servis araligi")
elif days > 365*2 and days<= 365*3:
    print("3. servis araligi")
else:
    print("hatali sure..")

numbers = [1,2,3,4,5]

for a in numbers:
    print("Hello")

names = ["cinar","sadik","sena"]

for name in names:
    print(f"my name is {name}")

name = "Sadik Turan"

for n in name:
    print(n)

tuple = [(1,2),(3,4),(5,7)]

for a,b in tuple:
    print(a)

d = {"k1":1,"k2":2,"k3":3}

for key,value in d.items():
    print(key,value)'''

sayilar = [1,3,5,7,9,12,19,21]

'''for sayi in sayilar:
    if (sayi %3 == 0):
        print(sayi)

toplam = 0
for sayi in sayilar:
    toplam += sayi
print("toplam:", toplam)

sayilar = [1,3,5,7,9,12,19,21]

for tek in sayilar:
    if (tek%2 == 1):
       print(tek**2)

sehirler = ["kocaeli", "istanbul", "ankara", "izmir", "rize"]



for sehir in sehirler:
    if (len(sehir)<=5):
        print(sehir)'''


urunler = [{'name':'samsung s6','price':'3000'},
{'name':'samsung s7','price':'4000'},
{'name':'samsung s8','price':'5000'},
{'name':'samsung s9','price':'6000'},
{'name':'samsung s10','price':'7000'}]

'''toplam = 0

for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat

print(toplam)

for urun in urunler:
   if (int(urun['price']) <= 5000):
        print(urun['name'])'''

#numbers = [1,2,3,4,5]

x = 0

'''while x <= 100:
    if x %2 == 1:
        print(f'sayi tek :{x}')
    else:
        print(f'sayi cift:{x}')
    x += 1

print('bitti')'''

'''name = ''
while not name.strip():
    name = input('isminizi giriniz')

print(f'Merhaba,{name}')'''

'''sayilar = [1,3,5,7,9,12,19,21]

i = 0
while (i < len(sayilar)):
    print(sayilar[i])
    i += 1

bas = int(input('baslangic degeri'))
son = int(input('son deger'))
i = bas
while i < son:
    i += 1
    if (i % 2 == 1):
        print(i)'''

'''sayi = (0,100)
i=100
while i >0:
    i -= 1
    print(i)'''

'''a = int(input('1. sayi'))
b = int(input('2. sayi'))
c = int(input('3. sayi'))
d = int(input('4. sayi'))
e = int(input('5. sayi'))

numbers = [a,b,c,d,e]
numbers = []
i = 0
while i<5:
        sayi = int(input('sayi: '))
        numbers.append(sayi)
        i += 1

numbers.sort()
print(numbers)'''

'''urunler = []

adet = int(input('kac adet urun eklemek isityon'))
i = 0

while (i<adet):
    name = input('urun ismi: ')
    price = input('urun fiyati: ')
    urunler.append({
        'name: ': name,
        'price:': price
    })
    i += 1

for urun in urunler:
    print(f'urun adi: {urun["name"]} urun fiyati: {urun["price"]}')'''

'''name = 'Sadik Turan'

for letter in name:
    if letter == 'i':
        continue
    print(letter)'''


'''x = 0
while x < 5:
    x+=1
    if x == 2:
        continue
    print(x)'''

'''x = 0
result = 0

while x <= 100:
    x += 1
    if x % 2 ==1:
        continue
    result+=x

print(f'toplam : {result}')'''

#list = [1,2,3]

'''for item in range(50,100,10):
    print(item)

print(list(range(5,100,10)))'''

#enumarate


'''greeting = 'hello there'

for index,item in enumerate(greeting):
    print(f'index:{index} letter:{item}')'''

'''list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = [100, 200, 300, 400, 500]

print(list(zip(list1, list2, list3)))

for item in zip(list1, list2, list3):
    print(item)'''



'''for a, b, c in zip(list1, list2, list3):
    print(a, b, c)'''

'''numbers = []
for x in range(10):
    numbers.append(x)
print(numbers)
numbers = [x for x in range(10)]
print(numbers)

for x in range(10):
    print(x**2)

numbers = [x**2 for x in range(10)]
print(numbers)

numbers = [x*x for x in range(10) if x %3 == 0]
print(numbers)

myString = 'Hello'
mylist = []

for letter in myString:
    mylist.append(letter)

print(mylist)

mylist = [letter for letter in myString]
print(mylist)

years = [1983, 1999, 2008, 1956, 1986]
ages = [2019- year for year in years]
print(ages)

result = [x if x%2 == 0 else 'TEK' for x in range(1,10)]
print(result)

result = []

for x in range(3):
    for y in range(3):
        result.append((x,y))

print(result)

numbers = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
numbers = [(x,y) for x in range(3) for y in range(3) ]
print(len(numbers))'''

#python random

import random

#random(0,100)
'''from random import randrange
puan = 'Puanin simdilik 100'
print(puan)
benimTuttugum = randrange(0, 3)
sayi = int(input('1 ile 3 arasi sayi gir la   '))
if sayi > benimTuttugum:
        print('bilemedin')
        print('cok attin')
        print('tekrar dene')
elif sayi < benimTuttugum:
    print('ufak attin')
else:
    print('ohaa bildin')

print(benimTuttugum)

if sayi == benimTuttugum:
    puan = 100+40
    print(f'Son puanin {puan}')
else:
    puan = 100-20
    print(f'Yeni Puanin {puan}')'''

'''sayi = random.randint(1, 10)
can = int(input('kac hak kullanmak isterseniz: '))
hak = can
sayac = 0
while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('tahmin: '))

    if sayi == tahmin:
        print(f'Tebrikler {sayac}. defada bildiniz. Toplam puaniniz :{100 - (100/can)*(sayac-1)}')
        break
    elif sayi > tahmin:
        print('yukari')
    else:
        print('asagi')

    if hak == 0:
        print(f'tahmin hakkiniz bitti. Tutulan sayi ; {sayi}')'''


'''sayiAsal = int(input('gir bakalim sayin asal mi? '))
asalmi = True

if sayiAsal == 1:
    asalmi = False
for i in range(2, sayiAsal):
    if (sayiAsal % i == 0):
        asalmi = False
        break

if asalmi:
    print('sayi asaldir')
else:
    print('sayi asal degildir')'''


'''if (sayiAsal/sayiAsal == 1) and (sayiAsal % random.randint(1, 1000) != 0):
    print('sayin ASAL')
else:
    print('sayin asal degil')'''

'''list = [1, 2, 3]

list.append(4)
list.pop()

print(type(list))
print(list)

myString = 'Hello'

print(myString.upper())


print(type(myString))'''

#function

'''def sayHello(name = 'user'):
    return 'Hello '+ name

msg = sayHello('Cinar')
msg = sayHello('cihan')

print(msg)

def total(num1, num2):
    return num1 + num2

result = total(10, 20)
result = total(15, 20)
print(result)

def yasHesapla(dogumyili):
    return 2019 - dogumyili

ageCinar = yasHesapla(2017)
ageAda = yasHesapla(2010)

print(ageCinar, ageAda)

def emekliligekacyilkaldi(dogumYili, isim):
   
    Docstring: dogumyiliniza gore emekliliginize kac yil kaldi
    Input: Dogum yili
    Output: kac yil kaldi

  
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0 :
        print(f'emekliliginize {emeklilik} yil kaldi')
    else:
        print('zaten emekli oldunuz')

emekliligekacyilkaldi(1983, 'Ali')
emekliligekacyilkaldi(1950, 'Ali')
emekliligekacyilkaldi(1974, 'Ali')

print(help(emekliligekacyilkaldi))

list = [1, 2, 3]

print(help(list.append))'''

'''def changeName(n):
    n = 'ada'

name = 'yigit'

changeName(name)
print(name)

def change(n):
    n[0] = 'istanbul'

sehirler = ['ankara', 'izmir']
n = sehirler [:]
n[0] = 'istanbul'

change(sehirler[:])


print(sehirler)
print(n)'''

'''def add(*params):
    print(type(params))
    sum = 0

    for n in params:
        sum = sum + n

    return sum

print(add(10, 20, 30,50, 100))
print(add(10, 20, 30))

def displayUser(**args):
    print(type(args))
    for key, value in args.items():
        print('{} is {} '.format(key, value))

displayUser(name = 'Cinar', age =2, city = 'Ankara')
displayUser(name = 'Ada', age =22, city = 'kocaeli', phone = '1234567')
displayUser(name = 'yigit', age =14, city = 'istanbul', phone = '1234567', email = 'yigitQemail.com')

def myfunc(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myfunc(10, 20, 30, 40, 50,60, 70, key1='value 1', key2 = 'value 2')'''

'''#kelime = input('kelime gonder: ')
def yaz(kelime, kere):
    print(kelime * kere)

yaz('Merhaba\n ', 10)
#kere = int(input('kac kere yazsin? '))
#return yaz()'''

'''def listeyeCevir(*params):
    liste = []

    for param in params:
        liste.append(param)

    return liste

result = listeyeCevir(10,5, 6 ,8, 6, 3, 20, 30, 'Merhaba')

print(result)'''



'''def asalSayiBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

sayi1 = int(input('1. sayiyi gir:'))
sayi2 = int(input('2. sayiyi gir:'))

asalSayiBul(sayi1, sayi2)'''

'''def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2, sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)

    return tamBolenler

print(tamBolenleriBul(90))'''

''''#def square(num): return num**3
#square = lambda num: num**2
numbers = [1, 3, 5, 9, 10, 4]

#list(map(square, numbers))
#result = list(map(square, numbers))
#result = list(map(lambda num: num**2, numbers))
#result = square(3 )
#for item in map(square, numbers):

def check_even(num): return num % 2 == 0

#result = list(filter(check_even, numbers))
#result = list(filter(lambda num: num%2==0, numbers))
#result = list(filter(check_even, numbers))
result = check_even(numbers[2])
print(result)'''
#global scope
'''x = 'global x'

def function():
    # local scope
    x = 'local x'
    print(x)
function()
print(x)'''

'''name = 'Cinar'

def changeName(new_name):
    name = new_name
    print(name)

changeName('Ada')
print(name)'''

'''name = 'global string'

def greeting():
    name = 'Cinar'

    def hello():
        #name = 'Ada'
        print('hello ' + name)

    hello()

greeting()'''

'''x = 50

def test():
    global x
    print(f'x = {x}')

    x = 100
    print(f'changed x to {x}')

test()
print(x)'''

#bankamatik

'''SadikHesap = {
    'ad' : 'Sadik Turan',
    'hesapNo': '12345678',
    'bakiye': 3000,
    'ekHesap': 2000
}
AliHesap = {
    'ad' : 'Ali Turan',
    'hesapNo': '12345678',
    'bakiye': 2500,
    'ekHesap': 1500,
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")
    bakiyeSorgula(hesap)
    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print(f" {miktar}  TL paranizi alabilirsiniz.")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input(f" {miktar} TL icin ek hesap kullanilsin mi (e/h) ")
            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = (hesap['bakiye'] + hesap['ekHesap']) - miktar
                hesap['bakiye'] = 0
                hesap['ekHesap'] = hesap['ekHesap'] - miktar
                print(f" {hesap['ekHesap']} TL ek hesabinizda kaldi.")
                print(f" {miktar}  TL paranizi alabilirsiniz.")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} bulunmaktadir.")
                bakiyeSorgula(hesap)
        else:
            print('uzgunuz')
            bakiyeSorgula(hesap)


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']}TL bulunmaktadir. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadir")


paraCek(SadikHesap, 3000)
print('***************')
paraCek(SadikHesap, 1300)
print('***************')
paraCek(SadikHesap, 600)
print('***************')
paraCek(SadikHesap, 50)
print('***************')
paraCek(SadikHesap, 25)
print('***************')'''


#class => Person (name, surname, birthday, calculateAge())

'''lst1 = [1, 2, 3]
lst2 = [1, 2, 3, 4]



result = type(lst1)
result = type(lst2)

print(result)

#class Person:
    #pass
    #class attributes

    # constructor (yapici method)
    def__init__(self, name, year):
    #object attributes
        self.name = name
        self.birthyear = year
        print('init methodu calisti')

    #methods

#object (instance)

p1 = Person('ali', 2022)
p2 = Person('yagmur', 2010)
print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1 == p2)'''


'''class Person:
    address = 'no information'
    def __init__ (self, name, year) :
        self.name = name
        self.year = year
        print('*****')
    def intro(self):
        print("Hello there.I am ", self.name)

    def calculateAge(self):
        return 2019 - self.year

p1 = Person(name='ali', year=2000)
p2 = Person(name='yagmur', year=2010)

#p1.name = 'ahmet'
#p1.address = 'kocaeli'

#print(f'p1 name: {p1.name} year: {p1.year} address : {p1.address}')
#print(f'p2 name: {p2.name} year: {p2.year} address : {p2.address}')

#print(p1)
#print(p2)

p1.intro()
p2.intro()

print(f'adim: {p1.name} ve yasim: {p1.calculateAge()}')
print(f'adim: {p1.name} ve yasim: {p2.calculateAge()}')'''

'''class Circle:
    #class object attribute
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    def cevre_hesapla(self):
        return 2*self.pi * self.yaricap

    def alan_hesapla(self):
        return self.pi * (self.yaricap **2)

c1 = Circle()
c2 = Circle(5)

print(f'c1: alan= {c1.alan_hesapla()} cevre = {c1.cevre_hesapla()}')
print(f'c2: alan= {c2.alan_hesapla()} cevre = {c2.cevre_hesapla()}')'''

'''class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('Person Created')

    def who_i_am(self):
        print('I am a person')

    def eat(self):
        print('I am eating')

class Student(Person):
    def __init__(self,fname,lname, number):
        Person.__init__(self, fname, lname)
        self.studentnumber = number
        print('Student Created')
#override
    def who_i_am(self):
        print('I am a student')

    def sayHello(self):
        print('Hello i am a student')

class Teacher(Person):
    def __init__(self,fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch
    def who_i_am(self):
        print(f'I am a {self.branch}teacher')

p1 = Person('Ali', 'Yilmaz')
s1 = Student('Cinar', 'Turan', 1256)
t1 = Teacher('Serkan', 'Yilmaz','math')
print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.studentnumber))

p1.who_i_am()
s1.who_i_am()
p1.eat()
s1.eat()
s1.sayHello()
t1.who_i_am()
'''

'''mylist = [1, 2, 3]
myString = 'my string'
print(len(mylist))
print(len(myString))
print(type(mylist))
print(type(myString))

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie objesi olusturuldu')

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration
    def __del__(self):
        print('film silindi')


m = Movie('film adi', ' yonetmen adi', 120)


#print(str(mylist))
print(str(m))

#print(len(mylist))
#print(len(m))


# print(m)'''

#class Quiz(self):
    #pass

'''class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-'+q)
        answer = input('cevap: ')
        self.guess(answer)
        self.loadQuestion()
    def guess(self, answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

 

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print('score: ', self.score)
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print('Quiz bitti.')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100,'*'))



q1 = Question('en iyi proglama dili hangisidir?', ['C#','python', 'Javascript', 'Java'], 'python')
q2 = Question('en iyi populer dili hangisidir?', ['Javascript', 'C#','python', 'Java'], 'python')
q3 = Question('en cok  kazandiran dili hangisidir?', ['Java','C#','python', 'Javascript'], 'python')
questions = [q1,q2,q3]
print(q1.checkAnswer('python'))
print(q2.checkAnswer('C#'))
print(q3.checkAnswer('python'))

quiz = Quiz(questions)
#question = quiz.getQuestion()
#print(question.text)

quiz.loadQuestion()'''
#YONTEM 2
#import math as islem

#value = dir(math)
#value = help(math)
#value = help(math.factorial)
#value = math.sqrt(49)
#value = math.factorial(9)
#value = math.floor(5.9)
#value = math.ceil(5.9)

#value = islem.factorial(5)



#print(value)

#YONTEM 2



from math import factorial,sqrt, ceil
'''def sqrt(x):
    print('x: ' + str(x))
#value = factorial(5)
value = sqrt(9)
#value = ceil(9)

print(value)'''

'''import random

#result = dir(random)
#result = help(random)

result = random.random()
result = random.random() * 100
result = int(random.uniform(10,100))
result = random.randint(1,100)

greeting = 'hello there'
names = ['ali', 'yagmur', 'deniz', 'cengiz']
#result = names[random.randint(0,len(names)-1)]
result = random.choice(names )
result = random.choice(greeting)

liste = list(range(10))
random.shuffle(liste)
result = liste

liste = range(100)
result = random.sample(liste, 3)
result = random.sample(names, 2)


print(result)'''

'''import mod

#result = help(mod)
#result = help(mod.func)

result = mod.number
print(result)
result = mod.numbers
print(result)
result = mod.person["name"]
print(result)
result = mod.person["age"]
print(result)
result = mod.func(10)
p = mod.Person()
p.speak()
print(result)

import sys
sys.path'''

#error

#print(a) => NameError

#int('1a2') ==> ValueError

#print(10/0) =>zerodivision error

#print('denem'e) =>syntax error
'''try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x/y)
except (ZeroDivisionError, ValueError) as e:
    print(e)
    print('yanlis bilgi')'''
#except ValueError:
    #print('x ve y icin sayisal deger girin5)

'''while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as ex:
        print(' yanlis bilgi', ex)
    else:
        break
    finally:
        print('try except sonlandi')'''

'''x = 10

if x > 5:
    raise Exception("x 5 den buyuk deger alamaz")'''

'''def check_password(psw):
    import re
    if len(psw) < 8:
        raise Exception("parola en az 7 karakter olmali")
    elif not re.search("[a-z]", psw):
        raise Exception("parola kucuk harf icermelidir")
    elif not re.search("[A-Z]", psw):
        raise Exception("parola buyuk harf icermelidir")
    elif not re.search("[0-9]", psw):
        raise Exception("parola rakam icermelidir")
    elif not re.search("[_@$]", psw):
        raise Exception("parola alpha numeric karakter icermelidir")
    elif re.search("\s", psw):
        raise Exception("parola bosluk icermemelidir")
    else:
        print("gecerli parola")
password = "12345_As"

try:
    check_password(password)

except Exception as ex:
    print(ex)
else:
    print("gecerli parola: else")

finally:
    print("validation tamamlandi")'''

'''class Person:
    def __init__(self,name, year):
        if len(name) > 10:
            raise Exception("name alani fazla karakter iceriyor")
        else:
            self.name = name

p = Person("aliiiiiiiiiiiii", 1989)'''

liste = ["1","2","5a","10b","abc","10","50"]

'''for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue'''

'''while True:
    sayi = input('sayi:')
    if sayi == 'q':
        break

    try:
        result = float(sayi)
        print('girdiginiz sayi: ', result)
    except ValueError:
        print('gecersiz sayi')
        continue'''

'''def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError('Negatif deger')

    result = 1

    for i in range(1, x+1):
        result *= i
    return result

for x in [5,10,20, -3,'10a']:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)'''

#file = open("newfile.txt","w")

#file.close()

#file = open("C:/users/admin/desktop/newfile.txt","w")
#file.close()
#file = open ("newfile.txt","w", encoding='utf-8')
#file.write("Cihan Büyükburç")
#file.close()

'''file = open ("newfile.txt","a", encoding='utf-8')
file.write("\nMert Cihan")
file.write("Mert Cihan")
file.close()'''

#file = open("newfile2.txt","a", encoding='utf-8')
'''try:
    file = open("newfile.txt","r")
except FileNotFoundError:
    print("dosya okuma hatasi")
finally:
    print("dosya kapandi.")
    file.close()

file = open("newfile.txt", "r", encoding="utf-8")'''

'''for i in file:
    print(i, end="")'''

'''content = file.read()

print("icerik 1")
print(content)

content2 = file.read()
print("icerik 2")
print(content2)'''
'''content= file.read(5)
content= file.read(3)
content= file.read(3)
print(content)
file.close()'''

'''content = file.readline()
print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline())

liste = file.readlines()
print(liste[0])
print(liste[1])
print(liste[2])

file.close()'''

'''with open("newfile.txt","r",encoding="utf-8") as file:

    content = file.read(0)
    print(content)
    file.seek(0)
    print(file.tell())
    content2 = file.read()
    print(content2)'''



'''with open("newfile.txt","r+",encoding="utf-8") as file:
    file.seek(20)
    file.write('deneme')

with open("newfile.txt","r+",encoding="utf-8") as file:
    print(file.read())'''
#****sayfa sonunda guncelleme****
'''with open("newfile.txt","a",encoding="utf-8") as file:
    file.write("\nEmel Turan")

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())'''
#****sayfa basinda guncelleme****
'''with open("newfile.txt","r+",encoding="utf-8") as file:
    content = file.read()
    content = "Efe Turan\n" + content
    file.seek(0)
    file.write(content)

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())'''

#****sayfa ortasinda guncelleme****

'''with open("newfile.txt","r+",encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1, "yilmaz\n")
    file.seek(0)
    for i in list:
        file.write(i)

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())'''

'''def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(':')
    ogrenciAdi = liste[0]
    notlar = liste[1].split(',')
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1+not2+not3)/3

    if ortalama>=90 and ortalama <=100:
        harf = "AA"
    elif ortalama>=85 and ortalama <= 89:
        harf = "BA"
    elif ortalama>=65 and ortalama <= 85:
        harf = "CC"
    else:
        harf = "FF"

    return ogrenciAdi + ": " + harf + "\n"

def ortalamalari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))

def not_gir():
    ad = input('Ogrenci adi: ')
    soyad = input('Ogrenci soyadi: ')
    not1 = input('Ogrenci not 1: ')
    not2 = input('Ogrenci not 2: ')
    not3 = input('Ogrenci not 3: ')

    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad + ' ' + soyad + ':' + not1+','+not2+','+not3+'\n')


def notlari_kayitet():
    with open('sinav_notlari.txt',"r", encoding="utf-8") as file:
        liste = []

        for i in file:
            liste.append(not_hesapla(i))

        with open("sonuclar.txt","w", encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)


while True:
    islem = input('1- Notlari oku\n2 - Not gir\n3 - Notlari kayit et\n4 - cikis\n')

    if islem == '1':
        ortalamalari_oku()
    elif islem == '2':
        not_gir()
    elif islem == '3':
        notlari_kayitet()
    else:
        break'''

'''def greeting(name):
    print('hello', name)

#print(greeting('Ali'))
#print(greeting())

sayHello = greeting
#print(sayHello)
#print(greeting)

#print(greeting('Ali'))
#print(sayHello('Ali'))

del sayHello
print(greeting)'''


#encapsulation


'''def outer(num1):
    print('outer')
    def inner_increment(num1):
        print('inner')
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1,num2)
outer(10)
#inner_increment(10)'''

'''def factorial(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer")

    if not number >= 0:
        raise ValueError("number must be zero or pozitive")


    def inner_factorial(number):
        if number <=1 :
            return 1

        return number * inner_factorial(number - 1)

    return inner_factorial(number)
try:
    print(factorial("4"))
except Exception as ex:
    print(ex)'''

'''def usalma(number):
    def inner(power):
        return number ** power
    
    return inner

two = usalma(2)
three = usalma(3)

print(two(3))
print(three(4))
'''

'''def yetki_sorgula(page):
    def inner(role):
        if role == 'Admin':
            return "{0} rolu {1} sayfasina ulasabilirsiniz.".format(role,page)
        else:
            return "{0} rolu {1} sayfasina ulasamazsiniz.".format(role,page)
    return inner
user1 = yetki_sorgula("Product Edit")
print(user1("Admin"))
print(user1("User"))'''

'''def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim*=i
        return carpim

    if islem_adi == "toplama":
        return toplam
    else:
        return carpma

toplama = islem("toplama")
print(toplama(1,3,5,6,7))

carpma = islem("carpma")
print(carpma(1,3,5,6,7))'''

'''def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def islem(f1,f2,f3,f4, islem_adi):
    if islem_adi == "toplama":
        print(f1(2,3))

    elif islem_adi == "cikarma":
        print(f2(5,3))

    elif islem_adi == "carpma":
        print(f3(3,4))

    elif islem_adi == "bolme":
        print(f4(10,2))

    else:
        print("gecersiz islem")

islem(toplama,cikarma,carpma,bolme,"toplama")
islem(toplama,cikarma,carpma,bolme,"cikarma")
islem(toplama,cikarma,carpma,bolme,"carpma")
islem(toplama,cikarma,carpma,bolme,"bolme")
islem(toplama,cikarma,carpma,bolme,"bolmeee")'''

'''def my_decorator(func):
    def wrapper(name):
        print("fonksiyondan onceki islemler")
        func(name)
        print("fonksiyondan sonraki islemler")
    return wrapper
@my_decorator
def sayhello(name):
    print("hello", name)

sayhello("ali")

def saygreeting():
    print("greeting")

sayhello = my_decorator(sayhello)
saygreeting = my_decorator(saygreeting)
saygreeting()'''

'''import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print("fonksiyon " +func.__name__+" "+ str(finish - start) + " saniye surdu.")
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))
@calculate_time
def faktoriyel(num):
    print(math.factorial(num))
@calculate_time
def toplama(a,b):
    print(a+b)
usalma(2,3)
faktoriyel(4)
toplama(10,20)
'''
'''
liste = [1,2,3,4,5]

iterator = iter(liste)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator))

for i in liste:
    print(i)

iterator = iter(liste)

while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break'''

'''class MyNumbers:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

list = MyNumbers(20,50)

myiter = iter(list)
#print(next(myiter))

while True:
    try:
        element = next(myiter)
        print(element)
    except StopIteration:
        break

#for x in list:
#    print(x)'''


'''def cube():

    for i in range(5):
        yield i**3

#iterator = cube()

#iterator = iter(generator)
for i in cube():
    print(i)'''

'''generator = (i**3 for i in range(5))

for i in generator:
    print(i)'''

'''from datetime import datetime
from datetime import timedelta
from datetime import date
from datetime import time

simdi = datetime.today()
result = (datetime.now())
result = datetime.now()
result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.second

result = datetime.ctime(simdi)
result = datetime.strftime(simdi,'%Y')
result = datetime.strftime(simdi,'%X')
result = datetime.strftime(simdi,'%D')
result = datetime.strftime(simdi,'%A')
result = datetime.strftime(simdi,'%B')
result = datetime.strftime(simdi,'%Y %B %A')

t = '21 Nisan 2019'

gun, ay, yil = t.split()
print(gun)
print(ay)
print(yil)

t = '15 April 2019 hour 10:12:30'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
result = result.year

birthday = datetime(1983, 5, 9, 12,30,10)
#print(birthday)
result = datetime.timestamp(birthday)
result = datetime.fromtimestamp(result)
result = datetime.fromtimestamp(0)

result = simdi - birthday #timedelta
#result = result.days
#result = result.seconds
#result = result.microseconds
print(simdi)
result = simdi + timedelta(days=730, minutes=10)
result = simdi - timedelta(days=10)

print(result)'''

'''import os
import datetime
result = dir(os)
result = os.name
dizin degistirme
os.chdir("..")
os.chdir("../..")
os.chdir("..")'''
'''result = os.getcwd()
#os.mkdir("newdirectory2")'''

#os.makedirs("C:\\newdirectory2/yeniklasor")
#result = os.listdir("C:\\")
#for dosya in os.listdir():
#    if dosya.endswith(".py"):
#        print(dosya)

#result = os.stat("main.py")
#result = result.st_size/1024
#result = datetime.datetime.fromtimestamp(result.st_ctime)
#result = datetime.datetime.fromtimestamp(result.st_ctime)
#result = datetime.datetime.fromtimestamp(result.st_atime)
#result = datetime.datetime.fromtimestamp(result.st_ctime)
#result = datetime.datetime.fromtimestamp(result.st_mtime)

#os.system("notepad.exe")

#os.rename("newdirectory2","yenibisi")
#os.rmdir("newdirectory")
#os.rmdir("yenibisi/yeniklasor")

# path
'''result = os.path.abspath("_os.py")
result = os.path.dirname("C:/Users/Admin/PycharmProjects/pythonProject/_os.py")
result = os.path.dirname(os.path.abspath("_os.py"))
result = os.path.exists("main.py")
result = os.path.isfile("C:/Users/Admin/PycharmProjects/pythonProject/main.py")
result = os.path.join("C:\\","deneme","deneme1")
result = os.path.split("C:\\deneme")
result = os.path.splitext("main.py")
#result = result[0]
#result = result[1]



print(result)'''

'''import re

result = dir(re)
#re module

str = "Python Kursu: Python Programlama Rehberi | 40 saat"

#result = re.findall("Python", str)
#result = len(result)

#result = re.split(" ",str)
#result = re.split("R",str)

#result = re.sub("\s","-",str)

#result = re.search("Python",str)
#result = result.span()
#result = result.start()
#result = result.end()
#result = result.group()
#result = result.string

result = re.findall("[abc]",str)
result = re.findall("[sat]",str)
result = re.findall("[P-z]",str)
#result = re.findall("[0-5]",str)
result = re.findall("[^abc]",str)
#regular expression

result = re.findall("Py..on",str)

result = re.findall("^P",str)

result = re.findall("saat$",str)
result = re.findall("saatt$",str)

result = re.findall("sa*t",str)
result = re.findall("sa+t",str)
result = re.findall("sa?t",str)
result = re.findall("sa?t",str)

result = re.findall("(a{2})",str)
result = re.findall("[0-9]{2}",str)

result = re.findall("saat\Z",str)

print(result)'''

#JSON
'''import json
import os


#JSON string to Dict

#result = json.loads(person_string)
#result = result["name"]
#result = result["languages"]

with open("person.json") as f:
    data = main.load(f)
    print(data)
print(result)
person_string = '{"name":"Ali","languages":["python","C#"]}'

person_dict ={"name":"Ali","languages":["Python","C++"]}

result = json.dumps(person_dict)
print(result)
print(type(result))

#with open("person.json","w") as f:
#    json.dump(person_dict, f)

person_dict = json.loads(person_string)
result = json.dumps(person_dict, indent = 4, sort_keys= True)
print(person_dict)
print(result)'''

'''import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        #load users from json file
        self.loadUser()

    def loadUser(self):
        if os.path.exists('users.json'):
            with open('users.json','r', encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username = user['username'], password=user['password'], email=user['email'])
                    self.users.append(newUser)
            print(self.users)
    def register(self,user: User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanici olusturuldu!")
    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('login yapildi')
                break
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('Cikis yapildi')

    def identity(self):
        if self.isLoggedIn:
            print(f'username: {self.currentUser.username}')
        else:
            print('giris yapilmadi')

    def savetoFile(self):
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open('users.json','w') as file:
            json.dump(list, file)

repository = UserRepository()

while True:
    print('Menu'.center(50,'*'))
    secim = input('1- Register\n2- Login\n3- Logout\n4- identity\n5- Exit\nseciminiz: ')
    if secim == '5':
        break
    else:
        if secim == '1':
            username = input('username: ')
            password = input('password: ')
            email = input('email: ')

            user = User(username = username, password = password, email= email)
            repository.register(user)


        elif secim == '2':
            if repository.isLoggedIn:
                print('zaten login oldunuz')
            else:
                username = input('username: ')
                password = input('password: ')
                repository.login(username, password)
        elif secim == '3':
            repository.logout()
        elif secim == '4':
            repository.identity()
        else:
            print("yanlis secim")'''

# Request Modulu

'''import requests
import json

result = requests.get('https://jsonplaceholder.typicode.com/todos')
result = json.loads(result.text)

for i in result:
    if i["userId"]==1:
        print(i["title"])


print(type(result))'''

'''import requests

url = "https://api.apilayer.com/exchangerates_data/latest?symbols={symbols}&base={base}"

payload = {}
headers= {
  "apikey": "996XAjQdBbT2DddAL6NA1sLbP2yRp2Wo"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text'''


#GITHUB
'''import requests
import json

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        #self.token = ''

    def getUser(self, username):
        response = requests.get(self.api_url+ '/users/'+ username)
        return response.json()
    def getRepositories(self,username):
        response = requests.get(self.api_url+'/users/'+ username+'/repos')
        return response.json()
    def createRepository(self, name):
        requests.post(self.api_url+'/user/repos?access_token'+self.token, json={})
github = Github()

while True:
    secim = input('1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSecim: ')

    if secim == '4':
        break
    else:
        if secim == '1':
            username = input('username: ')
            result = github.getUser(username)
            print(f"name: {result['name']}'public repos: {result['public_repos']} follower: {result['followers']}]")

        elif secim == '2':
            username = input('unsername: ')
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name'])
        elif secim == '3':
            pass
        else:
            print('yanlis secim')'''

'''import requests

class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "c2295ea1c729f8f6d308ff987b02a5b0"


    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSearchResults(self, keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()
movieApi = theMovieDb()

while True:
    secim = input("1- Popular Movies\n2- Search Movies\n3- Exit\nSecim: ")

    if secim == "3":
        break
    else:
        if secim == "1":
            movies = movieApi.getPopulars()
            for movie in movies['results']:
                print(movie['title'])
        if secim == "2":
            keyword = input('keyword: ')
            movies = movieApi.getSearchResults(keyword)
            for movie in movies['results']:
                print(movie['name'])'''

html_doc = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>ilk web sayfam</title>
</head>
<body>
    <h1 id="header">
        Python Kursu
    </h1>

    <div class="grup1">
        <h2>
           Programlama
        </h2>

        <ul>
            <li>Menu 1</li>
            <li>Menu 2</li>
            <li>Menu 3</li>

        </ul>
    </div>

    <div class="grup2">
        <h2>
           Moduller
        </h2>

        <ul>
            <li>Menu 1</li>
            <li>Menu 2</li>
            <li>Menu 3</li>

        </ul>
    </div>
    <div class="grup3">
        <h2>
           Django
        </h2>

        <ul>
            <li>Menu 1</li>
            <li>Menu 2</li>
            <li>Menu 3</li>

        </ul>
    </div>
</body>
</html>'''

'''from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,'html.parser')

result = soup.prettify()
result = soup.title
result = soup.head
result = soup.body

result = soup.title.name
result = soup.title.string
result = soup.h1
result = soup.h2.name
result = soup.h2.string
result = soup.h1.string
result = soup.find_all('h2')[0]
result = soup.find_all('h2')[1]

result = soup.div
result = soup.find_all('div')[1].ul.find_all('li')

result = soup.div.findChildren()
result = soup.div.findPreviousSibling().findNextSibling().findNextSibling()
print(result)'''

'''import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")

list = soup.find('tbody',{"class":"lister-list"}).find_all("tr",limit=10)
count = 1
for tr in list:
    title =tr.find("td",{"class":"titleColumn"}).find("a").text
    year = tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
    rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text


    print(f"{count}- film: {title.ljust(50)} yil: {year} degerlendirme {rating}")
    count += 1'''

'''import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content

soup = BeautifulSoup(html,"html.parser")

list = soup.find_all("li",{"class":"column"},limit =1)

for li in list:
    name = li.div.a.h3.text.strip()
    link = li.div.a.get("href")
    oldprice = li.find("del").find_all[1].text
    newprice = li.find("ins").find_all

    print(link)
    print(oldprice)
    print(newprice)'''

import selenium

print(dir(selenium))










