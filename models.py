from app import db
from sqlalchemy import UniqueConstraint


class Pais(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    
    fabricantes = db.relationship('Fabricante', backref='pais', lazy=True)
    marcas = db.relationship('Marca', backref='pais', lazy=True)
    proveedores = db.relationship('Proveedor', backref='pais', lazy=True)
    activo = db.Column(db.Boolean, default=True, nullable=False)

    def __str__(self):
        return self.nombre 

class Tipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    
    modelos = db.relationship('Modelo', backref='tipo', lazy=True)
    accesorios = db.relationship('Accesorio', backref='tipo', lazy=True)
    activo = db.Column(db.Boolean, default=True, nullable=False)

    def __str__(self):
        return self.nombre
    
class Posicion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)

    def __str__(self):
        return self.nombre

class TipoDocumento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)

    def __str__(self):
        return self.nombre

class Almacenamiento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)
    
    stocks = db.relationship('Stock', backref='almacenamiento', lazy=True)

    def __str__(self):
        return self.nombre
    
class Puesto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)
    
    empleados = db.relationship('Empleado', backref='puesto', lazy=True)

    def __str__(self):
        return self.nombre

class CondicionFiscal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)
    
    clientes = db.relationship('Cliente', backref='condicion_fiscal', lazy=True)

    def __str__(self):
        return self.nombre
    
class Condicion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)
    
    accesorios = db.relationship('Accesorio', backref='condicion', lazy=True)

    def __str__(self):
        return self.nombre

class Garantia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)

    def __str__(self):
        return self.nombre

class Compatibilidad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)
    
    accesorios = db.relationship('Accesorio', backref='compatibilidad', lazy=True)
    equipos = db.relationship('Equipo', backref='compatibilidad', lazy=True)

    def __str__(self):
        return self.nombre

class FormaPago(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)
    
    ventas = db.relationship('OrdenPago', backref='forma_pago', lazy=True)

    def __str__(self):
        return self.nombre

class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    razon_social = db.Column(db.String(50), unique=True, nullable=False)
    cuit = db.Column(db.Integer, unique=True, nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)
    
    ventas = db.relationship('Venta', backref='empresa', lazy=True)

    def __str__(self):
        return self.nombre

class Accesorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    tipo_id = db.Column(db.Integer, db.ForeignKey('tipo.id'), nullable=False)
    condicion_id = db.Column(db.Integer, db.ForeignKey('condicion.id'), nullable=False)
    compatibilidad_id = db.Column(db.Integer, db.ForeignKey('compatibilidad.id'), nullable=False)
    caracteristica_id = db.Column(db.Integer, db.ForeignKey('caracteristica.id'), nullable=False)
    garantia_id = db.Column(db.Integer, db.ForeignKey('garantia.id'), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    activo = db.Column(db.Boolean, default=True)
    productos = db.relationship('Producto', backref='accesorio', lazy=True)

class Caracteristica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    descripcion = db.Column(db.String(100), nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)
    
    accesorios = db.relationship('Accesorio', backref='caracteristica', lazy=True)
    equipos = db.relationship('Equipo', backref='caracteristica', lazy=True)

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    tipo_documento = db.Column(db.String(50), nullable=False)
    documento = db.Column(db.String(30), nullable=False)
    num_contacto = db.Column(db.String(30), nullable=False)
    correo = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(50), nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)
    
    empleados = db.relationship('Empleado', backref='persona', lazy=True)
    clientes = db.relationship('Cliente', backref='persona', lazy=True)

    __table_args__ = (
        UniqueConstraint('tipo_documento', 'documento', name='uix_tipo_documento_documento'),
    )

class Fabricante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    pais_id = db.Column(db.Integer, db.ForeignKey('pais.id'), nullable=False)
    num_contacto = db.Column(db.String(50), nullable=False)
    sede_principal = db.Column(db.String(50), nullable=False)
    pagina_web = db.Column(db.String(50), nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)

    def __str__(self):
        return self.nombre

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    pais_id = db.Column(db.Integer, db.ForeignKey('pais.id'), nullable=False)
    num_contacto = db.Column(db.String(50), nullable=False)
    sede_principal = db.Column(db.String(50), nullable=False)
    pagina_web = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(250), nullable=False)
    logotipo = db.Column(db.LargeBinary, nullable=True)
    activo = db.Column(db.Boolean, default=True, nullable=False)

    modelos = db.relationship('Modelo', backref='marca', lazy=True)
    accesorios = db.relationship('Accesorio', backref='marca', lazy=True)

    def __str__(self):
        return self.nombre

class Modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_id = db.Column(db.Integer, db.ForeignKey('tipo.id'), nullable=False)
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)

    equipos = db.relationship('Equipo', backref='modelo', lazy=True)

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelo.id'), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    condicion_id = db.Column(db.Integer, db.ForeignKey('condicion.id'), nullable=False)
    compatibilidad_id = db.Column(db.Integer, db.ForeignKey('compatibilidad.id'), nullable=False)
    caracteristica_id = db.Column(db.Integer, db.ForeignKey('caracteristica.id'), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)

    productos = db.relationship('Producto', backref='equipo', lazy=True)

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    razon_social = db.Column(db.String(50), nullable=False)
    pais_id = db.Column(db.Integer, db.ForeignKey('pais.id'), nullable=False)
    num_contacto = db.Column(db.String(50), nullable=False)
    sede_principal = db.Column(db.String(50), nullable=False)
    pagina_web = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(100), nullable=False)
    logotipo = db.Column(db.LargeBinary, nullable=True)
    activo = db.Column(db.Boolean, default=True, nullable=False)

class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False)
    puesto_id = db.Column(db.Integer, db.ForeignKey('puesto.id'), nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)

    stocks = db.relationship('Stock', backref='empleado', lazy=True)

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False)
    condicion_fiscal_id = db.Column(db.Integer, db.ForeignKey('condicion_fiscal.id'), nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)
    
    ventas = db.relationship('OrdenPago', backref='cliente', lazy=True)

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    almacenamiento_id = db.Column(db.Integer, db.ForeignKey('almacenamiento.id'), nullable=False)
    cant_disponible = db.Column(db.Integer, nullable=False)
    precio_compra = db.Column(db.Integer, nullable=False)
    fecha_carga = db.Column(db.DateTime, nullable=False)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleado.id'), nullable=False)
    condicion_id = db.Column(db.Integer, db.ForeignKey('condicion.id'), nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipo.id'), nullable=False)
    accesorio_id = db.Column(db.Integer, db.ForeignKey('accesorio.id'), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)

    ordenes_pago = db.relationship('OrdenPago', backref='producto', lazy=True)

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_venta = db.Column(db.DateTime, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id'), nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)

class OrdenPago(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    venta_id = db.Column(db.Integer, db.ForeignKey('venta.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)
    forma_pago_id = db.Column(db.Integer, db.ForeignKey('forma_pago.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Integer, nullable=False)
    precio_total = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.String(50), nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)

    
    

