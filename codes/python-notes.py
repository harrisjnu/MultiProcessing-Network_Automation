Python Basics


Coding - Python Basics
		#####################
		## Variables in Python
		#####################

		#defining variables
		miles = 10     #type integer
		name = 'John'  #type string (because the value of the variable is between single quotes)
		a, b, c = 1.5, 3, 'x'  #defining 3 variables on the same line (a float, an integer and a string)


		max_permitted_value = 500 #snake-case notation. PEP 8 recommends using snake case for variable names
		maxPermittedValue = 500  #camel-case notation


		#Illegal or not recommended names
		# 4you = 10  #illegal name, it starts with a digit
		# valu!es = 100 #illegal name, it contains special characters
		# str = 'Python'  #not recommended name, str is a Python language keyword
		# _location = 'Europe' #not recommended name. Avoid names that start with underscores (they have special meaning)



		#####################
		## Comments in Python
		#####################

		#this line is a comment. Comments in Python start with the hash character, #, and extend to the end of the physical line.
		#If you want to comment out more lines, insert a hash char at the beginning of each line

		#the following line is commented out and ignored by Python Interpreter
		#x = 1

		a = 7 #defines a variable that stores an integer

		my_str = 'A hash character # within a string literal is just a hash character.'



		#########################
		## Built-in Data Types
		#########################

		age = 31  #type integer

		miles = 3.4  #type float

		finished = True #type boolean

		name = 'Andrei' #type str (string)

		years = [2018, 2019, 2020]  #type list

		week_days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')  #type tuple

		vowels = {'a', 'e', 'o', 'u'}  #type set

		fs = frozenset((1, 2, 'abc', 'xyz'))   #type frozenset

		countries = {'de':'Germany', 'au':'Australia', 'us':'United States of America', 'gr':'Greece'}  #type dictionary



		#############################
		## Numbers and Math Operators
		#############################

		a = 9
		b = 4
		## Arithmethic Operators
		a + b   # addition operator => 13
		a - b   # substraction operator => 5
		a * b   # multiplication operator => 36
		a / b   # division operator => 2.25
		a // b  # floor division operator => 2
		5.0 // 3.0   # => 1.0 # works on floats too
		a ** b  # exponentiation operator (a to the power of b) => 6561
		a % b   # modulus operator => 1


		## Assignment Operators
		a = 5
		a += 2  #Shorthand for a = a + 2 => a = 7
		a -= 3  #Shorthand for a = a - 3 => a = 4
		a /= 2  #Shorthand for a = a / 2 => a = 2
		a *= 3  #Shorthand for a = a * 3 => a = 6
		a **=2  #Shorthand for a = a ** 2 => a = 36


		## Arithmethic Built-in Function
		divmod(9, 4)    #returns the quotient and remainder when using floor(integer) division => (2, 1)
		sum([1,2,4])    #returns the sum of an iterable => 7
		min(1,-2,3)     #returns the minimum value => -2
		max(1,2,4)      #returns the maximum value => 4
		a = 10/3        #a = 3.3333333333
		round(a, 4)     #returns a number rounded with 4 decimals => 3.3333
		pow(2, 4)       #2 ** 4 = 16



		######################################
		## Comparison and Identity Operators
		######################################

		# Assignment is =
		a = 2
		b = 3

		# Equality is == and compares the values stored by the variables
		a == b  # => False
		b == b  # => True

		# Inequality is !=
		a != b  # => True

		# More comparisons
		a > b   # => False
		5 >= 5  # => True
		b <= a  # => False

		'Python' == 'python'    # => False - case matters

		id(a)   # => returns the address where the value referenced by a is stored 140464475242000

		#is checks if two variables refer to the same object (saved at the same memory address)
		a is b  # => False = compares the address of a to the address of b



		#################################
		## Boolean Variables
		#################################

		## True equals 1 and False equals 0
		True == 1   # => True
		bool(True)  # => 1

		False == 0  # => True
		bool(False) # => 0


		1 is True   # => False
		0 is False  # => False


		True > False    # => True
		a = (True + True ) * 10     # => 20

		id(True)    # => 10714848 (you'll optain another value)
		id(4 > 2)   # => 10714848  - the address of True and False is constant during program execution

		#The next 2 expressions are equivalent
		(4 > 2) == True     # => True
		(4 > 2) is True     # => True



		## Truthiness of objects
		bool(0)     # => False
		bool(0.0)   # => False
		bool(10)    # => True
		bool(-1.5)  # => True

		bool('')    # => False (empty string)
		bool('py')  # => True

		bool([])    # => False (empty list)
		bool([1,2]) # => True

		bool(())    # => False (empty tuple)
		bool((3,4)) # => True

		bool({})        # => False (empty dictionary)
		bool({1:'abc',2:55,'a':5})   # => True



		#################################
		## Boolean Operators
		#################################
		# exp1 and exp2 -> True when both expressions are True and False otherwise
		# exp1 or exp2  -> True when any expression is True


		a, b = 3, 5

		a < 10 and b < 10       # => True
		a < 10 and b > 10       # => False

		a < 10 or b < 10        # => True
		a < 10 or b > 10        # => True


		# The next 2 expressions are equivalent
		2 < a < 6
		a < 2 and a < 6         # more readable

		a != 7 or b > 100       # => True

		not a == a              # => False
		a == 3 and not b == 7   # => True

		not a > 10 and b < 10       # => True


		a < 10 or b > 10            # => True
		not a < 10 or b > 10        # => False
		not (a < 10 or b > 10)      # => False


		# !!!!!!!!!!!
		# Python considers in fact 4 > 2 and 2 == True.
		4 > 2 == True         # => False
		(4 > 2) == True       # => True


Coding - Strings in Python



		#################################
		## Intro to Strings
		#################################

		## strings (str objects) are enclosed by single or double quotes (' or "). Just be consistent within your code!
		message1 = 'I love Python Programming!'
		message2 = "I love Python Programming!"

		## print() function displays the content of the string variable at console
		print(message1)

		#hello1 = 'Hi there! I\'m Andrei'   # => error, cannot use ' inside ' ' or " inside " "
		hello1 = 'Hi there! I\'m Andrei'    # => correct. ' inside ' ' must be escaped  using \
		hello2 = "Hi there! I'm Andrei"     # you can use ' inside " " or " inside ' '


		## Instructions between """ or ''' are treated as comments. It's recommended to use # to comment individual lines
		"""
		This is a multiline comment
		a = 5
		print(a)
		Comment ends here.
		"""

		# \n is a new line
		print('Hello \nWorld!')     # => it displays Hello World! on 2 lines



		#################################
		## User Input and Type Casting
		#################################

		## Simple way to get user input from console
		input_string_var = input("Enter some data: ") # Returns the data as a string

		# To perform arithmetic operations we must cast to int or float
		a = input('Enter a:')       # => a stores string
		b = int(input('Enter b:'))  # => b stores an int
		c = float(a) * b            # => here I multiply a float by an int


		## Type casting
		a = 3       # => type int
		b = 4.5     # => type float
		c = '1.2'   # => type str

		print('a is ' + str(a))     # => str(a) returns a string from an int
		print('b is ' + str(b))     # => str(b) returns a string from a float
		d = b * float(c)            # => here I multipy 2 floats. d is a float.

		str1 = '12 a'
		#float(str1)    # => error



		####################################
		## String Indexing, Operations and Slicing
		####################################

		## A string can be treated like a list of characters. Indexing starts from 0
		language = 'Python 3'
		language[0]              # => 'P'
		language[1]              # => 'y'
		language[-1]             # => '3'
		language[-2]             # => ' '
		"This is a string"[0]    # => 'T'

		#language[100]          # => IndexError: string index out of range

		# Cannot modify a string, it's immutable
		#language[0] = 'J'      # => TypeError: 'str' object does not support item assignment


		# You can find the length of a string
		len("This is a string")  # => 16


		## Strings can be concatenated with + and repeated with *
		print('Hello ' + 'world!')   # => 'Hello world!'
		print('Hello ' * 3)          # => 'Hello Hello Hello '
		print('PI:' + str(3.1415))   # => Can concatenate only strings


		## Slicing returns a new string
		## start index is included, end index is excluded
		movie = 'Star Wars'
		movie[0:4]    # => 'Star' -> from index 0 included to index 4 excluded
		movie[:4]     # => 'Star' -> start index defaults to zero
		movie[2:]     # => 'ar Wars' -> end index defaults to the index of the last char of the string
		movie[::]     # => 'Star Wars'
		movie[2:100]   # => 'ar Wars -> slicing doesn't return error when using index out of range
		movie[1:6:2]   # => 'trW' -> the 3rd index is the step (from index 2 included to 6 excluded in steps of 2)
		movie[6:1:-1]  # => 'aW ra' -> from index 6 included to index 1 excluded in steps of -1 (backwards)
		movie[::-1]    # => 'sraW ratS -> reverses the string



		#################################
		## Formatting Strings
		#################################
		price = 1.33
		quantity = 5

		# f-string literals (Python 3.6+) - NEW!
		f'The price is {price}'                    # => 'The price is 1.33'
		f'Total value is {price * quantity}'       # => 'Total value is 6.65'
		f'Total value is {price * quantity:.4f}'   # => 'Total value is 6.6500' -> displaying with 4 decimals

		# Classical method
		'The price is {}'.format(price)                      # => 'The price is 1.33'
		'The total value is {}'.format(price * quantity)     # => 'The total value is 6.65'
		'The total value is {:.4f}'.format(price * quantity) # => 'The total value is 6.6500' -> displaying with 4 decimals


		'The price is {} and the total value is {}'.format(price, price * quantity)    # => 'The price is 1.33 and the total value is 6.65'
		'The price is {0} and the total value is {1}'.format(price, price * quantity)  # => 'The price is 1.33 and the total value is 6.65'
		'The total value is {1} and the price is {0}'.format(price, price * quantity)  # => 'The total value is 6.65 and the price is 1.33'

		print('The total value is ', price * quantity)     # => 'The total value is 6.65'



		########################
		## String Methods
		########################

		dir(str)        # => lists all string methods
		help(str.find)  # => displays the help of a method

		## All string methods return a new string but don't modify the original string
		my_str = 'I learn Python Programming'
		my_str.upper()        # => 'I LEARN PYTHON PROGRAMMING'
		my_str.lower()        # => 'i learn python programming'

		my_ip = '  10.0.0.1 '
		my_ip.strip()       # => '10.0.0.1'

		my_ip = '$$$10.0.0.1$$'
		my_ip.strip('$')        # => '10.0.0.1'

		# Removes all leading whitespace in string
		my_ip.lstrip()      # => '10.0.0.1 '

		# Removes all trailing whitespace of string
		my_ip.rstrip()      # => '  10.0.0.1'

		my_str = 'I learn Python'
		my_str.replace('Python', 'Go')     # => 'I learn Go'

		## split() returns a list from a string having a delimiter
		my_ip.split('.')            # => ['10', '0', '0', '1']

		## Be default the delimiter is a whitespace
		my_list = my_str.split()      # => my_list = ['I', 'learn', 'Python', 'Programming']

		## join() returns a string from a list
		':'.join(my_list)       # => '10:0:0:1'

		## in and not in operators test membership
		'10' in my_ip           # => returns True
		'10' not in my_ip       # => returns False
		'20' in my_ip           # => returns False


		# Other string methods
		my_str = 'this is a string. this is a string'

		## Returns the first index in my_str where substring 'is' is found or -1 if it didn't find the substring
		my_str.find('is')       # => 2
		my_str.find('si')       # => -1

		# Returns a capitalized version of the string.
		my_str.capitalize()     # => 'This is a string. this is a string'

		## Returns True if my_str is an uppercase string, False otherwise
		my_str.isupper()        # => False

		## Returns True if my_str is a lowercase string, False otherwise
		my_str.lower().islower()    # => True

		# Returns the number of occurrences of substring 's' in my_str
		my_str.count('s')       # => 6

		'0123123'.isdigit()     # => True
		'0123123x'.isdigit()    # => False
		'abc'.isalpha()         # => True
		'0123123x'.isalnum()    # => True

		my_str1 = 'Hi everyone!'
		# Inverts case for all letters in string
		my_str1.swapcase()      # => 'hI EVERYONE!'


Coding - Program Flow Control


		##################################################################
		## if ... elif ... else Statements
		## Execute a specific block of code if a condition is evaluated to True
		##################################################################

		a, b = 3, 5
		if a < b: #if a is less that b execute the indented block of code under the if clause, otherwise go and test the elif condition
		    print('a is less than b')
		elif a == b: #if a is equal to b execute the indented block of code that fallows, otherwise execute the block of code under the else clause
		    print('a is equal to b')
		else:
		    print('a is greater than b')


		## or / and operators
		your_age = 14
		if your_age < 0 or your_age > 99: #if ANY of the expression is True execute the indented block of code under the if clause
		    print('Invalid age!')
		elif your_age <= 2:
		    print('You are an Infant')
		elif your_age < 18:
		    print('You are a child')
		else:
		    print('You are an adult')


		a = 3
		if 1 < a <= 9:
		    print('a is greater than 1 and less than of equal to 9')

		# equivalent to
		if a > 1 and a <= 9:
		    print('a is greater than 1 and less than of equal to 9')



		a = 12
		## The fallowing 3 exemples test if a number a is divisible by 6
		## 1st Example - nested if
		if a % 2 == 0:
		    if a % 3 ==0:
		        print('Example 1: a is divisible by 2 and 3 (or by 6)')


		## 2nd Example: and operator -> it returns True if both expressions are True, False otherwise
		if a % 2 == 0 and a % 3 == 0:
		    print('Example 2: a is divisible by 2 and 3 (or by 6)')

		## 3rd Example
		if not (a % 2  and a % 3 ): #the truthniness of an expression: a % 2 is equal to bool(a %2)
		    print('Example 2: a is divisible by 2 and 3 (or by 6)')


		## The truthiness of a variable
		b = 0
		if b:   #it test the truthiness of b or bool(b)
		    print('The truthiness of b: True')
		else:
		    print('The truthiness of b: False')

		my_str = 'some string'
		if my_str:   #it test the truthiness of my_str or bool(my_str)
		    print('The truthiness of my_str: True')
		else:
		    print('The truthiness of my_str: False')



		name = 'Andrei'
		## Pythonic version
		print('Hello Andrei') if name == 'Andrei' else print('You are not Andrei!')

		# equivalent to:
		if name == 'Andrei':
		    print('Hello Andrei')
		else:
		    print('You are not Andrei')



		#################################
		## For Loops and Ranges
		#################################

		movies = ['Star Wars', 'The Godfather', 'Harry Potter ', 'Lord of the Rings']

		for m in movies: #it iterates over a sequence and executes the code indented under the "for" clause for each element in the sequence
		    print(f'One of my favorites movie is {m}')
		else: #the indented code below "else" will be executed when "for" has finished looping over the entire list (no "break" statement executed)
		    print('This is the end of the list')


		for i in range(100):
		    pass    # => empty instruction or "no nothing"

		for i in range (10):  # => from 0 (default, included) to 10 excluded
		   print(i, end=' ')
		# it prints:  0 1 2 3 4 5 6 7 8 9

		for i in range (3, 9):  # => from 3 included to 9 excluded
		   print(i, end=' ')
		#it prints: 3 4 5 6 7 8


		for i in range (3, 20, 3):  # => from 3 included to 20 excluded in steps of 3
		   print(i, end=' ')
		#it prints: 3 6 9 12 15 18


		for i in range (8, -4, -2):  # => from 8 included to -4 excluded in steps of -2
		   print(i, end=' ')
		#it prints: 8 6 4 2 0 -2




		## for ... continue -> it prints all letters of the string without 'o'
		for letter in 'Python Go and Java Cobol':
		    if letter == 'o':
		        continue    #go to the beginning of the for loop and do the next iteration
		    print(letter, end='')


		## for ... break
		sequence = [1, 5, 19, 3, 31, 100, 55, 34]
		for item in sequence:
		    if item % 17 == 0:
		        print('A number divisible by 17 has been found! Breaking the loop...')
		        break   #breaks out of the loop (executes the first instruction (if any) after the else block of code)
		else:
		    print('There is no number divisible by 17 in the sequence')


		#################################
		## While Loops
		#################################

		a = 10
		## Infinite Loop, it prints 10 indefinitely

		#while a:  #it tests the truthiness of a or bool(a) which is always True
		#    print(a)

		## Prints numbers from 10 to 1
		while a:    # => "while a:" is equivalent to "while a > 0:"
		    print(a)
		    a -= 1
		else:   # => executes the below block of code after finishing the while looop (and if no "break" statement has been executed)
		    print('Finishing printing numbers. a is now 0')


		## it prints only odd numbers between 1 and 20
		a = 0
		while a < 20:
		    a += 1
		    if a % 2 == 0:
		        continue    # go the the beginning of the while loop
		    print(f'Odd number {a}')   #it reaches this line only if the continue statement hasn't been executed


		## it prints numbers greater than 2
		a = 7
		while a > 0:
		    a -= 1
		    if a == 2:
		        break   # => it breaks out of the while loop and executes the next instruction after the while block of code
		    print(a)

		print('Loop ended.')



Coding - Lists in Python



		#################################
		## Intro to Lists
		## A list is an ordered sequence of objects of different types
		#################################

		## Creating lists
		list1 = []      # empty list
		list2 = list()  # empty list
		list3 = list('Python')  # => ['P', 'y', 't', 'h', 'o', 'n'] -> creates a list from a string
		list4 = ['Python', 'Go', 2018, 4.5, [1,2.3, 'abc']]   # a list stores any type of object

		## Lists are indexed like strings
		list4[0]    # => 'Python'
		list4[-1]   # => [1, 2.3, 'abc']
		list4[4][1] # => 2.3
		#list4[10]  # Raises an IndexError (out of bounds index)

		## A list is a mutable object, it can be modified
		list4[0] = 'Rust'   # =>['Rust', 'Go', 2018, 4.5, [1, 2.3, 'abc']]

		## Lists are sliced like strings. Slicing returns a new list
		## The start is included and the stop is excluded
		numbers = [1, 2, 3, 4, 5]
		numbers[1:4]    # => [2, 3, 4]
		numbers[1:40]   # => [2, 3, 4, 5]   -> out of bound slicing doesn't return error
		numbers[:3]     # => [1, 2, 3]  -> by default start is zero
		numbers[2:]     # => [3, 4, 5]  -> by default stop is the end of the list
		numbers[::]     # => [1, 2, 3, 4, 5]    -> returns the entire list
		numbers[1:5:3]  # => [2, 5]     -> from 2 included to 5 excluded in steps of 3
		numbers[4:1:-2] # => [5, 3]
		numbers[0:2] = ['a', 'b']   # => ['a', 'b', 3, 4, 5]    -> slicing modifies a list
		numbers[0:2] = ['x', 'y', 'z']  # => ['x', 'y', 'z', 3, 4, 5]   -> no error


		l1 = [1, 2, 3]
		l2 = l1     # l1 and l2 referece the same object, l2 is not a copy of l1
		l1 is l2    # => True
		l1 == l2    # => True
		l1.append(4)    #here I've modified both l1 and l2, they are still the same list
		l1 is l2    # => True
		l1 == l2    # => True


		l3 = l1.copy()  # l2 is a copy of l1, they don't reference the same object
		l1 == l2    # => True
		l1 is l2    # => False
		l3.remove(1)
		l1 == l3    # => False
		l1 is l3    # => False


		l1 = [1, 2]
		id(l1)          # => 139875652516360 (you get another value here)
		l1 += [3, 4]    # => [1, 2, 3, 4]  -> concatenating a new list to l1 - equivalent to using the extend method()
		id(l1)          # => 139875652516360  -> it's the same list

		l1 = l1 + [5, 6]    # => [1, 2, 3, 4, 5, 6] -> concatenating a new list to l1
		id(l1)              # => 139875654318792    -> l1 is a new list


		## Iterating over a list
		ip_list = ['192.168.0.1', '192.168.0.2', '10.0.0.1']
		for ip in ip_list:
		    print(f'Connecting to {ip} ...')


		## in and not in operators test list membership
		'10.0.0.1' in ip_list      # => returns True
		'192' not in ip_list       # => returns True
		'192' in ip_list           # => returns False

		#################################
		## List Methods
		#################################

		dir(list)       # returns a list will all list methods

		list1 = [1, 2.2, 'abc']
		len(list1 )     # => 3

		## Adds a single element to the end of the list
		list1.append(5)         # => [1, 2.2, 'abc', 5]
		# list1.append(6, 7)    # TypeError: append() takes exactly one argument (2 given)
		list1.append([6, 7])    # => [1, 2.2, 'abc', 5, [6, 7]]

		## Extends the list with elements of an iterable object
		#list1.extend(5.2)          # TypeError: 'float' object is not iterable
		list1.extend([5.2])         # => [1, 2.2, 'abc', 5, [6, 7], 5.2]
		list1.extend(['x', 'y'])    # => [1, 2.2, 'abc', 5, [6, 7], 5.2, 'x', 'y']

		## Inserts an item at a given index
		list1.insert(2, 'T')            # => [1, 2.2, 'T', 'abc', 5, [6, 7], 5.2, 'x', 'y']
		#Inserts on the last position
		list1.insert(len(list1), 'Q')   # => [1, 2.2, 'T', 'abc', 5, [6, 7], 5.2, 'x', 'y', 'Q']


		## Removes and returns an element of the list
		print(list1)      # => [1, 2.2, 'T', 'abc', 5, [6, 7], 5.2, 'x', 'y', 'Q']
		list1.pop()       # => 'Q'
		list1.pop(2)      #=> 'T'
		print(list1)      # => [1, 2.2, 'abc', 5, [6, 7], 5.2, 'x', 'y']
		#list1.pop(50)    # IndexError: pop index out of range



		## Removes and doesn't return an item of the list
		print(list1)        #[1, 2.2, 'abc', 5, [6, 7], 5.2, 'x', 'y']
		list1.remove('abc') # => [1, 2.2, 5, [6, 7], 5.2, 'x', 'y']
		#list1.remove('a')  # ValueError: list.remove(x): x not in list

		## Returns the index of an item
		letters = list('abcabcabc')
		letters.index('b')          # => 1
		letters.index('b', 3)       # => 4 -> it starts from index 3
		letters.index('b', 3, 6)    # => 4 -> it searches from index 3 to index 6


		## Returns the no. of occurrences of an item in a list
		letters.count('a')  # => 3


		nums = [6, -1, 55, 2.3]
		sorted(nums)    # => [-1, 2.3, 6, 55] -> returns a new sorted list

		print(nums) # => [6, -1, 55, 2.3]
		nums.sort() # sorts the list in-place
		print(nums) # => [-1, 2.3, 6, 55]
		max(nums)   # => 55
		min(nums)   # => -1
		sum(nums)   # => 62.3

		## These methods return an error if the list is not sortable
		nums.append('5.5')
		#nums.sort()    TypeError: '<' not supported between instances of 'str' and 'int'
		#nums.max()     AttributeError: 'list' object has no attribute 'max'


		## Converts a list into a string and a string into a list
		ip_list = ['192.168.0.1', '192.168.0.2', '10.0.0.1']
		## join() returns a string from a list
		ip_str = ':'.join(ip_list)       # => ip_str is equal to '192.168.0.1:192.168.0.2:10.0.0.1'

		## split() returns a list from a string
		ip_list = ip_str.split(':')     # => ip_list is equal to ['192.168.0.1', '192.168.0.2', '10.0.0.1']



Coding - Lists in Python
		#################################
		## Intro to Lists
		## A list is an ordered sequence of objects of different types
		#################################

		## Creating lists
		list1 = []      # empty list
		list2 = list()  # empty list
		list3 = list('Python')  # => ['P', 'y', 't', 'h', 'o', 'n'] -> creates a list from a string
		list4 = ['Python', 'Go', 2018, 4.5, [1,2.3, 'abc']]   # a list stores any type of object

		## Lists are indexed like strings
		list4[0]    # => 'Python'
		list4[-1]   # => [1, 2.3, 'abc']
		list4[4][1] # => 2.3
		#list4[10]  # Raises an IndexError (out of bounds index)

		## A list is a mutable object, it can be modified
		list4[0] = 'Rust'   # =>['Rust', 'Go', 2018, 4.5, [1, 2.3, 'abc']]

		## Lists are sliced like strings. Slicing returns a new list
		## The start is included and the stop is excluded
		numbers = [1, 2, 3, 4, 5]
		numbers[1:4]    # => [2, 3, 4]
		numbers[1:40]   # => [2, 3, 4, 5]   -> out of bound slicing doesn't return error
		numbers[:3]     # => [1, 2, 3]  -> by default start is zero
		numbers[2:]     # => [3, 4, 5]  -> by default stop is the end of the list
		numbers[::]     # => [1, 2, 3, 4, 5]    -> returns the entire list
		numbers[1:5:3]  # => [2, 5]     -> from 2 included to 5 excluded in steps of 3
		numbers[4:1:-2] # => [5, 3]
		numbers[0:2] = ['a', 'b']   # => ['a', 'b', 3, 4, 5]    -> slicing modifies a list
		numbers[0:2] = ['x', 'y', 'z']  # => ['x', 'y', 'z', 3, 4, 5]   -> no error


		l1 = [1, 2, 3]
		l2 = l1     # l1 and l2 referece the same object, l2 is not a copy of l1
		l1 is l2    # => True
		l1 == l2    # => True
		l1.append(4)    #here I've modified both l1 and l2, they are still the same list
		l1 is l2    # => True
		l1 == l2    # => True


		l3 = l1.copy()  # l2 is a copy of l1, they don't reference the same object
		l1 == l2    # => True
		l1 is l2    # => False
		l3.remove(1)
		l1 == l3    # => False
		l1 is l3    # => False


		l1 = [1, 2]
		id(l1)          # => 139875652516360 (you get another value here)
		l1 += [3, 4]    # => [1, 2, 3, 4]  -> concatenating a new list to l1 - equivalent to using the extend method()
		id(l1)          # => 139875652516360  -> it's the same list

		l1 = l1 + [5, 6]    # => [1, 2, 3, 4, 5, 6] -> concatenating a new list to l1
		id(l1)              # => 139875654318792    -> l1 is a new list


		## Iterating over a list
		ip_list = ['192.168.0.1', '192.168.0.2', '10.0.0.1']
		for ip in ip_list:
		    print(f'Connecting to {ip} ...')


		## in and not in operators test list membership
		'10.0.0.1' in ip_list      # => returns True
		'192' not in ip_list       # => returns True
		'192' in ip_list           # => returns False

		#################################
		## List Methods
		#################################

		dir(list)       # returns a list will all list methods

		list1 = [1, 2.2, 'abc']
		len(list1 )     # => 3

		## Adds a single element to the end of the list
		list1.append(5)         # => [1, 2.2, 'abc', 5]
		# list1.append(6, 7)    # TypeError: append() takes exactly one argument (2 given)
		list1.append([6, 7])    # => [1, 2.2, 'abc', 5, [6, 7]]

		## Extends the list with elements of an iterable object
		#list1.extend(5.2)          # TypeError: 'float' object is not iterable
		list1.extend([5.2])         # => [1, 2.2, 'abc', 5, [6, 7], 5.2]
		list1.extend(['x', 'y'])    # => [1, 2.2, 'abc', 5, [6, 7], 5.2, 'x', 'y']

		## Inserts an item at a given index
		list1.insert(2, 'T')            # => [1, 2.2, 'T', 'abc', 5, [6, 7], 5.2, 'x', 'y']
		#Inserts on the last position
		list1.insert(len(list1), 'Q')   # => [1, 2.2, 'T', 'abc', 5, [6, 7], 5.2, 'x', 'y', 'Q']


		## Removes and returns an element of the list
		print(list1)      # => [1, 2.2, 'T', 'abc', 5, [6, 7], 5.2, 'x', 'y', 'Q']
		list1.pop()       # => 'Q'
		list1.pop(2)      #=> 'T'
		print(list1)      # => [1, 2.2, 'abc', 5, [6, 7], 5.2, 'x', 'y']
		#list1.pop(50)    # IndexError: pop index out of range



		## Removes and doesn't return an item of the list
		print(list1)        #[1, 2.2, 'abc', 5, [6, 7], 5.2, 'x', 'y']
		list1.remove('abc') # => [1, 2.2, 5, [6, 7], 5.2, 'x', 'y']
		#list1.remove('a')  # ValueError: list.remove(x): x not in list

		## Returns the index of an item
		letters = list('abcabcabc')
		letters.index('b')          # => 1
		letters.index('b', 3)       # => 4 -> it starts from index 3
		letters.index('b', 3, 6)    # => 4 -> it searches from index 3 to index 6


		## Returns the no. of occurrences of an item in a list
		letters.count('a')  # => 3


		nums = [6, -1, 55, 2.3]
		sorted(nums)    # => [-1, 2.3, 6, 55] -> returns a new sorted list

		print(nums) # => [6, -1, 55, 2.3]
		nums.sort() # sorts the list in-place
		print(nums) # => [-1, 2.3, 6, 55]
		max(nums)   # => 55
		min(nums)   # => -1
		sum(nums)   # => 62.3

		## These methods return an error if the list is not sortable
		nums.append('5.5')
		#nums.sort()    TypeError: '<' not supported between instances of 'str' and 'int'
		#nums.max()     AttributeError: 'list' object has no attribute 'max'


		## Converts a list into a string and a string into a list
		ip_list = ['192.168.0.1', '192.168.0.2', '10.0.0.1']
		## join() returns a string from a list
		ip_str = ':'.join(ip_list)       # => ip_str is equal to '192.168.0.1:192.168.0.2:10.0.0.1'

		## split() returns a list from a string
		ip_list = ip_str.split(':')     # => ip_list is equal to ['192.168.0.1', '192.168.0.2', '10.0.0.1']




Coding - Tuples in Python




		#################################
		## Python Tuples
		## A tuple is a immutable ordered sequence of objects of different types
		#################################


		## Creating tuples
		t0 = ()         # empty tuple
		t1 = tuple()    # empty tuple
		t = (1.2)       # this isn't a tuple!
		type(t)         # => float
		t2 = (1.2,)     # a tuple with a single element
		t3 = tuple('abc')            # creating a tuple from a iterable (string)
		t4 = tuple([1, 3.2, 'abc'])  # creating a tuple from a iterable (list)
		t5 = (1, 3.2, 'abc')

		## Tuples are indexed like strings and lists
		t5[0]       # => 1
		t5[2]       # => 'abc'
		t5[-1]      # => 'abc'
		#t5[10]     # => IndexError: tuple index out of range

		## A tuple is an immutable object. Can't be changed.
		#t5[0] = 4   # => TypeError: 'tuple' object does not support item assignment


		## Tuple are sliced like strings and lists.
		## The start is included and the stop is excluded
		print(t5)   # => (1, 3.2, 'abc')
		t5[0:2]     # => (1, 3.2)
		t5[:2]      # => (1, 3.2)
		t5[::]      # => (1, 3.2, 'abc')
		t5[::2]     # => (1, 'abc') -> in steps of 2
		t5[-1:0:-1] # => ('abc', 3.2)



		## Iterating over a tuple
		movies = ('The Wizard of Oz', 'The Legend', 'Casablanca')
		for movie in movies:
		    print('We are watching {movie}')

		## in and not in operators test tuple membership
		'The Legend' in movies      # => True
		'The Legend' not in movies  # => False


		#################################
		## Tuple Methods
		#################################

		dir(tuple)       # returns a list will all tuple methods

		my_tuple = (1, 2.2, 'abc', 1)
		len(my_tuple)     # => 4


		## Returns the index of an item
		my_tuple.index(1)   # => 0 -> the index of the first element with value 1
		my_tuple.index(10)  # => ValueError: tuple.index(x): x not in tuple


		## Returns the no. of occurrences of the item in tuple
		my_tuple.count(1)  # => 2


		nums = (6, -1, 55, 2.3)
		sorted(nums)    # => (-1, 2.3, 6, 55) -> returns a new sorted tuple
		max(nums)   # => 55
		min(nums)   # => -1
		sum(nums)   # => 62.3




Coding - Sets and Frozensets in Python


		#################################
		## Sets in Python
		## A set is a unordered collection of immutable unique objects.
		#################################

		## Creating sets
		set1 = set()        # empty set
		#x = {}             # x is a dictionary, not a set
		set2 = {'a', 1, 2, 1, 'a', 2.3, 'a'}    # => {1, 2, 2.3, 'a'} -> unique unordered collection
		set3 = set('hellooo python')            # =>{'n', 'e', 'p', 't', 'o', 'h', 'l', ' ', 'y'}
		set4 = set([1, 2.3, 1, 'a', 'a', 2.3, 'b', 5])  # => {1, 2.3, 5, 'a', 'b'}
		#set4[0]    # TypeError: 'set' object does not support indexing
		set5 = {(1, 2), 'a'}     # a set can contain immutable objects like tuples
		#set6 = {[1, 2], 'a'}    # TypeError: unhashable type: 'list' -> list is mutable, not allowed in set


		## Iterating over a set
		some_letters = set('abcabc')
		for letter in some_letters:     # prints: c a b
		    print(letter, end=' ')

		## in and not in operators test set membership
		'a' in some_letters         # => True
		'aa' in some_letters        # => False
		'bb' not in some_letters    # => True



		s1 = {1, 2, 3}
		s2 = {3, 1, 2}
		s1 == s2    # => True
		s1 == s2    # => True
		s1 is s2    # => False

		## The assignment operator (=) create a reference to the same object
		s3 = s1
		s3 is s1    # => True
		s3 == s1    # => True
		s3.add('x') # adds to the set
		print(s1)   # => {1, 2, 3, 'x'}
		s3 == s1    # => True
		s3 is s1    # => True


		# copy() method creats a copy of a set (not a reference to the same object)
		s4 = s1.copy()
		s4 is s1    # => False
		s4 == s1    # => True
		s4.add('z')
		s4 == s1    # => False

		print(s1)   # => {1, 2, 3, 'x'}
		## pop() method removes and returns an arbitrary set element
		item = s1.pop()
		print(f'item:{item}, s1:{s1}')  # => item:1, s1:{2, 3, 'x'}

		s1.discard(2)   # discards element from the set, s1 is {3, 'x'}
		s1.discard(22)  # no error if the element doesn't exist
		#s1.remove(1)   # KeyError if element doesn't exist
		s1.clear()      # Removes all elements from this set


		#################################
		## Set Operations and Frozensets
		#################################

		set1 = {1, 2, 3}
		set2 = {3, 4, 5}

		## difference() returns the set of elements that  exist only in set1, but not in set2.
		set1.difference(set2)   # => {1, 2}
		set1 - set2             # => {1, 2}

		## symetric_difference() returns the set of elements which are in either of the sets but not in both.
		set1.symmetric_difference(set2) # => {1, 2, 4, 5}
		set1 ^ set2                     # => {1, 2, 4, 5}

		## union() returns the set of all unique elements present in all the sets.
		set1.union(set2)        # => {1, 2, 3, 4, 5}
		set1 | set2             # => {1, 2, 3, 4, 5}

		## intersection() returns the set that contains the elements that exist in both sets
		set1.intersection(set2) # => {3}
		set1 & set2             # => {3}


		set1.isdisjoint(set2)   # => False
		set1.issubset(set2)     # => False
		set1 > set2             # => False
		set1 <= set2            # => False
		{1, 2} <= {1, 2, 3}     # => True


		## A frozenset is an immutable set
		fs1 = frozenset(set1)
		print(fs1)  # => frozenset({1, 2, 3})

		## All set methods that don't modify the set are available to frozensets
		fs1 & set2  # => frozenset({3})



Coding - Dictionaries in Python


		#################################
		## Dictionaries in Python
		## A dictionary is an unordered collection of key: value pairs
		#################################

		dict1 = {}      # empty dictionary
		dict2 = dict()  # empty dictionary

		## Keys for dictionaries have to be immutable types. This is to ensure that
		## the key can be converted to a constant hash value for quick look-ups.
		#invalid_dict = {[1,2,3]: "123"}  # => Raises a TypeError: unhashable type: 'list'
		#a key of type tuple is permitted (immutable). Values can be of any type, however.
		valid_dict = {(1,2,3):[1,2,3], 3: 'abc', 'abc':{14,'a'}, 4.5:True}

		product = {'id':1234, 'name':'Laptop'}
		product['seller'] = 'Amazon'        # adds a new key:value pair
		product.update({'price':888.99})    # another way to add to a dictionary

		p = product['price']                # getting the value of a key,  p is 888.00

		del product['seller']        # removing a key:value pair
		print(product)               # => {'id': 1234, 'name': 'Laptop', 'price': 888.99}
		#seller = product['seller']  # Looking up a non-existing key is a KeyError

		# Use get() method to retrieve the value of a key
		product.get("id")                   # => 1234
		product.get("review")               # => None -> it doesn't return KeyError
		# The get method supports a default argument when the value is missing
		product.get("id", 4)                # => 1234
		product.get("review", 'N/A')        # => 'N/A'

		## pop() removes specified key and return the corresponding value.
		## If key is not found, a default value is given, otherwise KeyError is raised
		name = product.pop('name')    # name is 'Laptop'
		print(product)                # => {'id': 1234, 'price': 888.99}

		#name = product.pop('name')                 # => KeyError: 'name', key 'name' doesn't exist anymore
		name = product.pop('name', 'No such key')   # => name is 'No such key'


		#################################
		## Dictionary Operations and Methods
		#################################

		product = {'id':1234, 'price':888.99}

		## in and not in operators test dictionary key membership
		## there is no direct method to test if a corresponding value belongs to the dictionary
		'price' in product  # => True
		5 in product        # => False

		## Dictionary views
		keys = product.keys()       # getting all keys as an iterable
		keys = list(keys)           # it can be converted to a list
		print(keys)                 # => ['id', 'price']

		values = product.values()   # getting all values as an iterable
		values = list(values)       # it can be converted to a list
		print(values)               # => [1234, 888.99]

		key_values = product.items()    # getting all key:value pairs as tuples
		key_values = list(key_values)   # it can be converted to a list of tuples
		print(key_values)               # => [('id', 1234), ('price', 888.99)]

		## Iterating over a dictionary

		## Iterating over the keys
		for k in product:
		    print(f'key:{k}')
		#equivalent to:
		for k in product.keys():
		    print(f'key:{k}')

		## Iterating over the values
		for v in product.values():
		    print(f'value:{v}')

		# Iterating over both the keys and the values
		for k,v in product.items():
		    print(f'key:{k}, value:{v}')

		## Creates a copy of a dictionary
		prod = product.copy()
		## Returns the no. of key:value pairs in the dictionary
		len(prod)
		# Removes all items from dictionary
		product.clear()


Coding - Functions and Lambda Expressions in Python



		#################################
		## Intro to Functions
		#################################

		## Use "def" to create new functions
		def my_function1():
		    """
		    This is function's docstring.
		    """
		    print('This is a function!')
		    #this function returns implicitly None

		## Calling the function
		my_function1()           # => This is a function!
		my_function1.__doc__     # => This is function's docstring.


		## return exits the function
		def my_function2():
		    x = 1
		    return x                             # the function ends here
		    print('Never reacheas this line!')   # it will never execute this line

		## Calling the function
		my_function1()      # returns 1


		## A function can return more values as a tuple
		def add_multiply_power(x, y):
		    return x + y, x * y, x ** y

		## Calling the function
		a, b, c = add_multiply_power(2, 3)  # returns (2 + 3, 2 * 3, 2 ** 3)
		print(a, b, c)                      # => 5 6 8



		########################
		## Function's Arguments
		########################

		## Function with positional parameters
		def add(x, y):
		    print(f"x is {x} and y is {y}")
		    return x + y  # Returns the result of x + y with a return statement

		# Calling function with positional arguments
		s = add(5, 6)  # => prints out "x is 5 and y is 6" and returns 11, s is 11

		## Calling function with keyword arguments
		s = add(y=1, x=8)  # => prints out "x is 8 and y is 1" and returns 9, s is 9


		## Function with default parameters
		def add(x=1, y=0):
		    print(f"x is {x} and y is {y}")
		    return x + y  # Returns the result of x + y with a return statement

		## Calling function with default arguments
		s = add()     # => prints out "x is 1 and y is 0" and returns 1, s is 1
		s = add(5)    # => prints out "x is 5 and y is 0" and returns 5, s is 5
		s = add(5,3)  # => prints out "x is 5 and y is 3" and returns 8, s is 8


		# Function that takes a variable number of positional arguments
		def concatenate(*args):
		    result = ''
		    for tmp in args:
		        result = result + tmp
		    return result

		## Calling the function
		result = concatenate()
		print(result)           # => '' -> empty string

		result = concatenate('Python', '!')
		print(result)           # => Python!

		result = concatenate('I', 'love ', 'programming')
		print(result)          # => Ilove programming


		# Function that takes a variable number of keyword arguments
		def device_info(**kwargs):  #kwargs is a dictionary
		    for k, v in kwargs.items():
		        print(f'{k}: {v}')

		## Calling the function
		#It prints out:
		# ip: 10.0.0.1
		# username: u1
		# password: secretpass
		device_info(name='Cisco Router', ip='10.0.0.1', username='u1', password='secretpass')



		#################################
		## Scopes and Namespaces
		#################################
		x = 3   # this is a global scoped variable

		def my_func1():
		    print(f'x is {x}')  # this is "x" variable from the global namespace

		## Calling the function
		my_func1()      # => x is 3


		def my_func2():
		    x = 6               # this is a local scoped variable
		    print(f'x is {x}')  # this is "x" varible from the global namespace

		## Calling the function
		my_func2()      # => x is 6
		print(x)        # => 3 -> "x" variable was not modified inside the function


		def my_func3():
		    global x    # importing x variable from the global namespace
		    x = x * 10  # this is "x" variable from the global namespace
		    print(f'x is {x}')

		## Calling the function
		my_func3()      # => x is 30
		print(x)        # => 30 -> global "x" variable was modified inside the function


		def my_func4():
		    print(f'x is {x}')
		    x += 7      # this is an error, we used local x before assignment

		## Calling the function
		my_func4()      # => UnboundLocalError: local variable 'x' referenced before assignment



		#########################
		## Lambda Expressions
		#########################

		# "x" and "y" are lambdas arguments.
		add = lambda x, y: x + y    # this creates a function
		type(add)                   # => function


		## Assigning lambda expression to a variable
		result = add(2, 3)      # => 5


		## We can use default arguments
		add = lambda x=1, y=0: x + y
		result = add()      # => 1


		## We can even use *args and **kwargs
		my_function = lambda x, *args, **kwargs: (x, *args, {**kwargs})
		# x is 2.3, args is (a, b, c) and kwargs is {arg1='abc', arg2='def', arg3='geh'}
		my_function(2.3, 'a', 'b', 'c', arg1='abc', arg2='def', arg3='geh')


		## Passing as an argument to a function
		## Lambdas are functions and can therefore be passed to any other function as an argument (or returned from another function)
		def my_func(x, fn):
		    return fn(x)

		result = my_func(2, lambda x: x**2)
		print(result)       # => 4

		result = my_func(2, lambda x: x**3)
		print(result)       # => 8

		result = my_func('a', lambda x: x * 3)
		print(result)       # => 'aaa'

		result = my_func('a:b:c', lambda x: x.split(':'))
		print(result)       # => ['a', 'b', 'c'] -> this is a list

		result = my_func(('p', 'y', 't', 'h', 'o', 'n'), lambda x: '-'.join(x))
		print(result)       # => p-y-t-h-o-n > this is a string



Coding - Errors and Exception Handling


		#################################
		## Exceptions Handling
		## Exceptions are run-time Errors
		#################################

		a = 2

		#for ZeroDivisionError
		# b = 0

		#for TypeError
		b = '0'

		#for another Exception
		#del b

		try:
		    ## try to execute this block of code!
		    c = a / b
		except ZeroDivisionError as e:
		    ## This block of code is executed when a ZeroDivisionError occurs
		    print(f'There was Division by zero: {e}')
		except TypeError as e:
		    ## This block of code is executed when a TypeError occurs
		    print(f'There was a Type Error: {e}')
		except Exception as e:
		    ## This block of code is executed when other exception occurs
		    print(f'Other exception accured: {e}')
		else:
		    ## This block of code is executed when no exception occurs
		    print(f'No exception raised. c is {c}')
		finally:
		    print('This block of code is always executed!')


		print('Continue script execution..')
		x = 2


Coding Section - Working with Text Files


		###############################
		##Working with Files in Python
		##############################

		## Opens a file named a.txt and returns a file object called f
		## a.txt it's in the same directory with the python script
		## use a correct relative or absolute path
		f = open('a.txt', 'r')  # it will be opened in read-only mode

		content = f.read()  # reads the entire file as a string
		print(content)

		f.closed        # => False, file is not closed

		## Closes the file
		f.close()


		## Opens the file in read-only mode and reads its contents in a list
		## the file object will be automatically closed
		with open('a.txt', 'r') as my_file:
		    content = my_file.readlines()   # content is a list

		my_file.closed      # => True, my_file has been closed automatically

		## file object is an iterable object
		with open('a.txt', 'r') as my_file:
		    for line in my_file:    #iterating over the lines within the file
		        print(line, end='')


		## Opens the file in write-mode.
		## Creates the file if it doesn't exist or overwrites the file if it already exists
		with open('my_file.txt', 'w') as file:
		    file.write('This file will be overwritten!')


		## Opens the file in append-mode.
		## Creates the file if it doesn't exist or appends to its end if it exists
		with open('another_file.txt', 'a') as file:
		    file.write('Appending to the end!')


		## Opens the file for both read and write
		## Doesn't create the file if it doesn't exist
		with open('my_file.txt', 'r+') as file:
		    file.seek(0)    # the cursor is positioned at the beginning of the file
		    file.write('Writing and the beginning') # writing and the beginning

		    file.seek(5)    # moving the cursor at position 5
		    content = file.read(10) # reading 10 characters starting from position 5
		    print(content)






Coding
Section - Working
with CSV Files
#################################
## CSV Module
## Readind CSV Files
#################################

###CSV File - (airtravel.csv) - attached to this lecture
# "Month", "1958", "1959", "1960"
# "JAN",  340,  360,  417
# "FEB",  318,  342,  391
# "MAR",  362,  406,  419
# "APR",  348,  396,  461
# "MAY",  363,  420,  472
# "JUN",  435,  472,  535
# "JUL",  491,  548,  622
# "AUG",  505,  559,  606
# "SEP",  404,  463,  508
# "OCT",  359,  407,  461
# "NOV",  310,  362,  390
# "DEC",  337,  405,  432

## Importing the module
import csv

## Opening the file in read-only mode. airtravel.csv is in the same directory with the python script
with open('airtravel.csv', 'r') as csv_file:
	reader = csv.reader(csv_file)  # using a csv.reader object

	next(reader)  # skipping the first line (header)
	for row in reader:
		print(row)  # row is a list, each field is list element

#################################
## CSV Module
## Writing CSV Files
#################################

## Importing the module
import csv

## Opening people.csv in append-mode
with open('people.csv', 'a') as csvfile:
	writer = csv.writer(csvfile)  # getting a csv.writer object
	csvdata = (5, 'Anne', 'Amsterdam')
	writer.writerow(csvdata)  # appending a line to the end file. csvdata is a tuple

## Opening numbers.csv in write-mode
with open('numbers.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	writer.writerow(['x', 'x**2', 'x**3', 'x**4'])
	for x in range(1, 101):
		writer.writerow([x, x ** 2, x ** 3, x ** 4])

#################################
## CSV Module
## Using CSV Dialects
#################################

import csv

## Printing available csv dialects
print(csv.list_dialects())

## passwd file - passwd.csv is attached to this lecture
# root:x:0:0:root:/root:/bin/bash
# daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
# bin:x:2:2:bin:/bin:/usr/sbin/nologin
# sys:x:3:3:sys:/dev:/usr/sbin/nologin
# sync:x:4:65534:sync:/bin:/bin/sync
# games:x:5:60:games:/usr/games:/usr/sbin/nologin
# man:x:6:12:man:/var/cache/man:/usr/sbin/nologin

## Reading /etc/passwd (Linux file) using a custom delimiter (:)
with open('/etc/passwd', 'r') as f:
	reader = csv.reader(f, delimiter=':', lineterminator='\n')
	for row in reader:
		print(row)

## item.csv file (attached to this lecture)
# items#quantity#price
# pens#3#8.8
# plates#15#2.6
# cups#44#1.1
# bottles#21#3.5

## Creating a custom dialect named hashes
csv.register_dialect('hashes', delimiter='#', quoting=csv.QUOTE_NONE, lineterminator='\n')

## Reading items.csv file
with open('items.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, dialect='hashes')
	for row in reader:
		print(row)

## Appending a line to the csv file
with open('items.csv', 'a') as csvfile:
	writer = csv.writer(csvfile, dialect='hashes')
	writer.writerow(('spoon', 3, 1.5))


Coding - Pickle

#################################
## Data Serialization and Deserialization with Pickle
#################################

import pickle

# Declaring a dictionary
friends = {"Dan": (20, "London", 13242252), "Maria": [25, "Madrid", 34232424]}

# Serializing the dictionary to binary file called `friends.dat`
with open('friends.dat', 'wb') as f:  # b -> binary mode
	pickle.dump(friends, f)

# Deserializing into a Python Object
with open('friends.dat', 'rb') as f:
	obj = pickle.load(f)

	print(type(obj))  # => dict
	print(obj)  # => {'Dan': (20, 'London', 13242252), 'Maria': [25, 'Madrid', 34232424]}

Coding - JSON
#################################
## Data Serialization and Deserialization with JSON
#################################

import json

# Declaring a dictionary
friends = {"Dan": (20, "London", 13242252), "Maria": [25, "Madrid", 34232424]}

# Serializing the dictionary to a text file called `friends.json`
with open('friends.json', 'wt') as f:
	json.dump(friends, f, indent=4)

# Serializing the dictionary to a JSON encoded string
json_string = json.dumps(friends, indent=4)
print(json_string)

# Deserializing from file into a Python Object
with open('friends.json') as f:
	obj = json.load(f)

	print(type(obj))  # => dict
	print(obj)  # => friends = {"Dan": (20, "London", 13242252), "Maria":[25, "Madrid", 34232424]}

# Loading a JSON encoded string intro a Python Object
json_string = """{
    "Dan": [
        20,
        "London",
        13242252
    ],
    "Maria": [
        25,
        "Madrid",
        34232424
    ]
}"""

obj = json.loads(json_string)
print(type(obj))  # => dict
print(obj)  # => friends = {"Dan": (20, "London", 13242252), "Maria":[25, "Madrid", 34232424]}


