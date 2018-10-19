class Memory:
  def __init__(self, INST):
    self.valor = INST
    self.prev  = None
    self.next  = None

  def getValor(self):
     return self.valor

  def __str__(self):
     return str(self.valor)

