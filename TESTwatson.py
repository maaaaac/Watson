
from Listen1.Listen1 import rec
from Hear2.Hear2 import hear
from chatbot3.interact_mmi import chatbotprep, chatbotmain
from pinYin4.pinYin4 import pinpin
from speak5.eval import audio
from playsound import playsound
rec()
hear()
chatbotprep()
chatbotmain()
pinpin()
audio()
playsound('speak5/logs-tacotron/eval-100000-000.wav')