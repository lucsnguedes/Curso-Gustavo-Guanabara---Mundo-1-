days = int(input('Quantos dias alugado? '))
km = float(input('Quantos km rodados? '))
pag = ((days * 60) + (km * 0.15))
print('O total a pagar é de R${:.2f}'.format(pag))
