##crear una clase llamada vehiculo capaz de procesar la informacion basica de los autos en una consecionaria. Debera tenerconstructor y los atributos del vehiculo seran: patente, marca, modelo y kilometraje. Crear metodos (de acceso) getter y (de modificacion) setter mostrara por pantalla al menos 1 atributo y modificar el kilometraje
class vehiculo:
  def__init__(self, patente, marca, modelo, kilometraje):
  self.patente = patente
  self.marca = marca
  self.modelo = modelo
  self.kilometraje = kilometraje

  def get_patente(self):
    return self.patente

  def set_kilometraje(self, nuevo_kilometraje):
    self.kilometraje = nuevo_kilometraje
    print("el kilometraje ha sido actualizado")
