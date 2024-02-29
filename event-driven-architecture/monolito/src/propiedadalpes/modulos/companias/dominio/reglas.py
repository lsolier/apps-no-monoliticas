"""Reglas de negocio del dominio de cliente

En este archivo usted encontrará reglas de negocio del dominio de cliente

"""

from propiedadalpes.seedwork.dominio.reglas import ReglaNegocio
  
class IdentificadorCompaniaUnicoPorPais(ReglaNegocio):

    es_identificador_unico: bool

    def __init__(self, es_identificador_unico, mensaje='El identificador de una compania debe ser unico por pais'):
        super().__init__(mensaje)
        self.es_identificador_unico = es_identificador_unico

    def es_valido(self) -> bool:
        return self.es_identificador_unico