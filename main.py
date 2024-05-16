import random

#Função principal para rolar dados
def rolar():
  roll = str(input("Role um dado no formato #d#:"))
  valores = []
  
#Função secundária para rolar o resultado. Iterada várias vezes caso o número de dados rolados seja maior que 1.
  
  def rolar_dado(tipo):
    try:
      if tipo == 4:
        result = random.randrange(1,4)
      if tipo == 6:
        result = random.randrange(1,6)
      if tipo == 8:
        result = random.randrange(1,8)      
      if tipo == 10:
        result = random.randrange(1,10)        
      if tipo == 12:
        result = random.randrange(1,12)       
      if tipo == 20:
        result = random.randrange(1,20)     
      if tipo == 100:
        result = random.randrange(1,100)

      valores.append(result)
      print(result)
      
    except:
      print("Tipo de dado inválido")
# ---------------
#Função principal para rolar dados (cont.)
  try:
    dado = roll.partition("d")
    (qnt,de,tipo) = dado
    qnt = int(qnt)
    tipo = int(tipo)
    
  except:
    print("ERRO! Role um dado no formato #d#:")

  if qnt == 1:
    rolar_dado(tipo)
  if qnt > 1:
    for i in range(qnt):
      rolar_dado(tipo)
      total = sum(valores)
    
    print("Total:",total)
      
rolar()