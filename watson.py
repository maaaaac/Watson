from Listen1.Listen1 import rec
from Hear2.Hear2 import hear
from chatbot3 import chatbotprep, chatbotmain
from wav6.synthesis import wavsynthesis
from playsound import playsound

#为chatbot的启用作准备（目前看来不需要放在循环内）
chatbotprep()


while True:
    try:
        rec()
        hear()
        chatbotmain()
        wavsynthesis()
        playsound('wav6/output/mel-batch_26_sentence_0.wav')
    except KeyboardInterrupt:
        if args.save_samples_path:
                samples_file.close()
        break
