import math

def cosine_similarity(a: list[float], b: list[float]) -> float:
    if len(a) != len(b):
        raise ValueError(f"hai vector phải cùng số chiều: {len(a)} != {len(b)}")

    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))

    if norm_a == 0 or norm_b == 0:
        raise ValueError("không tính được cosine cho vector 0")

    return dot / (norm_a * norm_b)

print(cosine_similarity([0.9, 0.1, 0.0], [0.8, 0.2, 0.1]))
