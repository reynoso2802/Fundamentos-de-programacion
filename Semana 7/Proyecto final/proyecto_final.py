# PROYECTO FINAL
# SISTEMA PARA EL MANTENIMIENTO DE FLOTILLAS VEHICULARES DE CEMEX

import time
import os


# ------------------------------------------------------------
# CARPETA DEL PROGRAMA

# Se obtiene automaticamente la carpeta en donde se encuentra
# este archivo .py. De esta forma los archivos de texto siempre
# se leen y modifican dentro de la carpeta del proyecto.

carpeta_programa = os.path.dirname(os.path.abspath(__file__))


# ------------------------------------------------------------
# COSTOS DE MANTENIMIENTO

# Mazda 3
mtmenor1 = 3050
mtmayor1 = 5650

# Toyota Hilux
mtmenor2 = 4705
mtmayor2 = 9550

# Chevrolet Suburban
mtmenor3 = 3600
mtmayor3 = 7559


# ------------------------------------------------------------
# VEHICULOS REGISTRADOS

vehiculos = [
    ["mazda 3", "Auto utilitario"],
    ["toyota hilux", "Vehiculo utilitario de carga"],
    ["chevrolet suburban", "Auto ejecutivo"]
]


# ------------------------------------------------------------
# ARCHIVOS PREVIAMENTE CREADOS

archivos = [
    "mazda_3.txt",
    "toyota_hilux.txt",
    "chevrolet_suburban.txt",
    "historial_general.txt"
]


# ------------------------------------------------------------
# MENU PRINCIPAL EN FORMA DE MATRIZ

menu = [
    [1, "Consultar costos del mantenimiento"],
    [2, "Registrar el mantenimiento"],
    [3, "Leer un archivo"],
    [4, "Anexar nueva informacion"],
    [5, "Salir del programa"]
]


# ------------------------------------------------------------
# FUNCION DE CARGA

# Esta funcion genera una pantalla de carga de 3 segundos.
# La duracion no supera los 5 segundos solicitados.

def carga():

    print("\nCargando sistema")

    for i in range(3):
        print(".")
        time.sleep(1)

    print("Sistema listo")


# ------------------------------------------------------------
# CONTROL DE INACTIVIDAD

# Cada vez que el programa espera una entrada del usuario,
# se mide el tiempo que tarda en responder.
#
# Si pasan 600 segundos, equivalentes a 10 minutos,
# se pregunta al usuario si desea continuar.
#
# Se utiliza un ciclo for para cumplir con el requisito
# de control de inactividad del proyecto.

def entrada_usuario(mensaje):

    ini = time.time()

    dato = input(mensaje)

    fin = time.time()

    seg = int(fin - ini)
    inact = False

    for i in range(seg + 1):

        if i >= 600:
            inact = True
            break

    if inact == True:

        while True:

            resp = input(
                '\nHan pasado 10 minutos de inactividad. '
                '¿Deseas continuar? Escribe "si" o "no": '
            ).strip().lower()

            if resp == "si" or resp == "sí":

                print("Continuando sesion")
                return dato

            elif resp == "no":

                print("Regresando a la pantalla de inicio")
                return None

            else:

                print('Escribe solamente "si" o "no".')

    return dato


# ------------------------------------------------------------
# MOSTRAR VEHICULOS

def mostrar_vehiculos():

    print("\nVEHICULOS REGISTRADOS")

    for i in range(len(vehiculos)):

        print(
            i + 1,
            "-",
            vehiculos[i][0].title(),
            "-",
            vehiculos[i][1]
        )


# ------------------------------------------------------------
# SELECCIONAR VEHICULO

# Esta funcion permite seleccionar el vehiculo mediante
# un numero o escribiendo su nombre.
#
# lower() permite aceptar mayusculas y minusculas.
# strip() elimina espacios antes y despues del texto.
#
# split() y join() permiten eliminar espacios adicionales
# entre las palabras.
#
# Tambien se aceptan algunas formas comunes de escribir
# los nombres para facilitar el uso del programa.

def seleccionar_vehiculo():

    while True:

        mostrar_vehiculos()

        entrada = entrada_usuario(
            "\nSelecciona el numero o escribe el nombre del vehiculo: "
        )

        if entrada == None:
            return None

        entrada = " ".join(
            entrada.strip().lower().split()
        )

        # Mazda 3
        if entrada == "1":
            return "mazda 3"

        elif entrada == "mazda 3":
            return "mazda 3"

        elif entrada == "mazda3":
            return "mazda 3"

        # Toyota Hilux
        elif entrada == "2":
            return "toyota hilux"

        elif entrada == "toyota hilux":
            return "toyota hilux"

        elif entrada == "hilux":
            return "toyota hilux"

        # Chevrolet Suburban
        elif entrada == "3":
            return "chevrolet suburban"

        elif entrada == "chevrolet suburban":
            return "chevrolet suburban"

        elif entrada == "suburban":
            return "chevrolet suburban"

        else:

            print("\nVehiculo no registrado.")
            print("Selecciona una de las opciones disponibles.")


# ------------------------------------------------------------
# MOSTRAR TIPO DE VEHICULO

def tipo_vehiculo(ncoche):

    if ncoche == "mazda 3":
        print("Tipo de vehiculo: Auto utilitario")

    elif ncoche == "toyota hilux":
        print("Tipo de vehiculo: Vehiculo utilitario de carga")

    elif ncoche == "chevrolet suburban":
        print("Tipo de vehiculo: Auto ejecutivo")


# ------------------------------------------------------------
# MOSTRAR ARCHIVOS

def mostrar_archivos():

    print("\nARCHIVOS DISPONIBLES")

    for i in range(len(archivos)):

        print(
            i + 1,
            "-",
            archivos[i]
        )


# ------------------------------------------------------------
# SELECCIONAR ARCHIVO

# El usuario puede seleccionar un archivo utilizando
# su numero o escribiendo el nombre completo.
#
# Se aceptan mayusculas, minusculas y espacios adicionales.

def seleccionar_archivo():

    while True:

        mostrar_archivos()

        entrada = entrada_usuario(
            "\nSelecciona el numero o escribe el nombre del archivo: "
        )

        if entrada == None:
            return None

        entrada = " ".join(
            entrada.strip().lower().split()
        )

        if entrada == "1":
            return "mazda_3.txt"

        elif entrada == "2":
            return "toyota_hilux.txt"

        elif entrada == "3":
            return "chevrolet_suburban.txt"

        elif entrada == "4":
            return "historial_general.txt"

        elif entrada in archivos:
            return entrada

        else:

            print("\nArchivo no registrado.")
            print("Selecciona uno de los archivos disponibles.")


# ------------------------------------------------------------
# PROGRAMA PRINCIPAL

prog = True

while prog == True:

    print("\n==============================================")
    print(" SISTEMA PARA EL MANTENIMIENTO DE FLOTILLAS CEMEX")
    print("==============================================")


    # --------------------------------------------------------
    # IDENTIFICACION DEL USUARIO

    usr = entrada_usuario(
        "Ingresa tu nombre o nickname: "
    )

    if usr == None:
        continue

    usr = usr.strip()

    # No se permite un nombre vacio.
    while usr == "":

        print("El nombre no puede quedar vacio.")

        usr = entrada_usuario(
            "Ingresa tu nombre o nickname: "
        )

        if usr == None:
            break

        usr = usr.strip()

    if usr == None:
        continue

    print("Bienvenido al sistema " + usr)


    # --------------------------------------------------------
    # CONTRASEÑA

    llave = entrada_usuario(
        "Ingresa la contraseña: "
    )

    if llave == None:
        continue

    llave = llave.strip()

    if llave != "cemex2026":

        print("Contraseña incorrecta, intente nuevamente")
        continue

    print("Acceso permitido")


    # --------------------------------------------------------
    # CAPTURA DE FECHA

    # Se inicializan las variables para evitar errores
    # en caso de regresar por inactividad.

    dia = None
    mes = None
    anio = None

    fecha_valida = False

    while fecha_valida == False:

        try:

            dia = entrada_usuario(
                "Ingresa el dia: "
            )

            if dia == None:
                break

            mes = entrada_usuario(
                "Ingresa el mes: "
            )

            if mes == None:
                break

            anio = entrada_usuario(
                "Ingresa el año: "
            )

            if anio == None:
                break


            # Se eliminan espacios antes y despues.
            dia = dia.strip()
            mes = mes.strip()
            anio = anio.strip()


            # Se comprueba que los datos no esten vacios.
            if dia == "" or mes == "" or anio == "":

                print(
                    "La fecha debe escribirse con dia, mes y año en numeros"
                )
                continue


            # Se comprueba que los tres datos sean numeros.
            if (
                dia.isdigit() == False
                or mes.isdigit() == False
                or anio.isdigit() == False
            ):

                print(
                    "La fecha debe escribirse con dia, mes y año en numeros"
                )
                continue


            # El año debe escribirse con cuatro numeros.
            if len(anio) != 4:

                print(
                    "El año debe escribirse con 4 numeros"
                )
                continue


            dia = int(dia)
            mes = int(mes)
            anio = int(anio)


            # Validacion del mes.
            if mes < 1 or mes > 12:

                print(
                    "El mes debe ser un numero entre 1 y 12"
                )
                continue


            # Validacion del año.
            if anio < 2000:

                print(
                    "Ingresa un año valido"
                )
                continue


            # ------------------------------------------------
            # DIAS DISPONIBLES SEGUN EL MES

            dias_mes = 31

            # Abril, junio, septiembre y noviembre
            # tienen solamente 30 dias.
            if (
                mes == 4
                or mes == 6
                or mes == 9
                or mes == 11
            ):

                dias_mes = 30


            # Febrero puede tener 28 o 29 dias.
            elif mes == 2:

                # Se verifica si el año es bisiesto.
                if (
                    anio % 400 == 0
                    or (
                        anio % 4 == 0
                        and anio % 100 != 0
                    )
                ):

                    dias_mes = 29

                else:

                    dias_mes = 28


            # Validacion final del dia segun el mes.
            if dia < 1 or dia > dias_mes:

                print(
                    "El dia ingresado no es valido para ese mes y año"
                )
                continue


            # La fecha se almacena en una tupla.
            Fecha = dia, mes, anio

            fecha_valida = True


        except ValueError:

            print(
                "La fecha debe escribirse con dia, mes y año en numeros"
            )


    # Si la inactividad hizo regresar al usuario,
    # se vuelve a la pantalla principal.

    if dia == None or mes == None or anio == None:
        continue


    # --------------------------------------------------------
    # PANTALLA DE CARGA

    carga()


    # --------------------------------------------------------
    # MENU PRINCIPAL

    menuact = True

    while menuact == True:

        print("\n----------------------------------------------")
        print("                MENU PRINCIPAL")

        # Se recorre la matriz del menu.
        for f in menu:

            print(
                f[0],
                "-",
                f[1]
            )


        # ----------------------------------------------------
        # VEHICULOS DISPONIBLES

        print("\nUNIDADES DISPONIBLES")

        for i in range(len(vehiculos)):

            print(
                i + 1,
                "-",
                vehiculos[i][0].title(),
                "-",
                vehiculos[i][1]
            )


        # ----------------------------------------------------
        # SELECCION DEL MENU

        opc = entrada_usuario(
            "\nSelecciona una opcion del menu: "
        )

        if opc == None:

            menuact = False
            continue

        opc = opc.strip().lower()


        # ====================================================
        # OPCION 1
        # CONSULTAR COSTOS DEL MANTENIMIENTO

        if opc == "1":

            print("\n----------------------------------------------")
            print("         CONSULTAR COSTO DE MANTENIMIENTO")

            ncoche = seleccionar_vehiculo()

            if ncoche == None:

                menuact = False
                continue

            print(
                "\nVehiculo seleccionado:",
                ncoche.title()
            )

            tipo_vehiculo(ncoche)


            # ------------------------------------------------
            # KILOMETRAJES

            try:

                kmactual = entrada_usuario(
                    "Ingresa el kilometraje actual: "
                )

                if kmactual == None:

                    menuact = False
                    continue


                kmserv = entrada_usuario(
                    "Ingresa el kilometraje del proximo servicio: "
                )

                if kmserv == None:

                    menuact = False
                    continue


                # Se eliminan espacios.
                kmactual = kmactual.strip()
                kmserv = kmserv.strip()


                # Se comprueba que no esten vacios.
                if kmactual == "" or kmserv == "":

                    print(
                        "Error: el kilometraje debe escribirse "
                        "utilizando numeros enteros positivos"
                    )

                    continue


                # Se comprueba que solamente contengan numeros.
                if (
                    kmactual.isdigit() == False
                    or kmserv.isdigit() == False
                ):

                    print(
                        "Error: el kilometraje debe escribirse "
                        "utilizando numeros enteros positivos"
                    )

                    continue


                kmactual = int(kmactual)
                kmserv = int(kmserv)


                # Los kilometrajes deben ser mayores que cero.
                if kmactual <= 0 or kmserv <= 0:

                    print(
                        "El kilometraje debe ser un numero "
                        "positivo mayor que 0"
                    )

                    continue


                # --------------------------------------------
                # SI REQUIERE MANTENIMIENTO

                if kmactual >= kmserv:

                    print(
                        "\nLa unidad requiere mantenimiento"
                    )

                    print(
                        "1 - Mantenimiento menor"
                    )

                    print(
                        "2 - Mantenimiento mayor"
                    )


                    tipo = entrada_usuario(
                        "Selecciona el tipo de mantenimiento: "
                    )

                    if tipo == None:

                        menuact = False
                        continue


                    # Se aceptan numeros, texto,
                    # mayusculas, minusculas y espacios extra.
                    tipo = " ".join(
                        tipo.strip().lower().split()
                    )


                    if (
                        tipo == "1"
                        or tipo == "mantenimiento menor"
                        or tipo == "menor"
                    ):

                        tipo = "1"


                    elif (
                        tipo == "2"
                        or tipo == "mantenimiento mayor"
                        or tipo == "mayor"
                    ):

                        tipo = "2"


                    else:

                        print(
                            "Tipo de mantenimiento no valido. "
                            "Selecciona 1 o 2."
                        )

                        continue


                    # ----------------------------------------
                    # MAZDA 3

                    if ncoche == "mazda 3":

                        if tipo == "1":

                            print(
                                "Costo del mantenimiento: $",
                                mtmenor1
                            )

                        elif tipo == "2":

                            print(
                                "Costo del mantenimiento: $",
                                mtmayor1
                            )


                    # ----------------------------------------
                    # TOYOTA HILUX

                    elif ncoche == "toyota hilux":

                        if tipo == "1":

                            print(
                                "Costo del mantenimiento: $",
                                mtmenor2
                            )

                        elif tipo == "2":

                            print(
                                "Costo del mantenimiento: $",
                                mtmayor2
                            )


                    # ----------------------------------------
                    # CHEVROLET SUBURBAN

                    elif ncoche == "chevrolet suburban":

                        if tipo == "1":

                            print(
                                "Costo del mantenimiento: $",
                                mtmenor3
                            )

                        elif tipo == "2":

                            print(
                                "Costo del mantenimiento: $",
                                mtmayor3
                            )


                # --------------------------------------------
                # SI TODAVIA NO REQUIERE MANTENIMIENTO

                else:

                    faltan = kmserv - kmactual

                    print(
                        "\nLa unidad no requiere mantenimiento"
                    )

                    print(
                        "Faltan",
                        faltan,
                        "km para el proximo servicio"
                    )


            except ValueError:

                print(
                    "Error: el kilometraje debe escribirse "
                    "utilizando numeros enteros"
                )


        # ====================================================
        # OPCION 2
        # REGISTRAR MANTENIMIENTO

        elif opc == "2":

            print("\n----------------------------------------------")
            print("         REGISTRAR MANTENIMIENTO")

            ncoche = seleccionar_vehiculo()

            if ncoche == None:

                menuact = False
                continue

            print(
                "\nVehiculo seleccionado:",
                ncoche.title()
            )

            tipo_vehiculo(ncoche)


            try:

                kmactual = entrada_usuario(
                    "Ingresa el kilometraje actual: "
                )

                if kmactual == None:

                    menuact = False
                    continue


                # Se eliminan espacios.
                kmactual = kmactual.strip()


                # Se comprueba que no este vacio.
                if kmactual == "":

                    print(
                        "El kilometraje debe escribirse "
                        "utilizando numeros enteros positivos"
                    )

                    continue


                # Se comprueba que solamente tenga numeros.
                if kmactual.isdigit() == False:

                    print(
                        "El kilometraje debe escribirse "
                        "utilizando numeros enteros positivos"
                    )

                    continue


                kmactual = int(kmactual)


                # Validacion del kilometraje.
                if kmactual <= 0:

                    print(
                        "El kilometraje debe ser un numero "
                        "positivo mayor que 0"
                    )

                    continue


                print(
                    "\n1 - Mantenimiento menor"
                )

                print(
                    "2 - Mantenimiento mayor"
                )


                tipo = entrada_usuario(
                    "Selecciona el tipo de mantenimiento: "
                )

                if tipo == None:

                    menuact = False
                    continue


                # Se aceptan numeros, texto,
                # mayusculas, minusculas y espacios extra.
                tipo = " ".join(
                    tipo.strip().lower().split()
                )


                if (
                    tipo == "1"
                    or tipo == "mantenimiento menor"
                    or tipo == "menor"
                ):

                    tipo = "1"


                elif (
                    tipo == "2"
                    or tipo == "mantenimiento mayor"
                    or tipo == "mayor"
                ):

                    tipo = "2"


                else:

                    print(
                        "Tipo de mantenimiento no valido. "
                        "Selecciona 1 o 2."
                    )

                    continue


                # Variables que se utilizaran para el registro.
                arch = ""
                cost = 0
                serv = ""


                # --------------------------------------------
                # MAZDA 3

                if ncoche == "mazda 3":

                    arch = "mazda_3.txt"

                    if tipo == "1":

                        cost = mtmenor1
                        serv = "Mantenimiento menor"

                    elif tipo == "2":

                        cost = mtmayor1
                        serv = "Mantenimiento mayor"


                # --------------------------------------------
                # TOYOTA HILUX

                elif ncoche == "toyota hilux":

                    arch = "toyota_hilux.txt"

                    if tipo == "1":

                        cost = mtmenor2
                        serv = "Mantenimiento menor"

                    elif tipo == "2":

                        cost = mtmayor2
                        serv = "Mantenimiento mayor"


                # --------------------------------------------
                # CHEVROLET SUBURBAN

                elif ncoche == "chevrolet suburban":

                    arch = "chevrolet_suburban.txt"

                    if tipo == "1":

                        cost = mtmenor3
                        serv = "Mantenimiento menor"

                    elif tipo == "2":

                        cost = mtmayor3
                        serv = "Mantenimiento mayor"


                # --------------------------------------------
                # REGISTRO EN ARCHIVOS

                if serv != "":

                    reg = (
                        "Fecha: "
                        + str(Fecha[0])
                        + "/"
                        + str(Fecha[1])
                        + "/"
                        + str(Fecha[2])
                    )

                    reg = reg + " | Usuario: " + usr
                    reg = reg + " | Vehiculo: " + ncoche
                    reg = reg + " | Km: " + str(kmactual)
                    reg = reg + " | Servicio: " + serv
                    reg = reg + " | Costo: $" + str(cost)
                    reg = reg + "\n"


                    try:

                        # Se registra la informacion en el
                        # archivo individual del vehiculo.

                        ruta_archivo = os.path.join(
                            carpeta_programa,
                            arch
                        )

                        with open(ruta_archivo, "a") as a:

                            a.write(reg)


                        # Tambien se guarda una copia en el
                        # historial general de la flotilla.

                        ruta_historial = os.path.join(
                            carpeta_programa,
                            "historial_general.txt"
                        )

                        with open(
                            ruta_historial,
                            "a"
                        ) as a:

                            a.write(reg)


                        print(
                            "\nMantenimiento registrado correctamente"
                        )


                    except FileNotFoundError:

                        print(
                            "No se encontro el archivo "
                            "correspondiente al vehiculo"
                        )


                    except PermissionError:

                        print(
                            "No tienes permisos para modificar "
                            "el archivo"
                        )


                    except OSError:

                        print(
                            "Ocurrio un error al guardar "
                            "la nueva informacion"
                        )


                else:

                    print(
                        "Tipo de mantenimiento no valido"
                    )


            except ValueError:

                print(
                    "El kilometraje debe escribirse "
                    "utilizando numeros"
                )


        # ====================================================
        # OPCION 3
        # LEER ARCHIVO

        elif opc == "3":

            print("\n----------------------------------------------")
            print("              LEER ARCHIVO")

            nom = seleccionar_archivo()

            if nom == None:

                menuact = False
                continue


            try:

                ruta_archivo = os.path.join(
                    carpeta_programa,
                    nom
                )

                with open(ruta_archivo, "r") as a:

                    cont = a.read()


                if cont == "":

                    print(
                        "\nEl archivo se encuentra vacio"
                    )

                else:

                    print(
                        "\nCONTENIDO DEL ARCHIVO"
                    )

                    print(
                        "----------------------------------------------"
                    )

                    print(cont)


            except FileNotFoundError:

                print(
                    "El archivo no existe o no se encuentra "
                    "en la carpeta del programa"
                )


            except PermissionError:

                print(
                    "No tienes permiso para abrir el archivo"
                )


            except OSError:

                print(
                    "Ocurrio un error al intentar leer "
                    "el archivo"
                )


        # ====================================================
        # OPCION 4
        # ANEXAR NUEVA INFORMACION

        elif opc == "4":

            print("\n----------------------------------------------")
            print("          ANEXAR INFORMACION")

            nom = seleccionar_archivo()

            if nom == None:

                menuact = False
                continue


            txt = entrada_usuario(
                "Escribe la informacion que deseas anexar: "
            )

            if txt == None:

                menuact = False
                continue

            txt = txt.strip()


            # No se permite agregar informacion vacia.
            if txt == "":

                print(
                    "No se puede anexar informacion vacia"
                )

                continue


            # Se agrega automaticamente la fecha y el usuario.
            reg = (
                "Fecha: "
                + str(Fecha[0])
                + "/"
                + str(Fecha[1])
                + "/"
                + str(Fecha[2])
            )

            reg = reg + " | Usuario: " + usr
            reg = reg + " | " + txt
            reg = reg + "\n"


            try:

                ruta_archivo = os.path.join(
                    carpeta_programa,
                    nom
                )

                # Primero se comprueba que el archivo exista.

                with open(ruta_archivo, "r") as a:

                    a.readline()


                # Posteriormente se abre en modo "a"
                # para anexar informacion sin borrar
                # el contenido anterior.

                with open(ruta_archivo, "a") as a:

                    a.write(reg)


                print(
                    "\nInformacion anexada correctamente"
                )


            except FileNotFoundError:

                print(
                    "El archivo no existe o no se encuentra "
                    "en la carpeta del programa"
                )


            except PermissionError:

                print(
                    "No tienes permiso para modificar "
                    "el archivo"
                )


            except OSError:

                print(
                    "Ocurrio un error al modificar "
                    "el archivo"
                )


        # ====================================================
        # OPCION 5
        # SALIR DEL PROGRAMA

        elif opc == "5":

            print(
                "\nSesion finalizada"
            )

            print(
                "Gracias por utilizar el sistema,",
                usr
            )

            menuact = False
            prog = False


        # ====================================================
        # OPCION INCORRECTA

        else:

            print(
                "\nOpcion no valida. "
                "Selecciona un numero del 1 al 5."
            )