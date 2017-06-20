import sys
import urllib3
import _json

class MyClass:
    def first(self, message):
        self.message = message
        print(message)

forlaura=MyClass()
#words="Hi Laura"
words = "I love you, Laura."
# forlaura.first(words)

i=0
while i < 100:
    forlaura.first(words)
    i=i+1



#http = urllib3.PoolManager()

#url = http.

