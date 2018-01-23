def fib(n):
	a,b = 0,1
	while b<n:
		print(b,end=" ")
		a,b = b,a+b
	print()
def fib2(n):
	result = []
	a,b = 0,1
	while b<n:
		result.append(b)
		a,b = b,a+b
	return result

# if __name__=='__main__':
# 	import sys
# 	fib(int(sys.argv[1]))

s = 'Hello,world.'
print(str(s))
print(repr(s))
print(str(1/7))
x = 10*3.25
y = 200*200
s = 'The value of x is '+repr(x)+', and y is '+repr(y)+'...'
print(s)
print(repr((x,y,('spam','eggs'))))
for x in range(1,11):
	print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')
	print(repr(x*x*x).rjust(4))
for x in range(1,11):
	print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))

print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.1415926'.zfill(5))
print('We are the {} who say "{}!"'.format('knights','Ni'))
print('{0} and {1}'.format('spam','eggs'))
print('{1} and {0}'.format('spam','eggs'))
print('This {food} is {adjective}.'.format(food='spam',adjective='absolutely horrible'))
print('The story of {0},{1}, and {other}'.format('Bill','Mafred',other='Georg'))

import math
print('The value of PI is approximately {}.'.format(math.pi))
print('The value of PI is approximately {!r}.'.format(math.pi))
print('The value of PI is approximately {0:.3f}.'.format(math.pi))
table={'Sjoerd':4127,'Jack': 4098,'Dcab':7678}
for name,phone in table.items():
	print('{0:10} ==> {1:10d}'.format(name,phone))
print('Jack: {0[Jack]:d};Sjoerd: {0[Sjoerd]:d}; '
	'Dcab: {0[Dcab]:d}'.format(table))
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
print('The value of PI is approximately %5.3f.' %math.pi)

#文件读写
f = open('test.txt','rb+')
# print(f.read())
# print(f.readline())
# print(f.readline())
# for line in f:
# 	print(line,end='')
# f.write('This is a test\n')
# print(f.read())
# value=('the answer',42)
# s = str(value)
# f.write(s)
# print(f.read())
# print(f.tell())
print(f.write(b'0123456789abcdef'))
print(f.seek(5))
print(f.read(1))
print(f.seek(-3,2))
print(f.read(1))
f.close()

with open('test.txt','r') as f:
	read_data = f.read()
print(f.closed)