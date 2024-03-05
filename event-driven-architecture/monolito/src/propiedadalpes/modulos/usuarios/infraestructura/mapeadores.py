from dataclasses import asdict
from itertools import groupby
from propiedadalpes.modulos.usuarios.dominio.eventos import UsuarioIngestado, EventoUsuario
from propiedadalpes.modulos.usuarios.infraestructura.despachadores import unix_time_millis

from propiedadalpes.seedwork.dominio.repositorios import Mapeador
from propiedadalpes.modulos.usuarios.dominio.entidades import Usuario
from .dto import Usuario as UsuarioDTO