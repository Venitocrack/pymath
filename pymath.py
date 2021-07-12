import numpy as np
import math

class PyMathError(Exception):
	pass

PyMathErr = PyMathError

def DIV(x):
	"""
	calc all dividers of x

	if type(x) is cls cls must have defined a non callable attribute named "_calc_dividents"
	recomended a property
	
	if x is a big number,it will take a while  
	"""
	try:
		u = []
		for i in range(int(x+1)):
			if i == 0:
				continue
			if x % i == 0:
				u.append(i)
			else:
				continue
		return  u[:]
	except (ValueError,TypeError) as e:
		return x._calc_dividents
	except MemoryError:
		return False
def MCD(x,y):
	"""
	return the MCD of x and y 
	"""
	try:
		divs1 = DIV(x)
		divs2 = DIV(y)
		result = 1
		for i in divs1:
			for j in divs2:
				if i > j and i > result and i in divs1 and i in divs2:
					result = i
		return result
	except TypeError:
		if type(PyMathErr) == Exception: #Error if not
			raise PyMathErr("[MemoryError] : divs failed donw and this return a boolean what is not usefull : \"False\"") 
		else:
			raise Exception("[MemoryError] : divs failed donw and this return a boolean what is not usefull : \"False\"")

def porcent(porcent,total):
	"""
	return the porcent "porcent" of "total"
	"""
	return (porcent*total)/100

def MCM(x,y):
	"""
	return the MCM of x and y (not recomended big numbers)
	"""
	return x*y/(MCD(x,y))

class farq():
	"""
	fraction data type,
	arguments:
		num:
			numerator
			pymath.farq(x,1)
			x
			-
			1
		den:
			denominator
			pymath.farq(1,x)
			1
			-
			x
	Examples:
		>>>import pymath as pm
		>>>f = pm.farq(2,1)
		>>>f
		1
		-
		2
		>>>f == .5
		True
		>>>f == pm.farq(2,4)
		True

	Warning:
		to compare you must use farq.bigger for ">"" or farq.smaller for "<"
	"""
	def __init__(self,num,den):
		self.num = num
		self.den = den
		self.__eq = num/den 
		self.__print__ = """"""+ str(self.num) + f"""\n{self.__underscore()}\n""" + str(self.den) + """"""
	def plus(self,other):
		"""sum self and other,
		do the same than self + farq"""
		try:
			if other.den == self.den:
				return farq(other.num + self.num,self.den)
			else:
				eq1,eq2 = self.make_eq_den(other)
				return eq1.plus(eq2)
		except AttributeError:
			raise TypeError(f"cannot plus a value that is not a frac. like {other}")
	def __underscore(self):
		"""internal"""
		r = ''
		r_ = ['-' for x in range(len(str(max(self.num,self.den))))]
		for i in r_:
			r = r + i 
		return r 
	def make_eq_den(self,other):
		"""
		return 2 fractions with same den
		arguments:
			other:
				a fraction
		returns:
			2 values of type fraq that are equivalents to self and other but have same denominator
		Examples:
			>>>import pymath as pm 
			>>>f1 = pm.farq(1,2)
			>>>f2 = f1**2
			>>>f2
			1
			-
			4
			>>>f1.make_eq_den(f2)
			[
			2
			-
			4,
			1
			-
			4
			]
		"""
		assert type(other) == farq,f"to make equal den must pass a fraction not {type(other)}"
		den = MCM(self.den,other.den)
		num1 = den/other.den*other.num 
		num2 = den/self.den*self.num
		first = farq(den = den,num = num1)
		second = farq(den = den,num = num2)
		return first,second
	def bigger(self,x):
		"""farq > x dont implemented yet,instead use farq.bigger(x)"""
		if isinstance(x,(float)):
			return self.__eq > x 
		elif isinstance(x,farq): #fraction
			return self.__eq > x.GetEq()
		else:
			try:
				return self.bigger(float(x))
			except TypeError:
				raise ValueError(
					"\"x\" must can be passed to float to be compared to a farq")
	def smaller(self,x):
		"""farq < x dont implemented yet,intead use farq.smaller(x)"""
		if isinstance(x,(float)):
			return self.__eq < x 
		elif isinstance(x,farq): #fraction
			return self.__eq < x.GetEq()
		else:
			try:
				return self.smaller(float(x))
			except TypeError:
				raise ValueError(
					"\"x\" must can be passed to float to be compared to a farq")
	def __eq__(self,other):
		try:
			return self.__eq == other.GetEq()
		except AttributeError:
			return self.__eq == other
	def irreducible(self):
		"""return the irreducible farq of \"self\""""
		return farq((self.num/MCD(self.den,self.num)),(self.den/MCD(self.den,self.num)))
	def min(self,other):
		"""do the same than farq - x"""
		if other.den == self.den:
			return farq(other.num - self.num,self.den)
		else:
			eq1,eq2 = self.make_eq_den(other)
			return eq1.min(eq2)
	def mult(self,other):
		"""do the same than farq * x"""
		try:
			return farq(self.num*other.num,self.den*other.den)
		except AttributeError:
			raise TypeError(f"cannot mult a value that is not a frac. like {other}")
	def div(self,other):
		"""do the same than farq / x
		Warning:
			TrueDiv dont implemented yet
		"""
		try:
			return farq(num = self.den*other.num,den = self.num*other.den)
		except AttributeError:
			raise TypeError(f"cannot div a value that is not a frac. like {other}")
	def of (self,num):
		"""
		return "self" of num
		Examples:
			>>>import pymath as pm
			>>>f = pm.farq(1,2)
			>>>f.of(2)
			1
		"""
		return num/self.den*self.num
	def GetEq(self):
		"""pass farq to decimal or float"""
		return self.__eq
	def __str__(self):
		return self.__print__
	def IsEq(self,other):
		"""same that self == other"""
		return self.__eq__(self,other )
	def __add__(self,other):
		try:
			return self.plus(other)
		except TypeError:
			return self.plus(_farq(other))
	def __neg__(self):
		return farq(-self.num,-self.den)
	def __abs__(self):
		return farq(abs(self.num),abs(self.den))
	def __mul__(self,other):
		try:
			return self.mult(other)
		except TypeError:
			return self.mult(_farq(other))
	def __bool__(self):
		return self.den > 10 and self.num > 10
	def __int__(self):
		return int(self.__eq)
	def __float__(self):
		return self.__eq
	def __sub__(self,other):
		try:
			return self.min(other)
		except TypeError:
			return self.min(_farq(other))
	def __div__(self,other):
		try:
			return self.div(other)
		except TypeError:
			return self.div(_farq(other))
	def __repr__(self):
		return str(self)
	def __pow__(self,exp):
		return farq(self.num**exp,self.den**exp)

def md(array,dec=True):
	u=[]
	for i in array:
		u.append(i*2)
	result = 0
	for i in u:
		result += i 
	if dec:
		return result/(len(u)*2)
	else:
		return result//(len(u)*2)
class Vector2():
	def __init__(self,x,y):
		self.x  =x 
		self.y = y 

pi = math.pi
e = math.e
__VERSION__ = "1.0.1"


def _farq(x):
	"""pass x to a farq
	*Warning*:
		to define how to convert x to a farq
		you must define a callable attribute called 
		'_farq_interface'
	"""
	if type(x) == int:
		return farq(x,1)
	elif type(x) == float:
		return farq(x*2,2)
	elif type(x) == farq:
		return x
	else:
		try:
			return getattr(x,'_farq_interface')() #check if you defined farq-transform into your x object class
		except AttributeError:
			raise TypeError(f'cant convert {type(x)} to farq')

def _porcentOf(num,other): 
 	return (num/other)*100



def PorcentOf(num,other):
	"""return what porcent is other respect num"""
	return _porcentOf(num,other)		

def IsComplex(n):
	"""return n is a complex number"""
	return type(n) == complex 

def Tetration(n,n2):
	"""
	if x**n 
	is x*x*x*x... n times
	pymath.Tetration(x,n)
	is x**x**x**x n times
	if the num is so big raises pymath.PymathErr
	"""
	try:
		y = n
		for i in range(n2):
			n = n**y
			y = n 
		return n
	except (MemoryError,OverflowError):
		raise PyMathErr("to big num") 
def module(n):
	try:
		return abs(n)
	except TypeError:
		return None

def root(n,n2 = 2):
	"""
	root(x,y) = y√x
	"""
	return n**(1.0/n2)  

__root__ = root

def sqrt(n):
	"""return the 2√n"""
	return __root__(n)

def crt(n):
	"""return the 3√n"""
	return __root__(n,n2 =3)

def __createRandDiv__(n):
	from random import choice
	o = DIV(n)
	u = choice(o)
	del(choice) #free memory
	return u

def RandDiv(n):
	"""return a random div of n"""
	return __createRandDiv__(n)

def RandMult(n):
	"""return a random number that always will fulfill RandMult(n) % n = 0"""
	return n*__createRandDiv__(n)

def sin(x):
	"""sin of x"""
	return math.sin(x)

def sen(x):
	"""sen of x"""
	return math.sen(x)

def cos(x):
	"""cos of x"""
	return math.cos(x)

def qrt(x):
	"""qrt(x) = 4√x"""
	return __root__(x,n2 = 5) 

def srt(x):
	"""srt(x) = 6√x"""
	return __root__(x,n2 = 6)

def qurt(x):
	"""qurt(x) = 4√x"""
	return __root__(x,n2 = 4)

def sert(x):
	"""sert(x) = 7√x"""
	return __root__(x,n2 = 7)

def eirt(x):
	"""eirt(x) = 8√x"""
	return __root__(x,n2 = 8)

def tert(x):
	"""tert(x) = 10√x"""
	return __root__(x,n2 = 10)

def nirt(x):
	"""nirt(x) = 9√x"""
	return __root__(x,n2 = 9)


def _mult(x,y):
	"""return if x % y = 0"""
	return x % y == 0

def hipt(q1,q2):
	"""the hypotenuse of a triangle with sides q1 and q2"""
	h = (q1**2) + (q2**2)
	return __root__(h,n2 = 2)

def _IsCorrectHipt(q1,q2,hip):
	"""return if hip is the hypotenuse of a triangle with sides q1 and q2"""
	return hipt(q1,q2) == hip 

def IsFloat(x):
	"""return x is float"""
	return type(x) == float 

def IsInt(x):
	"""return x is int"""
	return type(x) == int 

def IsStr(x):
	"""return x is string"""
	return type(x) == str 

def IsBool(x):
	"""return x is bool"""
	return type(x) == bool 

def IsList(x):
	"""return x is list"""
	return type(x) == list 

def __raise__(msg):
	raise PyMathErr(msg)

def _rage__(x):
	"""an ultra exponential formula"""
	return (x**3)**(x)

def Rage(x):
	"""an ultra exponential formula than increases faster than _rage__"""
	return _rage__(x)**2

def RandDat(a = 0,b = 100):
	"""return a random dat based on a and b"""
	from random import randint as rt
	i = __createRandDiv__(RandMult(rt(a = a,b = b)))
	del(rt)
	return i

def dTree(n1,n2,target = sqrt,rageRange = 0.000000012929281812932932983289):
	"""internal for next 1.1.2 or bigger,this will be implemented at same than pymath.FuncTree class"""
	if not callable(target):
		raise TypeError(f"cannot call the {target} value as a function")
	res = []
	iter = 2
	for i in range(n1):
		n2 = n2/iter
		res.append(target(n2))
		iter += rageRange
	return res 

def exponent(x):
	"""return x²"""
	try:
		return x**2
	except OverflowError:
		raise PyMathErr("to big num")

def mTree(n1,n2,target = exponent,rageRange = 0.0947756123129292818129329329832):
	"""internal for next 1.1.2 or bigger,this will be implemented at same than pymath.FuncTree class"""
	try:
		if not callable(target):
			raise TypeError(f"cannot call the {target} value as a function")
		res = []
		iter = 2
		for i in range(n1):
			n2 = n2*iter
			res.append(target(n2))
			iter += rageRange
		return res 
	except OverflowError:
		raise PyMathErr("to big num")


def _IsType(value,typ):
	"""return if value is of type typ"""
	return type(value) == typ 

def log(x):
	"""log of x"""
	return math.log(x)

def log2(x):
	"""log2 of x"""
	return math.log2(x)

def log1p(x):
	"""log1p of x"""
	return math.log1p(x)

def log10(x):
	"""log10 of x"""
	return math.log10(x)

def _exp(x):
	"""a ultra-exponential increase function"""
	return ((x**x)/x)**2 

from random import choice,randint 

def exp(x):
	"""exp of x"""
	return np.exp(x)

def dot(*x,**k):
	"""dot of x (x is all arguments)"""
	return np.dot(*x,**k)

def tan(x):
	"""tan of x"""
	return np.tan(x)

def FarqSum(farq1,farq2):
	"""same than farq1 + farq2"""
	return farq1 + farq2 

def FarqMin(farq1,far2):
	"""same than farq1 - farq2"""
	return farq1-far2

def FarqMult(farq1,farq2):
	"""same than farq1*farq2"""
	return farq1*farq2

def FarqDiv(farq1,farq2):
	"""same than farq1/farq2"""
	return farq1/farq2

def _IsMult(x,y):
	"""same than _mult"""
	return (x % y) == 0

def _IsDiv(x,y):
	"""return if y is a divider of x"""
 	return y in DIV(x)


def prime(x):
	"""return x is a prime number"""
	y = DIV(x)
	return y[1] == x

def _Sroot(x,n2 = 2):
	"""inverted root of x to n2"""
	return 1/(__root__(x,n2 = n2))

def Sroot(x,n2 = 2):
	"""same than _Sroot"""
	return x**(-1/n2)

def IRoot(x,y,z):
	"""hipt in 4 dimensions of sides x,y,z"""
	return _Sroot(x**2+y**2+z**2)


c = 299997.7 

def InterSection(x):
	"""an intersection of x"""
	return 1/sqrt(x**2+x**2)


def _sumather(n):
	"""a iterable object"""
	result = 0
	while True:
		result += n
		yield result 

def multTable(x,y):
	"""return the mult table of x in y iterations"""
	res = []
	iter = _sumather(x)
	for i in range(y):
		res.append(next(iter))
	return res

def IsTenMult(x,y):
	"""return y in multTable of x to 10"""
	return y in multTable(x,10)

def basic_sumather(a,b = 0):
	"""an iterable object of sum "a" content"""
	result = b 
	while True:
		for i in a:
			result += i 
			yield result 

class _i:
	def __init__(self,t):
		self.t = t 
	def __call__(self,count):
		return count + self.t


def sumather(key,b = 1):
	"""a sumather calling key if cant,if key is a unmber will simplysum key"""
	i = b 
	if not callable(key):
		key = _i(key)
	count = 0
	while True:
		i += key(count)
		count += 1 
		yield i 
def PreSumather(a,t,b = 0):
	"""return an array of len = t of a sumather of a and b"""
	res = []
	i = sumather(a,b=b)
	for y in range(t):
		res.append(next(i))
	return res 
#constants
st_sharp = 0.123456789101112131415161718192021
i = sqrt(-1)
au = (1+sqrt(5))/2
#constants list
constants = [(pi,"pi"),(e,"e"),(i,"i"),(c,"c"),(au,"au"),(st_sharp,"st_sharp")]

def expSeries__(t):
	"""return a list of all 2^n to 2^t"""
	i = 2 
	res = []
	for u in range(int(t)):
		res.append(i)
		i = i*2 
	return res

def expRate(r):
	"""return r**2^r"""
	o = expSeries__(r) 
	return r**o[r-1]

def A_rect(b,a):
	return b*a 

def A_squar(l):
	return l**2

def A_triangle(b,a):
	return A_rect(b,a)/2

def A_cir(r):
	global pi 
	return pi*(r**2) #πr²

def A_romb(b,a):
	return (a*b)/2

def sum_all_to(n):
	"""sum al numbers to n"""
	return (n*(n+1))/2

def mean(a):
	"""the mean of an array "a" """
	res = 0 
	for i in a:
		res += i 
	res = res/len(a)
	return res 

def mean_seq(a,a_s):
	"""mean implementing frequences"""
	res = 0 
	count = 0 
	for i in a:
		if count > len(a_s)-1:
			count = 0 
		res += i*a_s[count]
		count += 1
	cc = 0 
	for i in a_s:
		cc+= i   
	res = res/cc 
	return res 

def floor(n):
	return int(n)

def ceil(n):
	return round(n)

def _min(a,b):
	return min(a,b)

def _max(a,b):
	return max(a,b) 

def factorial(a):
	return math.factorial(a) 

def complex_factorial(a):
	"""an ultra-exponential increase function"""
	res = 1 
	rt = 0 
	for i in range(a):
		rt = rt*i 
		res += rt 
	return res 

def real(c):
	"""return the real part of c"""
	try:
		return c.real
	except AttributeError:
		raise TypeError("the argument 'c' must be a complex") 

def imag(c):
	"""return the imag part of c"""
	try:
		return c.imag
	except AttributeError:
		raise TypeError("the argument 'c' must be a complex") 

def neg(n):
	"""return -n,if n is a negative number return directly n"""
	if n>0:
		return ~n+1
	else:
		return n 

def Pos(n):
	"""return +n if n is a positive number return it"""
	if n<0:	#-x
		return ~n+1
	else:
		return n 

def power(a,b):
	"""another ultra-exponential increase function"""
	return ((a*b)**(b))

def isreal(n):
	"""return if n inherits of float or is float"""
	return isinstance(n,float) 

def isnat(n):
	"""return if n is an a natural number"""
	return isinstance(n,int) and x > 0

def isinteger(n):
	"""return if n inherits of int or is int"""
	return isinstance(n,int) 

def iscomplex(n):
	"""return if n inherits of complex or is complex"""
	return isinstance(n,complex) 

def fib(n):
	"""fib pre-implementation"""
	if n == 0:
		return 1
	return fib(n-1)+fib(n-2)

class proporcional:
	"""don recomended for user code for versions smaller than 1.2.1"""
	def __init__(self,units,t):
		self.unit = t/units
	def of(self,n):
		return self.unit*n

def prop_list(t):
	"""an iterable proporcional object"""
	t = proporcional(1,t)
	n = 0 
	while True:
		n+=1
		yield t.of(n)

def make_list(obj,le):
	"""return a list of all iterations with len = le"""
	r = []
	for i in range(le):
		r.append(next(obj))
	return r

def ten_prop(t):
	"""return the first 10 values with a unit of t"""
	obj = prop_list(t)
	return make_list(obj,10)

class __geometry:
	def __init__(self):
		global constants
		self.__pi = constants[0][0]
		self.__e= constants[1][0]  
		self.__i = constants[2][0]
	def A_cir(self,r):
		return A_cir(r) 
	def A_rect(self,b,a):
		return A_rect(b,a)
	def A_squar(self,l):
		return A_squar(l)
	def A_triangle(self,b,a):
		return A_triangle(b,a)
	def A_romb(self,b,a):
		return A_romb(b,a)
	def hipt(self,a,b):
		return hipt(a,b)
	def radius(self,d):
		return d/2
	def diameter(self,r):
		return r*2 
	def V_cir(self,r):
		return 4/3*self.__pi*(r**3) #
	def A_hex(self,l,ap):
		return l*6*ap/2
	def A_pent(self,l,ap):
		return l*5*ap/2
class __calc:
	def __init__(self):
		global constants
		self.__pi = constants[0][0]
		self.__e= constants[1][0]  
		self.__i = constants[2][0]
	def root(self,n,n2=2):
		return __root__(n,n2=n2)
	def farq_sumather(self,key,b=1):
		obj = sumather(key,b=b)
		while True:
			yield _farq(next(obj))
	def multieval_root(x,n2=2):
		a=__root__(x,n2=n2)
		if Pos(a):
			return (a,-a)
		else:
			return a
	def randfloat(self,fd):
		res='0.'
		for i in range(fd):
			res += str(randint(0,9))
		return float(res)
	def fib(self,n):
		if n == 1:
			return 0
		return fib(n-1) + n
	@property 
	def e(self):
		return self.__e 

	@property 
	def pi(self):
		return self.__pi 

	@property 
	def i(self):
		return self.__i 

"""sub-modules implementation"""
geom = __geometry() #pm.geom
calc = __calc() #pm.calc

