# Amharic Tokenizer

A simple Amharic text tokenizer with real-time colorized visualization of tokens. Supports multiple tokenization modes including server-side SentencePiece, local BPE-like, character, whitespace, and random subword tokenization.

<img width="1461" height="669" alt="Screenshot 2025-09-30 at 11 24 29 in the morning" src="https://github.com/user-attachments/assets/949e7725-07fc-4ea0-a15b-43121864527b" />

You can replace the tokenizer model trained with sentencepiece by using this.

```
spm_train --input=sentneces_dataset.txt --model_prefix=amharic --vocab_size=8000 --character_coverage=0.9995 --model_type=bpe
```
