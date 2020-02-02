from functools import reduce
class Material(tuple):
  def __new__(self, materialName, materialLoad):
    return tuple.__new__(Material,(materialName,materialLoad))
  
  def getName(self):
    return self[1]

  def getLoad(self):
    return self[0]

class Recipe:
  def __init__(self, output, inputs):
    self.output = output
    self.inputs = inputs

  def __str__(self):
    string = str(self.output.getLoad) + " of " + self.output.getName + ":"
    for material in self.inputs:
      childstring = str(material.getLoad) + " of " + material.getName +  ", "
      string += childstring

    return string

  def containsInputMaterialWithName(self, name):
    for input in self.inputs:
      if input.getName == name:
        return True
    return False

