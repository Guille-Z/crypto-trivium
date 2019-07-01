from trivium import *


key = 0xf0f0f0f0f0f0f0f0f0f0
iv = 0xfeaefeaefeaefeaefeae
cipher = Trivium(key, iv)
decipher = Trivium(key, iv)
# print("0x%X" % cipher.get_keystream_of_size(128))
# print("0x%X" % dar_vuelta(decipher.get_keystream_of_size(128), 128))
text = "Esto es un texto de prueba, esto es un texto de prueba, esto es un texto de prueba."
print("Texto plano: " + text)
text = cipher.encode(text)
print("Texto codificado: " + text)
text = decipher.encode(text)
print("Texto decodificado: " + text)

