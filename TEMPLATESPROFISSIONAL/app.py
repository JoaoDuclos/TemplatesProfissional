import streamlit as st

# Título principal
st.title("""GABRIEL BRAMONT""")
st.image("image/logo.png", caption="Logo", use_column_width=True)
# Sidebar com botões estilizados
st.sidebar.title("Navegação")

# Criando os botões na sidebar
col1, col2 = st.sidebar.columns([2, 1])  # Colunas para centralizar os botões

with col1:
    btn_sobre = st.button("Sobre Mim")
    btn_habilidades = st.button("Habilidades")
    btn_projetos = st.button("Projetos")
    btn_contato = st.button("Contato")
    btn_redes = st.button("Redes Sociais")
    btn_cv = st.button("Baixar CV")

# Seção "Sobre Mim"
if btn_sobre:
    st.header("Sobre Mim")
    st.write("""
    Sou programador e analista de dados na TIM. Tenho experiência em automação de processos, desenvolvimento de sistemas, e atualmente estou desenvolvendo um projeto chamado DataShowcase.
    """)

# Seção "Habilidades"
elif btn_habilidades:
    st.header("Habilidades")
    st.write("""
    - **Linguagens de Programação**: Python, SQL, JavaScript
    - **Ferramentas**: Streamlit, Power BI, Excel
    - **Inteligência Artificial**: Modelos de machine learning
    - **Desenvolvimento de Sistemas**: Automação de processos e visualização de dados
    """)

# Seção "Projetos"
elif btn_projetos:
    st.header("Projetos")
    st.write("""
    1. **DataShowcase**: Plataforma para apresentação de projetos de forma interativa.
    2. **Analisador Léxico**: Parte de uma tarefa acadêmica para a disciplina de Compiladores.
    """)

# Seção "Contato"
elif btn_contato:
    st.header("Contato")
    st.write("""
    - **Email**: joaovitorborge@gmail.com
    - **Telefone**: +55 21 99315-4480
    """)

# Seção "Redes Sociais"
elif btn_redes:
    st.header("Redes Sociais")
    st.write("[LinkedIn](https://www.linkedin.com)")
    st.write("[GitHub](https://github.com)")

# Seção "Baixar CV"
elif btn_cv:
    st.header("Baixar CV")
    with open("meu_cv.pdf", "rb") as file:
        btn = st.download_button(label="Baixar CV", data=file, file_name="meu_cv.pdf", mime="application/pdf")
