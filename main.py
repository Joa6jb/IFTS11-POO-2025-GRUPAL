
# Colaboradores: Fabian  Muiño, Isabella Sanchez, Lucia Diaz, Victoria Del Pino, Luis Canepa y Joaquin Fernandez.

class Perro(object):
    def __init__(self, nombre, raza, edad, tamaño, peso, estado_salud, vacunado, estado, temperamento, id):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.tamaño = tamaño
        self.peso = peso
        self.estado_salud = estado_salud
        self.vacunado = vacunado
        self.estado = estado
        self.temperamento = temperamento
        self.id = id
        
    
    
    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in ["disponible" , "reservado", "adoptado"]:
            self.estado_adopcion = nuevo_estado
            print("Estado actualizado")
        else:
            print("Estado invalido")
            
    
    
    def mostrar_informacion(self):
        return  {
            "Nombre": self.nombre,
            "Raza": self.raza,
            "Edad": self.edad,
            "Estado de Salud": self.estado_salud,
            "Tamaño": self.tamaño,
            "Vacunado": self.vacunado,
            "Estado de Adopción": self.estado_adopcion,
            "Temperamento": self.temperamento,
            "ID": self.id
        }
        


class UsuarioAdoptante(object):
    
    def __init__(self, nombre, apellido, telefono, dni, email, preferencias=None, historial_adopciones=None):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.dni = dni
        self.email = email
        self.preferencias = preferencias or []
        self.historial_adopciones = historial_adopciones or []
        
    
   
    def registrar_usuario(self, nombre, apellido, dni, email, telf, contraseña):
        if not all ([nombre, apellido, dni, email, telf, contraseña]):
            return "Debe llenar todos los campos"
        
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email
        self.telf = telf
        self.contraseña = contraseña
        
        return {
            "Nombre": self.nombre,
            "Apellido": self.apellido,
            "DNI": self.dni ,
            "Email": self.email,
            "Telefono": self.telf,
            "Contraseña": self.contraseña,
        }
        
    
    
    def Modificar_Datos(self, nuevo_email=None, nuevo_telefono=None, nueva_contraseña=None, nueva_preferencia=None):
        if nuevo_email:
            self.email = nuevo_email
        
        if nuevo_telefono:
            self.telf = nuevo_telefono
        
        if nueva_contraseña:
            self.contraseña = nueva_contraseña
            
        if nueva_preferencia:
            self.preferencias = nueva_preferencia
        
        return "Los datos fueron modificados correctamente."
    
    
    
    def datos_usuario(self):
        
        datos = {
            
            "Nombre =": self.nombre,
            "Apellido =": self.apellido,
            "Email =": self.email,
            "Teléfono =": self.telf,
            "DNI =": self.dni,
            "Contraseña =": self.contraseña,
            "Preferencias =": self.preferencias
        }
            
        return datos
    
    
    
    def ver_historial(self):
        if not self.historial_adopciones:
            return "Este usuario no tiene historial de adopciones."
        return self.historial_adopciones
    


class SistemaAdopcion(object):
    
    def __init__(self):
        self.perros = []
        self.usuarios = []
         
    
    
    def cargar_perro(self, nuevo_perro):
        self.perros.append(nuevo_perro)
        print(f"Perro cargado correctamente: {nuevo_perro.nombre, nuevo_perro.id}")
    
    
    
    def eliminar_perro(self, id_perro):
        for perro in self.perros:
            if perro.id == id_perro:
                self.perros.remove(perro)
                return "El perro fue removido correctamente."
        return "Este perro no existe."   
    
    
    
    def registrar_usuario(self,usuario):
        self.usuarios.append(usuario)
        return "El usuario se registro correctamente."
    
    
    
    def postularPerro(self,id):
        for perro in self.perros:
            if perro.id == id:
                if perro.estado== "disponible":
                    perro.cambiarEstado("reservado")
                    print(f"Perro {id} reservado con éxito!")
                    return perro
                else:
                    print(f"Este perro {id} se encuentra reservado, no es posible postularse")
                    return None
        print(f"No se encontró ningun perro con el ID {id}")
        return None
    
    
   
    def confirmar_adopcion(self, id_perro, usuario):
        for perro in self.perros:
            if perro.id == id_perro:
                if perro.estado_adopcion == "disponible":
                    perro.cambiar_estado("adoptado")
                    usuario.historial_adopciones.append(perro)
                    return "Felicidades!, el perro ha sido adoptado."
                else:
                    return "Este perro no esta disponible en este momento para ser adoptado."
        return "Este perro no existe."
    
    
   
    def sugerir_perros(self, usuario):
        sugerencia = []
        for perros in self.perros:
            if (
                perros.temperamento in usuario.preferencias or 
                perros.raza in usuario.preferencias or 
                perros.tamaño in usuario.preferencias or
                perros.edad in usuario.preferencias
            ):
                if perros not in sugerencia:
                    sugerencia.append(perros.mostrar_informacion())
        if not sugerencia:
            return "No hay perros que coincidan con las preferencias del usuario."
        return sugerencia
    
    
     
    def listado_perros_disponibles(self):
        disponibles = [perro.mostrar_informacion() for perro in self.perros if perro.estado_adopcion == "disponible"]
        if not disponibles:
            return "No hay perros disponibles en este momento."
        return disponibles
    
    
    
    def listado_perros_por_estado(self, estado):
        if estado not in ["disponible", "reservado", "adoptado"]:
            return "Este estado no es valido."
        estado_perros= [perro.mostrar_informacion() for perro in self.perros if perro.estado_adopcion == estado]
        return estado_perros
        

    
   
    def listado_perros_por_usuario(self, usuario):
        for usua in self.usuarios:
            if usua.nombre == usuario.nombre and usua.dni == usuario.dni:
                return usua.ver_historial()
        return "Este usuario no existe o no tiene historial de adopciones."
    

 # Sistema adopcion con while
 
"""class SistemaAdopcion():
    def __init__(self):
        self.perros = []
        self.usu_adoptante = []
    
    def cargar_perro(self, nuevo_perro):
        self.perros.append(nuevo_perro)
        print(f"Informacion cargada correctamente")
    
    def eliminar_perro(self, id):
        i = 0
        while i < len(self.perros):
            if self.perros[i].id == id:
                self.perros.remove(self.perros[i])
                print(f"Se ha eliminado correctamente")
                return
            else:
                i = i + 1
        print(f"Ese perro no encuentra en la lista")
        
    def registrar_usuarios(self, nuevo_usuario):
        self.usu_adoptante.append(nuevo_usuario)
        print(f"Usuario registrado corectamente")

    def confirmar_adopcion(self, id_Perro, dni_Usuario_adoptante):
        i = 0
        while i < len(self.perros):
            if self.perros[i].id == id_Perro:
                #vamos a buscar el usuario una ves se encuentra al perro
                l = 0 # uso l como indice porque i ya lo utilizo para buscar al perro
                while l < len(self.usu_adoptante):
                    if self.usu_adoptante[l].dni == dni_Usuario_adoptante:
                        if self.perros[i].estado == EstadoPerro.RESERVADO:
                            self.perros[i].cambiar_estado(EstadoPerro.ADOPTADO)
                            self.usu_adoptante[l].historial_adopciones.append(self.perros[i])
                            print(f"!Felicidades¡ Adopcion realizada")
                            return
                        else:
                            print(f"No se pudo realizar la adopcion")
                    l = l + 1
                print(f"Usuario invalido")
                return
            i = i + 1 
        print(f"El perro no fue encontrado, vuelva a intetarlo")
        return
    
    def sugerir_perro(self, dni, preferencias):
        i = 0
        while i < len(self.usu_adoptante):
            if self.usu_adoptante[i].dni == dni:
                preferencias = self.usu_adoptante[i].preferencias

                l = 0
                while l < len(self.perros):
                    if self.perros[l].estado == EstadoPerro.DISPONIBLE:
                        if "tamaño" in preferencias:
                            if self.perros[l].tamaño == preferencias["tamaño"]:
                                print(f"Segun sus preferencias se sugiere al perro: {self.perros[l].nombre}")
                                return self.perros[l]
                    l = l + 1
                print("No se encontro ningun perro de acuerdo a sus prefenrencias")
                return
            i = i + 1
        print("Usuario no encontrado")
        return
    
    def listado_perros_estado(self, estado_solicitado):
        i = 0 
        coincidencias = False
        while i < len(self.perros):
            if self.perros[i].estado == estado_solicitado:
                print(f"{self.perros[i].nombre} - Estado: {self.perros[i].estado.value}")
                coincidencias = True
            i = i + 1
        if coincidencias == False:
            print(f"No se encontraron perros en estado '{estado_solicitado.value}'.")
        return 
    
    def listado_usuario(self, dni_usuario):
        i = 0
        while i < len(self.usu_adoptante):
            if self.usu_adoptante[i].dni == dni_usuario:
                l = 0
                if len(self.usu_adoptante[i].historial_adopciones) == 0:
                    print(f"{self.usu_adoptante[i].nombre} no adopto ningun perro por el momento.")
                    return
                
                print(f"Perros adoptados por {self.usu_adoptante[i].nombre}:")
                while l < len(self.usu_adoptante[i].historial_adopciones):
                    perro = self.usu_adoptante[i].historial_adopciones[l]
                    print(f"{perro.nombre} ({perro.raza}, {perro.edad} años)")
                    l = l + 1
                return
            i = i + 1
        print(f"Usuario no encontrado")
        return """
    