from servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    print("\n========== RESTAURANTE APP ==========")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Registrar usuario")
    print("4. Listar usuarios")
    print("5. Vender producto")
    print("6. Consultar ventas de un usuario")
    print("7. Actualizar stock")
    print("8. Eliminar producto")
    print("9. Eliminar usuario")
    print("0. Salir")
    print("======================================")


def registrar_producto(
    restaurante: Restaurante
) -> None:

    try:
        codigo = input(
            "Código del producto: "
        ).strip()

        nombre = input(
            "Nombre del producto: "
        ).strip()

        precio = float(
            input("Precio: ")
        )

        stock = int(
            input("Stock: ")
        )

        if restaurante.registrar_producto(
            codigo,
            nombre,
            precio,
            stock
        ):
            print(
                "Producto registrado y guardado correctamente."
            )
        else:
            print(
                "No se pudo registrar el producto. "
                "El código puede estar repetido."
            )

    except ValueError as error:
        print(f"Error de validación: {error}")


def listar_productos(
    restaurante: Restaurante
) -> None:

    productos = restaurante.listar_productos()

    if not productos:
        print("No hay productos registrados.")
        return

    print("\n--- PRODUCTOS ---")

    for producto in productos:
        print(
            f"Código: {producto.codigo} | "
            f"Nombre: {producto.nombre} | "
            f"Precio: ${producto.precio:.2f} | "
            f"Stock: {producto.stock}"
        )


def registrar_usuario(
    restaurante: Restaurante
) -> None:

    try:
        identificacion = input(
            "Identificación: "
        ).strip()

        nombre = input(
            "Nombre: "
        ).strip()

        if restaurante.registrar_usuario(
            identificacion,
            nombre
        ):
            print(
                "Usuario registrado y guardado correctamente."
            )
        else:
            print(
                "No se pudo registrar el usuario. "
                "La identificación puede estar repetida."
            )

    except ValueError as error:
        print(f"Error de validación: {error}")


def listar_usuarios(
    restaurante: Restaurante
) -> None:

    usuarios = restaurante.listar_usuarios()

    if not usuarios:
        print("No hay usuarios registrados.")
        return

    print("\n--- USUARIOS ---")

    for usuario in usuarios:
        print(
            f"Identificación: {usuario.identificacion} | "
            f"Nombre: {usuario.nombre}"
        )


def vender_producto(
    restaurante: Restaurante
) -> None:

    try:
        identificacion = input(
            "Identificación del usuario: "
        ).strip()

        codigo = input(
            "Código del producto: "
        ).strip()

        cantidad = int(
            input("Cantidad a comprar: ")
        )

        if restaurante.vender_producto(
            codigo,
            identificacion,
            cantidad
        ):
            print(
                "Venta registrada correctamente."
            )

            producto = restaurante.buscar_producto(
                codigo
            )

            if producto is not None:
                print(
                    f"Stock restante de "
                    f"{producto.nombre}: "
                    f"{producto.stock}"
                )

        else:
            print(
                "Venta rechazada. Verifique que el "
                "usuario y producto existan, que la "
                "cantidad sea mayor que cero y que "
                "exista stock suficiente."
            )

    except ValueError as error:
        print(f"Error de validación: {error}")


def consultar_ventas_usuario(
    restaurante: Restaurante
) -> None:

    identificacion = input(
        "Identificación del usuario: "
    ).strip()

    usuario = restaurante.buscar_usuario(
        identificacion
    )

    if usuario is None:
        print("El usuario no existe.")
        return

    ventas = restaurante.consultar_ventas_usuario(
        identificacion
    )

    if not ventas:
        print(
            "El usuario no tiene ventas registradas."
        )
        return

    print(
        f"\n--- VENTAS DE {usuario.nombre} ---"
    )

    for venta in ventas:

        producto = restaurante.buscar_producto(
            venta.producto_codigo
        )

        if producto is not None:
            nombre_producto = producto.nombre
        else:
            nombre_producto = "Producto no disponible"

        print(
            f"Producto: {nombre_producto} | "
            f"Código: {venta.producto_codigo} | "
            f"Cantidad: {venta.cantidad}"
        )


def actualizar_stock(
    restaurante: Restaurante
) -> None:

    try:
        codigo = input(
            "Código del producto: "
        ).strip()

        nuevo_stock = int(
            input("Nuevo stock: ")
        )

        if restaurante.actualizar_stock(
            codigo,
            nuevo_stock
        ):
            print(
                "Stock actualizado y guardado correctamente."
            )
        else:
            print(
                "No se pudo actualizar el stock. "
                "Verifique el código."
            )

    except ValueError as error:
        print(f"Error de validación: {error}")


def eliminar_producto(
    restaurante: Restaurante
) -> None:

    codigo = input(
        "Código del producto a eliminar: "
    ).strip()

    if restaurante.eliminar_producto(codigo):
        print(
            "Producto eliminado y cambios guardados."
        )
    else:
        print("El producto no existe.")


def eliminar_usuario(
    restaurante: Restaurante
) -> None:

    identificacion = input(
        "Identificación del usuario a eliminar: "
    ).strip()

    if restaurante.eliminar_usuario(
        identificacion
    ):
        print(
            "Usuario eliminado y cambios guardados."
        )
    else:
        print("El usuario no existe.")


def main() -> None:

    restaurante = Restaurante()

    print(
        "Datos cargados correctamente "
        "desde los archivos JSON."
    )

    while True:

        mostrar_menu()

        opcion = input(
            "Seleccione una opción: "
        ).strip()

        if opcion == "1":
            registrar_producto(restaurante)

        elif opcion == "2":
            listar_productos(restaurante)

        elif opcion == "3":
            registrar_usuario(restaurante)

        elif opcion == "4":
            listar_usuarios(restaurante)

        elif opcion == "5":
            vender_producto(restaurante)

        elif opcion == "6":
            consultar_ventas_usuario(restaurante)

        elif opcion == "7":
            actualizar_stock(restaurante)

        elif opcion == "8":
            eliminar_producto(restaurante)

        elif opcion == "9":
            eliminar_usuario(restaurante)

        elif opcion == "0":
            restaurante.guardar_datos()

            print(
                "Programa finalizado. "
                "Los datos quedaron guardados."
            )

            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()