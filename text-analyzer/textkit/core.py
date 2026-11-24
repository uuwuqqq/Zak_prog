def normalize_whitespace(text:str)->str:
    """Nahradí skupiny bílých znaků jednou mezerou."""
    return " ".join(text.split())


def count_words(text:str)->int:
    """Vrátí počet slov oddělených bílými znaky."""
    return len(text.split())



def word_frequencies(text: str) -> dict[str, int]:
  """Vrátí četnosti slov bez ohledu na velikost písmen."""
  cleaned = text.lower()
  for char in ".,!?;:—-\"()":
    cleaned = cleaned.replace(char, "")
  words = cleaned.split()
  counts: dict[str, int] = {}
  for word in words:
    counts[word] = counts.get(word, 0) + 1
  return counts

        
def most_common_words(text: str, limit: int = 5) -> list[tuple[str, int]]:
  """Vrátí nejčastější slova a jejich počty."""
  if limit <= 0:
    return []
  freqs = word_frequencies(text)
  sorted_words = sorted(freqs.items(), key=lambda item: (-item[1], item[0]))
  return sorted_words[:limit]


    


print(normalize_whitespace("Ahoj \n svete"))
print(count_words("Ahoj \n svete "))
print(count_words(" "))
print(word_frequencies("Pes, kocka a pes"))

print(most_common_words("Pes, kocka a pes"))
