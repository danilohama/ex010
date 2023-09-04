# Crie um programa quanto de dinheiro uma pessoa tem na carteira e mostre quantos dolares ele pode comprar

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.20
euro = real / 5.74
libra = real / 6.25
print('Com R${} Reais, Você pode comprar U$${:0.2f} dolares'.format(real, dolar))
print('Com R${} Reais, Você pode comprar €{:0.2f} Euros'.format(real, euro))
print('Com R${} Reais, Você pode comprar £{} Libras'.format(real, libra))
