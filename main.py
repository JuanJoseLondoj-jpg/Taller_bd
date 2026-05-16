import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text, Column, Integer, String, Date, DateTime, Float
from sqlalchemy.orm import declarative_base
from faker import Faker
from datetime import datetime

load_dotenv()

Base = declarative_base()
fake = Faker('es_CO')


class PersonasJuan(Base):
    __tablename__ = 'personas_juan'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    correo = Column(String(150), nullable=False)
    telefono = Column(String(20))
    ciudad = Column(String(100))
    direccion = Column(String(200))
    fecha_nacimiento = Column(Date)
    ocupacion = Column(String(100))
    salario = Column(Float)
    fecha_registro = Column(DateTime, default=datetime.utcnow)


def get_engine():
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST', 'localhost')
    port = os.getenv('DB_PORT', '3306')
    database = os.getenv('DB_NAME')

    connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(connection_string, echo=False)
    return engine


def crear_tabla(engine):
    print("Creando tabla si no existe...")
    Base.metadata.create_all(engine)
    print("Tabla 'personas_juan' lista.")


def generar_registros(n=100_000):
    print(f"Generando {n:,} registros con Faker...")
    registros = []
    for _ in range(n):
        registros.append({
            'nombre': fake.first_name(),
            'apellido': fake.last_name(),
            'correo': fake.email(),
            'telefono': fake.phone_number(),
            'ciudad': fake.city(),
            'direccion': fake.address().replace('\n', ', '),
            'fecha_nacimiento': fake.date_of_birth(minimum_age=18, maximum_age=80),
            'ocupacion': fake.job(),
            'salario': round(fake.random_number(digits=7) / 100, 2),
            'fecha_registro': fake.date_time_this_decade(),
        })
    print("Registros generados.")
    return registros


def insertar_registros(engine, registros, batch_size=5000):
    print(f"Insertando {len(registros):,} registros en lotes de {batch_size:,}...")
    tabla = PersonasJuan.__table__
    total = len(registros)

    with engine.connect() as conn:
        for i in range(0, total, batch_size):
            lote = registros[i:i + batch_size]
            conn.execute(tabla.insert(), lote)
            conn.commit()
            print(f"  Insertados {min(i + batch_size, total):,} / {total:,}")

    print("Inserción completada.")


def main():
    engine = get_engine()
    crear_tabla(engine)
    registros = generar_registros(100_000)
    insertar_registros(engine, registros)

    with engine.connect() as conn:
        resultado = conn.execute(text("SELECT COUNT(*) FROM personas_juan"))
        count = resultado.scalar()
        print(f"\n✅ Total de registros en la tabla: {count:,}")


if __name__ == "__main__":
    main()
