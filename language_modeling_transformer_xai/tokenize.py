import sentencepiece as spm
import os 
import numpy as np
from config import PROCESSED_DATA_DIR, MODELS_DIR

def train_sentencepiece_model(input_file, model_prefix, vocab_size=16000):
    """
    Train a sentencepiece model on the given input file.
    Args:
        input_file (txt): Path to the input text file.
        model_prefix (str): Name prefix for the output model files.
        vocab_size ( int ): size of the vocabulary to be generated.
    Returns:
        None
    """

    spm.SentencePieceTrainer.train(
        input=input_file,
        model_prefix=model_prefix,
        vocab_size=vocab_size,              
        model_type='bpe',              # Can also try: 'unigram', 'word', 'char'
        character_coverage=1.0,        # For English, 1.0 is fine
        pad_id=0, unk_id=1, bos_id=2, eos_id=3
        )
    print(f"SentencePiece model trained and saved with prefix: {model_prefix} at ")

if __name__ == "__main__":
    model_prefix = f"{MODELS_DIR}/corpus_tokenizer"
    input_path = f"{PROCESSED_DATA_DIR}/corpus.txt"
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file {input_path} does not exist. Please ensure the corpus is created first")

    train_sentencepiece_model(input_file=input_path, model_prefix=model_prefix)
    