preço = float(input('Qual é o preço do produto: R$'))
vf = preço - (preço * 5 / 100)
print(f'O produto que custava R${preço:.2f}, na promoção com desconto de 5% vai custar R${vf:.2f}.')
