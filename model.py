import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

def load_all():
    model = load_model("saved_model/model.h5")

    with open("saved_model/tokenizer.pkl", "rb") as f:
        tokenizer = pickle.load(f)

    with open("saved_model/max_len.pkl", "rb") as f:
        max_len = pickle.load(f)

    return model, tokenizer, max_len


def predict_top_words(model, tokenizer, text, max_len, top_n=3):
    token_list = tokenizer.texts_to_sequences([text])[0]
    token_list = pad_sequences([token_list], maxlen=max_len-1, padding='pre')

    preds = model.predict(token_list, verbose=0)[0]

    top_indices = preds.argsort()[-top_n:][::-1]

    words = []
    for idx in top_indices:
        for word, i in tokenizer.word_index.items():
            if i == idx:
                words.append(word)
                break

    return words