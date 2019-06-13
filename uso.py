from trivium import *


key = 0xf0f0f0f0f0f0f0f0f0f0
iv = 0xaeaeaeaeaeaeaeaeaeae
cipher = Trivium(key, iv)
decipher = Trivium(key, iv)
print("0x%X" % cipher.get_keystream_of_size(128))
print("0x%X" % dar_vuelta(decipher.get_keystream_of_size(128),128))
text = cipher.encode("Hola, ¿Cómo estás?")
print(text)
text = decipher.encode(text)
print(text)

