import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import DataPreprocessingHapd as Dp
Max_Number_of_words = 200
vocab_size = 400
x = []
y = []
Train_Path = '/home/mohammed/Downloads/Train.csv'
Data =['my name is mohammed morse' , 'okay no problem']
def ConvertRowToListOfNumbers(Quections, Answers):
# Create a word index "cat": unique num
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(Quections)
    tokenizer.fit_on_texts(Answers)

#then convert all text to list of Num
    QuectionsEncoded = tokenizer.texts_to_sequences(Quections)
    AnswersEncoded = tokenizer.texts_to_sequences(Answers)

#convert
    QuectionsEncoded = pad_sequences(QuectionsEncoded , maxlen=Max_Number_of_words)
    AnswersEncoded =pad_sequences(AnswersEncoded , maxlen= Max_Number_of_words ,padding='post')

    return QuectionsEncoded , AnswersEncoded , tokenizer.word_index

x , y =Dp.DataPreprocessing(Train_Path , x,y)
Questions , Answers ,Vocab= ConvertRowToListOfNumbers(x , y )
print (Questions)
print (Answers)
print (Vocab)
