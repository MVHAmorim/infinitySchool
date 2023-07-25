# Escreva um programa em python que pergunte ao usuário a velocidade de um carro. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h.
velocidade: float
multa: float

velocidade = float(input('Qual a velocidade do carro: '))

if velocidade > 80.0:
    multa = (velocidade - 80.0) * 20
    print(f'Você foi multado por excesso de velocidade, o valor da multa é de: {multa}')

else:
    print('Você é um bom condutor, parabéns!!!')