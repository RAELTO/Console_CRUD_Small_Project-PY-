import menus_submenus as ms
import add_products as adp
import add_employees as adem
import add_clients as adc
import sales_modify as sm
import ini_sesion as ins
import survey_variables as sv #ejecuta cambios en las variables
import operaciones as op
import detalles as dt
from datetime import date
productos = ['TREK', 'SPZD', 'BMC']
tipo = ['NAL', 'IMP', 'IMP']
indice = [1, 2, 3]
employees = ['ADMIN']
code_e = ['13*33331']
indice_e = [0, 1]
clients = []
cc = []
indice_c = [0]
venta = []
fecha_v = []
indice_v = [0]
while True:
  #desplegará el meú principal
  result_menu1 = ms.menu_1()
  if result_menu1 == '1':
    # según las elecciones del menú principal
    # se desplegaran los respectivos submenús y sus opciones
    result_submenu1 = ms.submenu1(productos)
    adp.add_products(result_menu1, result_submenu1, productos, tipo, indice)
  elif result_menu1 == '2':
    result_submenu2 = ms.submenu2(employees, code_e)
    adem.add_employees(result_menu1, result_submenu2, employees, indice_e, code_e)
  elif result_menu1 == '3':
    result_submenu3 = ms.submenu3(clients, cc)
    adc.add_clients(result_menu1, result_submenu3, indice_c, clients, cc)
  elif result_menu1 == '4':
    print('''--------------------------
    PARA REGISTRAR LA VENTA
    ---------------------------------''')
    code = input('Ingrese su código de acceso: ')
    iniciar_s = ins.user_code(code, code_e)
    print(iniciar_s)
    if iniciar_s == 'invalid code' or iniciar_s == 'No usar los siguientes carácteres: @ + = &':
        print('Código de vendedor no válido...')
        print('Intente nuevamente...')
        print('////////////////////////////////////')
        result_menu1
        # si el codigo ingresado no es valido retorna al menu principal
    else:
      #El código debe estar en la lista de códigos empleados
      #Si el código es válido --> ejecuta formulario y detalles
      pos = code_e.index(code)
      salesman = employees[pos]
      print(f'WELCOME {salesman}')
      print('--------------------------------------')
      result_submenu4 = ms.submenu4(venta, fecha_v, employees)
      if result_submenu4 == '1':
        print("==========================================================")
        print("| Formulario")
        print("==========================================================")
        print("| Ingresa un numero para realizar la operacion.")
        print("==========================================================")
        print(f'''| Las marcas disponibles son:
        Marca: {productos} \n Índice {indice}''')
        marca = input('Seleccione la marca de la bicicleta según índice: ')
        marca_bici = sv.marca_b(marca, indice, productos, result_menu1)
        tipob = sv.tipo_b(marca, indice, productos, result_menu1, tipo)
        IVA = sv.iva_bici(tipob)
        print("==========================================================")
        print("| Color: roja[1] negra[2] roja-negra[3]")
        color = input('Seleccione el color de la bicicleta: ')
        color = sv.color_bici(color)
        print("==========================================================")
        print("| Tamaño de la bicicleta: S[1]  M[2] L[3]  XL[4]")
        tamaño = input('Elija el tamaño de la bicicleta: ')
        tamaño = sv.tamaño_bici(tamaño)
        print("==========================================================")
        print('| Escriba el precio de la bicicleta sin comas ni puntos.')
        print("==========================================================")
        print("| Precio de la bicicleta por unidad")
        precio_bici = int(input('Ingrese el precio de la bicicleta: '))
        print("==========================================================")
        print("| Cantidad de bicicletas vendidas")
        cantidad = int(input('Ingrese la cantidad de bicicletas vendidas: '))
        print("==========================================================")
        print('| Escriba los datos requeridos')
        print("==========================================================")
        print("| Nombre del cliente")
        cliente = input('Ingrese el nombre del cliente: ')
        print("==========================================================")
        print("| Identificación - Cliente")
        cc2 = input('Ingrese el número del documento del cliente sin puntos ni comas: ')
        print("==========================================================")
        subtotal = op.p_subtotal(precio_bici, cantidad)
        print("==========================================================")
        total_iva = op.valor_iva(IVA, cantidad, precio_bici)
        print("==========================================================")
        precio_total = op.p_final(subtotal, total_iva)
        print("==========================================================")
        fecha = date.today()
        venta.append(f'{precio_total:,}')
        fecha_v.append(fecha)
        contar_v = indice_v[-1]
        indice_v.append(contar_v+1)
        print('SE HA REGISTRADO LA VENTA')
        vendedor = salesman
        print(f'''
        Vendedor: {salesman} \n Venta: {venta} \n Fecha: {fecha_v}''')
        print(" ==============================================================")
        bonificacion = op.bono_vendedor(subtotal)
        bono = op.tipo_bono(subtotal)
        det_venta = input('''Desea generar los detalles de la venta?
  [1] Sí
  [2] No
  : ''')
        if det_venta.isdigit() == True:
          if det_venta == '1':
            detalle_venta = dt.detalles(code, salesman, marca_bici, cantidad, bonificacion, bono, fecha, cc2, cliente, precio_bici, tipob, tamaño, color, subtotal, total_iva, precio_total)
            print(detalle_venta)
            result_menu1
          elif det_venta == '2':
            print('Volviendo al menú principal...')
            print('//////////////////////////////')
            result_menu1
          else:
            print('ERROR - OPCION NO VALIDA')
            print('////////////////////////////////')
            result_menu1
        elif det_venta.isdigit() == False:
          print('ERROR - OPCION NO VALIDA')
          print('////////////////////////////////')
          result_menu1
      else:
        modi_sale = sm.sales_modify(result_menu1, result_submenu4, indice_v, venta, fecha_v, salesman)
  elif result_menu1 == '5':
    print('GOOD BYE...')
    break
  else:
    print('OPCION NO VALIDA')
    print('//////////////////////')
    result_menu1