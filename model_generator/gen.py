import definitions as utils
import json
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import text as txtProcessor
from tensorflow.keras.preprocessing.text import Tokenizer


def generate():

    #load the template data
    template = (json.loads(utils.template_data))

    #Parse and tokenized the language data
    tenkenizer = Tokenizer(num_words=None, filters='!"$%&()*,./:;<=>?@[\\]^_`{|}~\t\n', lower=True, split='\,', char_level=False, oov_token=None)
    tenkenizer.fit_on_texts(template['languages'].split(","))
    language_of_interest = tenkenizer.word_index    

    #Parse and tokenized the library data
    tenkenizer = Tokenizer(num_words=None, filters='!"#$%&()*+,./:;<=>?@[\\]^_`{|}~\t\n', lower=True, split='\,', char_level=False, oov_token=None)
    tenkenizer.fit_on_texts( template['technology'].split(","))
    lib_of_interest = tenkenizer.word_index

    #Parse and tokenized the classification data
    tenkenizer = Tokenizer(num_words=None, filters='!"$%&()*,./:;<=>?@[\\]^_`{|}~\t\n', lower=True, split='\,', char_level=False, oov_token=None)
    tenkenizer.fit_on_texts(template['classifications'].split(","))
    classifications_sequence = tenkenizer.word_index


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
        entry = utils.gen_classification_data(entry_data, lib_of_interest, language_of_interest, classifications_sequence)
        table+=(entry)

    #for expert
    for entry_data in template['expert']:
        entry = utils.gen_classification_data(entry_data, lib_of_interest, language_of_interest, classifications_sequence)
        table+=(entry)

    #for novice
    for entry_data in template['novice']:
        entry = utils.gen_classification_data(entry_data, lib_of_interest, language_of_interest, classifications_sequence)
        table+=(entry)

    #for intermediate
    for entry_data in template['intermediate']:
        entry = utils.gen_classification_data(entry_data, lib_of_interest, language_of_interest, classifications_sequence)
        table+=(entry)


    my_df = pd.DataFrame(table)
    my_df.to_csv('truth_template_dataset.csv', index=True)

    return 0
