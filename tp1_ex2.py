#!/usr/bin/env python3

#
# A REMPLIR
#
# Expression conditionnelle
# retourne True si x > 0, False si x <= 0 ou si x vaut None
def expression_5_version1(x) :
	return  True if (x > 0) else False if (x<=0 or x == None) else False

def expression_5_version2(x) :
	if x > 0 : return True
	if x <=0 or x == None : return False

# Cetter version fonctionne aussi pour x == None
def expression_5(x) :
	return  False if (x == None or x<=0) else True if (x>0) else False




# AJOUTER D'AUTRES TESTS
#  [valeur_x, resultat_attendu]
def testData():
	return [[5, True], [None, False], [-2, False], [-3.4, False]]


#
# NE PAS MODIFIER
#
def testExpr(data) :
	score = 0
	ldata = len(data)
	for i, dt in enumerate(data) :
		print('  test %d/%d : ' % (i + 1, ldata), end='')
		x = dt[0]
		refr = dt[1]
		r = expression_5(x)
		if r == refr :
			score+=1
			print('ok')
		else :
			print('ECHEC')
			print('    entree  : %s' % x)
			print('    calcule : %s' % r)
			print('    attendu : %s' % refr)

	print('Score %d/%d' % (score, ldata))


if __name__ == '__main__':
	testExpr(testData())
