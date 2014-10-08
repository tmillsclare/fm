
import sys

f = open("fmceverton.fmv", "rb")
bytes = f.read()
f.close()

start = 2692

try:
	f = open("everton-cut-"+str(start), "wb")
	f.write(bytes[start:])
	sys.exit()
except Exception as e:
	pass

f.close()

