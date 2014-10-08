
import sys
from subprocess import call
import zlib

f = open("fmceverton.fmv", "rb")
bytes = f.read()
f.close()

start = 18
offset = 4000

for num in range(0, len(bytes)):
	fileName = "everton" + str(start)
	#newFile = open("everton" + str(start), "wb")
	#newFile.write(bytes[start:])

	#print("Trying from byte" + str(start))
	#print(bytes[start:start+5])

	try:
		decompressed_bytes = zlib.decompress(bytes[start:offset], 15, len(bytes))
		print("Decompressed @" + str(offset))
		f = open("everton-decompressed", "wb")
		f.write(decompressed_bytes)
		sys.exit()
	except Exception as e:
		pass

	offset += 1

	'''cont = input("e to end")
	if cont == 'e':
		sys.exit()'''

	#newFile.close()

	#call(["file", fileName])

