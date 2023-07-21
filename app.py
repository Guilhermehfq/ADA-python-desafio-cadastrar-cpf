# Variaveis iniciais
from collections import namedtuple
Pessoa = namedtuple(
    'Pessoa', ['cpf', 'nome', 'idade', 'sexo', 'renda', "estado"])
lista_vazia = 'Essa lista está vazia, portanto não é possivel calcular a media'


# Definindo as funções
def cadastrar_usuario():
    continuar_cadastro = True

    cadastros = {}

    while continuar_cadastro:
        cadastrar = input('Deseja inserir um novo cadastro? ')
        if cadastrar.lower() in ['sim', 's', 'yes', 'y']:
            cpf = input('Insira o cpf: ')
            nome = input('Insira o nome: ')
            idade = int(input('Insira a idade: '))
            sexo = input(
                'Insira o sexo [M] para masculino ou [F] para feminino: ').upper()
            renda = float(input('Insira a renda: '))
            estado = input('Insira o estado (exemplo: [PA]): ').upper()
            cadastro = Pessoa(cpf=cpf, nome=nome, idade=idade,
                              sexo=sexo, renda=renda, estado=estado)
            cadastros[cpf] = cadastro
        elif cadastrar.lower() in ['não', 'n', 'nao', 'no']:
            print(
                f'Cadastro finalizado, inserido {len(cadastros)} novos cadastros')
            continuar_cadastro = False
        else:
            print(f'Opção invalida. Foi inserido "{cadastrar}",\
escolha entre [sim, s, yes, y] para cadastrar uma nova pessoa ou [não, nao, n, no] para parar')
    return cadastros


def calcule_media_idade_por_sexo(cadastros):
    lista_idade_homens = []
    lista_idade_mulheres = []
    for pessoa in cadastros.values():
        if pessoa.sexo == 'M':
            lista_idade_homens.append(pessoa.idade)
        else:
            lista_idade_mulheres.append(pessoa.idade)
    if len(lista_idade_homens) != 0:
        media_idade_homens = sum(lista_idade_homens) / len(lista_idade_homens)
    else:
        media_idade_homens = lista_vazia
    if len(lista_idade_mulheres) != 0:
        media_idade_mulheres = sum(
            lista_idade_mulheres) / len(lista_idade_mulheres)
    else:
        media_idade_mulheres = lista_vazia
    return ((f'A media das idades dos homens é:\n{media_idade_homens}\nA media das idades das mulheres é:\n{media_idade_mulheres}\n'))


def conte_quantidade_por_sexo(cadastros):
    quantidade_homens = 0
    quantidade_mulheres = 0
    for pessoa in cadastros.values():
        if pessoa.sexo == 'M':
            quantidade_homens += 1
        else:
            quantidade_mulheres += 1
    return (f'Foi registrado um total de {quantidade_homens} homens e {quantidade_mulheres} mulheres')


def filtre_dados(cadastros, estado):
    pessoas_estado_filtrado = []
    for pessoa in cadastros.values():
        if pessoa.estado == estado.upper():
            pessoas_estado_filtrado.append(pessoa)
    return (f'Os cadastros referentes ao estado {estado} são {pessoas_estado_filtrado}')


def delete_cadastro(cadastros, cpf):
    for pessoa in cadastros.keys():
        if pessoa == cpf:
            pessoa_removida = cadastros.pop(pessoa)
            return (f'A pessoa removida foi {pessoa_removida}')


# Testando o programa
cadastros = cadastrar_usuario()
print(cadastros)
print(calcule_media_idade_por_sexo(cadastros))
print(conte_quantidade_por_sexo(cadastros))
print(filtre_dados(cadastros, estado='PA'))
print(delete_cadastro(cadastros, '01234567811'))
