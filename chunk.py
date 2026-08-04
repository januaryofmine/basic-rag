text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

## 1. Basic Chunk with chunk size

# for i in range(0, len(text), chunk_size):
#     chunk = text[i:i + chunk_size]
#     chunks.append(chunk)
def basic_chunk(text: str, chunk_size: int) -> list[str]:
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# print("Basic chunk: ",  basic_chunk(text, 3))


## 2. Basic Chunk with chunk size & overlap
def overlap_chunks(text: str, chunk_size: int, overlap: int) -> list[str]:
    if not 0 <= overlap < chunk_size:
        raise ValueError(f"overlap ({overlap}) phải >= 0 và < chunk_size ({chunk_size})")

    chunks = []
    step = chunk_size - overlap
    for i in range(0, len(text), step):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)

    return chunks

# print("Basic chunk with chunk size and overlap: ",  overlap_chunks(text, 5, 2))

## 3. Word Based Chunk
def word_chunks(text: str, chunk_size: int, overlap: int) -> list[str]:
    if not 0 <= overlap < chunk_size:
        raise ValueError(f"overlap ({overlap}) phải >= 0 và < chunk_size ({chunk_size})")

    words = text.split()
    step = chunk_size - overlap

    chunks: list[str] = []
    for i in range(0, len(words), step):
        words_in_chunk = words[i:i+chunk_size]
        chunk = " ".join(words_in_chunk)
        chunks.append(chunk)

    return chunks

# print("Word-based chunk: ",  word_chunks(text, 5, 2))

def greedy_word_chunks(text: str, max_chars: int, overlap_words: int = 0) -> list[str]:
    if max_chars <= 0:
        raise ValueError(f"max_chars phải > 0, nhận được {max_chars}")
    if overlap_words < 0:
        raise ValueError(f"overlap_words phải >= 0, nhận được {overlap_words}")

    words = text.split()

    chunks: list[str] = []
    current: list[str] = []
    for word in words:
        candidate = current + [word]
        candidate_len = len(" ".join(candidate))

        if current and candidate_len > max_chars:
            chunks.append(" ".join(current))
            current = current[-overlap_words:] if overlap_words else []

            if len(" ".join(current + [word])) > max_chars:
                current = []

        current.append(word)

    if current:
        chunks.append(" ".join(current))

    return chunks

print("Greedy Word-based chunk: ",  greedy_word_chunks(text, 40, 5))
