from flask import Flask, render_template, request, redirect, url_for, flash

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'  # Cambia esto a una clave secreta única y segura

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/efi_ppy_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importar modelos después de inicializar SQLAlchemy
import models

# Definir las rutas

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/almacenamiento')
def almacenamiento():
    todos_almacenamientos = models.Almacenamiento.query.filter_by(activo=True).all()
    return render_template('/complem/almacenamiento.html', almacenamientos=todos_almacenamientos)


# Crear un nuevo almacenamiento
@app.route('/almacenamiento/nuevo', methods=['GET', 'POST'])
def nuevo_almacenamiento():
    if request.method == 'POST':
        tipo = request.form['tipo']
        capacidad = request.form['capacidad']

        nuevo_almacenamiento = models.Almacenamiento(tipo=tipo, capacidad=capacidad)
        db.session.add(nuevo_almacenamiento)
        db.session.commit()

        return redirect(url_for('almacenamiento'))
    
    return render_template('/complem/nuevo_almacenamiento.html')

# Actualizar un almacenamiento existente
@app.route('/almacenamiento/editar/<int:id>', methods=['GET', 'POST'])
def editar_almacenamiento(id):
    almacenamiento = models.Almacenamiento.query.get_or_404(id)

    if request.method == 'POST':
        almacenamiento.tipo = request.form['tipo']
        almacenamiento.capacidad = request.form['capacidad']
        db.session.commit()

        return redirect(url_for('almacenamiento'))
    
    return render_template('/complem/editar_almacenamiento.html', almacenamiento=almacenamiento)

# Eliminar (desactivar) un almacenamiento
@app.route('/almacenamiento/eliminar/<int:id>', methods=['POST'])
def eliminar_almacenamiento(id):
    almacenamiento = models.Almacenamiento.query.get_or_404(id)
    almacenamiento.activo = False  # Desactivar en lugar de eliminar físicamente
    db.session.commit()

    return redirect(url_for('almacenamiento'))

@app.route('/compatibilidades')
def compatibilidades():
    compatibilidades = models.Compatibilidad.query.all()
    return render_template('compatibilidad.html', compatibilidades=compatibilidades)

@app.route('/compatibilidad/nueva', methods=['GET', 'POST'])
def nueva_compatibilidad():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nueva_compatibilidad = models.Compatibilidad(nombre=nombre)
        db.session.add(nueva_compatibilidad)
        db.session.commit()
        return redirect(url_for('compatibilidades'))
    return render_template('cargas/nueva_compatibilidad.html')

@app.route('/compatibilidad/editar/<int:id>', methods=['GET', 'POST'])
def editar_compatibilidad(id):
    compatibilidad = models.Compatibilidad.query.get_or_404(id)
    if request.method == 'POST':
        compatibilidad.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('compatibilidades'))
    return render_template('edits/editar_compatibilidad.html', compatibilidad=compatibilidad)

@app.route('/compatibilidad/eliminar/<int:id>', methods=['POST'])
def eliminar_compatibilidad(id):
    compatibilidad = models.Compatibilidad.query.get_or_404(id)
    db.session.delete(compatibilidad)
    db.session.commit()
    return redirect(url_for('compatibilidades'))



@app.route('/condiciones')
def condiciones():
    todas_condiciones = models.Condicion.query.all()
    return render_template('condicion.html', condiciones=todas_condiciones)

@app.route('/condicion/nueva', methods=['GET', 'POST'])
def nueva_condicion():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nueva_condicion = models.Condicion(nombre=nombre)
        db.session.add(nueva_condicion)
        db.session.commit()
        return redirect(url_for('condiciones'))
    return render_template('cargas/nueva_condicion.html')

@app.route('/condicion/editar/<int:id>', methods=['GET', 'POST'])
def editar_condicion(id):
    condicion = models.Condicion.query.get_or_404(id)
    if request.method == 'POST':
        condicion.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('condiciones'))
    return render_template('edits/editar_condicion.html', condicion=condicion)

@app.route('/condicion/eliminar/<int:id>', methods=['POST'])
def eliminar_condicion(id):
    condicion = models.Condicion.query.get_or_404(id)
    db.session.delete(condicion)
    db.session.commit()
    return redirect(url_for('condiciones'))




@app.route('/condiciones_fiscales')
def condiciones_fiscales():
    todas_condiciones_fiscales = models.CondicionFiscal.query.all()
    return render_template('condicionFiscal.html', condiciones=todas_condiciones_fiscales)

@app.route('/condicionFiscal/nueva', methods=['GET', 'POST'])
def nueva_condicionFiscal():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nueva_condicionFiscal = models.CondicionFiscal(nombre=nombre)
        db.session.add(nueva_condicionFiscal)
        db.session.commit()
        return redirect(url_for('condiciones_fiscales'))  # Aquí va el nombre de la función, no la URL
    return render_template('cargas/nueva_condicionFiscal.html')

@app.route('/condicionFiscal/editar/<int:id>', methods=['GET', 'POST'])
def editar_condicionFiscal(id):
    condicionFiscal = models.CondicionFiscal.query.get_or_404(id)
    if request.method == 'POST':
        condicionFiscal.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('condiciones_fiscales'))  # Aquí también
    return render_template('edits/editar_condicionFiscal.html', condicionFiscal=condicionFiscal)


@app.route('/condicionFiscal/eliminar/<int:id>', methods=['POST'])
def eliminar_condicionFiscal(id):
    condicionFiscal = models.CondicionFiscal.query.get_or_404(id)
    db.session.delete(condicionFiscal)
    db.session.commit()
    return redirect(url_for('condiciones_fiscales'))


@app.route('/personas')
def lista_personas():
    todas_personas = models.Persona.query.all()
    return render_template('complem/listado_persona.html', personas=todas_personas)

@app.route('/persona/nueva', methods=['GET', 'POST'])
def nueva_persona():
    if request.method == 'POST':
        nombre = request.form['nombre']
        tipo_documento = request.form['tipo_documento']
        documento = request.form['documento']
        num_contacto = request.form['num_contacto']
        correo = request.form['correo']
        direccion = request.form['direccion']
        activo = True if request.form.get('activo') else False

        # Verifica si ya existe una persona con el mismo tipo de documento y número de documento
        persona_existente = models.Persona.query.filter_by(tipo_documento=tipo_documento, documento=documento).first()
        if persona_existente:
            flash('Ya existe una persona con el mismo tipo de documento y número de documento.')
            return redirect(url_for('nueva_persona'))

        nueva_persona = models.Persona(
            nombre=nombre, tipo_documento=tipo_documento, documento=documento,
            num_contacto=num_contacto, correo=correo, direccion=direccion, activo=activo
        )
        db.session.add(nueva_persona)
        db.session.commit()
        flash('Persona creada con éxito')
        return redirect(url_for('lista_personas'))
    return render_template('cargas/nueva_persona.html')


@app.route('/persona/editar/<int:id>', methods=['GET', 'POST'])
def editar_persona(id):
    persona = models.Persona.query.get_or_404(id)
    if request.method == 'POST':
        nombre = request.form['nombre']
        tipo_documento = request.form['tipo_documento']
        documento = request.form['documento']
        num_contacto = request.form['num_contacto']
        correo = request.form['correo']
        direccion = request.form['direccion']
        activo = True if request.form.get('activo') else False

        # Verifica si ya existe una persona con el mismo tipo de documento y número de documento
        persona_existente = models.Persona.query.filter_by(tipo_documento=tipo_documento, documento=documento).first()
        if persona_existente and persona_existente.id != id:
            flash('Ya existe una persona con el mismo tipo de documento y número de documento.')
            return redirect(url_for('editar_persona', id=id))

        persona.nombre = nombre
        persona.tipo_documento = tipo_documento
        persona.documento = documento
        persona.num_contacto = num_contacto
        persona.correo = correo
        persona.direccion = direccion
        persona.activo = activo

        db.session.commit()
        flash('Persona actualizada con éxito')
        return redirect(url_for('lista_personas'))
    return render_template('edits/editar_persona.html', persona=persona)


@app.route('/persona/eliminar/<int:id>', methods=['POST'])
def eliminar_persona(id):
    persona = models.Persona.query.get_or_404(id)
    db.session.delete(persona)
    db.session.commit()
    flash('Persona eliminada con éxito')
    return redirect(url_for('lista_personas'))




@app.route('/formas_pago')
def formas_pago():
    todas_formas_pago = models.FormaPago.query.all()
    return render_template('formaPago.html', formas=todas_formas_pago)

@app.route('/formaPago/nueva', methods=['GET', 'POST'])
def nueva_formaPago():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nueva_formaPago = models.FormaPago(nombre=nombre)
        db.session.add(nueva_formaPago)
        db.session.commit()
        return redirect(url_for('complem/formaPago'))
    return render_template('cargas/nueva_formaPago.html')

@app.route('/formaPago/editar/<int:id>', methods=['GET', 'POST'])
def editar_formaPago(id):
    formaPago = models.FormaPago.query.get_or_404(id)
    if request.method == 'POST':
        formaPago.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('complem/formaPago'))
    return render_template('edits/editar_formaPago.html', formaPago=formaPago)

@app.route('/formaPago/eliminar/<int:id>', methods=['POST'])
def eliminar_formaPago(id):
    formaPago = models.FormaPago.query.get_or_404(id)
    db.session.delete(formaPago)
    db.session.commit()
    return redirect(url_for('complem/formaPago'))




@app.route('/garantias')
def garantias():
    todas_garantias = models.Garantia.query.all()
    return render_template('garantia.html', garantias=todas_garantias)

@app.route('/garantia/nueva', methods=['GET', 'POST'])
def nueva_garantia():
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        nueva_garantia = models.Garantia(descripcion=descripcion)
        db.session.add(nueva_garantia)
        db.session.commit()
        return redirect(url_for('comples/garantia'))
    return render_template('cargas/nueva_garantia.html')

@app.route('/garantia/editar/<int:id>', methods=['GET', 'POST'])
def editar_garantia(id):
    garantia = models.Garantia.query.get_or_404(id)
    if request.method == 'POST':
        garantia.descripcion = request.form['descripcion']
        db.session.commit()
        return redirect(url_for('garantias'))
    return render_template('edits/editar_garantia.html', garantia=garantia)

@app.route('/garantia/eliminar/<int:id>', methods=['POST'])
def eliminar_garantia(id):
    garantia = models.Garantia.query.get_or_404(id)
    db.session.delete(garantia)
    db.session.commit()
    return redirect(url_for('garantias'))



@app.route('/paises')
def paises():
    todos_paises = models.Pais.query.all()
    return render_template('pais.html', paises=todos_paises)

@app.route('/pais/nuevo', methods=['GET', 'POST'])
def nuevo_pais():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevo_pais = models.Pais(nombre=nombre)
        db.session.add(nuevo_pais)
        db.session.commit()
        return redirect(url_for('paises'))
    return render_template('cargas/nuevo_pais.html')

@app.route('/pais/editar/<int:id>', methods=['GET', 'POST'])
def editar_pais(id):
    pais = models.Pais.query.get_or_404(id)
    if request.method == 'POST':
        pais.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('paises'))
    return render_template('edits/editar_pais.html', pais=pais)

@app.route('/pais/eliminar/<int:id>', methods=['POST'])
def eliminar_pais(id):
    pais = models.Pais.query.get_or_404(id)
    db.session.delete(pais)
    db.session.commit()
    return redirect(url_for('paises'))



@app.route('/posiciones')
def posiciones():
    todas_posiciones = models.Posicion.query.all()
    return render_template('posicion.html', posiciones=todas_posiciones)

@app.route('/posicion/nueva', methods=['GET', 'POST'])
def nueva_posicion():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nueva_posicion = models.Posicion(nombre=nombre)
        db.session.add(nueva_posicion)
        db.session.commit()
        return redirect(url_for('posiciones'))
    return render_template('cargas/nueva_posicion.html')

@app.route('/posicion/editar/<int:id>', methods=['GET', 'POST'])
def editar_posicion(id):
    posicion = models.Posicion.query.get_or_404(id)
    if request.method == 'POST':
        posicion.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('posiciones'))
    return render_template('edits/editar_posicion.html', posicion=posicion)

@app.route('/posicion/eliminar/<int:id>', methods=['POST'])
def eliminar_posicion(id):
    posicion = models.Posicion.query.get_or_404(id)
    db.session.delete(posicion)
    db.session.commit()
    return redirect(url_for('posiciones'))





@app.route('/puestos')
def puestos():
    todos_puestos = models.Puesto.query.all()
    return render_template('puesto.html', puestos=todos_puestos)

@app.route('/puesto/nuevo', methods=['GET', 'POST'])
def nuevo_puesto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevo_puesto = models.Puesto(nombre=nombre)
        db.session.add(nuevo_puesto)
        db.session.commit()
        return redirect(url_for('puestos'))
    return render_template('cargas/nuevo_puesto.html')

@app.route('/puesto/editar/<int:id>', methods=['GET', 'POST'])
def editar_puesto(id):
    puesto = models.Puesto.query.get_or_404(id)
    if request.method == 'POST':
        puesto.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('puestos'))
    return render_template('edits/editar_puesto.html', puesto=puesto)

@app.route('/puesto/eliminar/<int:id>', methods=['POST'])
def eliminar_puesto(id):
    puesto = models.Puesto.query.get_or_404(id)
    db.session.delete(puesto)
    db.session.commit()
    return redirect(url_for('puestos'))




@app.route('/tipos')
def tipos():
    todos_tipos = models.Tipo.query.all()
    return render_template('tipo.html', tipos=todos_tipos)

@app.route('/tipo/nuevo', methods=['GET', 'POST'])
def nuevo_tipo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevo_tipo = models.Tipo(nombre=nombre)
        db.session.add(nuevo_tipo)
        db.session.commit()
        return redirect(url_for('tipos'))
    return render_template('cargas/nuevo_tipo.html')

@app.route('/tipo/editar/<int:id>', methods=['GET', 'POST'])
def editar_tipo(id):
    tipo = models.Tipo.query.get_or_404(id)
    if request.method == 'POST':
        tipo.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('tipos'))
    return render_template('edits/editar_tipo.html', tipo=tipo)

@app.route('/tipo/eliminar/<int:id>', methods=['POST'])
def eliminar_tipo(id):
    tipo = models.Tipo.query.get_or_404(id)
    db.session.delete(tipo)
    db.session.commit()
    return redirect(url_for('tipos'))





@app.route('/tipos_documento')
def tipos_documento():
    todos_tipos_documento = models.TipoDocumento.query.all()
    return render_template('tipo_documento.html', tipos_documento=todos_tipos_documento)

@app.route('/tipo_documento/nuevo', methods=['GET', 'POST'])
def nuevo_tipo_documento():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevo_tipo_documento = models.TipoDocumento(nombre=nombre)
        db.session.add(nuevo_tipo_documento)
        db.session.commit()
        return redirect(url_for('tipos_documento'))
    return render_template('cargas/nuevo_tipo_documento.html')

@app.route('/tipo_documento/editar/<int:id>', methods=['GET', 'POST'])
def editar_tipo_documento(id):
    tipo_documento = models.TipoDocumento.query.get_or_404(id)
    if request.method == 'POST':
        tipo_documento.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('tipos_documento'))
    return render_template('edits/editar_tipo_documento.html', tipo_documento=tipo_documento)

@app.route('/tipo_documento/eliminar/<int:id>', methods=['POST'])
def eliminar_tipo_documento(id):
    tipo_documento = models.TipoDocumento.query.get_or_404(id)
    db.session.delete(tipo_documento)
    db.session.commit()
    return redirect(url_for('tipos_documento'))




@app.route('/accesorios')
def accesorios():
    todos_accesorios = models.Accesorio.query.all()
    return render_template('accesorios.html', accesorios=todos_accesorios)



@app.route('/accesorio/nuevo', methods=['GET', 'POST'])
def nuevo_accesorio():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        activo = request.form.get('activo', 'false') == 'true'
        nuevo_accesorio = models.Accesorio(nombre=nombre, precio=precio, activo=activo)
        db.session.add(nuevo_accesorio)
        db.session.commit()
        return redirect(url_for('accesorios'))
    return render_template('cargas/nuevo_accesorio.html')

@app.route('/accesorio/editar/<int:id>', methods=['GET', 'POST'])
def editar_accesorio(id):
    accesorio = models.Accesorio.query.get_or_404(id)
    if request.method == 'POST':
        accesorio.nombre = request.form['nombre']
        accesorio.precio = request.form['precio']
        accesorio.activo = request.form.get('activo', 'false') == 'true'
        db.session.commit()
        return redirect(url_for('accesorios'))
    return render_template('edits/editar_accesorio.html', accesorio=accesorio)

@app.route('/accesorio/eliminar/<int:id>', methods=['POST'])
def eliminar_accesorio(id):
    accesorio = models.Accesorio.query.get_or_404(id)
    db.session.delete(accesorio)
    db.session.commit()
    return redirect(url_for('accesorios'))



@app.route('/caracteristicas')
def caracteristicas():
    todas_caracteristicas = models.Caracteristica.query.all()
    return render_template('caracteristicas.html', caracteristicas=todas_caracteristicas)

@app.route('/caracteristicas/nueva', methods=['GET', 'POST'])
def nueva_caracteristica():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nueva_caracteristica = models.Caracteristica(nombre=nombre)
        db.session.add(nueva_caracteristica)
        db.session.commit()
        return redirect(url_for('caracteristicas'))
    return render_template('cargas/nueva_caracteristica.html')

@app.route('/caracteristicas/editar/<int:id>', methods=['GET', 'POST'])
def editar_caracteristica(id):
    caracteristica = models.Caracteristica.query.get_or_404(id)
    if request.method == 'POST':
        caracteristica.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('caracteristicas'))
    return render_template('edits/editar_caracteristica.html', caracteristica=caracteristica)

@app.route('/caracteristicas/eliminar/<int:id>', methods=['POST'])
def eliminar_caracteristica(id):
    caracteristica = models.Caracteristica.query.get_or_404(id)
    db.session.delete(caracteristica)
    db.session.commit()
    return redirect(url_for('caracteristicas'))


@app.route('/equipo')
def equipo():
    todos_equipos = models.Equipo.query.all()
    return render_template('equipo.html', equipos=todos_equipos)

@app.route('/equipo/nuevo', methods=['GET', 'POST'])
def nuevo_equipo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        modelo = request.form['modelo']
        nuevo_equipo = models.Equipo(nombre=nombre, modelo=modelo)
        db.session.add(nuevo_equipo)
        db.session.commit()
        return redirect(url_for('equipo'))
    return render_template('cargas/nuevo_equipo.html')

@app.route('/equipo/editar/<int:id>', methods=['GET', 'POST'])
def editar_equipo(id):
    equipo = models.Equipo.query.get_or_404(id)
    if request.method == 'POST':
        equipo.nombre = request.form['nombre']
        equipo.modelo = request.form['modelo']
        db.session.commit()
        return redirect(url_for('equipo'))
    return render_template('edits/editar_equipo.html', equipo=equipo)

@app.route('/equipo/eliminar/<int:id>', methods=['POST'])
def eliminar_equipo(id):
    equipo = models.Equipo.query.get_or_404(id)
    db.session.delete(equipo)
    db.session.commit()
    return redirect(url_for('equipo'))



@app.route('/fabricantes')
def fabricantes():
    todos_fabricantes = models.Fabricante.query.all()
    return render_template('fabricante.html', fabricantes=todos_fabricantes)

@app.route('/fabricante/nuevo', methods=['GET', 'POST'])
def nuevo_fabricante():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevo_fabricante = models.Fabricante(nombre=nombre)
        db.session.add(nuevo_fabricante)
        db.session.commit()
        return redirect(url_for('fabricantes'))
    return render_template('cargas/nuevo_fabricante.html')

@app.route('/fabricante/editar/<int:id>', methods=['GET', 'POST'])
def editar_fabricante(id):
    fabricante = models.Fabricante.query.get_or_404(id)
    if request.method == 'POST':
        fabricante.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('fabricantes'))
    return render_template('edits/editar_fabricante.html', fabricante=fabricante)

@app.route('/fabricante/eliminar/<int:id>', methods=['POST'])
def eliminar_fabricante(id):
    fabricante = models.Fabricante.query.get_or_404(id)
    db.session.delete(fabricante)
    db.session.commit()
    return redirect(url_for('fabricantes'))



@app.route('/marca')
def marca():
    todas_marcas = models.Marca.query.all()
    return render_template('marca.html', marcas=todas_marcas)

@app.route('/marca/nueva', methods=['GET', 'POST'])
def nueva_marca():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nueva_marca = models.Marca(nombre=nombre)
        db.session.add(nueva_marca)
        db.session.commit()
        return redirect(url_for('marca'))
    return render_template('cargas/nueva_marca.html')

@app.route('/marca/editar/<int:id>', methods=['GET', 'POST'])
def editar_marca(id):
    marca = models.Marca.query.get_or_404(id)
    if request.method == 'POST':
        marca.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('marca'))
    return render_template('edits/editar_marca.html', marca=marca)

@app.route('/marca/eliminar/<int:id>', methods=['POST'])
def eliminar_marca(id):
    marca = models.Marca.query.get_or_404(id)
    db.session.delete(marca)
    db.session.commit()
    return redirect(url_for('marca'))



@app.route('/modelos')
def modelos():
    todos_modelos = models.Modelo.query.all()
    return render_template('modelos.html', modelos=todos_modelos)

@app.route('/modelo/nuevo', methods=['GET', 'POST'])
def nuevo_modelo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        fabricante_id = request.form['fabricante_id']
        nuevo_modelo = models.Modelo(nombre=nombre, fabricante_id=fabricante_id)
        db.session.add(nuevo_modelo)
        db.session.commit()
        return redirect(url_for('modelos'))
    fabricantes = models.Fabricante.query.all()
    return render_template('cargas/nuevo_modelo.html', fabricantes=fabricantes)

@app.route('/modelo/editar/<int:id>', methods=['GET', 'POST'])
def editar_modelo(id):
    modelo = models.Modelo.query.get_or_404(id)
    if request.method == 'POST':
        modelo.nombre = request.form['nombre']
        modelo.fabricante_id = request.form['fabricante_id']
        db.session.commit()
        return redirect(url_for('modelos'))
    fabricantes = models.Fabricante.query.all()
    return render_template('edits/editar_modelo.html', modelo=modelo, fabricantes=fabricantes)

@app.route('/modelo/eliminar/<int:id>', methods=['POST'])
def eliminar_modelo(id):
    modelo = models.Modelo.query.get_or_404(id)
    db.session.delete(modelo)
    db.session.commit()
    return redirect(url_for('modelos'))



@app.route('/stocks')
def stocks():
    todos_stocks = models.Stock.query.all()
    return render_template('stocks.html', stocks=todos_stocks)

@app.route('/stock/nuevo', methods=['GET', 'POST'])
def nuevo_stock():
    if request.method == 'POST':
        cantidad = request.form['cantidad']
        equipo_id = request.form['equipo_id']
        nuevo_stock = models.Stock(cantidad=cantidad, equipo_id=equipo_id)
        db.session.add(nuevo_stock)
        db.session.commit()
        return redirect(url_for('stocks'))
    equipos = models.Equipo.query.all()
    return render_template('cargas/nuevo_stock.html', equipos=equipos)

@app.route('/stock/editar/<int:id>', methods=['GET', 'POST'])
def editar_stock(id):
    stock = models.Stock.query.get_or_404(id)
    if request.method == 'POST':
        stock.cantidad = request.form['cantidad']
        stock.equipo_id = request.form['equipo_id']
        db.session.commit()
        return redirect(url_for('stocks'))
    equipos = models.Equipo.query.all()
    return render_template('edits/editar_stock.html', stock=stock, equipos=equipos)

@app.route('/stock/eliminar/<int:id>', methods=['POST'])
def eliminar_stock(id):
    stock = models.Stock.query.get_or_404(id)
    db.session.delete(stock)
    db.session.commit()
    return redirect(url_for('stocks'))



@app.route('/ventas')
def ventas():
    todas_ventas = models.Venta.query.all()
    return render_template('ventas.html', ventas=todas_ventas)

@app.route('/venta/nueva', methods=['GET', 'POST'])
def nueva_venta():
    if request.method == 'POST':
        fecha = request.form['fecha']
        cliente_id = request.form['cliente_id']
        total = request.form['total']
        nueva_venta = models.Venta(fecha=fecha, cliente_id=cliente_id, total=total)
        db.session.add(nueva_venta)
        db.session.commit()
        return redirect(url_for('ventas'))
    clientes = models.Cliente.query.all()
    return render_template('cargas/nueva_venta.html', clientes=clientes)

@app.route('/venta/editar/<int:id>', methods=['GET', 'POST'])
def editar_venta(id):
    venta = models.Venta.query.get_or_404(id)
    if request.method == 'POST':
        venta.fecha = request.form['fecha']
        venta.cliente_id = request.form['cliente_id']
        venta.total = request.form['total']
        db.session.commit()
        return redirect(url_for('ventas'))
    clientes = models.Cliente.query.all()
    return render_template('edits/editar_venta.html', venta=venta, clientes=clientes)

@app.route('/venta/eliminar/<int:id>', methods=['POST'])
def eliminar_venta(id):
    venta = models.Venta.query.get_or_404(id)
    db.session.delete(venta)
    db.session.commit()
    return redirect(url_for('ventas'))


@app.route('/ordenes_pago')
def ordenes_pago():
    todas_ordenes = models.orden_Pago.query.all()
    return render_template('ordenPago.html', ordenes=todas_ordenes)

@app.route('/ordenPago/nueva', methods=['GET', 'POST'])
def nueva_ordenPago():
    if request.method == 'POST':
        cliente_id = request.form['cliente_id']
        venta_id = request.form['venta_id']
        producto_id = request.form['producto_id']
        forma_pago_id = request.form['forma_pago_id']
        cantidad = request.form['cantidad']
        precio_unitario = request.form['precio_unitario']
        precio_total = request.form['precio_total']
        descripcion = request.form['descripcion']
        nueva_orden = models.orden_Pago(
            cliente_id=cliente_id,
            venta_id=venta_id,
            producto_id=producto_id,
            forma_pago_id=forma_pago_id,
            cantidad=cantidad,
            precio_unitario=precio_unitario,
            precio_total=precio_total,
            descripcion=descripcion
        )
        db.session.add(nueva_orden)
        db.session.commit()
        return redirect(url_for('ordenes_pago'))
    return render_template('cargas/nueva_ordenPago.html')

@app.route('/ordenPago/editar/<int:id>', methods=['GET', 'POST'])
def editar_ordenPago(id):
    orden = models.orden_Pago.query.get_or_404(id)
    if request.method == 'POST':
        orden.cliente_id = request.form['cliente_id']
        orden.venta_id = request.form['venta_id']
        orden.producto_id = request.form['producto_id']
        orden.forma_pago_id = request.form['forma_pago_id']
        orden.cantidad = request.form['cantidad']
        orden.precio_unitario = request.form['precio_unitario']
        orden.precio_total = request.form['precio_total']
        orden.descripcion = request.form['descripcion']
        db.session.commit()
        return redirect(url_for('ordenes_pago'))
    return render_template('edits/editar_ordenPago.html', orden=orden)

@app.route('/ordenPago/eliminar/<int:id>', methods=['POST'])
def eliminar_ordenPago(id):
    orden = models.orden_Pago.query.get_or_404(id)
    db.session.delete(orden)
    db.session.commit()
    return redirect(url_for('ordenes_pago'))




@app.route('/clientes')
def clientes():
    todos_clientes = models.Cliente.query.all()
    return render_template('clientes.html', clientes=todos_clientes)

@app.route('/cliente/nuevo', methods=['GET', 'POST'])
def nuevo_cliente():
    if request.method == 'POST':
        condiciones_fiscales_id = request.form.get('condiciones_fiscales_id')
        persona_id = request.form.get('persona_id')

        # Verificar si la persona existe
        persona = models.Persona.query.get(persona_id)
        if not persona:
            flash('La persona especificada no existe.')
            return redirect(url_for('nuevo_cliente'))

        # Crear el cliente
        nuevo_cliente = models.Cliente(condiciones_fiscales_id = condiciones_fiscales_id, persona_id=persona_id)
        db.session.add(nuevo_cliente)
        db.session.commit()
        flash('Cliente creado con éxito')
        return redirect(url_for('clientes'))

    personas = models.Persona.query.all()
    return render_template('cargas/nuevo_cliente.html', personas=personas)

@app.route('/cliente/editar/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    cliente = models.Cliente.query.get_or_404(id)
    if request.method == 'POST':
        cliente.nombre = request.form['nombre']
        cliente.email = request.form['email']
        db.session.commit()
        return redirect(url_for('clientes'))
    return render_template('edits/editar_cliente.html', cliente=cliente)

@app.route('/cliente/eliminar/<int:id>', methods=['POST'])
def eliminar_cliente(id):
    cliente = models.Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('clientes'))



@app.route('/empleados')
def empleados():
    todos_empleados = models.Empleado.query.all()
    return render_template('empleados.html', empleados=todos_empleados)

@app.route('/nuevo_empleado', methods=['GET', 'POST'])
def nuevo_empleado():
    if request.method == 'POST':
        nombre = request.form['nombre']
        persona_id = request.form.get('persona_id')

        if not persona_id:
            return "Debes seleccionar una persona para crear un empleado.", 400

        persona = models.Persona.query.get(persona_id)
        if not persona:
            return "La persona seleccionada no existe.", 400

        nuevo_empleado = models.Empleado(nombre=nombre, persona_id=persona_id)
        db.session.add(nuevo_empleado)
        db.session.commit()
        return redirect(url_for('lista_empleados'))

    personas = models.Persona.query.all()
    return render_template('cargas/nuevo_empleado.html', personas=personas)

@app.route('/empleado/editar/<int:id>', methods=['GET', 'POST'])
def editar_empleado(id):
    empleado = models.Empleado.query.get_or_404(id)
    if request.method == 'POST':
        empleado.nombre = request.form['nombre']
        empleado.email = request.form['email']
        db.session.commit()
        return redirect(url_for('empleados'))
    return render_template('edits/editar_empleado.html', empleado=empleado)

@app.route('/empleado/eliminar/<int:id>', methods=['POST'])
def eliminar_empleado(id):
    empleado = models.Empleado.query.get_or_404(id)
    db.session.delete(empleado)
    db.session.commit()
    return redirect(url_for('empleados'))




@app.route('/proveedores')
def proveedores():
    todos_proveedores = models.Proveedor.query.all()
    return render_template('proveedores.html', proveedores=todos_proveedores)

@app.route('/proveedor/nuevo', methods=['GET', 'POST'])
def nuevo_proveedor():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contacto = request.form['contacto']
        nuevo_proveedor = models.Proveedor(nombre=nombre, contacto=contacto)
        db.session.add(nuevo_proveedor)
        db.session.commit()
        return redirect(url_for('proveedores'))
    return render_template('cargas/nuevo_proveedor.html')

@app.route('/proveedor/editar/<int:id>', methods=['GET', 'POST'])
def editar_proveedor(id):
    proveedor = models.Proveedor.query.get_or_404(id)
    if request.method == 'POST':
        proveedor.nombre = request.form['nombre']
        proveedor.contacto = request.form['contacto']
        db.session.commit()
        return redirect(url_for('proveedores'))
    return render_template('edits/editar_proveedor.html', proveedor=proveedor)

@app.route('/proveedor/eliminar/<int:id>', methods=['POST'])
def eliminar_proveedor(id):
    proveedor = models.Proveedor.query.get_or_404(id)
    db.session.delete(proveedor)
    db.session.commit()
    return redirect(url_for('proveedores'))








if __name__ == '__main__':
    app.run(debug=True)
