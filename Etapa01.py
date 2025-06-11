# criar uma função para fazer a abertura e leitura do arquivo
def ler(Ubirajara):
    try:
        with open(Ubirajara, 'r', encoding='utf-8') as arquivo:
            conteudo_arq = arquivo.read()
            return conteudo_arq
    except FileNotFoundError:
        print(f"Erro: O arquivo '{Ubirajara}' não foi encontrado.")
        return None
    except PermissionError:
        print(f"Erro: Permissão negada para acessar o arquivo '{Ubirajara}'.")
        return None
    except Exception as e:
        print(f"Erro inesperado ao abrir o arquivo: {e}")
        return None

"""
# Caminho Absoluto
# Uma Versão mais complexa, porém facilita no acerto do arquivo.
# Pois escpecifica o local definitivo.
texto = ler('C:\\Users\\glima\\Documents\\Faculdade\\Codigo - quarta\\04.06\\Ubirajara.txt')
print(len(texto))
"""


# Caminho Relativo
# Essa maneira é mais prática e sucinta.
# Mas é necessário manter o arquivo lido e o arquivo de código na mesma pasta.
texto = ler('Ubirajara.txt')

if texto is not None:
    print(len(texto))
else:
    print("Não foi possível ler o arquivo.")
