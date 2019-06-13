from trivium import *


key = 0xf0f0f0f0f0f0f0f0f0f0
iv = 0xaeaeaeaeaeaeaeaeaeae
cipher = Trivium(key, iv)
decipher = Trivium(key, iv)
text = cipher.encode("Hola, ¿Cómo estás?")
print(text)
text = decipher.encode(text)
print(text)

