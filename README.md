# Simulador de Aprendizagem de Rotas em Labirintos

## Descrição
Este projeto consiste num simulador de rotas em labirintos, onde utilizando determinados algoritmos pré-criados pelos desenvolvedores da aplicação o usuário irá conseguir procurar o caminho desde a casa final até às casas finais caso essa ou essas existam.
O projeto tem como propósito ver como diversos algoritmos utilizam as suas próprias maneiras para procurar os caminhos existentes no labirinto criado também pelo utilizador.

## Instalação
Devido a este projeto utilizar diversas dependências e o prazo final ser iminente, o projeto não inclui um executável. No entanto, abaixo é indicado o passo a passo para executar a aplicação em qualquer máquina.

### Requisitos do sistema
- Sistema Operativo: Windows, macOS, Linux
- Python 3.12.0
- Git

### Dependências
- Pygame
- Pygame_widgets
- Pygame_gui
- threading
- random
- os
- time
- typing
- math
- traceback
- platform

### Passos para a instalação
1.	Instalar o Git
    1.1.	Acesse o site oficial do Git: https://git-scm.com/
    1.2.	Clique em "Download" e siga as instruções de instalação para o seu sistema operacional (Windows, macOS ou Linux).
    1.3.	Após a instalação, abra um terminal e execute o comando git --version para verificar se o Git foi instalado corretamente.
2.	Instalar o Visual Studio Code
    2.1.	Acesse o site oficial do Visual Studio Code: https://code.visualstudio.com/
    2.2.	Clique no botão "Download" e siga as instruções de instalação para o seu sistema operacional (Windows, macOS ou Linux).
3.	Instalar o Python
    3.1.	Acesse o site oficial do Python: https://www.python.org/
    3.2.	Clique em "Downloads" e escolha a versão adequada para o seu sistema operacional.
    3.3.	Durante a instalação, certifique-se de marcar a opção "Add Python to PATH".
4.	Clonar o Repositório do GitHub
    4.1.	Abra o Visual Studio Code.
    4.2.	Pressione Ctrl + ç no Windows ou Cmd + ç no macOS, para abrir o terminal
    4.3.	Utilize o comando “cd” para se dirigir para o local onde pretende clonar o repositório
            “cd caminho/para/o/diretório/de/destino”
    4.4.	Digite o “Git clone” seguido do URL do github do projeto para clonar o mesmo para o diretório.
            “Git clone https://github.com/fjppf/ProjetoFinalMaze.git “
5.	Abrir o Projeto no Visual Studio Code
    5.1.	No Visual Studio Code, clique em "File" > "Open Folder".
    5.2.	Navegue até à pasta onde o repositório foi clonado e selecione-a.
    5.3.	O Visual Studio Code irá abrir a pasta do projeto.
6.	Instalar as Dependências do Projeto
    6.1.	Abra um terminal integrado no Visual Studio Code (pressione Crtl + ç ou Cmd + ç)
    6.2.	Certifique-se de que o terminal está na raiz do projeto (onde está localizado o arquivo requirements.txt).
    6.3.	Execute o seguinte comando para instalar as bibliotecas necessárias:
            “pip install -r requirements.txt”
            Este comando irá ler o arquivo requirements.txt e instalar todas as dependências listadas.
7.	Executar a Aplicação
    7.1.	Por fim, pode agora fazer duplo clique no ficheiro main.py e, em seguida, clicar duas vezes na seta que aparece no canto superior direito do Visual Studio Code.

Seguindo estes passos, conseguirás instalar e executar qualquer projeto localizado no GitHub. Se encontrares problemas, consulta a documentação do projeto ou os arquivos README.md fornecidos pelo autor do repositório.
   

## Uso
Para o utilizador conseguir visualizar e realizar todos os propósitos pretendidos por este projeto, a aplicação contém várias funcionalidades. As funcionalidades mais importantes são as que foram chamadas de gerais e estas são: Inserir linhas e colunas, Criar, Resolver, Apagar e Salvar. 

Insert Rows and columns- Esta funcionalidade permite que o utilizador insira o número que pretende de linhas e colunas para posteriormente a funcionalidade criar, utilize estes valores numéricos passados pelo utilizador para realizar a sua função. Estes valores são passados de forma interativa, ou seja, o utilizador tem dois elementos visuais no ecrã devidamente etiquetados onde este sabe qual valor é para colocar em cada um.

Create- Esta permite que o utilizador crie um labirinto no ecrã da aplicação, com os valores passados pela funcionalidade “Inserir linhas e colunas”. Esta funcionalidade verifica também esses valores inseridos, pois consoante o tamanho do utilizador o valor máximo permitido de linhas e colunas pode variar.

Solve- O utilizador tem também acesso à funcionalidade “Resolver” que permite que o mesmo, como o próprio nome indica, resolva o labirinto que criou anteriormente. O meio de resolução do labirinto altera consoante o tamanho do mesmo.

Clear- O utilizador pode também decidir apagar o labirinto que criou a qualquer momento incluindo enquanto um algoritmo se encontra a resolver o mesmo.

Save- Para uma futura análise ou meramente por o utilizador quiser guardar, o mesmo tem então à sua disposição a funcionalidade “Guardar”.

Existem ainda outras funcionalidades, nomeadamente funcionalidades visuais e algorítmicas. As funcionalidades visuais têm como objetivo permitir que o utilizador personalize a aplicação ao seu gosto, e consistem em duas funcionalidades específicas.

Pick color walls- Esta funcionalidade permite, através de uma janela secundária que se abre ao clicar no botão com o texto "Pick color" ao lado do texto "Walls color:", escolher a cor desejada para as paredes do labirinto.

Pick color backgorund- Esta funcionalidade, à semelhança da anterior, permite que o utilizador selecione uma cor, mas desta vez para o fundo do labirinto em vez de para as paredes.

Por último, existem as funcionalidades algorítmicas, que são as que permitem ao utilizador escolher qual o algoritmo com que pretendem resolver o labirinto que acabaram de criar.

Flood Fill- Esta funcionalidade é precisamente o algoritmo de procura Flood Fill. Este algoritmo resolve o labirinto explorando em profundidade, utilizando backtracking para percorrer todas as casas (células) existentes. No final, encontra o melhor caminho possível, caso exista, com base no custo de cada célula.

Breadth- Este explora todo o labirinto em largura até encontrar a(s) casa(s) final(is), caso existam. Devido a esta exploração em largura, garante sempre que encontra o menor caminho possível entre a casa inicial e a casa final, se existir uma casa final.

Depth- Esta funcionalidade permite que o utilizador explore todo o labirinto em profundidade até encontrar a(s) casa(s) final(is). Utiliza backtracking nos casos em que encontra um beco sem saída, retrocedendo para a última interseção disponível até encontrar uma que ainda tenha vizinhos não visitados.

A* Search- Esta funcionalidade utiliza precisamente o algoritmo “A* Search” para explorar todo o labirinto de forma a encontrar o caminho mais curto entre a casa inicial e a(s) casa(s) final(is), caso existam. Para isto este utiliza uma função heurística para avaliar o custo total do caminho.

## Exemplo de utilização
1.	Iniciar a aplicação seguindo os passos descritos na instalação.
2.	Inserir o número desejado de colunas e linhas.
3.	Escolher as cores para as paredes e fundo do labirinto clicando em ambos os botões "Escolher cor", um de cada vez.
4.	Clicar no botão "Criar" para gerar um labirinto com o número de colunas e linhas especificado anteriormente.
5.	Clicar no botão "Resolver" para encontrar a solução para o labirinto.
6.	Clicar no botão "Guardar" para salvar uma imagem do labirinto na pasta "Imagens" do computador.
7.	Clicar no botão "Limpar" para apagar o labirinto e poder criar outro.

## Licença
Este projeto foi desenvolvido como parte de um projeto escolar e não está licenciado para uso ou distribuição pública. Para qualquer dúvida ou pedido de utilização, por favor, entre em contacto com o autor ou a instituição responsável.

## Créditos
Este projeto não teria sido possível sem a colaboração e o apoio de várias pessoas. Gostaríamos de agradecer a todos os que contribuíram para o seu sucesso: 

### Equipa de Desenvolvimento 
- **Diogo Almeida** 
- **Guilherme Botelho** 
- **Francisco Furtado** 
- **Francisco Furtado** 

### Agradecimentos Especiais 
- **Professor Doutor Adrian-Horia Dediu** - Orientação e apoio ao longo do projeto 
- **Colegas da Turma** - Feedback e sugestões valiosas 

A todos, os nossos sinceros agradecimentos pelos contributos e dedicação.

# Contactos
Devido a este projeto ter sido realizado com fins escolares, não disponibilizamos contactos para futuras dúvidas ou pedidos.


