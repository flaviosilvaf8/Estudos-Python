aluno = {'nome': 'Flavio', 'idade': 22, 'nota_final': '10', 'aprovação': True}
#          key     value     key   value   key        value    key       value

print(aluno['nome']) # utiliza o index buscando pela key e não pelo numero do index

aluno.update({'nome': 'José', 'nota_final': 8}) #atualizara o nome para José e nota final para 8

print(aluno['nome'])
print(aluno['nota_final'])

aluno.update({'endereco': 'Rua A'}) # Adicionara o endereço dentro do meu dicionario Aluno

print(aluno['endereco'])


