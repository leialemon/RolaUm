import random

#Função principal para rolar dados
def rolar():
  roll = str(input("Role um dado no formato #d#:"))
  valores = []
  
#Função secundária para rolar o resultado. Iterada várias vezes caso o número de dados rolados seja maior que 1.
  
  def rolar_dado(tipo):
    result = None
    match tipo:
      case 4:
        result = random.randrange(1,4)
      case 6:
        result = random.randrange(1,6)
      case 8:
        result = random.randrange(1,8)      
      case 10:
         result = random.randrange(1,10)        
      case 12:
        result = random.randrange(1,12)       
      case 20:
        result = random.randrange(1,20)     
      case 100:
        result = random.randrange(1,100)
      case _: print("Tipo de dado inválido")
    
    valores.append(result)
    print(result)
# ---------------
#Função principal para rolar dados (cont.)
  try:
    dado = roll.partition("d")
    (qnt,de,tipo) = dado
    qnt = int(qnt)
    tipo = int(tipo)
    
    if qnt == 1:
      rolar_dado(tipo)
    if qnt > 1:
      for i in range(qnt):
        rolar_dado(tipo)
        total = sum(valores)
      print("Total:",total)
  
  except:
    print("ERRO! Role um dado no formato #d#:")

rolar()