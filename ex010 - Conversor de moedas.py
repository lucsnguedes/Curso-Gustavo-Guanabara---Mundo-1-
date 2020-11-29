x = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = x / 3.27
print('Com RS{:.2f} você pode comprar US${:.2f}'.format(x, dolar))
