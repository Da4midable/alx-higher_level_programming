#!/usr/bin/python3
print('{0}'.format(''.join([chr(i) + chr(i+1).lower()
                            for i in range(65, 91, 2)])[::-1]), end="")
