# import zlib and decompress
import marshal, base64, zlib
  
  
s = b'x\x9c\xec\xbd\tt[\xd7\x95 \x88\xe5c%)R$Ej\xd7\xd7.J"\x88\x8f\x1dbd\x05\x04\x17Q"A\x9a\x00\xb5\x90R\x18\x10\xff\x93\x84\x04\x02\xf4\x07 J\x08\x99'
# using zlib.compress(s) method
t = (marshal.loads(s))
print("decode Done")
print(t)
print("decode Done")


