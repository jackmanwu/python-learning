o = 1
print("helloword")
flag = True
flag = False
print(flag);

my_name = "ssss"
print(my_name);

price = 12.05
print(price)
print("价格：%s" %price)

if True:
	print("Hello Python")
if 2>1:
	print("2大于1")

if 1>2:
	print("1>2")
else:
	print("1<2")

if 2>4:
	print("2>4")
elif 2>1:
	print("2>1")
else:
	print("未知")

num = 1;
while num<=10:
	print(num)
	num+=1
loom_flag = True
while loom_flag:
	print("Loop Condition keeps: %s" %loom_flag)
	loom_flag = False
for x in range(1,11):
	print(x)

my_integers = [1,2,3,4,5]
print(my_integers[0])
print(my_integers[3])

names = ["hello1","hello2","阿三"]
print(names[1])

values = []
values.append("Hello")
values.append("Pthon")
values.append("List")
print(values[2])

dictionary_example = {
	"key1":"value1",
	"key2":"value2",
	"key3":12
}
print("字典值：%s" %dictionary_example["key3"])

dictionary_example[3]  =45
print(dictionary_example[3])

for n in names:
	print(n)
for key in dictionary_example:
	print("%s : %s" %(key ,dictionary_example[key]))
for key,value in dictionary_example.items():
	print("%s -- %s" %(key,value))

words = ["cat","window","defenestrate"]
for w in words:
	print(w,len(w))
for w in words[:]:
	if len(w)>6:
		words.insert(0,w)
for w in words:
	print("结果: %s" %w)

for i in range(5):
	print(i)
for i in range(1,4):
	print(i)
for i in range(2,2):
	print("结果",i)
for i in range(-10,-100,-30):
 	print(i)

a = ["a","b","c","d"]
for i in range(len(a)):
 	print(i,a[i])
print(range(10))

list(range(5))
for i in range(2,10):
	for x in range(2,i):
		if i%x==0:
			print(i,"equals",x,"*",i//x)
			break;
	else:
		print(i,"is a prime number")
for i in range(2,10):
	if i%2==0:
		print("Found an even number",i)
		continue
	print("Found a number",i)
def fib(n):
	"""Print a Fibonacci series up to n."""
	a,b = 0,1
	while a<n:
		print(a,end = ' ')
		a,b = b,a+b
	print()
fib(2000)
f = fib
print(f(10))
def fib2(n):
	result = []
	a,b = 0,1
	while a<n:
		result.append(a)
		a,b = b,a+b
	return result
f100 = fib2(100)
for x in f100:
	print(x,end=" ")
print()
def ask_ok(prompt,retries=4,complaint='Yes or no,please!'):
	while True:
		ok = input(prompt)
		if ok in ('y','ye','yes'):
			return True
		if ok in ('n','no','nop','nope'):
			return False
		retries = retries-1
		if retries<0:
			raise OSError('uncoomperative user')
		print(complaint)
#ask_ok('Do you really want to quit?',2,'Come on,only yes or no!')
def f(a,L = []):
	L.append(a)
	return L
print(f(1))
print(f(2))
print(f(3))

def s(a,L = None):
	if L is None:
		L = [];
	L.append(a)
	return L
print(s(12))
print(s(10))

def parrot(voltage,state='a stiff',action='voom',type='Norwegian Blue'):
	print("--This parrot wouldn't",action,end=' ')
	print("if you put",voltage,'volts through it.')
	print("--Lovely plumage,the",type)
	print("--It's",state,"!")
parrot(100)
parrot(voltage=2000)
parrot(action='ssss',voltage='ZOOOM')

def function(a):
	pass
def chesseshop(kind,*arguments,**keywords):
	print("--Do you have any",kind,"?")
	print("--I'm sorry, we're all out of",kind)
	for arg in arguments:
		print(arg)
	print("-"*40)
	keys = sorted(keywords.keys())
	for kw in keys:
		print(kw,":",keywords[kw])
chesseshop("Limburger",
	"It's very runny,sir.",
	"It's really very, VERY runny,sir.",
	shopkeeper="Michael Plain",
	client="John Cleese",
	sketch = "Cheese Shop Sketch")
def concat(*args,sep="/"):
	return sep.join(args)
print(concat("earth","mars","venus"))
print(concat("earth","mars","venus",sep="."))
args=[3,6]
print(range(*args))
d={"voltage":"four million","state":"bleedin' demised", "action": "VOOM"}
parrot(**d)

def make_incrementor(n):
	return lambda x:x+n
g = make_incrementor(42)
print(g(0))
print(g(1))
pairs = [(1,"one"),(2,"two"),(3,"three"),(4,"four")]
pairs.sort(key = lambda pair:pair[1])
print(pairs)
def my_function():
	"""Do nothing ,but document it.
    
	No,really,it doesn't do anything.
	"""
	pass
print(my_function.__doc__)
def k(ham:42,eggs:int='spam')->"Nothing to see here":
	print("Annotations:",k.__annotations__)
	print("Arguments:",ham,eggs)
k("wonderful")

l = [[1,2,4],
[4,5,6],
[7,8,9]
]
print(l)
for i in l:
	for x in i:
		print(x,end=" ")
	print()