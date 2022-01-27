#!/usr/bin/env python3
def ex1():
    for i in range(0,10):
        print(i)

def ex2():
    print(list(range(2, 11)))
    print(list(range(2, 12, 2)))
    print(list(range(10, 1,-2)))

def ex3():
    a = [i for i in range(0, 14, 2)]
    b = [i for i in "abcdef"]
    c = reverse(a)
    d = [(i, j) for i, j in zip(b, c)]
    return a, b, c, d

def ex4():
    _, _, _, l3 = ex3()
    a = l3[2:5]
    b = l3[1::2]
    c = l3[:]
    aux = [i*7 for i in range(20+1)]
    l5 = pos_mod(aux)
    return a, b, c, l5

def pos_mod(tab):
    return [0 if idx % 3 == 2 else v for idx, v in enumerate(tab)]

def reverse(a):
    return list(reversed(a))
	
def crible_eratosthene(n):
# calcule la table de booléens où la i-ème position est True
# si et seulement si i est un nombre premier.
    tab = [True]*(n+1)
    tab[0] = False 
    tab[1] = False
    for i in range(2, len(tab)):
        if tab[i] == True:
            start = i*i
            step = i
            for idx in range(start, len(tab), step):
                tab[idx] = False
    return tab

def test_crible(n):
    c=crible_eratosthene(n)
    for i in range(len(c)):
        if c[i]:
           print(i, end= ' ')
    print()

def ex6():
    l = [i for i in list(range(0, 36)) if i % 3 == 2]
    lg = l[:len(l)//2] 
    ld = l[len(l)//2:] 

def f(l):
    l[0] = 2022
def g(l):
    l[-1] = 2022



#
# A REMPLIR
#
def somme_impairs(x) :
    """Calcule la somme des entiers impairs de 1 a x"""
# calcule la somme des entiers impairs de 1 à x
    ls = range(1, x+1)
    res = 0
    for i in ls:
        if(est_impair(i)):
            print(i)
            res+=i
    return res

def est_impair(i):
    return i % 2 != 0

def test_somme(n) :
# teste que la somme des entiers impairs de 1 à x =
#    (x/2)*(x/2) si x est pair
#    (x+1)/2*(x+1)/2 sinon
# pour tout 1 <= x <= n
	return True


# AJOUTER D'AUTRES TESTS
#  [valeur_x, resultat_attendu]
def testDataSomme() :
    """retourne un jeu de tests"""
    return [[0, 0], [3, 4], [24, 144], [-3, 0]]


#
# NE PAS MODIFIER
#
def testOp(op, data) :
	print('\n\n* Test function %s:' % op.__name__)
	score = 0
	ldata = len(data)
	for i, dt in enumerate(data) :
		print('** test %d/%d : ' % (i + 1, ldata), end='')
		x = dt[0]
		refr = dt[1]
		r = op(x)
		if r == refr :
			score+=1
			print('ok')
		else :
			print('ECHEC')
			print('    entree  : %s' % x)
			print('    calcule : %s' % r)
			print('    attendu : %s' % refr)
	print('** Score %d/%d' % (score, ldata))


if __name__ == '__main__':
        test_crible(50)
        testOp(somme_impairs, testDataSomme())
