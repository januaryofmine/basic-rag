from cosine_similarity import cosine_similarity

def top_k(query_vector: list[float], vectors: list[list[float]], k: int) -> list[tuple[int, float]]:
      if k <= 0:
          raise ValueError(f"k phải > 0, nhận được {k}")

      scored = []
      for i in range(len(vectors)):
          score = cosine_similarity(query_vector, vectors[i])
          scored.append((i, score))

      ranked = sorted(scored, key=lambda score: score[1], reverse=True)
      return ranked[:k]

# print(top_k([1, 0], [[0, 1], [1, 0], [1, 1]], 2))
# print(top_k([0.9, 0.1, 0.0], [[0.1, 0.9, 0.2], [0.9, 0.1, 0.0], [0.8, 0.2, 0.1], [0.2, 0.1, 0.9]], 3))
