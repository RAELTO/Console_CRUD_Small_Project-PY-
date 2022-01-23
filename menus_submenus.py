#FUNCIONES QUE HACEN DE MENÚS Y SUBMENÚS E INTERACTUAN CON EL MAIN Y LOS DEMÁS MÓDULOS
def menu_1():
  print('''         --------------          
          MARKET CICLE         
              MENU
         --------------    
------------------------------------------
| Escriba el numero para elegir la opción:
------------------------------------------
[1] AGREGAR PRODUCTOS
[2] AGREGAR EMPLEADOS
[3] AGREGAR CLIENTES
[4] REGISTRAR VENTA
[5] SALIR
________________________________________''')
  elegir_menu1 = input('| Elija la acción que desea realizar: ')
  print('----------------------------------------')
  return elegir_menu1

def submenu1(productos):
      print(f'| Los productos actuales son: {productos}')
      print(''' --------------------------------------------------   
  [1] Para registrar un nuevo producto
  [2] Para consultar un producto.
  [3] Para actualizar un producto.
  [4] Para eliminar un producto.
  [5] Para volver al menú principal.
--------------------------------------------------''')
      elegir_menu2 = input(f'|Seleccione una opción: ')
      print('--------------------------------------------------')
      return elegir_menu2

def submenu2(employees, code_e):
      print(f'''| Los empleados actuales son: 
      NOMBRE: {employees} \n      CODIGO: {code_e}''')
      print(''' --------------------------------------------------   
  [1] Para registrar un nuevo empleado
  [2] Para consultar información del empleado.
  [3] Para actualizar información del empleado.
  [4] Para eliminar un empleado del registro.
  [5] Para volver al menú principal.
--------------------------------------------------''')
      elegir_menu3 = input(f'|Seleccione una opción: ')
      print('--------------------------------------------------')
      return elegir_menu3

def submenu3(clients, cc):
      print(f'''| Los CLIENTES actuales son: 
      NOMBRE: {clients} \n      ID:     {cc}''')
      print(''' --------------------------------------------------   
  [1] Para registrar un nuevo cliente.
  [2] Para consultar información del cliente.
  [3] Para actualizar información del cliente.
  [4] Para eliminar un cliente del registro.
  [5] Para volver al menú principal.
--------------------------------------------------''')
      elegir_menu4 = input(f'|Seleccione una opción: ')
      print('--------------------------------------------------')
      return elegir_menu4

def submenu4(venta, fecha_v, employees):
      print(f'''| Las VENTAS actuales son: 
      VENTA: {venta} \n      FECHA: {fecha_v}''')
      print(''' --------------------------------------------------   
  [1] Para registrar una venta.
  [2] Para consultar ventas.
  [3] Para actualizar ventas.
  [4] Para eliminar una venta del registro.
  [5] Para volver al menú principal.
--------------------------------------------------''')
      elegir_menu5 = input(f'|Seleccione una opción: ')
      print('--------------------------------------------------')
      return elegir_menu5