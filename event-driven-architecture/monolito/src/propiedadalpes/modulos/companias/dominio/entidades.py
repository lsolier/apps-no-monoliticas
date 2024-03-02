"""Entidades del dominio de vuelos

En este archivo usted encontrará las entidades del dominio de vuelos

"""

from __future__ import annotations
from dataclasses import dataclass, field
from itertools import groupby

import propiedadalpes.modulos.companias.dominio.objetos_valor as ov
from propiedadalpes.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class Contacto(Entidad):
    nombre: str = field(default_factory=str)
    numero_telefono: str = field(default_factory=str)

@dataclass
class Sucursal(Entidad):
    departamento: str = field(default_factory=str)
    distrito: str = field(default_factory=str)
    direcciones: list[ov.Direccion] = field(default_factory=list)

@dataclass
class Compania(AgregacionRaiz):
    nombre: str = field(default_factory=str)
    numero_identificacion: str = field(default_factory=str)
    codigo_iso_pais: str = field(default_factory=str)
    contactos: list[Contacto] = field(default_factory=list)
    sucursales: list[Sucursal] = field(default_factory=list)

    def obtener_sucursales_por_departamento(self, departamento: str):
        sucursales_por_departamento: list[Sucursal] = sorted(self.sucursales,  key=lambda sucural: sucural.departamento)
        sucursales_agrupadas = {}
        for clave, grupo in groupby(sucursales_por_departamento, lambda sucural: sucural.departamento):
            sucursales_agrupadas[clave] = list(grupo)
        return sucursales_agrupadas[departamento]
    
    def obtener_sucursales_por_distrito(self, distrito: str):
        sucursales_por_distrito: list[Sucursal] = sorted(self.sucursales,  key=lambda sucural: sucural.distrito)
        sucursales_agrupadas = {}
        for clave, grupo in groupby(sucursales_por_distrito, lambda sucural: sucural.distrito):
            sucursales_agrupadas[clave] = list(grupo)
        return sucursales_agrupadas[distrito]
