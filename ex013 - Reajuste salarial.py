salário = float(input('Qual é o salário do funcionário: RS'))
vf = salário + (salário * 15 / 100)
print('Um funcionário que ganhava RS{:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(salário, vf))
