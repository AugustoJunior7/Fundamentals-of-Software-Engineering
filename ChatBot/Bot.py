from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from Conversa import getConversa

bot = ChatBot('Bot')

conversa = getConversa()

bot.set_trainer(ListTrainer)
bot.train(conversa)

while True:
    entrada = input('Você: ')
    resposta = bot.get_response(entrada)
    print('Bot: ', resposta)
