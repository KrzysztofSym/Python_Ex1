### KURS:
### https://kursy.kodolamacz.pl/kurs/python-kurs-podstawowy/

### Importowanie bibliotek.
##############################

import importlib as im

import numpy
import numpy as np
from numpy import sqrt

# przeładowanie modułów
im.reload(numpy)

help(print)
### Operatory: arytmetyczne, przypisania, porównania, logiczne.
##################################################################

numpy.sqrt(9)

np.sqrt(9)

sqrt(9)

# Przypisanie przez referencję.
p1 = 3 * [1]
p2 = p1
p2[2] = 9

p1, p2

# Przypisanie przez wartość (płytka kopia).
p1 = 3 * [1]
p2 = p1.copy()
p2[2] = 9

p1, p2

# Przypisanie przez wartość (płytka kopia - problem).
p1 = [1, 1, [1, 1]]
p2 = p1.copy()
p2[1] = 9
p2[2][1] = 9

p1, p2

# Przypisanie przez wartość (głęboka kopia).
import copy

p1 = [1, 1, [1, 1]]
p2 = copy.deepcopy(p1)
p2[1] = 9
p2[2][1] = 9

p1, p2

### Typy danych: logiczne, numeryczne, tekstowe.
###################################################

# Arytmetyka wartości logicznych.
sum([True, False, False, True, True])

str(True)
int(True)
int(False)
float(True)
float(False)

# Niemutowalność.
txt = 'Ala ma kota.'
txt[-2] = 'y'


# konkatenacja

txt + " Ma też" + ' papugę.'

1 + "Nie ma" + " automatycznej konwersji przy łączeniu"

str(1) + " Nie ma" + " automatycznej konwersji przy łączeniu"

3 * "Powielanie "

'Py' 'thon'

strr = ('Umieszczenie kilku tekstów w nawiasie ' 'powoduje ich połączenie')

len(strr)

### * Struktury danych: krotka (tuple)

# Jedyna niemutowalna struktura danych.
p = (1, 1, 1)
p[1] = 9

type(p)
### Struktury danych: lista.
###############################

# Akceptuje dane różnego typu.
[3, 'a', True]

lst = [3, 'a', True]

type(lst[0])

type(lst[1])

type(lst[2])

lst.append("nowy")

lst.insert(1, 'druga')

lst

del lst[1]

del lst

# Indeksowanie...
pts = ['element 1', 'element 2', 'element 3']

type(pts)

pts[0]
pts[1] 
pts[-1]
pts[2]

### Struktury danych: słownik.
#################################

marks = {'student 1' : 5, 'student 2' : 5, 'student 3' : 4}

type(marks)

# Indeksowanie...
marks['student 1'] # ...tylko po nazwie.
# marks[1] # ...niemożliwe, słownik nie zachowuje kolejnosci elementow.

marks1 = {'lista1': [1, 2, 3], 'lista2': [1, 1, 1, 1, 1]}

marks1['lista1'][2]

### Struktury danych: zbiór.
###############################

values = {3, 5, 4, 5}

type(values)

# Tylko unikalne elementy.
values

# Nie da się indeksować
# values[1]

# ...za to można sprawdzić, czy zbiór zawiera element.
3 in values

### Instrukcja warunkowa i operator trójargumentowy.
#######################################################

amt = 36000
if amt > 5000:
    print('tax [5%]: ' + str(0.05 * amt))
elif amt > 2000:
    print('tax [3%]: ' + str(0.03 * amt))
else:
    print('tax [1%]: ' + str(0.01 * amt))

### Pętla: for.
##################

pts = [5, 3, 2]

for p in pts:
    print(str(p) + ' : ' + str(2 * p))
    
for i, p in enumerate(pts):
    print(i, ') ' + str(p) + ' : ' + str(2 * p))
    print(i+1, '/', len(pts))
    
for p in enumerate(pts):
    print(str(p) + ' : ' + str(2 * p))
    
x, y = (1, 2)

for i, p in enumerate(pts):
    print(i, str(p) + ' : ' + str(2 * p))
else:
    print("Koniec wektora")

### Pętla: while.
####################

pts = [5, 3, 2]

i = 0
while i < len(pts):
    print(str(pts[i]) + ' : ' + str(2 * pts[i]))
    i += 1 # i = i + 1
    
i = 0
while True:
    if i > 5:  
        print('6 iteracja')
        break
    print("iteracja: ", i)
    i += 1


i = 0
while True:
    print("iteracja: ", i)
    if i > 5:  
        break
    if i == 3:
        continue
    i += 1
    
i = 0
while True:
    i += 1
    if i > 5:  
        break
    if i == 3:
        continue
    print("iteracja: ", i)
    #print('test')
    

### ...-comprehension.
#########################

pts = [5, 3, 2]

lst = []
for p in pts:
    lst.append(p*2)

# list-comprehension
[2*p for p in pts]

# set-comprehension
{p % 3 for p in pts}

# dict-comprehension
{p : 2 * p for p in pts}

# generator
gen = (2 * p for p in pts)

for item in gen:
    print(item)
    
### Funkcje.
###############

def rate_of_return(v1, v2):
    return (v2 - v1) / v1

rate_of_return(120, 140)


### Funkcje lambda.
######################

def opp(v1, v2, f): 
    return f(v1, v2)

def opp2(lst, f): 
    return f(lst)

opp(2, 3, lambda x, y: x + y)
opp(2, 3, lambda x, y: x * y)
opp(2, 3, lambda x, y: x**y)
opp2([2, 3, 4], sum)

opp('2', '3', lambda x, y: x + y)
opp([2, 3], [4, 1, 2], lambda x, y: x + y)

### Obiektowość.
###################

class Example:
    def __init__(self, val):
        self._val = val #_ oznacza prywatną zmienną
        self.val2 = val * 2
        
    def get_val(self):
        return self._val #self?
    
    def change_val(self, x):
        self.val2 = x
        
class Example2:
    def __init__(self, val):
        self._val = val #_ oznacza prywatną zmienną
        self.val2 = val * 3
        
    def get_val(self):
        return self._val #self?
    
    def change_val(self, x):
        self.val2 = x

e = Example(3)
e.get_val() # <=> Example.get_val(e)
e.val2
e.change_val(7)
e.val2
e.val2 = 9

e1 = Example2(3)

e.get_val()
e.val2

e1.get_val()
e1.val2

### Dziedziczenie.
#####################

class Mammal:
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    
class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
    super().__init__('Dog')
    
mm1 = Mammal('Cow')
d1 = Dog()


class BetterExample(Example):
    def __init__(self, val):
        super().__init__(val)
        self.val2 = val * 10
    
    def set_val(self, val):
        self._val = val

be = BetterExample(3)
be.get_val()
be.set_val(2)
be.get_val()
be.val2

e.set_val(1)

#be._val = 3

# po wielu klasach

class Animal:
  def __init__(self, Animal):
    print(Animal, 'is an animal.');

class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    super().__init__(mammalName)
    
class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammal):
    print(NonWingedMammal, "can't fly.")
    super().__init__(NonWingedMammal)

class NonMarineMammal(Mammal):
  def __init__(self, NonMarineMammal):
    print(NonMarineMammal, "can't swim.")
    super().__init__(NonMarineMammal)

class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self):
    print('Dog has 4 legs.');
    super().__init__('Dog')
    
    
d = Dog()
bat = NonMarineMammal('Bat')


#----
# https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance

class First:
    def __init__(self):
        super(First, self).__init__()
        print("first")

class Second:
    def __init__(self):
        super(Second, self).__init__()
        print("second")

class Third(First, Second):
    def __init__(self):
        super(Second, self).__init__()
        print("third")

xx = Third()

### Polimorfizm.
###################

class Animal:
    def voice(self):
        raise Exception()

class Cat(Animal):
    def voice(self):
        print('Meaw!')

class Dog(Animal):
    def voice(self):
        print('Bark!')

class Rat(Animal):
    def voice(self):
        print('Piiii!')

def pet(a):
    a.voice()

cat, dog = Cat(), Dog()

pet(cat)
pet(dog)

isinstance(cat, Cat)
isinstance(cat, Animal)
isinstance(cat, Dog)

isinstance(e, Animal)

pet(e)

def better_pet(x):
    if isinstance(x, Animal):
        return pet(x)
    else:
        print('This is an object from other class!')
    
better_pet(cat)
rat = Rat()
better_pet(rat)
better_pet(e)


#Dekoratory
import functools

def log_method_call(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        class_name = self.__class__.__name__
        print(f"[{class_name}] Wywołanie metody: {func.__name__} z argumentami: {args}, {kwargs}")
        result = func(self, *args, **kwargs)
        print(f"[{class_name}] Metoda {func.__name__} zakończona. Wynik: {result}")
        return result
    return wrapper

class MyClass:
    def __init__(self, value):
        self.value = value

    @log_method_call
    def process_value(self, factor):
        new_value = self.value * factor
        self.value = new_value
        return new_value

print("--- Demonstracja Dekoratora ---")
obj = MyClass(10)
print(f"Wartość początkowa: {obj.value}")
result = obj.process_value(2)
print(f"Wartość po przetworzeniu: {obj.value}")
print("-" * 20)


#Hinty typów
from typing import List, Dict, Optional

class Book:
    title: str
    author: str
    year: int
    reviews: List[str]

    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.reviews = []

    def add_review(self, review_text: str) -> None:
        self.reviews.append(review_text)

    def get_info(self) -> str:
        return f"{self.title} by {self.author} ({self.year})"

    def get_reviews_dict(self, include_year: bool = False) -> Dict[int, str]:
         return {i: review for i, review in enumerate(self.reviews)}


print("\n--- Demonstracja Hintów Typów ---")
my_book: Book = Book("Władca Pierścieni", "J.R.R. Tolkien", 1954)
my_book.add_review("Epicka opowieść!")
info: str = my_book.get_info()
print(info)
print(f"Recenzje ({type(my_book.reviews)}): {my_book.reviews}")
reviews_dict: Dict[int, str] = my_book.get_reviews_dict()
print(f"Recenzje w słowniku ({type(reviews_dict)}): {reviews_dict}")
print("-" * 20)

#dataclasses

from dataclasses import dataclass, field
from typing import List

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0
    tags: List[str] = field(default_factory=list)

print("\n--- Demonstracja Dataclasses ---")
laptop = Product("Laptop XYZ", 1200.50, 5)
keyboard = Product("Klawiatura ABC", 75.00, quantity=10)
mouse = Product("Mysz DEF", 25.00)
phone = Product("Telefon GHI", 800.00, tags=["smartfon", "5G"])

print(laptop)
print(keyboard)
print(mouse)
print(phone)

print(f"Czy laptop == keyboard? {laptop == keyboard}")
same_laptop = Product("Laptop XYZ", 1200.50, 5, tags=[])
print(f"Czy laptop == same_laptop? {laptop == same_laptop}")
same_laptop_strict = Product("Telefon GHI", 800.00, tags=["smartfon", "5G"])
print(f"Czy phone == same_laptop_strict? {phone == same_laptop_strict}")

print(f"Nazwa: {laptop.name}, Cena: {laptop.price}, Ilość: {laptop.quantity}")
print(f"Tagi telefonu: {phone.tags}")
print("-" * 20)