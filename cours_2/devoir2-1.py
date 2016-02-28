def conversion(grade):
	try:
		grade = float(grade)
		if grade >= 18 and grade <= 20:
			print "A"
		elif  grade >= 16 and grade < 18:
			print "B"
		elif grade >= 14 and grade < 16:
			print "C"
		elif grade >= 12 and grade < 14:
			print "D"
		elif grade >= 0 and grade < 12:
			print "F"
		else:
			print "Note doit etre entre 0 et 20"
	except:
		print "Il faut une valeur num\xc3\xa9rique."
conversion(raw_input("Encoder la cote sur 20 : "))
