# Propiedad de los Alpes

Repositorio con código base para el desarrollo de una arquitectura hexagonal siguiendo los principios y patrones de DDD.


## Estructura del proyecto

El repositorio en su raíz está: 

- **src**: En este directorio encuentra el código fuente para PropiedadAlpes. En la siguiente sección se explica un poco mejor la estructura del mismo ([link](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure%3E) para más información)
- **tests**: Directorio con todos los archivos de prueba, tanto unitarios como de integración. Sigue el estándar [recomendado por pytest](https://docs.pytest.org/en/7.1.x/explanation/goodpractices.html) y usado por [boto](https://github.com/boto/boto).
- **.gitignore**: Archivo con la definición de archivos que se deben ignorar en el repositorio GIT
- **README.md**: El archivo que está leyendo :)
- **requirements.txt**: Archivo con los requerimientos para el correcto funcionamiento del proyecto (librerias Python)


## Ejecutar Aplicación

Desde el directorio principal ejecute el siguiente comando.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

```bash
flask --app src/propiedadlapes/api run
```

Siempre puede ejecutarlo en modo DEBUG:

```bash
flask --app src/propiedadlapes/api --debug run
```


## Request de ejemplo

Los siguientes JSON pueden ser usados para probar el API:

### 

- **Endpoint**: `/companias/coleccion`
- **Método**: `POST`
- **Headers**: `Content-Type='aplication/json'`

```json
{
    "nombre": "REMAX STRATUM Q S.A.S.",
    "numero_identificacion": "NIT901253697-7",
    "codigo_iso_pais": "COL",
    "contactos_clave": [
        {
            "nombre": "Edgar Vivar Villanueva",
            "numero_telefono": "+57876543786",
        },
        {
            "nombre": "Roberto Gomez Bolaños",
            "numero_telefono": "+5715551234",
        },
    ],
    "sucursales": [
        {
            "departamento": "Antioquia",
            "distrito": "Medellin",
            "direcciones": [
                {
                    "nombre": "Avenida las perlas",
                    "numero": 150,
                    "codigo_postal": "050001"
                }
            ]
        }
    ]
}
```

### Ver Reserva(s)

- **Endpoint**: `/companias/coleccion/{id}`
- **Método**: `GET`
- **Headers**: `Content-Type='aplication/json'`

## Ejecutar pruebas

```bash
coverage run -m pytest
```

# Ver reporte de covertura
```bash
coverage report
```
