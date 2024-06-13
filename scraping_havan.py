# Importando as bibliotecas necessárias

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Criando a classe para realizar o scraping no site da Havan
class Requesthavan:

    
    def execute_command(self, query): 
        
        url = f"https://www.havan.com.br/catalogsearch/result/?q={query}"  #montando a url passando a query que usaremos para pesquisar.
        
        # Definindo os cabeçalhos para a requisição HTTP, simulando um navegador Chrome para evitar bloqueios por parte do site
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        }

        
        response = requests.get(url, headers=headers)  #fazendo a requesição GET para poder buscar algo o site passando a url e o headers.

        
        if response.status_code == 200:
            print(f"Status code: {response.status_code} - Query: {query}")
            
            # Obtém o conteúdo HTML da resposta
            html = response.text
            
            soup = BeautifulSoup(html, "html.parser")   # parseando a estrutura html com beatifulsoap para melhor manipulação.

            
            results = soup.find_all("li", class_="item product product-item")  #definindo uma tag inicial

            
            if results:
                print(f"Found {len(results)} products for '{query}'.")
            else:
                print(f"No products found for '{query}'.")

            data = []  # criando um objeto vazio para colocar os dados extraídos posteriormente.

            
            for i, result in enumerate(results):
                title = "No title"
                price = "No price"
                link = "No link"

                
                title_tag = result.find("a", class_="product-item-link")  # Encontrando o título do produto
                if title_tag:
                    title = title_tag.text.strip()
                    print(f"Product {i+1}: Title found - {title}")
                else:
                    print(f"Product {i+1}: Title not found")

                
                price_tag = result.find("div", class_="price-box price-final_price") # Encontrando o preço do produto
                if price_tag:
                    price_span = price_tag.find("span", class_="price-container price-final_price tax weee")
                    if price_span:
                        price = price_span.text.strip()
                        print(f"Product {i+1}: Price found - {price}")
                    else:
                        print(f"Product {i+1}: Price span not found")
                else:
                    print(f"Product {i+1}: Price tag not found")

                
                link_tag = result.find("a", class_="product-item-link")  # Obtendo o link do produto
                if link_tag:
                    link = link_tag.get("href")
                    print(f"Product {i+1}: Link found - {link}")
                else:
                    print(f"Product {i+1}: Link not found")

                # inserindo os dados extraídos na variável data
                data.append({"Produto": title, "Preco": price, "URL": link})

            return data
        else:
            
            print(f"Failed to retrieve data from URL: {url}")
            return None

    # Método para transformar a lista de dados em um DataFrame
    def transform_df(self, queries):
        all_data = []

        # Itera sobre cada query de busca fornecida
        for query in queries:
            data = self.execute_command(query)
            if data:
                all_data.extend(data)  # Adiciona os dados da consulta atual à lista geral

        # Verifica se algum dado foi coletado e cria o DataFrame
        if all_data:
            df = pd.DataFrame(all_data)
            return df
        else:
            print("No data retrieved.")
            return None

# Cria uma instância da classe e realiza a busca para múltiplas queries
crawler = Requesthavan()
dataframe = crawler.transform_df(["blusa", "short", "meia", "calça", "vestido", "body"])


if dataframe is not None:
    print(dataframe)
else:
    print("No data retrieved or error occurred.")



