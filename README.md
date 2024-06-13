# **Projeto de Web Scraping do Site da Havan**
Site: [Havan](https://www.havan.com.br/)

Objetivo: Realizar a raspagem de dados do site da Havan para extrair informações sobre produtos. Para alcançar este objetivo, utilizamos as seguintes bibliotecas:

Requests: Para realizar requisições GET ao site da Havan.
BeautifulSoup: Para manipulação e extração dos dados das estruturas HTML.
Pandas: Para criação, manipulação e visualização do DataFrame gerado a partir dos dados extraídos.
Descrição do Processo:
Requisições Web: Utilizamos a biblioteca requests para enviar requisições GET ao site da Havan. Esta etapa é crucial para obter o conteúdo HTML das páginas de busca.

Parsing HTML: Com a ajuda da biblioteca BeautifulSoup, fazemos o parsing do conteúdo HTML para localizar e extrair informações específicas dos produtos, como título, preço e link.

Estruturação dos Dados: Os dados extraídos são organizados em um DataFrame utilizando a biblioteca Pandas, facilitando assim a manipulação e análise das informações coletadas.

Benefícios do Projeto:
Automação: Automatiza a coleta de dados, economizando tempo e esforço em comparação com a coleta manual.
Atualização Dinâmica: Permite a atualização frequente dos dados dos produtos, garantindo informações sempre atualizadas.
Análise de Dados: Com os dados estruturados em um DataFrame, torna-se mais fácil realizar análises e visualizações, auxiliando na tomada de decisões informadas.

