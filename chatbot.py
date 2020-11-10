from chatterbot import ChatBot, response_selection, comparisons
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from pytz import UTC

# Creating ChatBot Instance
chatbot = ChatBot(
    'Samantha',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        #'chatterbot.logic.TimeLogicAdapter', de aqui viene el current time
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Wey no te entiendo jejeje, ando aprendiendo no manches.',
            'maximum_similarity_threshold': 0.90
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'Help me!',
            'output_text': 'Ok, No te preocupes, cuentame qué te sucede'
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'Chao',
            'output_text': 'Puedes cerrar este chat cuando desees'
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

 # Training with Personal Ques & Ans 
#training_data_quesans = open('training_data/ques_ans.txt').read().splitlines()
training_data_personal = open('training_data/personal_ques.txt', encoding="utf8").read().splitlines()
training_data_bot = open('training_data/bot.txt', encoding="utf8").read().splitlines()
training_data_emociones = open('training_data/emociones.txt', encoding="utf8").read().splitlines()
training_data_saludos = open('training_data/saludos.txt', encoding="utf8").read().splitlines()
training_data_trivia = open('training_data/trivia.txt', encoding="utf8").read().splitlines()
training_data_trivia = open('training_data/psico2.txt', encoding="utf8").read().splitlines()
training_data_trivia = open('training_data/psico3.txt', encoding="utf8").read().splitlines()

#Entrenamiento
training_data = training_data_personal + training_data_bot + training_data_emociones + training_data_saludos + training_data_trivia
#####

trainer = ListTrainer(chatbot)
for i in range(0,10):
    trainer.train(training_data)  

# Training with English Corpus Data 
'''trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english.psychology'
) '''