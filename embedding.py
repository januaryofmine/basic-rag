
def tokenize(text: str) -> list[str]:
    return text.lower().split()

print(tokenize("Con mèo ngồi trên thảm"))


def build_vocab(corpus: list[str]) -> dict[str, int]:
    vocab: dict[str, int] = {}
    for text in corpus:
        for word in tokenize(text):
            if word not in vocab:
                vocab[word] = len(vocab)  # từ mới -> index kế tiếp
    return vocab


# bag-of-words
def embed(text: str, vocab: dict[str, int]) -> list[float]:
    vector = [0.0] * len(vocab)
    for word in tokenize(text):
        if word in vocab:
            vector[vocab[word]] += 1.0
    return vector

# corpus = ["con mèo ngồi trên thảm", "con chó nằm trên sàn"]
# vocab = build_vocab(corpus)
# print(vocab)
# print(embed("con mèo con mèo", vocab))
