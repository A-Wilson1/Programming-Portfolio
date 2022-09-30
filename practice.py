Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> python3
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    python3
NameError: name 'python3' is not defined
>>> print("the program has executed")
the program has executed
>>> print("the program has executed")
the program has executed
>>> help()

Welcome to Python 3.6's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.6/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> help(input)
Help on built-in function input in module builtins:

input(prompt=None, /)
    Read a string from standard input.  The trailing newline is stripped.
    
    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.
    
    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.

>>> 
>>> 45+20
65
>>> 10 + 20 - 15
15
>>> 10 * 5
50
>>> 100 / 33
3.0303030303030303
>>> 100 // 33
3
>>> 10 ** 2
100
>>> 
>>> 10 % 3
1
>>> 
>>> 10 + 5 * 2
20
>>> 10 - 5 * 10 + 5
-35
>>> 5 * 10 ** 2
500
>>> (10 + 5) * 2
30
>>> 10 - 5 * (10 + 5)
-65
>>> (5 * 10) ** 2
2500
>>> 12 + (5 * 2 + 3)
25
>>> 12 + (5 * (2 + 3))
37
>>> 10+
SyntaxError: invalid syntax
>>> print("Ten divided by zero is", 10/0 )
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print("Ten divided by zero is", 10/0 )
ZeroDivisionError: division by zero
>>> 
