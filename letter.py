import string

def string_to_regional(texto):

    texto  =texto.lower()
    alphabet = list(string.ascii_lowercase)
    alphabet.append(" ")
    acento =(
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u")
    )

    for a, b in acento:
        texto = texto.replace(a, b)

    texto = list(texto)

    for i in texto:
        if i not in alphabet:
           return ":regional_indicator_e: :regional_indicator_r: :regional_indicator_r: :regional_indicator_o: :regional_indicator_r: "
    for i in range(len(texto)):
        texto[i] = f":regional_indicator_{texto[i]}: "

    texto = "".join(texto)
    texto = texto.replace(":regional_indicator_ :", "  ")
    
    return texto

