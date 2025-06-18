from legendador import legendar
import streamlit as st

#legenda = legendar("video.mp4")

def meu_app():
    st.header("Meu Legendador", divider=True)
    st.markdown('#### Gere a legenda de qualquer vídeo ou áudio automáticamente')

    contexto = st.text_input("Dê algum contexto do que o vídeo se trata para ajudar na legenda")
    arquivo = st.file_uploader("Selecione o vídeo (.mp4) para legenda em mp4 OU O ÁDUIO (.MP3) para legendar", type=["mp4", "mp3"])
    if arquivo:
        legenda = legendar(arquivo, contexto)
        st.write(f"Arquivo {arquivo.name} legendado com sucesso")
        st.write(legenda)

if __name__ == "__main__":
    meu_app() 