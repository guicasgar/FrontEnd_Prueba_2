from enum import Enum


class Estado(Enum):
    Original = 0
    Alta = 1
    Baja = 2
    Modificado = 3  # Tiene fecha de modificación rellena.
    ModificadoNuevo = 4  # Tiene fecha mod rellena y es más reciente que la última sincronización
    ConflictoModificados = 5  # El registro local y el de servidor están modificados independientemente
    ConflictoModificadoBaja = 6  # Registro local baja y servidor modificado o viceversa
