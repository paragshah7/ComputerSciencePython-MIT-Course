# Paste your code here
class myDict(object):
    """ Implements a dictionary without using a dictionary """

    def __init__(self):
        """ initialization of your representation """
        # FILL THIS IN
        print(self)
        self.key = ''
        self.value = ''
        self.keys = [self.key]
        self.values = []

    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        # FILL THIS IN
        print("In assign")
        self.key = k
        self.key.value = v
        key = self.key
        self.keys.append(key)
        self.keys.append(k)
        self.values.append(v)

    def getval(self, k):
        """ k, immutable object  """
        # FILL THIS IN
        for i in self.keys:
            if i == k:
                return i.value

        # index = self.keys.index(k)
        # return self.values[index]

    def delete(self, k):
        """ k, immutable object """
        # FILL THIS IN
        index = self.keys.index(k)
        self.keys.remove(k)
        self.values.pop(index)


result = myDict()

result.assign(1, 10)
print(result.getval(1))


