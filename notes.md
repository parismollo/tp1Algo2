Paris Mollo - Groupe 3

# Exercice 1
1. 
```bash
  >>> print("Hello World")
  Hello World
  >>> exit()
```

2. When we run py hello.py the program is executed but when we use the flag -i, the interpreter is launched after the program launches. 
   
```bash
PS C:\Users\paris\uni\s4\Algo2\TP1> py hello.py
Bonjour Le monde!
PS C:\Users\paris\uni\s4\Algo2\TP1> py -i hello.py
Bonjour Le monde!
>>> 
```

3. The hello file is now present in the dir results. Is now identifiable. 
```bash
  >>> dir()
  ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
  >>> import hello
  Bonjour Le monde!
  >>> dir()
  ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'hello']
  >>>
```

5. The operator / returns a float number and the operator // the whole number. 
```python
>>> 13/4
3.25
>>> 4/2
2.0 
>>> 13//4
3   
>>> 4//2
2  
```

6. After importing the math lib
```python
>>> import math 
>>> math.sqrt(3) + 56/9.0 * abs(-1/4) + 63**2
3972.2876063631243

```

1. Results
```python
>>> import hello
Bonjour Le monde!
>>> affiche()
Traceback (most recent call last):      
  File "<stdin>", line 1, in <module>   
NameError: name 'affiche' is not defined
>>> hello.affiche()
Bonjour Le monde!
>>> hello.affiche()
Bonjour Le monde!
>>> import hello
>>> hello.affiche()
Bonjour Le monde!
>>> import imp
__main__:1: DeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses
>>> imp.reload(hello)
Bonjour Le monde - maj!
<module 'hello' from 'C:\\Users\\paris\\uni\\s4\\Algo2\\TP1\\hello.py'>
>>> hello.affiche()   
Bonjour Le monde - maj!
>>> from hello import affiche
>>> affiche()
Bonjour Le monde - maj!
>>> hello.affiche()
Bonjour Le monde - maj!
>>>
```

8. Results
```python
  >>> from hello import *
  >>> affiche()
  Bonjour Le monde - maj!
  >>> dev()
  Bonjour developpeur Paris Mollo
  >>> hello.dev()
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  NameError: name 'hello' is not defined
  >>> hello.affiche()
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  NameError: name 'hello' is not defined
  >>>
```

# Exercice 2
1. Pour z non définie on a un erreur, NameError: name 'z' is not defined. Pendant, lorsque z = None, on a un objet du type classe NoneType.

```python
>>> print(Z)
Traceback (most recent call last):   
  File "<stdin>", line 1, in <module>
NameError: name 'Z' is not defined   
>>> Z = None
>>> print(Z)
None
>>> Z = ""
>>> print(Z)
```

2. Results
```python
  >>> Z = None
  >>> Z == None 
  True
  >>> del Z
  >>> Z == None
  Traceback (most recent call last):   
    File "<stdin>", line 1, in <module>
  NameError: name 'Z' is not defined
  >>> Z = ""    
  >>> Z == None
  False
```

3. Results
``` python
  >>> Z = None                 
  >>> print("Sans valeur") if Z == None else print("chaine vide") if Z =="" else print("autre")
  Sans valeur
  >>> Z = "" 
  >>> print("Sans valeur") if Z == None else print("chaine vide") if Z =="" else print("autre")
  chaine vide
  >>> Z = "r"
  >>> Z = "r"
  >>> print("Sans valeur") if Z == None else print("chaine vide") if Z =="" else print("autre")
  autre

```

4. Results
``` python
  >>> x = 3
  >>> True if x > 0 else False
  True
  >>> x = -55
  >>> x = -5 
  >>> True if x > 0 else False
  False
  >>> x = None
  >>> True if x > 0 else False
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: '>' not supported between instances of 'NoneType' and 'int'
  >>> del x
  >>> True if x > 0 else False
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  NameError: name 'x' is not defined

```
b) 
``` python

  >>> x = 3
  >>> None if x == None else True if x > 0 else False
  True
  >>> x = -5                                          
  >>> None if x == None else True if x > 0 else False 
  False
  >>> x = None
  >>> None if x == None else True if x > 0 else False
  >>> 

```

# Exercice 3
- Voir fichier tp1_ex3
