import streamlit as st

# Título
st.title("Perfil Profissional - João Vitor Borge Duclos")

# Seção Sobre Mim
st.header("Sobre Mim")
st.write("""
Sou programador e analista de dados na TIM. Tenho experiência em automação de processos, desenvolvimento de sistemas, e atualmente estou desenvolvendo um projeto chamado DataShowcase.
""")

# Seção Habilidades
st.header("Habilidades")
st.write("""
- **Linguagens de Programação**: Python, SQL, JavaScript
- **Ferramentas**: Streamlit, Power BI, Excel
- **Inteligência Artificial**: Modelos de machine learning
- **Desenvolvimento de Sistemas**: Automação de processos e visualização de dados
""")

# Seção Projetos
st.header("Projetos")
st.write("""
1. **DataShowcase**: Plataforma para apresentação de projetos de forma interativa.
2. **Analisador Léxico**: Parte de uma tarefa acadêmica para a disciplina de Compiladores.
""")

# Seção Contato
st.header("Contato")
st.write("""
- **Email**: joaovitorborge@gmail.com
- **Telefone**: +55 21 99315-4480
- [LinkedIn](https://www.linkedin.com)
""")

# Seção Redes Sociais
st.header("Redes Sociais")
st.write("Siga-me nas redes sociais:")
st.write("[LinkedIn](https://www.linkedin.com)")
st.write("[GitHub](https://github.com)")

# Seção Download do CV
with open("meu_cv.pdf", "rb") as file:
    btn = st.download_button(label="Baixar CV", data=file, file_name="meu_cv.pdf", mime="application/pdf")