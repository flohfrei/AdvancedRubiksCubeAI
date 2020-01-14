import numpy as np
import matplotlib.pyplot as plt
from matplotlib import widgets
from MagicCube.code.projection import Quaternion, project_points
import pycuber as pc
import tensorflow as tf


mycube = pc.Cube()
mycube("R U R' U'")
print(mycube)
print(type(mycube))
