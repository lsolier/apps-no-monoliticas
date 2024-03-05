from dataclasses import dataclass, field
from propiedadalpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class UsuarioDTO(DTO):
    id: str = field(default_factory=str)
    nombre: str = field(default_factory=str)