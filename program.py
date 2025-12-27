import json
import requests
import mysql.connector

def request_api(url):
    return requests.get(url).json()

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="camara_leg_db"
    )

def add_deputados(cursor, request):
    for item in request.get('dados', []):
        cursor.execute(
            '''INSERT INTO Deputados(uri, nome, sigla_partido, email) VALUES(%s, %s, %s, %s)''',
            (item.get('uri'),
             item.get('nome'),
             item.get('siglaPartido'),
             item.get('email'))
        )

def add_partidos(cursor, request):
    for item in request.get('dados', []):
        cursor.execute(
            '''INSERT INTO Partidos(sigla, nome, uri) VALUES (%s, %s, %s)''',
            (item.get('sigla'),
             item.get('nome'),
             item.get('uri'))
        )


def add_grupos(cursor, request):
    for item in request.get('dados', []):
        cursor.execute(
            '''INSERT INTO Grupos(uri, nome, ano_criacao) VALUES (%s, %s, %s)''',
            (item.get('uri'),
             item.get('nome'),
             item.get('anoCriacao'))
        )


def add_frentes(cursor, request):
    for item in request.get('dados', []):
        cursor.execute(
            '''INSERT INTO Frentes(uri, titulo, id_legislativo) VALUES (%s, %s, %s)''',
            (item.get('uri'),
             item.get('titulo'),
             item.get('idLegislatura'))
        )

clearing_data = []

#Requisição da API - GET
url = 'https://dadosabertos.camara.leg.br/api/v2/'

options = {
    '1': 'deputados',
    '2': 'partidos',
    '3': 'grupos',
    '4': 'frentes'
}

db = connect_to_db()
cursor = db.cursor()
while True:
    print('1-depudatos \n2-partidos \n3-grupos \n4-frentes')
    option = input('Escolha uma opção: ').strip()
    path = options.get(option)

    response = request_api(url + path)

    '''Impresão do resultado'''
    print('Dados da solicitação: ')
    print(json.dumps(response, indent=4, ensure_ascii=False))

    #Salvando dados no BANDO DE DADOS
    '''Conexão com o banco de dados'''


    add_db = input('Deseja salvar os dados no banco de dados? (S/N): ').strip().lower()

    if add_db == 's':
        match path:
            case 'deputados':
                add_deputados(cursor, response)
            case 'partidos':
                add_partidos(cursor, response)
            case 'grupos':
                add_grupos(cursor, response)
            case 'frentes':
                add_frentes(cursor, response)
            case _:
                print('Opção invalida')
        db.commit()

    continue_app = input('Deseja continuar? (S/N): ').strip().lower()
    if continue_app =="n":
        break

print('Obrigado por utilizar o programa!!')

#Fechando operações e conexão
cursor.close()
db.close()
