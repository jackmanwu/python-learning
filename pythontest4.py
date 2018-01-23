# while True:
# 	try:
# 		x = int(input("Please enter a number:"))
# 		break
# 	except ValueError:
# 		print("Oops! That was no valid number. Try again...")

import sys

try:
	f = open('test.txt')
	s = f.readline()
	i  =int(s.strip())
except OSError as err:
	print('OS error: {0}'.format(err))
except ValueError:
	print('Could not convert date to an integer.')
except:
	print('Unexpected error:',sys.exc_info()[0])
	raise

for arg in sys.argv[1:]:
	try:
		f = open(arg,'r')
	except IOError:
		print('cannot open',arg)
	else:
		print(arg,'has',len(f.readline()),'lines')
		f.close()

try:
	raise Exception('spam','eggs')
except Exception as inst:
	print(type(inst))
	print(inst.args)
	print(inst)

	x,y = inst.args
	print('x=',x)
	print('y=',y)

def this_fail():
	x = 1/0
try:
	this_fail()
except ZeroDivisionError as e:
	print('Handing run-time error:',e)
# raise NameError('HiThere')

# try:
# 	raise NameError('HiThere')
# except NameError:
# 	print('An exception flew by!')
# 	raise

class MyError(Exception):
	def __init__(self,value):
		self.value=value
	def __str__(self):
		return repr(self.value)

# try:
# 	raise MyError(2*2)
# except MyError as e:
# 	print('My exception occurred,value:',e.value)
# raise MyError("oops!")

class Error(Exception):
	pass
class InputError(Error):
	def __init__(self,expression,message):
		self.expression=expression
		self.message=message
class TransitionError(Error):
	def __init__(self,previous,next,message):
		self.previous=previous
		self.next = next
		self.message=message
# try:
# 	raise KeyboardInterrupt
# finally:
# 	print('Goodbye,world!')
def divide(x,y):
	try:
		result = x/y
	except ZeroDivisionError:
		print('division by zero!')
	else:
		print('result is',result)
	finally:
		print('executing finally clause')
divide(2,1)
# divide(2,0)
# divide('2','1')
with open('test.txt') as f:
	for line in f:
		print(line)