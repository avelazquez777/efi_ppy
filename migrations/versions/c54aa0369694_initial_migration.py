"""Initial migration

Revision ID: c54aa0369694
Revises: 
Create Date: 2024-08-11 17:21:21.286224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c54aa0369694'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('almacenamiento',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('caracteristica',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('descripcion', sa.String(length=100), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('compatibilidad',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('condicion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('condicion_fiscal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('empresa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('razon_social', sa.String(length=50), nullable=False),
    sa.Column('cuit', sa.Integer(), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('forma_pago',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('garantia',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pais',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('persona',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('tipo_documento', sa.String(length=50), nullable=False),
    sa.Column('documento', sa.String(length=30), nullable=False),
    sa.Column('num_contacto', sa.String(length=30), nullable=False),
    sa.Column('correo', sa.String(length=50), nullable=False),
    sa.Column('direccion', sa.String(length=50), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('posicion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('puesto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tipo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tipo_documento',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cliente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('persona_id', sa.Integer(), nullable=False),
    sa.Column('condicion_fiscal_id', sa.Integer(), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['condicion_fiscal_id'], ['condicion_fiscal.id'], ),
    sa.ForeignKeyConstraint(['persona_id'], ['persona.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('empleado',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('persona_id', sa.Integer(), nullable=False),
    sa.Column('puesto_id', sa.Integer(), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['persona_id'], ['persona.id'], ),
    sa.ForeignKeyConstraint(['puesto_id'], ['puesto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fabricante',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('pais_id', sa.Integer(), nullable=False),
    sa.Column('num_contacto', sa.String(length=50), nullable=False),
    sa.Column('sede_principal', sa.String(length=50), nullable=False),
    sa.Column('pagina_web', sa.String(length=50), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['pais_id'], ['pais.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('marca',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('pais_id', sa.Integer(), nullable=False),
    sa.Column('num_contacto', sa.String(length=50), nullable=False),
    sa.Column('sede_principal', sa.String(length=50), nullable=False),
    sa.Column('pagina_web', sa.String(length=50), nullable=False),
    sa.Column('descripcion', sa.String(length=250), nullable=False),
    sa.Column('logotipo', sa.LargeBinary(), nullable=True),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['pais_id'], ['pais.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('proveedor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('razon_social', sa.String(length=50), nullable=False),
    sa.Column('pais_id', sa.Integer(), nullable=False),
    sa.Column('num_contacto', sa.String(length=50), nullable=False),
    sa.Column('sede_principal', sa.String(length=50), nullable=False),
    sa.Column('pagina_web', sa.String(length=50), nullable=False),
    sa.Column('descripcion', sa.String(length=100), nullable=False),
    sa.Column('logotipo', sa.LargeBinary(), nullable=True),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['pais_id'], ['pais.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('venta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fecha_venta', sa.DateTime(), nullable=False),
    sa.Column('total', sa.Integer(), nullable=False),
    sa.Column('empresa_id', sa.Integer(), nullable=False),
    sa.Column('tipo_documento', sa.String(length=50), nullable=False),
    sa.Column('estado', sa.String(length=50), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['empresa_id'], ['empresa.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('accesorio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('marca_id', sa.Integer(), nullable=False),
    sa.Column('tipo_id', sa.Integer(), nullable=False),
    sa.Column('condicion_id', sa.Integer(), nullable=False),
    sa.Column('compatibilidad_id', sa.Integer(), nullable=False),
    sa.Column('caracteristica_id', sa.Integer(), nullable=False),
    sa.Column('garantia_id', sa.Integer(), nullable=False),
    sa.Column('precio', sa.Integer(), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['caracteristica_id'], ['caracteristica.id'], ),
    sa.ForeignKeyConstraint(['compatibilidad_id'], ['compatibilidad.id'], ),
    sa.ForeignKeyConstraint(['condicion_id'], ['condicion.id'], ),
    sa.ForeignKeyConstraint(['garantia_id'], ['garantia.id'], ),
    sa.ForeignKeyConstraint(['marca_id'], ['marca.id'], ),
    sa.ForeignKeyConstraint(['tipo_id'], ['tipo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('modelo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo_id', sa.Integer(), nullable=False),
    sa.Column('marca_id', sa.Integer(), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['marca_id'], ['marca.id'], ),
    sa.ForeignKeyConstraint(['tipo_id'], ['tipo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('almacenamiento_id', sa.Integer(), nullable=False),
    sa.Column('cant_disponible', sa.Integer(), nullable=False),
    sa.Column('precio_compra', sa.Integer(), nullable=False),
    sa.Column('fecha_carga', sa.DateTime(), nullable=False),
    sa.Column('empleado_id', sa.Integer(), nullable=False),
    sa.Column('condicion_id', sa.Integer(), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['almacenamiento_id'], ['almacenamiento.id'], ),
    sa.ForeignKeyConstraint(['condicion_id'], ['condicion.id'], ),
    sa.ForeignKeyConstraint(['empleado_id'], ['empleado.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('equipo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('modelo_id', sa.Integer(), nullable=False),
    sa.Column('categoria', sa.String(length=50), nullable=False),
    sa.Column('condicion_id', sa.Integer(), nullable=False),
    sa.Column('compatibilidad_id', sa.Integer(), nullable=False),
    sa.Column('caracteristica_id', sa.Integer(), nullable=False),
    sa.Column('precio', sa.Integer(), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['caracteristica_id'], ['caracteristica.id'], ),
    sa.ForeignKeyConstraint(['compatibilidad_id'], ['compatibilidad.id'], ),
    sa.ForeignKeyConstraint(['condicion_id'], ['condicion.id'], ),
    sa.ForeignKeyConstraint(['modelo_id'], ['modelo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('producto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('equipo_id', sa.Integer(), nullable=False),
    sa.Column('accesorio_id', sa.Integer(), nullable=False),
    sa.Column('precio', sa.Integer(), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['accesorio_id'], ['accesorio.id'], ),
    sa.ForeignKeyConstraint(['equipo_id'], ['equipo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('venta_cliente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cliente_id', sa.Integer(), nullable=False),
    sa.Column('venta_id', sa.Integer(), nullable=False),
    sa.Column('producto_id', sa.Integer(), nullable=False),
    sa.Column('forma_pago_id', sa.Integer(), nullable=False),
    sa.Column('cantidad', sa.Integer(), nullable=False),
    sa.Column('precio_unitario', sa.Integer(), nullable=False),
    sa.Column('precio_total', sa.Integer(), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['cliente_id'], ['cliente.id'], ),
    sa.ForeignKeyConstraint(['forma_pago_id'], ['forma_pago.id'], ),
    sa.ForeignKeyConstraint(['producto_id'], ['producto.id'], ),
    sa.ForeignKeyConstraint(['venta_id'], ['venta.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('venta_cliente')
    op.drop_table('producto')
    op.drop_table('equipo')
    op.drop_table('stock')
    op.drop_table('modelo')
    op.drop_table('accesorio')
    op.drop_table('venta')
    op.drop_table('proveedor')
    op.drop_table('marca')
    op.drop_table('fabricante')
    op.drop_table('empleado')
    op.drop_table('cliente')
    op.drop_table('tipo_documento')
    op.drop_table('tipo')
    op.drop_table('puesto')
    op.drop_table('posicion')
    op.drop_table('persona')
    op.drop_table('pais')
    op.drop_table('garantia')
    op.drop_table('forma_pago')
    op.drop_table('empresa')
    op.drop_table('condicion_fiscal')
    op.drop_table('condicion')
    op.drop_table('compatibilidad')
    op.drop_table('caracteristica')
    op.drop_table('almacenamiento')
    # ### end Alembic commands ###
