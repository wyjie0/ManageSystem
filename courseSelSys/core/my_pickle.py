import pickle
import os

from courseSelSys.core.school import Course
from courseSelSys.core.school import Classes
from courseSelSys.core.teacher import *

class MyPickle:
    def __init__(self,filename):
        self.filename = filename

    def dump(self,obj):
        with open(self.filename,'ab') as f:
            pickle.dump(obj,f)

    def loaditer(self):
        with open(self.filename, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    yield obj
                except:
                    break

    def edit(self,obj):
        f2 = MyPickle(self.filename+'.bak')
        for item in self.loaditer():
            if item.name == obj.name:
                f2.dump(obj)
            else:
                f2.dump(item)
        os.remove(self.filename)
        os.rename(self.filename+'.bak',self.filename)