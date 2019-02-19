import pickle

class MyPickle:
    def __init__(self,filename):
        self.filename = filename

    def dump(self,obj):
        with open(self.filename,'ab') as f:
            pickle.dump(obj,f)

    def loaditer(self):
        with open(self.filename, 'rb') as f:
            for obj in pickle.load(f):
                yield obj