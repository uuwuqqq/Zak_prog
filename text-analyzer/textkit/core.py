def normalize_whitespace(text:str)->str:
    """Nahradí skupiny bílých znaků jednou mezerou."""
    return " ".join(text.split())


def count_words(text:str)->int:
    """Vrátí počet slov oddělených bílými znaky."""
    return len(text.split())



def word_frequencies(text: str) -> dict[str, int]:
    """Vrátí četnosti slov bez ohledu na velikost písmen."""
    text_lower=text.lower()
    for char in ".,!?;:—-\"()":
        text = text.replace(char, "")
    words=text.split()
    counts={}
    for a in words:
        counts[a]=counts.get(a,0)+1
    return counts
        

def most_common_words(text: str, limit: int = 5) -> list[tuple[str, int]]:
    """Vrátí nejčastější slova a jejich počty."""
    slovo_max = max(count_words(text), key=lambda )


print(normalize_whitespace("Ahoj \n svete"))
print(count_words("Ahoj \n svete "))
print(count_words(" "))
print(word_frequencies("Pes, kocka a pes"))

