def scope_test():
	def do_local():
		spam = 'local spam'
	def do_nonlocal():
		nonlocal spam
		spam='nonlocal spam'
	def do_global():
		global spam
		spam='global spam'
	spam='test spam'
	do_local()
	print('After local assignment:',spam)
	do_nonlocal()
	print('After nonlocal assignment:',spam)
	do_global()
	print('After global assignment:',spam)
scope_test()
print('In global scope:',spam)

class MyClass:
	"""A simple example class"""
	i = 12345
	def __init__(self,realpart,imagpart):
		self.r = realpart
		self.i = imagpart
	def f(self):
		return 'hello world'
print(MyClass.__doc__)
print(MyClass.i)
print(MyClass.f)
x=  MyClass(3.0,-4.5)
print(x.r,x.i)
x.count=1
while x.count<10:
	x.count=x.count*2
print(x.count)
del x.count
print(x.f())
xf = x.f
print(xf())

class Dog:
	kind = 'canine'

	tricks=[]

	def __init__(self,name):
		self.name=name

	def add_trick(self,trick):
		self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)

class Dog2:
	def __init__(self,name):
		self.name=name
		self.tricks=[]

	def add_trick(self,trick):
		self.tricks.append(trick)
d = Dog2('Fido')
e = Dog2('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)

def f1(self,x,y):
	return min(x,y)
class C:
	f = f1
	def g(self):
		return 'hello world'
	h = g
c = C()
print(c.f(2,4))
class Bag:
	def __init__(self):
		self.data=[]
	def add(self,x):
		self.data.append(x)
	def addtwice(self,x):
		self.add(x)
		self.add(x)
b = Bag()
b.add(3)
b.addtwice(2)
print(b.data)
print(b.__class__)

class Mapping:
	def __init__(self,iterable):
		self.items_list=[]
		self.__update(iterable)
	def update(self,iterable):
		for item in iterable:
			self.items_list.append(item)
	__update=update
class MappingSubclass(Mapping):
	def update(self,keys,values):
		for item in zip(keys,values):
			self.items_list.append(item)
m = Mapping([1,2,3])
print(m.items_list)
m.update([4,5,6])
print(m.items_list)
ms = MappingSubclass(['a','b','c'])
print(ms.items_list)
ms.update([3,4],['d','e'])
print(ms.items_list)
print(ms.update.__self__)
print(ms.update.__func__)
class Employee:
	pass
john = Employee()
john.name='John Doe'
john.dept='computer lab'
john.salary=1000
print(john.name,john.dept,john.salary)

class B(Exception):
	pass
class C(B):
	pass
class D(C):
	pass

for cls in [B,C,D]:
	try:
		raise cls()
	except D:
		print('D')
	except C:
		print('C')
	except B:
		print('B')

for element in [1,2,3]:
	print(element)
for element in (1,2,3):
	print(element)
for key in {'one':1,'two':2}:
	print(key)
for char in '123':
	print(char)
for line in open('test.txt'):
	print(line)

s = 'abc'
it = iter(s)
print(it)
print(next(it))
print(next(it))
print(next(it))

class Reverse:
	"""Iterator for looping over a sequence backwards."""
	def __init__(self,data):
		self.data=data
		self.index=len(data)
	def __iter__(self):
		return self
	def __next__(self):
		if self.index==0:
			raise StopIteration
		self.index=self.index-1
		return self.data[self.index]
rev = Reverse('spam')
iter(rev)
for char in rev:
	print(char)

def reverse(data):
	for index in range(len(data)-1,-1,-1):
		yield data[index]
for char in reverse('golf'):
	print(char,end=' ')

print()
print(sum(i*i for i in range(10)))
xvec = [10,20,30]
yvec=[7,5,3]
print(sum(x*y for x,y in zip(xvec,yvec)))

from math import pi,sin
sine_table={x:sin(x*pi/180) for x in range(0,91)}
# unique_words=set(word for line in page for word in line.split())
# valedictorian=max((student.gpa,student.name) for student in graduates)
data='golf'
print(list(data[i] for i in range(len(data)-1,-1,-1)))