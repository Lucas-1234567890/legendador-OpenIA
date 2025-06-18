from openai import OpenAI
from dotenv import load_dotenv
from pydub import AudioSegment

def legendar(arquivo_video, contexto):
    extensao_arquivo = arquivo_video.name.split(".")[1]
    audio = AudioSegment.from_file(file=arquivo_video,format=extensao_arquivo)

    audio.export("audio2.mp3", format="mp3")

    load_dotenv()

    cliente = OpenAI()

    contexto = "Esse áudio é de um anúncio da jornada Full Stack da hashtag, um conteúdo completaço sobre desenvolvimento."

    with open(r"C:\Users\Lucas\OneDrive\Arquivos diversos\Desktop\legendador\audio.mp3", "rb") as arquivo:
        transcricao = cliente.audio.transcriptions.create(
            file=arquivo,
            model="whisper-1",
            language="pt",
            response_format="srt",
            prompt=contexto)

    with open ("legenda.srt", "w", encoding='utf-8') as arquivo_legenda:
        arquivo_legenda.write(transcricao)

    return transcricao