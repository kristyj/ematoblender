__author__ = "Alexander Hewer"
__email__ = "hewer@coli.uni-saarland.de"

import mathutils

from .ModelData import ModelData
from .ModelSpace import ModelSpace
from .ModelConvert import ModelConvert

class ModelReconstructor:

    def __init__(self, modelData):

        self.modelData = modelData
        self.modelSpace = ModelSpace(modelData)
        self.convert = ModelConvert(modelData)

    def get_mean(self):

        result = []

        for i in range(0, self.modelData.dimTarget // 3):

            x = self.modelData.mean[i*3 + 0]
            y = self.modelData.mean[i*3 + 1]
            z = self.modelData.mean[i*3 + 2]
            position = mathutils.Vector()
            position[0] = x
            position[1] = y
            position[2] = z
            result.append(position)

        return result


    def reconstruct_from_variations(self, variations):

        weights = self.convert.to_weights(variations)
        return self.reconstruct_from_weights(weights)

    def reconstruct_from_weights(self, weights):

        target = self.__reconstruct_target_from_weights(weights)

        result = []

        for i in range(0, self.modelData.dimTarget // 3):

            x = target[i*3 + 0]
            y = target[i*3 + 1]
            z = target[i*3 + 2]
            position = mathutils.Vector()
            position[0] = x
            position[1] = y
            position[2] = z
            result.append(position)

        return result

    def __reconstruct_target_from_weights(self, weights):

        identity = self.modelSpace.identity(weights.idWeights)
        result = identity.dot(weights.expWeights) + self.modelData.mean
        return result