# 🎥 Legendador de Vídeos e Áudios com OpenAI Whisper + Streamlit

Projeto simples e direto ao ponto: um **app web em Streamlit** que recebe um **vídeo (.mp4)** ou **áudio (.mp3)**, extrai o áudio e gera a legenda automática no formato **.srt**, usando a API da **OpenAI (Whisper)**.

---

## 🚀 Tecnologias utilizadas

- Python 🐍
- Streamlit 🌐
- OpenAI API (Whisper) 🤖
- Pydub 🎵
- dotenv 🔑

---

## 🛠️ Como funciona o fluxo:

1. Usuário faz upload de um vídeo ou áudio via interface Streamlit
2. O app extrai o áudio usando **Pydub**
3. Envia o áudio para o **Whisper da OpenAI** com um contexto (prompt)
4. Gera o arquivo `.srt` com as legendas
5. Exibe a transcrição direto na interface

---

## 📂 Estrutura básica de pastas

