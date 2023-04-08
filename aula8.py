import datetime

nome = 'Rafael'
sobrenome = 'Barboa Kretzer'
idade = 21
ano_nascimento = datetime.date.today().year - idade
maior_de_idade = idade >= 18
altura_metros = 1.82

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)
