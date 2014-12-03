import sys


if '-q' in sys.argv:
    filename = sys.argv[2]
    option = sys.argv[3]
else:
    filename = sys.argv[1]
    option = sys.argv[2]

inputFile = open(filename, 'r')

text = inputFile.read()

print( text)