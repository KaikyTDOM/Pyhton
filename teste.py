import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('QUESTIONÁRIO SOCIOECONÔMICO 1.csv', usecols=(8, 9, 10))
dados_df = pd.DataFrame(dados)
# dia = dados_df['7. Agora vamos falar sobre sua idade:\nEm qual dia você nasceu?']
# mes = dados_df['7-1. Em qual mês você nasceu?']
# ano = dados_df['7-2. Em qual ano você nasceu?']
dados_df['Data de nascimento'] = ""
linha = 0

for valor in dados_df.values:
    if valor[1] == 'Janeiro':
        valor[1] = 1
    elif valor[1] == 'Fevereiro':
        valor[1] = 2
    elif valor[1] == 'Março':
        valor[1] = 3
    elif valor[1] == 'Abril':
        valor[1] = 4
    elif valor[1] == 'Maio':
        valor[1] = 5
    elif valor[1] == 'Junho':
        valor[1] = 6
    elif valor[1] == 'Julho':
        valor[1] = 7
    elif valor[1] == 'Agosto':
        valor[1] = 8
    elif valor[1] == 'Setembro':
        valor[1] = 9
    elif valor[1] == 'Outubro':
        valor[1] = 10
    elif valor[1] == 'Novembro':
        valor[1] = 11
    elif valor[1] == 'Dezembro':
        valor[1] = 12

    dados_df.loc[linha, 'Data de nascimento'] = f'{valor[0]}/{valor[1]}/{valor[2]}'
    linha += 1


print(dados_df['Data de nascimento'])
data = dados_df['Data de nascimento']

plt.pie(data.index)
plt.legend(data)
plt.show()


