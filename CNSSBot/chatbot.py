from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging


logging.basicConfig(level=logging.INFO)
# Creating ChatBot Instance
chatbot = ChatBot(
    'CNSSBot',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'desoler,reformulez votre question svp!',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='mongodb://localhost:27017/chatterbot-database'
) 



 # Training 



training_data_empl = open('training_data/employ_maison.txt', encoding = 'utf8').read().splitlines()
training_data_regime = open('training_data/regime_general.txt', encoding = 'utf8').read().splitlines()
training_non_salarie = open('training_data/non_salarie.txt', encoding = 'utf8').read().splitlines()

training_data =  training_data_empl + training_data_regime + training_non_salarie



trainer = ListTrainer(chatbot)
trainer.train(training_data)  




# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus'
    
) 