import math

def is_number(num):
    try:
        float(num)
        if float(num) or num == 0:
            return 1
    except ValueError:
        return 0
        
        
def val_espaciado(list_num):
    list_num = sorted(list_num)
    h = float(list_num[0]) - float(list_num[1])
    for i in range(len(list_num)-1):
        if (float(list_num[i]) - float(list_num[i+1])) != h:
            print ("No cumple con la condicion: Tener la misma separacion entre puntos.")
            return 0
    return 1
    
def val_contenido(list_num):
    for item in list_num:
        if is_number(item) == 0:
            print ("Hay un elemento no numerico en la lista. [{}]".format(item))
            return 0
    return 1
    
def input_listas():
    x_list = input("Ingresa la lista de los valores de x: ")
    x_list = x_list.split(",")
    while (val_contenido(x_list) == 0 or val_espaciado(x_list) == 0):
        x_list = []
        x_list = input("Ingresa la lista de los valores de x: ")
        x_list = x_list.split(",")
    x_list = [float(i) for i in x_list]
    
    y_list = input("Ingresa la lista de los valores de y: ")
    y_list = y_list.split(",")
    while (val_contenido(y_list) == 0):
        y_list = []
        y_list = input("Ingresa la lista de los valores de y: ")
        y_list = y_list.split(",")
    y_list = [float(i) for i in y_list]
    return x_list, y_list
    
def delta_y(y_list):
    delta_y0 = []
    delta = []
    last = 0
    
    for i in range(len(y_list)-1):
        val = y_list[i+1] - y_list[i]
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
    delta = [y_list[0]] + delta
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
    
def ecuacion(c_values, x_list, x_new):
    number_val = 0
    eq_str = ""
    eq_str2 = ""
    ans = 0
    
    for i in range(len(c_values)):
        eq_str += "" + (str(c_values[number_val]))
        for j in range(0, number_val):
            eq_str += "(" + str(x_new) + " - " + str(x_list[j]) + ")"
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
    while (is_number(x_new) != 1):
        x_new = input("Valor de x para buscar el valor y (f(x)): ")
    h = x_list[1] - x_list[0]
    delta_values = delta_y(y_list)
    c = c_values_list(delta_values, h) 
    answer = ecuacion(c, x_list, x_new)
    print ("y({}) = {}".format(x_new, round(answer,4)))
    
metodo()        