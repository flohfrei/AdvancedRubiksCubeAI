import pycuber as pc
import pdb
import numpy as np

"""
This wrapper class should construct an enivornment where the neural network can take actions in like reinfocement learning dictates.
The additional idea is that this class should support multithreading such that the same network can be trained simultaniously on multiple instances.
Also included in the environment is the reward function. 
The problem in solving rubiks cube is that most actions are pointless unless the appear as a formula.
Hence actions or formulas are not rewarded in the simplest model of a reward function.
Therefore only the solved cube is rewarded which leads to inefficient learning curve when a lot of actions are needed for the solution.
"""
class CubeWrapper:
    def __init__(self):
        self.solvedCube = pc.Cube()
        self.scramblingCube = pc.Cube()
        self.color_mapper = { "L": 0, "r":0, "U":0.2 , "y":0.2, "F":0.4, "g":0.4, "D":0.6, "w":0.6, "R": 0.8, "o":0.8, "B": 1, "b":1}
        self.N = 54;
        
    def step(self,move):
        self.scramblingCube(move)

    def print(self):
        print(self.solvedCube)
        print(self.scramblingCube)
        
    def to1D(self):
        color_list=[]
        current_object = str(self.scramblingCube)
        for current_char in current_object:
                if(current_char == "r"):
                    color_list.append(0.)
                if(current_char == "y"):
                    color_list.append(0.2)
                if(current_char == "g"):
                    color_list.append(0.4)
                if(current_char == "w"):
                    color_list.append(0.6)
                if(current_char == "o"):
                    color_list.append(0.8)
                if(current_char == "b"):
                    color_list.append(1.0)
        return np.array(color_list)
        
    def solved(self):
        if(self.scramblingCube == self.solvedCube):
            return true
        else:
            return false
        

if __name__ == "__main__":
    #pdb.set_trace()
    object_test = CubeWrapper()
    #object_test.step("R'")
    print(object_test.to1D())
