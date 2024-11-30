"""Definir una funcion palindromo"""
import re
from unicodedata import normalize

frase1 = input("Ingresa una frase palindroma: ")
print(frase1)
frase1 = frase1.lower()
f = re.sub(r"[^a-záéíóúñ]", "", frase1)
f = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+",
           r"\1", normalize("NFD", f), 0, re.I)

f = normalize("NFC", f)
print(f)
f = list(f)


if f == f[::-1]:
    print("Es una frase Palindroma")
else:
    print("No es una frase Palindroma")
