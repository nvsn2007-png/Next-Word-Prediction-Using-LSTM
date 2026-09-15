import numpy as np
import matplotlib.pyplot as plt
import pickle

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense


# --------------------------------------------------
# 1. TRAINING TEXT DATA
# --------------------------------------------------

text = """
machine learning is a powerful technology
machine learning helps computers learn
artificial intelligence is changing the world
artificial intelligence helps solve problems
deep learning uses neural networks
neural networks learn from data
data science is an important field
python is popular for machine learning
machine learning and deep learning are useful
artificial intelligence uses machine learning
"""


# --------------------------------------------------
# 2. TOKENIZATION
# --------------------------------------------------

tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])

total_words = len(tokenizer.word_index) + 1

print("Total Words:", total_words)


# --------------------------------------------------
# 3. CREATE INPUT SEQUENCES
# --------------------------------------------------

input_sequences = []

for line in text.strip().split("\n"):
    token_list = tokenizer.texts_to_sequences([line])[0]

    for i in range(1, len(token_list)):
        input_sequences.append(token_list[:i + 1])


# --------------------------------------------------
# 4. PADDING
# --------------------------------------------------

max_sequence_len = max(len(sequence) for sequence in input_sequences)

input_sequences = pad_sequences(
    input_sequences,
    maxlen=max_sequence_len,
    padding='pre'
)


# --------------------------------------------------
# 5. SPLIT INPUT AND OUTPUT
# --------------------------------------------------

X = input_sequences[:, :-1]
y = input_sequences[:, -1]


# --------------------------------------------------
# 6. BUILD LSTM MODEL
# --------------------------------------------------

model = Sequential([
    Embedding(
        input_dim=total_words,
        output_dim=50,
        input_length=max_sequence_len - 1
    ),

    LSTM(100),

    Dense(total_words, activation='softmax')
])


# --------------------------------------------------
# 7. COMPILE MODEL
# --------------------------------------------------

model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)


# --------------------------------------------------
# 8. TRAIN MODEL
# --------------------------------------------------

history = model.fit(
    X,
    y,
    epochs=200,
    verbose=1
)


# --------------------------------------------------
# 9. SAVE MODEL
# --------------------------------------------------

model.save("word_model.keras")

print("\nModel trained and saved successfully!")


# --------------------------------------------------
# 10. SAVE TOKENIZER
# --------------------------------------------------

with open("tokenizer.pkl", "wb") as file:
    pickle.dump(tokenizer, file)

print("Tokenizer saved successfully!")


# --------------------------------------------------
# 11. PLOT TRAINING GRAPH
# --------------------------------------------------

plt.figure(figsize=(10, 5))

plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["accuracy"], label="Training Accuracy")

plt.title("LSTM Training Performance")
plt.xlabel("Epoch")
plt.ylabel("Value")
plt.legend()
plt.grid()

plt.savefig("training_graph.png")

plt.show()