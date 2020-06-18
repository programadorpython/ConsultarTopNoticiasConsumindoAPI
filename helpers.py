import requests
from config import CHAVE_API, URL_BASE_TOP_HEADLINES


def top_noticias(pais):
    """
    Retorna as top noticias do site newsapi.org
    :param pais: inserir o país para pesquisar as noticias
    :return: Lista de noticias do país
    """
    url = f"{URL_BASE_TOP_HEADLINES}country={pais}&apiKey={CHAVE_API}"

    # Coletando dados em formato json
    resposta = requests.get(url).json()
    # print(resposta)

    # Pegando todos os artigos
    artigos = resposta['articles']
    # print(artigos)

    # Lista vazia para preencher com noticias
    noticias = []

    for artigo in artigos:
        noticias.append(f"{artigo['title']}, "
                        f"Imagem: {artigo['urlToImage']}, "
                        f"Publicado em: {artigo['publishedAt']}")

    # print(noticias)
    return noticias
