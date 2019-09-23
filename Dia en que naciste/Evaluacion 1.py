
#OJO, este codigo es Spanglish



def born_day(dia,mes,anno):
  cod_mes = 0
  cod_siglo = 6
  semana = ["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]
  menor = 0
  mayor = 99

  while True:
    if menor <= anno and anno <= mayor:
      break
    if cod_siglo <= 0:
      cod_siglo = 8
    menor += 100        
    mayor += 100
    cod_siglo -= 2

  if mes == 1: cod_mes = 0
  elif mes == 2: cod_mes = 3
  elif mes == 3: cod_mes = 3
  elif mes == 4: cod_mes = 6
  elif mes == 5: cod_mes = 1
  elif mes == 6: cod_mes = 4
  elif mes == 7: cod_mes = 6
  elif mes == 8: cod_mes = 2
  elif mes == 9: cod_mes = 5
  elif mes == 10: cod_mes = 0
  elif mes == 11: cod_mes = 3
  else: 
    if mes == 12: 
      cod_mes = 5
  
  letra = str(anno)
  num = len(letra)
  while True:
    if num % 2 == 0:
      t = letra[2:]
    else:
      t = letra[1:]
    break
  año = int(t)
  

  formula = dia + cod_mes + año + (año/4) + cod_siglo
  res = formula%7
  imp = semana[int(res)] 
  print(imp)

born_day(5,7,1995)  #Miercoles
born_day(13,9,1993) #Lunes
born_day(18,9,1996) #Miercoles
born_day(8,10,1995) #Domingo. Mi cumpleaños Anthony
born_day(25,9,2000) #Lunes
born_day(11,8,1996) #Domingo
born_day(28,8,2002) #Miercoles
born_day(12,2,2005) #Sabado
born_day(28,8,2002) #Miercoles
born_day(18,8,1997) #Lunes
born_day(20,5,955)  #Martes


