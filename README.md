# Taller U3 — Automatización de BD con Python, Faker y Git

Proyecto desarrollado para la materia **Bases de Datos** (UdeA).  
Automatiza la creación y poblado de una tabla MySQL con 100.000 registros usando Python, SQLAlchemy y Faker.

---

## ¿Qué hace el script?

- Se conecta a una base de datos MySQL local usando **SQLAlchemy**
- Crea automáticamente la tabla `personas_juan` si no existe
- Genera **100.000 registros** de personas ficticias con la librería **Faker** (locale `es_CO`)
- Inserta los registros en lotes de 5.000 para mejor rendimiento

### Atributos de la tabla

| Columna           | Tipo        | Descripción                        |
|-------------------|-------------|------------------------------------|
| id                | INT (PK)    | Clave primaria autoincremental     |
| nombre            | VARCHAR     | Nombre de pila                     |
| apellido          | VARCHAR     | Apellido                           |
| correo            | VARCHAR     | Correo electrónico                 |
| telefono          | VARCHAR     | Número de teléfono                 |
| ciudad            | VARCHAR     | Ciudad de residencia               |
| direccion         | VARCHAR     | Dirección completa                 |
| fecha_nacimiento  | DATE        | Fecha de nacimiento                |
| ocupacion         | VARCHAR     | Profesión u ocupación              |
| salario           | FLOAT       | Salario mensual                    |
| fecha_registro    | DATETIME    | Fecha y hora de registro           |

---

## Instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/JuanJoseLondoj-jpg/Taller_bd.git
cd Taller_bd
```

### 2. Crea y activa el entorno virtual

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac / Linux
source .venv/bin/activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configura las variables de entorno

Copia el archivo de ejemplo y completa con tus datos reales:

```bash
cp .env.example .env
```

Edita el archivo `.env`:

```
DB_USER=root
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=3306
DB_NAME=nombre_de_tu_bd
```

---

## Ejecución

```bash
python main.py
```

El script mostrará el progreso de inserción y al finalizar imprimirá el total de registros insertados.

---

## Verificación en DBeaver

Ejecuta el siguiente query para validar los registros:

```sql
SELECT COUNT(*) FROM personas_juan;
```

El resultado debe ser **100.000**.
