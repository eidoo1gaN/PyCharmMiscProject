from string import capwords


class HelloWorld:
    def __init__(self, args):
        self.args = args

    def __str__(self):
        return str(self.args)

    def HelloWorld(self, HelloWorld):
        print(str(self.args))
        print(capwords(HelloWorld))
        return "Hello WOORld"

def worldHello(*helloworlds):
    for helloworld in helloworlds:
        print("", helloworld, "")

helloWorld = HelloWorld("Hello World")
helloworld = HelloWorld("helloWorld")
HEllOWorld = helloworld.HelloWorld(str(helloWorld.HelloWorld("hello world")))
HELL0WORLD = [worldHello(helloWorld, HEllOWorld), worldHello(helloworld), worldHello(HEllOWorld)]
print("I don't know what's happening anymore")
