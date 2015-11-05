from django.db import models

class Empresa(models.Model):
    identificacion       =models.CharField(max_length=15)
    razonSocial          = models.CharField(max_length=200, blank=True)
    direccion            = models.CharField(max_length=100, blank=True)
    idEstadoEmpresa      = models.IntegerField()
    eliminado            = models.BooleanField(default=False)

    def __str__(self):
        return self.razonSocial
        
class Cliente(models.Model):
    identificacion       = models.CharField(max_length=15)
    razonSocial          = models.CharField(max_length=200, blank=True)
    idTipoId             = models.IntegerField()
    nombres              = models.CharField(max_length=100, blank=True)
    apellidos            = models.CharField(max_length=100, blank=True)
    email                = models.EmailField(max_length=100, blank=True)
    direccion            = models.CharField(max_length=100, blank=True)
    idEstadoCliente      = models.IntegerField()
    Telefonos            = models.CharField(max_length=100, blank=True)
    eliminado            = models.BooleanField(default=False)
    
    
    def __str__(self):
        if self.nombres <>'' and self.apellidos <>'':
            return "%s %s"  % (self.nombres,self.apellidos)
        elif self.razonSocial <>'' :
            return self.razonSocial
 

  
class Factura(models.Model):
    numFactura          = models.CharField(max_length=10)
    fecha               = models.DateField()
    cliente             = models.ForeignKey('Cliente')
    direccion           = models.CharField(max_length=100, blank=True)
    telefonos           = models.CharField(max_length=100, blank=True)
    idEstadoFactura     = models.IntegerField()
    eliminado           = models.BooleanField(default=False)
    empresa             = models.ForeignKey('Empresa')
    
    def __str__(self):
        return self.numFactura
    

class Producto(models.Model):
    refProducto          = models.CharField(max_length=100, blank=True,unique=True)
    descProducto         = models.CharField(max_length=100, blank=True)
    idTipoProducto       = models.IntegerField()
    idCategoriaProducto  = models.IntegerField()
    idEstadoProducto     = models.IntegerField()   
    eliminado            = models.BooleanField(default=False)
    
    def __str__(self):
        return self.descProducto

class DetFactura(models.Model): 
    cant                = models.DecimalField(max_digits=10, decimal_places=2)
    precio              = models.DecimalField(max_digits=10, decimal_places=2)
    producto            = models.ForeignKey('Producto')
    factura             = models.ForeignKey('Factura')
    descuento           = models.IntegerField()
    idEstadoDetFactura  = models.IntegerField()
    eliminado           = models.BooleanField(default=False)
    



class Parametro(models.Model):
    atributo        =models.CharField(max_length=50)
    descripcion      =models.CharField(max_length=200)
    estadoParametro =models.CharField(max_length=1)
 
    def __str__(self):
        return self.atributo


class ValorParametro(models.Model):
    
    valor                =models.CharField(max_length=30)
    parametro            = models.ForeignKey('Parametro')
    orden                =models.CharField(max_length=3)
    estadoValorParametro =models.CharField(max_length=1)
    

    def __str__(self):
        return self.valor
