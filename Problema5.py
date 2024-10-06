class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre  
        self.num_registro = numero_registro  
        self.edad = None  
        self.nota = None  
    
    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de registro: {self.num_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        else:
            print("Edad: No asignada")
        if self.nota is not None:
            print(f"Nota: {self.nota}")
        else:
            print("Nota: No asignada")

    def setAge(self, edad):
        self.edad = edad
    

    def setNota(self, nota):
        self.nota = nota


alumno1 = Alumno("Andrea Valle", "19110118")


alumno1.setAge(24)
alumno1.setNota(18)


alumno1.display()

