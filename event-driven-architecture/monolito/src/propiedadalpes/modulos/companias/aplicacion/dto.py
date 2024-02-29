from dataclasses import dataclass, field
from propiedadalpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class DireccionDTO(DTO):
    nombre: str = field(default_factory=str)
    numero: int = field(default_factory=int)
    codigo_postal: str = field(default_factory=str)

@dataclass(frozen=True)
class SucursalDTO(DTO):
    departamento: str = field(default_factory=str)
    distrito: str = field(default_factory=str)
    direcciones: list[DireccionDTO] = field(default_factory=list)

@dataclass(frozen=True)
class ContactoDTO(DTO):
    nombre: str = field(default_factory=str)
    numero_telefono: str = field(default_factory=str)

@dataclass(frozen=True)
class CompaniaDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    nombre: str = field(default_factory=str)
    numero_identificacion: str = field(default_factory=str)
    codigo_iso_pais: str = field(default_factory=str)
    contactos: list[ContactoDTO] = field(default_factory=list)
    sucursales: list[SucursalDTO] = field(default_factory=list)