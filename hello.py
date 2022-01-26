import math
from operator import truediv
from xmlrpc.client import ExpatParser
def affiche():
    print("Bonjour Le monde!")
    

def dev():
    print("Bonjour developpeur Paris Mollo")

def exp(z):
    return z == None 
    
def seg(expression):
    if expression == None:
        return "sans valeur"
    elif expression == "":
        return "chaine vide"
    else:
        return "autre"

def seg2(z):
    print("sans valeur") if z == None else print("chaine vide") if z == "" else print("autre")

def expr2(x):
    print("True") if x > 0 else print("False")

def expr3(x):
    print("None") if x == None else print("True") if x > 0 else print("False")
# print(math.sqrt(3) + 56/9.0 * abs(-1/4) + 63**2)