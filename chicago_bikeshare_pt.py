#!/usr/bin/env python3
# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt
import statistics

#Quantidades de linhas iniciais para ler do arquivo
INICIAL_LINES = 20

#Constantes criadas para definir o índice das colunas
COLUMN_START_TIME,COLUMN_END_TIME,COLUMN_TRIP_DURATION,COLUMN_START_STATION,COLUMN_END_STATION,COLUMN_USER_TYPE,COLUMN_GENDER,COLUMN_BITH_YEAR = range(0,8)

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
if len(data_list) >= INICIAL_LINES+1: #somando cabeçalho
    for x in range(1, INICIAL_LINES+1, 1):
        # print(data_set.readline())
        print(data_list[x])
else:
    print("O arquivo possui menos de 20 linhas!")
    for data in data_list:
        print(data)

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for x in range(INICIAL_LINES):
    print(data_list[x][COLUMN_GENDER])

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data: list, index: int) -> list:
    """
    Função utilizada para adicionar uma coluna dos dados em uma lista
    Argumentos:
        data: Lista de dados condensada
        index: Índice da coluna alvo
    Retorna:
        Lista contendo os dados da coluna alvo
    """
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for db in data:
        column_list.append(db[index])
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# Conte cada gênero. Você não deveria usar uma função para isso.
gender = []
gender = column_to_list(data_list, -2)
male = gender.count("Male")
female = gender.count("Female")

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list: list) -> list:
    gender = []
    gender = column_to_list(data_list, -2)
    male = gender.count("Male")
    female = gender.count("Female")
    return [male, female]

print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list: list) -> str:
    gender = []
    answer = ""
    gender = column_to_list(data_list, -2)
    try:
        answer = statistics.mode(gender)
    except:
        answer = "Equal"
    finally:
        return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
def count_types(db_set: set, idx: int) -> list:
    """
    Função utilizada para contar a quantidade de qualquer tipo de dados em data_list
    Argumentos:
        db_set: set com os dados do eixo X
        index: Índice da coluna alvo
    Retorna:
        Lista contendo a quantidade de cada chave dentro do data_set
    """
    types = []
    total = []
    types = column_to_list(data_list, idx)
    for db in db_set:
        total.append(types.count(db))
    return total

print("\nTAREFA 7: Verifique o gráfico!")
user_type_list = column_to_list(data_list, COLUMN_USER_TYPE)
types = set(user_type_list)
quantity = count_types(types, COLUMN_USER_TYPE)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipos')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Existem dados que não foram preenchidos na coluna em questão.\n \
A comparação não leva em conta os dados em branco e por isto retorna falso."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
def maximum(trip_data: list) -> float:
    """
    Função utilizada para localizar o valor máximo da lista
    Argumentos:
        trip_data: Lista contendo os dados de duração da viagem
    Retorna:
        Float contendo o valor máximo encontrado.
    """
    maximum_value = trip_data[0]
    for data in trip_data:
        maximum_value = data if data > maximum_value else maximum_value
    return maximum_value

def minimum(trip_data: list) -> float:
    """
    Função utilizada para localizar o valor mínimo da lista
    Argumentos:
        trip_data: Lista contendo os dados de duração da viagem
    Retorna:
        Float contendo o valor mínimo encontrado.
    """
    minimum_value = trip_data[0]
    for data in trip_data:
        minimum_value = data if data < minimum_value else minimum_value
    return minimum_value

def media(trip_data: list) -> float:
    """
    Função utilizada para calcular a média.
    Argumentos:
        trip_data: Lista contendo os dados de duração da viagem
    Retorna:
        Um float contendo a média ou 0 caso tente dividir por 0.
    """
    if len(trip_data) != 0:
        medium_value = 0.
        for data in trip_data:
            medium_value += data
        return medium_value / len(trip_data)
    else:
        print("Não é possível dividir por zero")
        return 0

def median(trip_data: list) -> int:
    """
    Função utilizada para calcular a mediana.
    Argumentos:
        trip_data: Lista contendo os dados de duração da viagem
    Retorna:
        Um inteiro contendo a mediana.
    """
    n = len(trip_data)
    trip_data.sort()
    if n % 2 == 0:
        high_med = int(n/2)
        low_med = int((n-1)/2)
        median = (trip_data[low_med]+trip_data[high_med])/2.
    else:
        index = int(n/2)
        median = trip_data[index]
    return median

trip_duration_list = column_to_list(data_list, COLUMN_TRIP_DURATION)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.
# Lista para guardar os valores que não são brancos
float_trip = []
for trip in trip_duration_list:
    if trip:
        float_trip.append(float(trip))
#calcula máxmo e mínimo utilizando funções criadas
min_trip = minimum(float_trip)
max_trip = maximum(float_trip)
mean_trip = media(float_trip)
median_trip = median(float_trip)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list, COLUMN_START_STATION))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
#      """
#      Função de exemplo com anotações.
#      Argumentos:
#          param1: O primeiro parâmetro.
#          param2: O segundo parâmetro.
#      Retorna:
#          Uma lista de valores x.
#
#      """

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list: list):
    """
    Função utilizada para verificar quantidade de itens e ocorrências dos mesmos
    Argumentos:
        column_list: Lista contendo os dados para verificação
    Retorna:
        Uma lista contendo a quantidade de tipos e outra lista contendo a quantidade
        de cada item
    """
    item_types = set(column_list)
    count_items = []
    total = []
    for db in item_types:
        total.append(column_list.count(db))
    count_items = total
    return item_types, count_items

if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------