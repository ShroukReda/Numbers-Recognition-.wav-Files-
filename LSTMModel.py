from bokeh.core.property.validation import validate
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, Embedding, Dropout, TimeDistributed
from keras.layers import LSTM
#-----------------------------------Import my classes------------------------------
import DataPreprocessingHapd as dp
import LstmWordEmbeddingGenerator as we
#----------------------------------------------------------------------------------
test_path = '/home/mohammed/Downloads/Test.csv'
Max_Number_of_words = 256
Num_Of_Hidden_LayersOrOutDim = 200
patch_size=30
Vocab_Size= 5000
num_epochs = 150
train_path = '/home/mohammed/Downloads/Train.csv'
Quections =[]
QuectionsTest =[]
AnswersTest =[]
Answers=[]
WordToVectorWordEmbeddingSize = 32
def PrepareModel(NumOfHiddenLayers ):
    model = Sequential()
    #There is Embedding Layer
    #                   Vocab Size  ,  Length of one Word WE    ,   max length of sentance
    model.add(Embedding( Vocab_Size,WordToVectorWordEmbeddingSize,input_length=we.Max_Number_of_words ))
    model.add(LSTM(NumOfHiddenLayers ))
    #model.add(LSTM(NumOfHiddenLayers))
    model.add(Activation('softmax'))
    return model
def RunModel (model , Quections_data , Answers_Data  ,TestQuections , TestAnswers):
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['categorical_accuracy'])
        print (model.summary())
        model.fit(Quections_data, Answers_Data,validation_data=(TestQuections , TestAnswers), epochs=num_epochs, batch_size=10)
        return model


Quections , Answers = dp.DataPreprocessing(train_path,Quections , Answers)
QuectionsEncoded , AnswersEncoded , Vocab = we.ConvertRowToListOfNumbers(Quections , Answers)
#----------------------------------------------------------------------------------------------
QuectionsTest , AnswersTest = dp.DataPreprocessing(test_path,QuectionsTest , AnswersTest)
QuectionsEncodedTest , AnswersEncodedTest , VocabTest = we.ConvertRowToListOfNumbers(QuectionsTest , AnswersTest)
#----------------------------------------------------------------------------------------------
Model = PrepareModel(Num_Of_Hidden_LayersOrOutDim)
Model =RunModel(Model , QuectionsEncoded , AnswersEncoded  , QuectionsEncodedTest , AnswersEncodedTest)
print ("Model Run Successfully")
#print (Model.evaluate())