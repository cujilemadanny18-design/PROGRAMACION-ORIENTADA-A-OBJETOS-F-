class Usuario:
    def __init__(self, identificacion: str, nombre: str):
        if not identificacion.strip():
            raise ValueError(
                "La identificación no puede estar vacía."
            )

        if not nombre.strip():
            raise ValueError(
                "El nombre no puede estar vacío."
            )

        self.identificacion = identificacion.strip()
        self.nombre = nombre.strip()

    def convertir_a_diccionario(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre
        }

    @classmethod
    def desde_diccionario(cls, datos: dict) -> "Usuario":
        try:
            return cls(
                identificacion=str(datos["identificacion"]),
                nombre=str(datos["nombre"])
            )
        except KeyError as error:
            raise KeyError(
                f"Falta la clave {error} en el usuario."
            ) from error
