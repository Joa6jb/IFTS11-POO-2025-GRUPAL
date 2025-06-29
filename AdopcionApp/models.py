from django.db import models

# Create your models here.

class Perro(models.Model):
    
    RAZAS_CHOICES = [
        ('Golden Retriever', 'Golden Retriever'),
        ('Labrador', 'Labrador'),
        ('Bulldog', 'Bulldog'),
        ('Beagle', 'Beagle'),
        ('Callejero', 'Callejero'),
        ('Husky Siberiano', 'Husky Siberiano'),
        ('Pequines', 'Pequinés'),
        ('Pitbull', 'Pitbull'),
        ('Pastor Alemán', 'Pastor Alemán'),
        ('Otro', 'Otro'),
        ('xx', 'Cualquiera')
       ]
    
    ESTADO_SALUD_CHOICES = [
        ('Saludable', 'Saludable'),
        ('En tratamiento', 'En tratamiento')
    ]

    TAMAÑO_CHOICES = [
        ('S', 'Pequeño'),
        ('M', 'Mediano'),
        ('L', 'Grande'),
        ('XL', 'Extra Grande'),
        ('xx', 'Cualquiera')
        ]

    TEMPERAMENTO_CHOICES = [
        ('Cariñoso', 'Cariñoso'),
        ('Timido', 'Tímido'),
        ('Juguetón', 'Juguetón'),
        ('Agresivo', 'Agresivo'),
        
    ]
    
    ESTADO_ADOPCION_CHOICES = [
        ('disponible', 'Disponible'),
        ('reservado', 'Reservado'),
        ('adoptado', 'Adoptado'),
        
    ]
    
    SEXO_CHOICES = [
        ('Macho', 'Macho'),
        ('Hembra', 'Hembra'),
        ('xx', 'Cualquiera')
        
    ]
    
    EDAD_CHOICES = [
        ('Cachorro', 'Cachorro'),
        ('Joven', 'Joven'),
        ('Adulto', 'Adulto'),
        ('Viejito', 'Viejito'),
        ('xx', 'Cualquiera')
    ]
    
    nombre = models.CharField(max_length=25)
    raza = models.CharField(max_length=25, choices=RAZAS_CHOICES)
    sexo = models.CharField(max_length=6, choices=SEXO_CHOICES)
    edad = models.CharField(max_length=10, choices=EDAD_CHOICES)
    peso = models.FloatField()
    estado_salud = models.CharField(max_length=25, choices=ESTADO_SALUD_CHOICES)
    tamaño = models.CharField(max_length=2, choices=TAMAÑO_CHOICES)
    vacunado = models.BooleanField(default=False)
    estado_adopcion = models.CharField(max_length=25, default='disponible', choices = ESTADO_ADOPCION_CHOICES) 
    temperamento = models.CharField(max_length=25, choices=TEMPERAMENTO_CHOICES) 
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return f"{self.nombre} {self.raza} ({self.id})"
    
    
class UsuarioAdoptante(models.Model):
    
    """ PREFERENCIAS_CHOICES = [
        ('Golden Retriever', 'Golden Retriever'),
        ('Labrador', 'Labrador'),
        ('Bulldog', 'Bulldog'),
        ('Beagle', 'Beagle'),
        ('Callejero', 'Callejero'),
        ('Husky Siberiano', 'Husky Siberiano'),
        ('Pequines', 'Pequinés'),
    ] """
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    telf = models.CharField(max_length=15)
    #preferencias= models.CharField(max_length=25, choices=Perro.RAZAS_CHOICES)
    pref_raza = models.CharField(max_length=25, choices=Perro.RAZAS_CHOICES, default='Cualquiera', blank=True)
    pref_edad = models.CharField(max_length=10, choices=Perro.EDAD_CHOICES, default='Cualquiera', blank=True)
    pref_tamaño = models.CharField(max_length=2, choices=Perro.TAMAÑO_CHOICES, default='Cualquiera', blank=True)
    pref_sexo = models.CharField(max_length=6, choices=Perro.SEXO_CHOICES, default='Cualquiera', blank=True)
    historial_adopciones = models.ManyToManyField(Perro, blank=True)
    
    #pref_raza = models.CharField(max_lenght=25, choices=PREFERENCIAS_RAZA_CHOICES)
    #pref_edad = models.CharField(max_length=10, choices=Perro.EDAD_CHOICES)
    #pref_tamaño = models.CharField(max_length=2, choices=Perro.TAMAÑO_CHOICES)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.dni})"
    
class Adopcion(models.Model):
    
    ESTADO_ADOPCION_CHOICES_2 = [
        ('reservado', 'Reservado'),
        ('adoptado', 'Adoptado')
    ]
    
    adoptante = models.ForeignKey(UsuarioAdoptante, on_delete=models.CASCADE)
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE)
    estado_adopcion = models.CharField( max_length=50, choices = ESTADO_ADOPCION_CHOICES_2)
    comentarios = models.TextField(null=True, blank=True)

    #Actualizo el estado en la tabla perro
    def save(self, *args, **kwargs):
        self.perro.estado_adopcion = self.estado_adopcion.lower()
        self.perro.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.adoptante.nombre} {self.adoptante.apellido} adoptó a {self.perro.nombre} - Estado: {self.estado_adopcion}"
