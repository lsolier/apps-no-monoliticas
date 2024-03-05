from dataclasses import dataclass, field
from propiedadalpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class PropiedadDTO(DTO):
    #id: str = field(default_factory=str)
    nombre: str = field(default_factory=str)
    ubicacion: str = field(default_factory=str)
    direccion: str = field(default_factory=str)
    ciudad: str = field(default_factory=str)