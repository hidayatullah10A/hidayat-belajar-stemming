import ntlk
from ntlk.steam import PorterSteamer 
porter = PorterSteamer()

tokens = ['stream','streaming','streamed']

for token in tokens:
    print(token + " : " + porter.stem(token))
study : stream
studying : stream
studies : stream

#Author : Hidayat
#Belajar Stemming & Lemmatization dengan Python dan NLTK