# importando as bibliotecas
import streamlit as st 
from pathlib import Path
from PIL import Image
import webbrowser as web

# configurações Estruturas
diretorios =Path(__file__).parent if '__file__' in locals() else Path.cwd()
arquivo_css = diretorios / "styles" / 'geral.css'
foto = diretorios / 'assets'/ 'foto.jpeg'
foto1 = diretorios / 'assets'/ 'cod.jpeg'
foto2 = diretorios / 'assets'/ 'python.jpeg'


# configurações gerais

titulo = 'Curriculum | Diogo Silveira Monteiro'

nome = 'Diogo Silveira Monteiro'

descricao = '''

Olá, seja muito bem-vindo (a) ao meu portfólio de projetos de Ciências de Dados.

Nessa página, eu demonstro minhas habilidades em resolver problemas de negócio utilizando conceitos de ferramentas da Ciência de Dados, através  de projetos com dados públicos.

Você vai encontrar também, minhas experiências  profissionais, habilidades, ferramentas e conceitos envolvendo a Ciência de Dados.

Sinta-se à vontade para entrar em contato através dos links no final da página.


'''

Email = 'diogo.monteiro99@hotmail.com'

LinkedIn = 'https://www.linkedin.com/in/diogo-s-monteiro'

Github = 'https://github.com/DiogoMonteiro99/repos'

projeto_coracao = 'https://github.com/DiogoMonteiro99/Ciencias-de-dados/blob/main/coracao.ipynb'

projeto_cancer_mama = 'https://github.com/DiogoMonteiro99/Ciencias-de-dados/blob/main/cancer_mama1.ipynb'

Sobre_mim = '''

    Meu nome é Diogo Monteiro, estou cursando graduação em Ciências de Dados, na faculdade Ampli & Anhanguera.

Trabalho com projetos pessoais de Ciências de Dados, para adquirir experiências na solução de problemas de negócio e domínio sobre as ferramentas de análise de dados.

Estou buscando uma oportunidade de trabalhar profissionalmente como Cientista de Dados para melhorar a tomada de decisão da empresa, através da construção de soluções usando dados.

'''
Habilidades = '''


**Linguagens de programação e Banco de Dados** 

* Python para análise de dados

* Web scraping com Python

* SQL para extração de dados

* Banco de Dados SQlite, Postres, Mysql.  
	
**Estatística e Machine Learning**

* Estatística descritiva (lcalização, dispersão, assimetria, kurtosis, densidade)

* Algoritmos de Regressão, Classificação, clusterização.

**Visualização de Dados**

* Matplotlib, Plotly, Seaborn.

* Power BI

**Engenharia de Software**

* git, github

* Google Cloud Platform

'''

ferramentas = '''

* Python, Pandas, Numpy, Seaborn, matplotlib, plotly

* Anaconda, vscode, Jupyter Notebook, Google Colab

* Scikit-learn, XGbooster

'''

projeto1 = '''

Identificação de doenças cardíacas através de análises de dados com Python e modelo de classificação (machine learning)

'''

projeto2 = '''

Identificação de câncer de mama através de análises de dados com Python e modelo de classificação (machine learning)

'''




st.set_page_config(
    page_title=titulo
    
)

# Carregando assets 


with open(arquivo_css) as c:
    st.markdown('<style>{}</style>'.format(c.read()), unsafe_allow_html=True)
    
imagem = Image.open(foto)
col1, col2 = st.columns(2, gap='small')
with col1:
    st.image(imagem, width=150)
    if st.button('**LinkedIn**'):
        web.open_new_tab(LinkedIn)
            
with col2:
    st.title(nome)
    if st.button('📧 **E-mail**'):
        Email
          
    # Midias socias
    if st.button('**GitHub**'):
        web.open_new_tab(Github)
        
        
    
# Saudação
st.header('Boas vindas')    
st.write(descricao)
    
# Sobre mim
st.header('Sobre mim')
st.write(Sobre_mim)
    
# Habilidades
st.header('Habilidades')
st.write(Habilidades)
    
# Experiência
st.header('Experiências')
imagem1 = Image.open(foto1)
col3, col4 = st.columns(2, gap='small')
    
with col3:
    st.image(imagem1, width=350)
    st.write('**Identificação de doenças cardíacas**')
    st.write(projeto1)
    st.write('**As ferramentas utilizadas foram:**')
    st.write(ferramentas)
    if st.button('**Projeto 1**'):
        web.open_new_tab(projeto_coracao)
imagem2 = Image.open(foto2)   
     
with col4:
    st.image(imagem2, width=350)
    st.write('**Identificação de câncer de mama**')
    st.write(projeto2)
    st.write('**As ferramentas utilizadas foram:**')
    st.write(ferramentas)
    if st.button('**Projeto 2**'):
        web.open_new_tab(projeto_cancer_mama)
        
            

    
   