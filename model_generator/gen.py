import definitions as utils
import json
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import text as txtProcessor
from tensorflow.keras.preprocessing.text import Tokenizer




#Parse and tokenized the library data
tenkenizer = Tokenizer(num_words=None, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=True, split='\,', char_level=False, oov_token=None)
tenkenizer.fit_on_texts(utils.libraries.split(","))
librarySequence = tenkenizer.word_index

#Parse and tokenized the language data
tenkenizer = Tokenizer(num_words=None, filters='!"$%&()*,./:;<=>?@[\\]^_`{|}~\t\n', lower=True, split='\,', char_level=False, oov_token=None)
tenkenizer.fit_on_texts(utils.programming_languages.split(","))
programming_laguage_sequence = tenkenizer.word_index

#Parse and tokenized the classification data
tenkenizer = Tokenizer(num_words=None, filters='!"$%&()*,./:;<=>?@[\\]^_`{|}~\t\n', lower=True, split='\,', char_level=False, oov_token=None)
tenkenizer.fit_on_texts(utils.classifications.split(","))
classifications_sequence = tenkenizer.word_index

#load the template data
template = (json.loads(utils.template_data))

language_of_interest = []
for language in template['languages']:
    language = language.lower()
    if language in programming_laguage_sequence:
        token = programming_laguage_sequence[language] 
    else:
        token = programming_laguage_sequence["none"]    

    language_of_interest.append(token)

lib_of_interest = []
for lib in template['technology']:
    lib = lib.lower()
    if lib in librarySequence:
        token = librarySequence[lib] 
    else:
        token = librarySequence["none"]    
        
    lib_of_interest.append(token)


header = ["language",
            "library",
            "imported_library",
            "commit_count",
            "days_since_last_commit",
            "code_churn",
            "classificatioin"]

table = []
table.append(header)

#for disqualified
for entry_data in template['disqualified']:
    entry = utils.gen_classification_data(entry_data, librarySequence, programming_laguage_sequence, classifications_sequence)
    table+=(entry)

#for expert
for entry_data in template['expert']:
    entry = utils.gen_classification_data(entry_data, librarySequence, programming_laguage_sequence, classifications_sequence)
    table+=(entry)

#for novice
for entry_data in template['novice']:
    entry = utils.gen_classification_data(entry_data, librarySequence, programming_laguage_sequence, classifications_sequence)
    table+=(entry)

#for intermediate
for entry_data in template['intermediate']:
    entry = utils.gen_classification_data(entry_data, librarySequence, programming_laguage_sequence, classifications_sequence)
    table+=(entry)


my_df = pd.DataFrame(table)
my_df.to_csv('my_csv.csv', index=False, header=False)

