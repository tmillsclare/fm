import zlib

SECTION_HEADER=b'\x78\x9C'

sections = []

def compressed_parts(file_bytes):
	newStart = 0
	location = file_bytes[newStart:].find(SECTION_HEADER)

	while location != -1:
		newStart += location + 1
		sections.append(newStart - 1)
		location = file_bytes[newStart:].find(SECTION_HEADER)

def decompress_section(file_bytes, start):
	print("Decompressing section starting: " + str(start))
	try:
		return zlib.decompress(file_bytes[start:])
	except Exception as e:
		print("Error decompressing block %d" % start)
		return None


f = open("fmceverton.fmv", "rb")
bytes = f.read()
f.close()

compressed_parts(bytes)

count = 0

for section in sections:
	decompressed_bytes = decompress_section(bytes, section)

	if decompressed_bytes != None:
		f = open("sections/everton-%d" % section, "wb")
		f.write(decompressed_bytes)
		f.close()

	count += 1
