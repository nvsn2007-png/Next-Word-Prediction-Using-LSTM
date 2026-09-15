# Next Word Prediction Using LSTM

## Project Description

This project implements a Deep Learning-based Next Word Prediction system using a Long Short-Term Memory (LSTM) neural network.

The model learns word sequences from a training dataset and predicts the most probable next word given an input text sequence.

## Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Matplotlib
- LSTM
- Word Embeddings
- Tokenization
- Softmax

## Architecture

Input Text  
↓  
Tokenization  
↓  
Word Embedding  
↓  
LSTM Layer  
↓  
Dense Layer with Softmax  
↓  
Predicted Next Word

## Project Files

- `next_word_prediction.py` – Trains the LSTM model
- `demo.py` – Runs interactive next-word prediction
- `word_model.keras` – Saved trained LSTM model
- `tokenizer.pkl` – Saved tokenizer
- `training_graph.png` – Training loss and accuracy graph

## Example

Input:

`machine learning helps`

Predicted Next Word:

`computers`

Another example:

`deep learning uses`

Predicted Next Word:

`neural`

## How to Run

Install the required libraries:

```bash
pip install tensorflow numpy matplotlib
