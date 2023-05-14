#Clase para instanciar todos los elementos de la clinica
class Clinica:
    def __init__(self):
        self.medicos = []
        self.pacientes = []
        self.enfermeras = []
        


#Metodo para agregar a enfermeras a la clinica con sobrecarga de metodos
    def agregar_enfermera(self, *enfermeras):
        for enfermera in enfermeras:
            if isinstance(enfermera, Enfermera):
                self.enfermeras.append(enfermera)
            else:
                print("Error: El objeto no es de la clase Enfermera")


#Metodo para agregar al doctor a base de datos
    def agregar_medico(self, medico):
        if isinstance(medico, Medico):
            self.medicos.append(medico)
        else:
            print("Error: El objeto no es de la clase Medico")

#Metodo para agregar a paciente y traerlo de vuelta cuando el doctor lo llame a atenderse
    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)
        

    def obtener_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return paciente
        return None
    







#Clase Paciente
class Paciente:
    def __init__(self, id, nombre, password):
        self.id = id
        self.nombre = nombre
        self.password = password
        self.asignado = False
        self.medico = None
        self.enfermera_asignada = None
        self.calificacion = None



#Metodo para quejarse
    def quejarse(self):
        print(f"El paciente {self.nombre} esta gritando de dolor: Ay! que dolor!!")

#Metodo para llamar a la enfermera
    def llamar_enfermera(self, enfermera):
        if isinstance(enfermera, Enfermera):
            self.enfermera_asignada = enfermera
            print(f"ATENCION Enfermera {enfermera.nombre}: Esta siendo solicitada por el paciente: {self.nombre}")
        else:
            print("Error: El objeto no es de la clase Enfermera")

#Metodo para calificar el servicio
    def calificar_servicio(self, calificacion):
        if not (1 <= calificacion <= 5):
            print("Error: La calificación debe ser un número entero entre 1 y 5.")
        else:
            self.calificacion = calificacion
            print(f"Gracias por su calificación, {self.nombre}. Para nuestra institucion su opinion es importante")

#Metodo para solicitar atencion especial
    def solicitar_atencion_especial(self):
            nivel_prioridad = int(input("Ingrese el nivel de prioridad de la solicitud (1 a 10), siendo 1 muy urgente y 10 poco urgente: "))
            if nivel_prioridad < 1 or nivel_prioridad > 10:
                print("Error: El nivel de prioridad debe estar entre 1 y 10.")
                return

            print(f"El paciente {self.nombre} solicita atención especial con nivel de prioridad {nivel_prioridad}")










#Clase medico
class Medico:
    def __init__(self, id, nombre, password, especialidad):
        self.id = id
        self.nombre = nombre
        self.password = password
        self.especialidad = especialidad
        self.pacientes = []
        self.enfermera = None


#Metodo para tomar a paciente
    def tomar_paciente(self, id_paciente):
        paciente = clinica.obtener_paciente(id_paciente)
        if paciente is not None and not paciente.asignado:
            paciente.asignado = True
            paciente.medico = self
            self.pacientes.append(paciente)
            print(f"El paciente {paciente.nombre} ha sido asignado al médico {self.nombre}")
        elif paciente is None:
            print(f"No se encontró un paciente con el id {id_paciente}")
        else:
            print(f"El paciente {paciente.nombre} ya ha sido asignado a un médico")

#Metodo para asignar una enfermera a su servicio
    def asignar_enfermera(self, enfermera):
        self.enfermera = enfermera
        print(f"La enfermera {enfermera.nombre} ha sido solicitada por el medico {self.nombre}")

#Metodo para dar de alta a un paciente
    def dar_alta(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                paciente.asignado = False
                paciente.medico = None
                self.pacientes.remove(paciente)
                print(f"El paciente {paciente.nombre} ha sido dado de alta por el médico {self.nombre}")
                return
        print(f"No se encontró un paciente con el id {id_paciente}")
    
#Metodo para dar dias de descanso a un paciente
    def dar_descanso(self, id_paciente, dias):
        paciente = clinica.obtener_paciente(id_paciente)
        if paciente is not None and paciente.asignado and paciente.medico == self:
            paciente.descanso = dias
            print(f"El paciente {paciente.nombre} ha recibido {dias} días de descanso.")
        elif paciente is None:
            print(f"No se encontró un paciente con el id {id_paciente}")
        elif not paciente.asignado:
            print(f"El paciente {paciente.nombre} no está asignado a este médico.")
        else:
            print(f"Error: el objeto asignado a la propiedad 'medico' del paciente no es de la clase Medico.")



#Clase enfermera
class Enfermera: 
    def __init__(self, id, nombre, password):
        self.id = id
        self.nombre = nombre
        self.password = password


#Funcion para tomar signos vitales a los pacientes
    def tomar_signos_vitales(self, paciente):
        presion_arterial = input("Ingrese la presión arterial del paciente: ")
        temperatura = input("Ingrese la temperatura del paciente: ")
        print(f"El paciente {paciente.nombre}, tiene una presion arterial de {presion_arterial} y una temperatura de {temperatura} grados")


#Metodo para registrar medicamentos
    def registrar_medicacion(self, paciente):
        medicamento = input("Ingrese el nombre del medicamento: ")
        dosis = input("Ingrese la dosis: ")
        print(f"La enfermera {self.nombre} ha registrado la medicación para el paciente {paciente.nombre}: {medicamento}, {dosis}.")


#Metodo para llamar a medico
    def llamar_medico(self):
        id_medico = input("Ingrese el ID del médico que desea llamar: ")
        for medico in clinica.medicos:
            if medico.id == id_medico:
                print(f"Enfermera {self.nombre} está llamando al médico {medico.nombre}")
                
#metodo para enviar reporte medico
    def enviar_reporte_medico(self, paciente):
        mensaje = input("Ingrese el reporte del paciente: ")
        print(f"Enfermera {self.nombre} reporta que el paciente {paciente.nombre}, {mensaje}")                
                

#--------------------------------------------------------
#Instanciamos la clinica
clinica = Clinica()


#Instanciamos el primer paciente y lo ingresamos a la clinica con agregar_paciente
p01 = Paciente(1, "Pedro Mendoza", "p1")
clinica.agregar_paciente(p01)

#Instancias de medicos
m01 = Medico("m01", "Juan Ramirez", "m01", "Medicina General")
m02 = Medico("m02", "Fernanda Guzman", "m02", "Cardiologia")
clinica.agregar_medico(m01)
clinica.agregar_medico(m02)


#Instancias de enfermeras 
e01 = Enfermera("e01", "Laura Garcia", "e01")
e02 = Enfermera("e02", "Claudia Martinez", "e02")
e03 = Enfermera("e03", "Macarena Tapia", "e03")
clinica.agregar_enfermera(e03, e01, e02)

#Prueba metodo tomar_paciente
m01.tomar_paciente(1)
m02.tomar_paciente(1)

#Prueba para asignar a una enfermera
m01.asignar_enfermera(e01)


#prueba para dar licencia medica
m01.dar_descanso(1, 11)

#prueba para dar de alta a un paciente
m01.dar_alta(1)

#pruebas clase paciente
p01.quejarse()
p01.llamar_enfermera(e01)
p01.calificar_servicio(5)
p01.solicitar_atencion_especial()

#pruebas clase enfermera
e01.tomar_signos_vitales(p01)
e01.registrar_medicacion(p01)
e01.llamar_medico()
e01.enviar_reporte_medico(p01)






