from aip import AipSpeech

APP_ID = '21319620'
API_KEY = 'bVEqHCkKAq0a2f3yTPo01Iog'
SECRET_KEY = 'Orem1tImgkVqAlLBrGockguSEdGNSiaD'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def hear():
    path = '/Users/Mac/.pyenv/versions/3.6.11/envs/finale/Listen1/recording.wav'
    with open(path, 'rb') as f:
        audio_data = f.read()

    result = client.asr(audio_data, 'wav', 16000, {
        'dev_pid': 1537,
    })

    result_text = result["result"][0]
    f = open('hear.txt', 'w')
    f.write(result_text)
    print(result_text)
    f.close()

    return result_text

hear()