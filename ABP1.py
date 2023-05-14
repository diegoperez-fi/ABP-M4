
#ATENCION
#ESTA TAREA NO ESTA LISTA, SE CONTINUARA A MODO DE PROYECTO



#Definimos clase paciente, con ID, nombre, edad, contacto, password
class Paciente:
    def __init__(self, id , nombre, edad, contacto, password):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.contacto = contacto
        self.password = password


#Funcion para ingresar a la cuenta, si las credenciales son correctas, entonces nos muestra un menu deopciones que podemos realizar
    def ingresar_paciente(self):
        codigo = input("Por favor ingrese su codigo: ")
        password = input("Por favor ingrese su contraseña: ")
        if self.id == codigo and self.password == password:
            print("Bienvenido, Paciente", self.nombre)
        else:
            print("Credenciales inválidas")
        opcion = ""
        while opcion != "0":
            print("Seleccione una opción:")
            print("1. Pedir receta")
            print("2. Agendar proxima cita")
            print("0. Salir")
            opcion = input("Ingrese su opcion: ")

            if opcion == "1":
                self.pedir_receta()
            elif opcion == "2":
                self.agendar_cita()
            elif opcion == "0":
                print("Hasta luego")
            else:
                print("Opción inválida")



    def pedir_receta():
        pass
    def agendar_cita():
        pass





class Tutor: 
    def __init__(self, id, numero, nombre, password):
        self.id = id
        self.numero = numero
        self.nombre = nombre
        self.password = password

#Funcion para ingresar a la cuenta, si las credenciales son correctas, entonces nos muestra un menu deopciones que podemos realizar
    def ingresar_tutor(self):
        codigo = input("Por favor ingrese su codigo: ")
        password = input("Por favor ingrese su contraseña: ")
        if self.id == codigo and self.password == password:
            print("Bienvenido, Tutor", self.nombre)
        else:
            print("Credenciales inválidas")

        opcion = ""
        while opcion != "0":
            print("Seleccione una opción:")
            print("1. Ver horario de visitas")
            print("2. Ver proxima cita")
            print("0. Salir")
            opcion = input("Ingrese su opcion: ")

            if opcion == "1":
                self.ver_horario_visitas()
            elif opcion == "2":
                self.ver_prox_cita()
            elif opcion == "0":
                print("Hasta luego")
            else:
                print("Opción inválida")
    

    def ver_horario_visitas():
        pass
    def ver_prox_cita():
        pass






class Doctor:
    def __init__(self, codigo, password, especialidad, pacientes):
        self.codigo = codigo
        self.password = password
        self.especialidad = especialidad
        self.pacientes = pacientes


#Funcion para ingresar a la cuenta, si las credenciales son correctas, entonces nos muestra un menu deopciones que podemos realizar
    def ingresar_doctor(self):
        codigo = input("Por favor ingrese su codigo: ")
        password = input("Por favor ingrese su contraseña: ")
        if self.codigo == codigo and self.password == password:
            print("Bienvenido, Doctor", self.codigo)
        else:
            print("Credenciales inválidas")

        opcion = ""
        while opcion != "0":
            print("Seleccione una opción:")
            print("1. Ver pacientes")
            print("2. Agregar pacientes")
            print("0. Salir")
            opcion = input("Ingrese su opcion: ")

            if opcion == "1":
                self.ver_pacientes()
            elif opcion == "2":
                self.agregar_paciente()
            elif opcion == "0":
                print("Hasta luego")
            else:
                print("Opción inválida")


#Funcion para agregar a un nuevo paciente
    def agregar_paciente(self):
        print("Ingrese los datos del nuevo paciente:")
        id = input("ID: ")
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        contacto = input("Contacto: ")
        password = None
        nuevo_paciente = Paciente(id, nombre, edad, contacto, password)

        self.pacientes.append(nuevo_paciente)
        print("Paciente agregado a la lista del Doctor", self.codigo)

#Funcion para ver los pacientes que se han agregado
    def ver_pacientes(self):
        print("Lista de pacientes del Doctor", self.codigo)
        for paciente in self.pacientes:
            print("ID:", paciente.id, "Nombre:", paciente.nombre, "Edad:", paciente.edad, "Contacto:", paciente.contacto)





pacientes_doctor1 = []
doctor1 = Doctor("D001", "Medicina123", "Cardiologia", pacientes_doctor1)


paciente1 = Paciente("P001", "Diego", 24, 85858596, "Paciente123")


tutor1 = Tutor("P001", 85858596, "Andrea", "Tutor123" )





#INICIO DEL PROGRAMA, ELEGIR UN PERFIL.
print("Seleccione un perfil:")
print("1. Paciente")
print("2. Doctor")
print("3. Tutor")

opcion = input("Ingrese su opcion: ")


if opcion == "1":
    paciente1.ingresar_paciente()

elif opcion == "2":
    doctor1.ingresar_doctor()

elif opcion == "3":
    tutor1.ingresar_tutor()

else:
    print("Opción inválida")










