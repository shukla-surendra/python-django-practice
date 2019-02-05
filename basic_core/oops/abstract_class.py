from abc import ABC, abstractmethod

class AbstractModel(ABC):
    @abstractmethod
    def save():
        pass

class Model(AbstractModel):
    def save(self):
        '''
            In the function, self will always passed as a first argument, if you miss to define that Error will be thrown.
            function save() takes 1 positional argument and Zero is given.
        '''
        print("saved")


model = Model()
model.save()