

dias = int(input('Quantos dias alugou? '))
km = float(input('Quantos km rodados? '))

# coloquei 50 reais o dia e 20 centavos o km rodado

valor = (dias * 50) + (km * 0.20)

print('Total a pagar: R${:.2f}'.format(valor))
