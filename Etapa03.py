import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


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


def limpar(lista):
    lixo = '.,:;?!"`´^~()}{[]/\|@#$%¨&*-'
    quase_limpo = [x.strip(lixo).lower() for x in lista]
    return [x for x in quase_limpo if x.isalpha() or '-' not in x]


# Função de busca com contexto
def buscador(alvo, texto):
    texto = texto.replace('\n', ' ').replace('\t', ' ')
    
    texto_lower = texto.lower()
    alvo_lower = alvo.lower()
    
    ocorrencias = []
    encontrado_aqui = texto_lower.find(alvo_lower, 0)

    # encontrado_aqui = texto.find(alvo, 0)
    # Se encontra a palavra, informa a posição
    # Se não encontrar, informa -1
    
    while encontrado_aqui >= 0:
        pos_inicial = max(encontrado_aqui - 10, 0)
        pos_final = min(encontrado_aqui + len(alvo_lower) + 10, len(texto_lower))
        trecho = texto[pos_inicial:pos_final]
        
        ocorrencias.append(trecho)

        encontrado_aqui = texto_lower.find(alvo_lower, encontrado_aqui + 1)
        
    contagem = len(ocorrencias)
    return ocorrencias, (f"--- A palavra se repetiu {contagem} vezes. ---")
    

# --- Execução ---
texto = ler('Ubirajara.txt')

if texto is not None:
    print(f"Tamanho original: {len(texto)}")
    texto_limpo = limpar(texto)
    print(f"Tamanho após limpeza: {len(texto_limpo)}")

    palavra = 'peito'
    resultados, resumo = buscador(palavra, texto_limpo)

    for trecho in resultados:
        print(trecho)
    print(resumo)
else:
    print("Não foi possível ler o arquivo.")