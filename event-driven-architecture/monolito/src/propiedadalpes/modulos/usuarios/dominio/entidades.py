from __future__ import annotations
from dataclasses import dataclass, field
from itertools import groupby
from propiedadalpes.modulos.usuarios.dominio.eventos import UsuarioIngestado


from propiedadalpes.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass 
class Usuario(AgregacionRaiz):
    nombre: str = field(default_factory=str)

    def ingestar_usuario(self, usuario: Usuario):
        self.nombre = usuario.nombre

        self.agregar_evento(UsuarioIngestado(id_usuario=self.id, nombre=self.nombre))
