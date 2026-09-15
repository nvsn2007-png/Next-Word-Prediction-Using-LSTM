import pickle
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


# Load trained model
model = load_model("word_model.keras")


# Load tokenizer
with open("tokenizer.pkl", "rb") as file:
    tokenizer = pickle.load(file)


# Maximum sequence length
max_sequence_len = 5


print("\n===================================")
print("   NEXT WORD PREDICTION USING LSTM")
print("===================================\n")


while True:

    input_text = input("Enter text (or type 'exit'): ")

    if input_text.lower() == "exit":
        print("\nThank you!")
        break


    # Convert text to sequence
    token_list = tokenizer.texts_to_sequences([input_text])[0]


    # Pad sequence
    token_list = pad_sequences(
        [token_list],
        maxlen=max_sequence_len - 1,
        padding='pre'
    )


    # Predict next word
    predicted = model.predict(token_list, verbose=0)

    predicted_index = np.argmax(predicted)


    # Find predicted word
    predicted_word = ""

    for word, index in tokenizer.word_index.items():

        if index == predicted_index:
            predicted_word = word
            break


    print("\nPredicted Next Word:", predicted_word)
    print()
    