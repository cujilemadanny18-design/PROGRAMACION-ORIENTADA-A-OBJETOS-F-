from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class restaurante:
    def __init__(
        self,
        archivo_servicio: ArchivoServicio | None = None
    ):
        self._archivo_servicio = (
            archivo_servicio or ArchivoServicio()
        )

        self._productos: list[Producto] = (
            self._archivo_servicio.cargar_productos()
        )

        self._usuarios: list[Usuario] = (
            self._archivo_servicio.cargar_usuarios()
        )

        self._ventas: list[Venta] = (
            self._archivo_servicio.cargar_ventas()
        )

    def guardar_datos(self) -> bool:
        return self._archivo_servicio.guardar_todo(
            self._productos,
            self._usuarios,
            self._ventas
        )

    # ==============================
    # PRODUCTOS
    # ==============================

    def buscar_producto(
        self,
        codigo: str
    ) -> Producto | None:

        for producto in self._productos:
            if producto.codigo == codigo:
                return producto

        return None

    def registrar_producto(
        self,
        codigo: str,
        nombre: str,
        precio: float,
        stock: int
    ) -> bool:

        if self.buscar_producto(codigo) is not None:
            return False

        producto = Producto(
            codigo,
            nombre,
            precio,
            stock
        )

        self._productos.append(producto)

        return self._archivo_servicio.guardar_productos(
            self._productos
        )

    def listar_productos(self) -> list[Producto]:
        return list(self._productos)

    def actualizar_stock(
        self,
        codigo: str,
        nuevo_stock: int
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        producto.actualizar_stock(nuevo_stock)

        return self._archivo_servicio.guardar_productos(
            self._productos
        )

    def eliminar_producto(
        self,
        codigo: str
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self._productos.remove(producto)

        return self._archivo_servicio.guardar_productos(
            self._productos
        )

    # ==============================
    # USUARIOS
    # ==============================

    def buscar_usuario(
        self,
        identificacion: str
    ) -> Usuario | None:

        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario

        return None

    def registrar_usuario(
        self,
        identificacion: str,
        nombre: str
    ) -> bool:

        if self.buscar_usuario(identificacion) is not None:
            return False

        usuario = Usuario(
            identificacion,
            nombre
        )

        self._usuarios.append(usuario)

        return self._archivo_servicio.guardar_usuarios(
            self._usuarios
        )

    def listar_usuarios(self) -> list[Usuario]:
        return list(self._usuarios)

    def eliminar_usuario(
        self,
        identificacion: str
    ) -> bool:

        usuario = self.buscar_usuario(identificacion)

        if usuario is None:
            return False

        self._usuarios.remove(usuario)

        return self._archivo_servicio.guardar_usuarios(
            self._usuarios
        )

    # ==============================
    # VENTAS
    # ==============================

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int
    ) -> bool:

        usuario = self.buscar_usuario(
            identificacion_usuario
        )

        producto = self.buscar_producto(
            codigo_producto
        )

        if usuario is None or producto is None:
            return False

        if cantidad <= 0:
            return False

        if producto.stock < cantidad:
            return False

        venta = Venta(
            usuario.identificacion,
            producto.codigo,
            cantidad
        )

        self._ventas.append(venta)

        producto.vender(cantidad)

        ventas_ok = self._archivo_servicio.guardar_ventas(
            self._ventas
        )

        productos_ok = self._archivo_servicio.guardar_productos(
            self._productos
        )

        return ventas_ok and productos_ok

    def consultar_ventas_usuario(
        self,
        identificacion_usuario: str
    ) -> list[Venta]:

        ventas_usuario: list[Venta] = []

        for venta in self._ventas:
            if venta.usuario_id == identificacion_usuario:
                ventas_usuario.append(venta)

        return ventas_usuario

    def listar_ventas(self) -> list[Venta]:
        return list(self._ventas)
