n1 = input ("Informe sua primeira nota:\n")
n2 = input ("Informe sua segunda nota:\n")
media = (float (n1) + float(n2))/2

if media >=7:
    print("APROVADO")
  
else:
	nrecup = input ("Informe sua nota da recuperação:\n")
	nrecup = (float (media) + float(nrecup))/2

if nrecup >=5:
	print("APROVADO APÓS RECUPERAÇÃO!!")
else:
	print("REPROVADO!!")
