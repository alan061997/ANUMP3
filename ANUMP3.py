import math

# Validaciones
def is_number(num):
	try:
		float(num)
		if float(num) or num == 0:
			return 1
	except ValueError:
		return 0
		
		
def val_espaciado(list_num):
	list_num = sorted(list_num)
	if len(list_num) < 2:
		print ("La lista debe tener por lo menos 2 valores")
		return 0
	h = round(float(list_num[1]) - float(list_num[0]), 4)
	for i in range(len(list_num)-1):
		resta = round(float(list_num[i+1]) - float(list_num[i]), 4)
		if resta != h:
			print ("No cumple con la condicion: Tener la misma separacion entre puntos.")
			return 0
	return 1
	
def val_contenido(list_num):
	for item in list_num:
		if is_number(item) == 0:
			print ("Hay un elemento no numerico en la lista. [{}]".format(item))
			return 0
	return 1

def tabla(xy_list):
	columnas = 2
	filas = len(xy_list)
	print ("\t+------------+------------+\n\t|     {}      |     {}      |\n\t+------------+------------+".format("X", "Y"))
	for i in range(len(xy_list)):
		print ("\t|   %.4f   |   %.4f   |\n\t+------------+------------+" % (xy_list[i][0], xy_list[i][1]))
	
	
	
def input_listas():
	# Lista de valores x
	x_list = input("Ingresa la lista de los valores de x (x0,x1,x2,x3,...,xn): ")
	x_list = x_list.split(",")
	while (val_contenido(x_list) == 0 or val_espaciado(x_list) == 0):
		x_list = []
		x_list = input("Ingresa la lista de los valores de x (x0,x1,x2,x3,...,xn): ")
		x_list = x_list.split(",")
	# Conversion de los elementos de la lista string a flotantes
	x_list = [float(i) for i in x_list]
	
	# Lista de valores y
	y_list = input("Ingresa la lista de los valores de y (y0,y1,y2,y3,...,yn): ")
	y_list = y_list.split(",")
	while (val_contenido(y_list) == 0 or (len(y_list) != len(x_list))):
		if (len(y_list) != len(x_list)):
			print("No tienen la misma cantidad de x's de y's.")
		y_list = []
		y_list = input("Ingresa la lista de los valores de y (y0,y1,y2,y3,...,yn): ")
		y_list = y_list.split(",")
	# Conversion de los elementos de la lista string a flotantes
	y_list = [float(i) for i in y_list]
	return x_list, y_list
	
def delta_y(xy_list):
	delta_y0 = []
	delta = []
	last = 0
	
	# Obtencion de los valores delta y
	for i in range(len(xy_list)-1):
		val = xy_list[i+1][1] - xy_list[i][1]
		val = round(val, 4) 
		delta.append(val)
	delta_y0.append(delta)
	delta = []
	
	while (len(delta_y0[last]) > 1):
		for i in range(len(delta_y0[last])-1):
			val = delta_y0[last][i+1] - delta_y0[last][i]
			val = round(val, 4)
			delta.append(val)
		delta_y0.append(delta)
		delta = []
		last += 1
	
	for i in range(len(delta_y0)):
		delta.append(delta_y0[i][0])
	delta = [xy_list[0][1]] + delta
	return delta
	
def c_values_list(delta, h):
	number_terms = 0
	c_val = []
	for item in delta:
		val = item/(math.factorial(number_terms)*(h**number_terms))
		val = round(val, 4)
		c_val.append(val)
		number_terms += 1
	return c_val
	
def ecuacion(c_values, xy_list, x_new):
	number_val = 0
	eq_str = ""
	eq_str2 = ""
	ans = 0
	
	for i in range(len(c_values)):
		eq_str += "" + (str(c_values[number_val]))
		for j in range(0, number_val):
			#print (xy_list)
			#print ("xy_list[{}][0]".format(j))
			eq_str += "(" + str(x_new) + " - " + str(xy_list[j][0]) + ")"
		number_val += 1
		if i < (len(c_values)-1):
			eq_str += " + "
		else:
			eq_str += ""
	
	print ("y({}) = {}".format(x_new, eq_str))	
	eq_str = eq_str.split("+")
	for i in range(len(eq_str)):
		eq_str[i] = eq_str[i].replace('(', "*(")
	
	for item in eq_str:
		ans += eval(item)
	return ans
	
def metodo():
	x_list, y_list = input_listas()
	x_new = input("Valor de x para buscar el valor y (f(x)): ")
	xy_list = sorted(zip(x_list, y_list))
	while (is_number(x_new) != 1):
		x_new = input("Valor de x para buscar el valor y (f(x)): ")
	h = x_list[1] - x_list[0]
	delta_values = delta_y(xy_list)
	c = c_values_list(delta_values, h)
	tabla (xy_list)
	answer = ecuacion(c, xy_list, x_new)
	print ("y({}) = {}".format(x_new, round(answer,4)))
metodo()		
