def printA(a):
	for v in a:
		print(v,end=" ")
	print()
a = [66.25,333,333,1,1234.5]
printA(a)
print(a.count(333),a.count(66.25),a.count('x'))
a.insert(2,-1)
a.append(333)
printA(a)
print(a.index(333))
a.remove(333)
printA(a)
a.reverse()
printA(a)
a.sort()
printA(a)
print(a.pop())
printA(a)

#列表当做堆栈使用
stack = [3,4,5]
stack.append(6)
stack.append(7)
printA(stack)
stack.pop()
stack.pop()
printA(stack)
stack.pop()
printA(stack)

#队列
from collections import deque
queue = deque(["Eric","John","Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())
print(queue.popleft())

squares = []
for x in range(10):
	squares.append(x**2)
printA(squares)
print(x)
squares1 = list(map(lambda i:i**2,range(10)))
printA(squares1)
squares2 = [i**2 for i in range(10)]
printA(squares2)
print(x)
squares3  =[(m,n) for m in [1,2,3] for n in[3,1,4] if m!=n]
printA(squares3)

vec = [-4,-2,0,2,4]
printA([m*2 for m in vec])
printA([m for m in vec if m>0])
printA([abs(m) for m in vec])
freshfruit = [' banana','  loganberry  ','passion fruit  ']
printA([m.strip() for m in freshfruit])
printA([(m,m**2) for m in range(6)])
s=[[1,2,3],[4,5,6],[7,8,9]]
printA([num for elem in s for num in elem])
from math import pi
printA([str(round(pi,m)) for m in range(1,6)])
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
printA(matrix)
printA([[row[m] for row in matrix] for m in range(4)])
printA(zip(*matrix))

z = [-1,1,66,25,333,333,1234.5]
printA(z)
del z[0]
printA(z)
del z[2:4]
printA(z)
del z[:]
print(len(z))
del z

# 元组
t = 12345,54321,'hello!'
print(t[0])
u = t,(1,2,3,4,5)
print(u)
v = ([1,2,3],[3,2,1])
printA(v)
empty = ()
print(len(empty))
singleton = 'hello',
print(len(singleton))
print(singleton)

#集合
basket={'apple','orange','apple','pear','orange','banana'}
print(basket)
print('orange' in basket)
a=set('abracadabra')
print(a)
b =set('alacazam')
print(b)
print(a-b)
print(a|b)
print(a&b)
print(a^b)
print({x for x in 'abracadabra' if x not in 'abc'})

#字典
tel={'jack':4098,'sape':4139}
tel['guido']=4127
print(tel)
del tel['sape']
print(tel)
print(tel.keys())
print(sorted(tel.keys()))
print('guido' in tel)
print(dict([('sape',4212),('dasc',5241)]))
print({x:x**2 for x in (2,4,6)})
print(dict(sape=4231,sda=5623,uttr=1231))
for k,v in tel.items():
	print(k,v)
a = ['ssss','cccc','nnnn']
for i,v in enumerate(a):
	print(i,v)
questions = ['name','quest','favorite color']
answers=['lancelot','the holy grail','blue']
for q,a in zip(questions,answers):
	print("What is your {0}? It's {1}".format(q,a))
for i in reversed(range(3)):
	print(i,end=" ")
print()
for b in sorted(set(basket)):
	print(b, end=' ')
print()
words=['cat','window','defenestrate']
for w in words[:]:
	if(len(w)>6):
		words.insert(0,w)
print(words)
string1,string2,string3='','Trondheim', 'Hammer Dance'
print(string1 or string2 or string3)

print((1,2,3)>(1,2,4))
print('ABC'<'C'<'Pascal'<'Python')
print((1,2,3,4)<(1,2,4))
print((1,2,3)==(1.0,2.0,3.0))