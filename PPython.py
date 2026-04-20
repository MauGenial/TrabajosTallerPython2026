def eje1():
    print("Ejercicio 1 ejecutandose")
    n1=int(input("Ingresar primer numero entero "))
    n2=int(input("Ingresar segundo numero entero "))
    r=n1+n2
    print("Primer digito : ", n1," Segundo digito : ", n2, " Resultado : ", r)
    if(n1>n2):
        print("El primer digito es mayor")
    if (n2>n1):
        print("El segundo digito es mayor")
    else:
        print("Los digitos son iguales")
#eje1()

def eje2():
    print("Ejercicio 2 ejecutandose")
    n1=int(input("Ingresar primer numero entero "))
    n2=int(input("Ingresar segundo numero entero "))
    n3=int(input("Ingresar tercer numero entero "))
    n4=int(input("Ingresar cuarto numero entero "))
    r=n1+n2+n3+n4
    print("Primer digito : ", n1," Segundo digito : ", n2, " Tercer digito : ", n3, " Cuarto digito : ", n4, " Resultado : ", r)
#eje2()

def eje2dif():
    print("Ejercicio 2 dif ejecutandose")
    arr=[]
    for i in range(4):
        arr.append(int(input("Ingrese un numero entero")))
    print("Suma de todos los numeros : ", sum(arr))
#eje2dif()

def eje3():
    print("Ejercicio 3 ejecutandose")
    n1=int(input("Ingresar la base del rectangulo "))
    n2=int(input("Ingresar la altura del rectangulo "))
    r=n1*n2
    print("Area del rectangulo : ", r)
#eje3()

def eje4():
    print("Ejercicio 4 ejecutandose")
    n1=float(input("Ingresar un lado del cuadrado con decimales "))
    r=n1*n1
    print("Area del cuadrado : ", r)
#eje4()

def eje5():
    print("--Ejercicio 5 ejecutandose--")
    n1=int(input("Ingresar las horas "))
    n2=int(input("Ingresar los minutos "))
    n3=int(input("Ingresar los segundos "))
    r=n1*3600+n2*60+n3
    print("Segundos totales : ", r)
#eje5()

def eje6():
    print("--Ejercicio 6 ejecutandose--")
    n1=int(input("Ingresar la base del triangulo "))
    n2=int(input("Ingresar la altura del triangulo "))
    r=(n1*n2)/2
    print("Area del triangulo : ", r)
#eje6()

def eje7():
    print("--Ejercicio 7 ejecutandose--")
    n1=float(input("Ingresar primer numero "))
    n2=float(input("Ingresar segundo numero "))
    n3=float(input("Ingresar tercer numero "))
    n4=float(input("Ingresar cuarto numero "))
    n5=float(input("Ingresar quinto numero "))
    n6=float(input("Ingresar sexto numero "))
    S=n1+n2+n3+n4+n5+n6
    r= S/6
    print("Suma de los numeros : ", S, " Promedio : ", r)
#eje7()

def eje7alt():
    print("--Ejercicio 7 ejecutandose--")
    arr=[]
    for i in range(4):
        arr.append(int(input("Ingrese un numero entero")))
    sum(arr)
    r= S/6
    print("Suma de los numeros : ", S, " Promedio : ", r)
#eje7alt()


def eje8():
    print("--Ejercicio 8 ejecutandose--")
    n1=float(input("Ingresar el primer digito "))
    n2=float(input("Ingresar el segundo digito "))
    r=(n1/n2)*100
    print("Porcentaje : ", r, "%")
#eje8()

def eje9():
    print("--Ejercicio 9 ejecutandose--")
    n1=int(input("Ingresar fecha en DDMMAAAA "))
    m=n1%1000000
    me=int(m//10000)  
    d=int(n1//1000000)
    a=n1%10000
    print("La fecha de hoy es : ", "Dia : ", d, "Mes :", me ,"Año : ", a)
    print(d,me,a)
#eje9()

def eje10():
    print("--Ejercicio 10 ejecutandose--")
    n1=float(input("Nota de los Examenes Parciales : "))
    n2=float(input("Nota de los Trabajos Practicos : "))
    n3=float(input("Nota del Examen : ")) 
    if(n1>=0 and n2>=0 and n3>=0 and n1<=10 and n2<=10 and n3<=10):
        r=(n1*0.3)+(n2*0.2)+(n3*0.5)
        print("Nota final : ", r)
    else:
        print("Alguna/s de las notas ingresadas es/son invalida/s")
#eje10()

def eje11():
    print("--Ejercicio 11 ejecutandose--")
    v=0
    i=0
    n1=int(input("Ingresar la cantidad de autos vendidos : "))
    arr=[]
    while i < n1:
        arr.append(int(input(f"Ingrese el valor del auto N°{i+1} : ")))
        v +=arr[i]*0.05
        i += 1
    r=5500+(n1*200)+v
    print("Su salario este mes sera de : ", r)
#eje11()