import streamlit as st

st.sidebar.header('Trabalho de Desenvolvimento Rapido em Python (Streamlit)')

opcao = st.sidebar.selectbox('Sobre o Streamlit',
                             ('Historia Do Streamlit', 'Funcionalidades Do Streamlit',
                              'Projeto Streamlit')
                             )
def open_sidebar():
    js = """
    <script>
    document.getElementsByClassName('sidebar-container')[0].style = 'display: block'
    </script>
    """
    st.markdown(js, unsafe_allow_html=True)

# Chamando a função para abrir a barra lateral
open_sidebar()
st.sidebar.text('Alunos:\n'
                'Daniel\n'
                'Henrique\n'
                'Arthur\n'
                'Gabriel')
if opcao == 'Historia Do Streamlit':
    st.header('Streamlit Historia')
    st.write('''
    
    Streamlit é uma plataforma de código aberto que permite aos desenvolvedores
    criar aplicativos da web interativos para análise de dados e machine learning 
    com Python de uma maneira rápida e fácil. A história do Streamlit começa com 
    o desejo de simplificar o processo de criação de aplicativos da web para análise
    de dados e machine learning.
    
    Os fundadores do Streamlit, Adrien Treuille, Thiago Teixeira e Amanda Kelly, 
    eram pesquisadores e engenheiros de software que frequentemente se deparavam com 
    a necessidade de criar interfaces de usuário para suas análises e experimentos. 
    Eles perceberam que o processo de desenvolvimento dessas interfaces era muitas vezes 
    demorado e complexo, exigindo habilidades de programação em várias tecnologias diferentes.
    
    Com o objetivo de simplificar esse processo, os fundadores começaram a desenvolver o Streamlit em 2018.
    A ideia por trás do Streamlit era fornecer aos usuários uma maneira simples e direta de transformar scripts
    Python em aplicativos da web interativos. Eles queriam criar uma ferramenta que permitisse aos desenvolvedores
    se concentrarem no desenvolvimento do modelo e na análise de dados, em vez de se preocuparem com a complexidade 
    da criação da interface do usuário
    
    Ao longo do tempo, o Streamlit ganhou popularidade na comunidade de ciência de dados e machine learning devido
    à sua facilidade de uso e flexibilidade. Os desenvolvedores apreciaram a capacidade do Streamlit de permitir 
    a criação rápida de aplicativos interativos com apenas algumas linhas de código Python.
    O Streamlit continua a evoluir, com atualizações frequentes e uma comunidade ativa de desenvolvedores contribuindo
    para o seu desenvolvimento. A plataforma agora suporta uma ampla gama de recursos, incluindo widgets interativos,
    visualizações de dados, suporte a múltiplas páginas, integração com bibliotecas populares de machine learning,
    entre outros.
    
    Em resumo, o Streamlit é uma ferramenta poderosa que torna a criação de aplicativos da web para análise de dados
    e machine learning acessível a uma ampla gama de usuários, desde iniciantes até profissionais experientes. 
    Sua história é uma história de simplificação e democratização do desenvolvimento de aplicativos da web para 
    ciência de dados e machine learning.''')

elif opcao == 'Funcionalidades Do Streamlit':
    st.markdown(''' # Funcionalidades Do Streamlit
O Streamlit oferece uma variedade de funcionalidades que o tornam uma ferramenta poderosa para criar aplicativos 
da web interativos em Python. Aqui estão algumas das principais funcionalidades:

1. **Simplicidade de uso**: O Streamlit foi projetado para ser simples e intuitivo. 
Com apenas algumas linhas de código Python, você pode criar rapidamente um aplicativo da web interativo.
    
2. **Widgets interativos**: O Streamlit fornece uma variedade de widgets interativos que podem s
er facilmente adicionados ao seu aplicativo. Isso inclui botões, caixas de seleção, controles deslizantes, 
campos de texto e muito mais. Esses widgets permitem que os usuários interajam com o aplicativo e ajustem 
os parâmetros em tempo real.
    
3. **Visualizações de dados**: Você pode facilmente integrar visualizações de dados em seu aplicativo 
usando bibliotecas populares como Matplotlib, Plotly e Altair. O Streamlit permite exibir gráficos, mapas,
 tabelas e outros tipos de visualizações de forma interativa.
    
4. **Suporte a múltiplas páginas**: Com o Streamlit, você pode criar aplicativos de 
várias páginas com facilidade. Isso permite organizar seu aplicativo em seções distintas e 
navegar entre elas de forma intuitiva.
    
5. **Integração com bibliotecas de machine learning**: O Streamlit se integra 
perfeitamente a bibliotecas populares de machine learning, como TensorFlow, PyTorch e Scikit-learn.
 Isso permite que você crie aplicativos interativos para treinar modelos, fazer previsões e visualizar resultados.
    
6. **Personalização avançada**: Embora o Streamlit seja fácil de usar para iniciantes, também oferece opções
 avançadas de personalização para usuários mais experientes. Você pode personalizar a aparência do seu aplicativo, 
 criar layouts complexos e adicionar funcionalidades avançadas usando o Python puro.
    
7. **Implantação simplificada**: O Streamlit facilita a implantação de seus aplicativos da web em uma variedade 
de plataformas, incluindo serviços de hospedagem em nuvem como Heroku, AWS e Azure. Você pode implantar seu aplicativo 
com apenas alguns comandos, sem a necessidade de configurar servidores ou infraestrutura complexa.
    

Essas são apenas algumas das funcionalidades principais do Streamlit. No geral, o Streamlit é uma 
ferramenta versátil e poderosa que simplifica o processo de criação de aplicativos da web interativos para análise de 
dados e machine learning''')
elif opcao == 'Projeto Streamlit':
    st.markdown('''# Projeto Streamlit
**Contexto do Projeto:** Imagine que você é um entusiasta de finanças pessoais e deseja criar um aplicativo
     da web para analisar e visualizar seus gastos mensais. Você coletou dados sobre seus gastos ao longo de vários 
     meses e agora deseja criar uma ferramenta interativa para entender melhor seus hábitos de gastos e identificar 
     áreas onde você pode economizar.

**Funcionalidades Principais:**

1. **Importação de Dados:** A primeira funcionalidade do seu aplicativo será importar os dados de gastos mensais. Você 
pode usar o Streamlit para criar uma interface simples onde o usuário possa fazer upload de um arquivo CSV contendo os
 dados.
    
2. **Visualizações de Dados:** Com os dados importados, você pode criar visualizações interativas para ajudar
 a entender os padrões de gastos ao longo do tempo. Isso pode incluir gráficos de linhas mostrando a variação dos 
 gastos mês a mês, gráficos de pizza mostrando a distribuição de gastos por categoria e histogramas mostrando os gastos 
 em diferentes faixas de valores.
    
3. **Análise Descritiva:** Além das visualizações, você pode incluir funcionalidades de 
análise descritiva para fornecer insights sobre os dados. Isso pode incluir estatísticas básicas como média 
de gastos mensais, gasto total ao longo do período de tempo, categorias de gastos mais comuns e variações sazonais
 nos gastos.
    
4. **Comparação de Períodos:** Uma funcionalidade útil seria a capacidade de comparar os gastos 
de diferentes períodos de tempo. Por exemplo, você pode permitir que o usuário selecione dois meses 
diferentes e compare seus gastos lado a lado para identificar tendências e mudanças ao longo do tempo.
    
5. **Recomendações de Economia:** Com base na análise dos dados, você pode incluir recomendações personalizadas 
para ajudar o usuário a economizar dinheiro. Isso pode incluir sugestões de redução de gastos em categorias específicas, 
insights sobre onde os gastos podem estar excessivos e dicas para criar um orçamento mais eficaz.
    
6. **Interação do Usuário:** Por fim, todas essas funcionalidades devem ser apresentadas de forma 
interativa e intuitiva para o usuário. Você pode usar widgets interativos do Streamlit, como botões, caixas 
de seleção e controles deslizantes, para permitir que o usuário personalize a análise de acordo com suas necessidades 
e interesses.
    

**Conclusão:**

O projeto de análise de dados de finanças pessoais é um exemplo prático de como o Streamlit pode ser usado para 
criar aplicativos da web interativos para análise de dados. Com suas funcionalidades de importação de dados, 
visualizações interativas, análise descritiva e interação do usuário, você pode criar uma ferramenta poderosa para 
ajudar as pessoasa entenderem e controlarem melhor seus hábitos de gastos.''')
