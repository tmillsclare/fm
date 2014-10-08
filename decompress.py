import zlib

start = [18, 2692, 10335585]

def writePart(name, start, bytes, findEnd=False):

	if not findEnd:
		decompressed_bytes = zlib.decompress(bytes[start:])
		f = open(name, "wb")
		f.write(decompressed_bytes)
		f.close()
	else:
		end = start + 1
		error = True

		while error:
			try:
				decompressed_bytes = zlib.decompress(bytes[start:end])
				print("Decompressed at offset " + str(end))
				error = False
			except Exception as e:
				end += 1
		

f = open("fmceverton.fmv", "rb")
bytes = f.read()
f.close()

try:
	#part1
	writePart("everton-part1", 18, bytes, True)

	#part2
	writePart("everton-part2", 2692, bytes, True)

	#part2
	writePart("everton-part3", 10335585, bytes, True)
except Exception as e:
	raise e