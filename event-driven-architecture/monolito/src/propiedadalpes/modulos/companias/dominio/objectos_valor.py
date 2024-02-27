from dataclasses import dataclass, field

from aeroalpes.seedwork.dominio.objetos_valor import ObjetoValor

@dataclass(frozen=True)
class Itinerario(ObjetoValor):
    odos: list[Odo] = field(default_factory=list)

    @classmethod
    def es_ida_y_vuelta(self) -> bool:
        return self.odos[0].origen() == self.odos[-1].destino()

    @classmethod
    def es_solo_ida(self) -> bool:
        return len(self.odos) == 1

    def tipo_vuelo(self):
        if self.es_ida_y_vuelta():
            return TipoVuelo.IDA_Y_VUELTA
        elif self.es_solo_ida:
            return TipoVuelo.IDA
        else:
            return TipoVuelo.OPEN_JAW

    def ruta(self):
        if self.es_ida_y_vuelta():
            return f"{str(self.odos[0].origen())}-{str(self.odos[-1].origen())}"
        elif self.es_solo_ida:
            return f"{str(self.odos[0].origen())}-{str(self.odos[0].destino())}"
        else:
            return f"{str(self.odos[0].origen())}-{str(self.odos[-1].destino())}"