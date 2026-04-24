def classficar_nota(nota):
   
   if nota < 50:
      return "Reprovado"
   elif nota <=60:
      return "Suficiente"
   elif nota <=89:
      return "Bom"
   else:
        return "Excelente"

nota = float(input("Digite a nota: "))    

if 0 <= nota <= 100:
   resultado = classficar_nota(nota)
   print(resultado)
else:
   print("Nota inválida")
