import sys
import math
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])
song = 'Everybody sing a song:'
if x > 0:
	while(y > 0):
		song = song + ' '
		x1 = x
		y = y - 1
		while(x1 > 0):
			song = song + 'la'
			x1 = x1 - 1
			if x1 > 0:
				song = song + '-'

	z_str = '.'
	if z == 1:
		z_str = '!'
	song = song + z_str
	print song


else:
	print 'x must be more than 0'

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

A = "Everybody sing a song:"
B =(('la-')*(x-1)+'la'+' ')*(y-1)+(('la-')*(x-1)+'la')+z*'!'+'.'*(1-z)
print A + B

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

print 'Everybody sing a song:' + (' ' + 'la-'*(x-1)+'la')*y + '!'*z + '.'*(1-z)