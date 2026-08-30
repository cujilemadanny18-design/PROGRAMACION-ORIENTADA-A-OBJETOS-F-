import json
from pathlib import Path

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:
    def __init__(self, carpeta_datos: str = "datos"):
        self.carpeta_datos = Path(carpeta_datos)

        self.carpeta_datos.mkdir(
            parents=True,
            exist_ok=True
        )

        self.archivo_productos = (
            self.carpeta_datos / "productos.json"
        )

        self.archivo_usuarios = (
            self.carpeta_datos / "usuarios.json"
        )

        self.archivo_ventas = (
            self.carpeta_datos / "ventas.json"
        )

    def _leer_json(self, ruta: Path) -> list[dict]:
        try:
            with open(
                ruta,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

            if not isinstance(datos, list):
                raise ValueError(
                    f"El archivo {ruta.name} debe contener "
                    "una lista JSON."
                )

            return datos

        except FileNotFoundError:
            return []

        except json.JSONDecodeError as error:
            print(
                f"Error: el archivo {ruta.name} contiene "
                f"JSON inválido: {error}"
            )
            return []

        except PermissionError as error:
            print(
                f"Error: no hay permisos para leer "
                f"{ruta.name}: {error}"
            )
            return []

    def _guardar_json(
        self,
        ruta: Path,
        datos: list[dict]
    ) -> bool:

        try:
            with open(
                ruta,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

            return True

        except PermissionError as error:
            print(
                f"Error: no hay permisos para escribir "
                f"{ruta.name}: {error}"
            )
            return False

    def cargar_productos(self) -> list[Producto]:
        productos = []

        for datos in self._leer_json(
            self.archivo_productos
        ):
            try:
                producto = Producto.desde_diccionario(datos)
                productos.append(producto)

            except (KeyError, ValueError) as error:
                print(
                    f"Producto inválido en JSON: {error}"
                )

        return productos

    def cargar_usuarios(self) -> list[Usuario]:
        usuarios = []

        for datos in self._leer_json(
            self.archivo_usuarios
        ):
            try:
                usuario = Usuario.desde_diccionario(datos)
                usuarios.append(usuario)

            except (KeyError, ValueError) as error:
                print(
                    f"Usuario inválido en JSON: {error}"
                )

        return usuarios

    def cargar_ventas(self) -> list[Venta]:
        ventas = []

        for datos in self._leer_json(
            self.archivo_ventas
        ):
            try:
                venta = Venta.desde_diccionario(datos)
                ventas.append(venta)

            except (KeyError, ValueError) as error:
                print(
                    f"Venta inválida en JSON: {error}"
                )

        return ventas

    def guardar_productos(
        self,
        productos: list[Producto]
    ) -> bool:

        datos = [
            producto.convertir_a_diccionario()
            for producto in productos
        ]

        return self._guardar_json(
            self.archivo_productos,
            datos
        )

    def guardar_usuarios(
        self,
        usuarios: list[Usuario]
    ) -> bool:

        datos = [
            usuario.convertir_a_diccionario()
            for usuario in usuarios
        ]

        return self._guardar_json(
            self.archivo_usuarios,
            datos
        )

    def guardar_ventas(
        self,
        ventas: list[Venta]
    ) -> bool:

        datos = [
            venta.convertir_a_diccionario()
            for venta in ventas
        ]

        return self._guardar_json(
            self.archivo_ventas,
            datos
        )

    def guardar_todo(
        self,
        productos: list[Producto],
        usuarios: list[Usuario],
        ventas: list[Venta]
    ) -> bool:

        productos_ok = self.guardar_productos(productos)
        usuarios_ok = self.guardar_usuarios(usuarios)
        ventas_ok = self.guardar_ventas(ventas)

        return (
            productos_ok
            and usuarios_ok
            and ventas_ok
        )
