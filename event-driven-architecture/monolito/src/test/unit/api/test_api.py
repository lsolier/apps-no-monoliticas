import os
import tempfile

import pytest
import json

from propiedadalpes.api import create_app, importar_modelos_alchemy
from propiedadalpes.config.db import init_db
from propiedadalpes.config.db import db

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create a temporary file to isolate the database for each test
    db_fd, db_path = tempfile.mkstemp()
    # create the app with common test config
    app = create_app({"TESTING": True, "DATABASE": db_path})

    # create the database and load test data
    with app.app_context():
        init_db(app)

        from propiedadalpes.config.db import db

        importar_modelos_alchemy()
        db.create_all()

    yield app

    # close and remove the temporary database
    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()

def test_servidor_levanta(client):

    # Dado un cliente a endpoint health
    rv = client.get('/health')

    # Devuelve estados the UP el servidor
    assert rv.data is not None
    assert rv.status_code == 200

    response = json.loads(rv.data)

    assert response['status'] == 'up'


def ingesta_compania_correcta():
    return {
    "nombre": "REMAX STRATUM Q S.A.S.",
    "numero_identificacion": "NIT901253697-7",
    "codigo_iso_pais": "COL",
    "contactos_clave": [
        {
            "nombre": "Edgar Vivar Villanueva",
            "numero_telefono": "+57876543786"
        },
        {
            "nombre": "Roberto Gomez Bolaños",
            "numero_telefono": "+5715551234"
        }
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
                },
                {
                    "nombre": "Avenida alamedas",
                    "numero": 250,
                    "codigo_postal": "050501"
                }
            ]
        }
    ]
}

def test_reservar_vuelo(client):
    rv = client.post('/colecciones/companias', data=json.dumps(ingesta_compania_correcta()), content_type='application/json')
    assert rv is not None