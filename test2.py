import sys

def getFreeMemLocations():
		A = []
		i = 0
		while True:
			try:
				i = ''.join(mainMem).index('.',i)
				index = i
			except:
				break
			blockSize = 0
			while mainMem[i] == '.':
				print i
				blockSize +=1
				i+=1
				if i == len(mainMem):
					break
			A.append((index, blockSize))
		return A



mem = '########AAAAAAA....BBBB.......CCCCC.......DDDDEEEE...FFFFF....'

mainMem = list(mem)
mainMem[23] = 'Z'

print ''.join(mainMem)

print getFreeMemLocations()

# print mem
# i = mem.count('.'); mem = mem.replace('.',''); mem = mem + '.'* i;
# print mem




