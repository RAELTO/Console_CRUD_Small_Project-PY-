#FUNCIÓN PARA MODIFICAR, ELIMINAR, CONSULTAR VENTAS EN LA LISTA
def sales_modify(result_menu1, result_submenu4, indice_v, venta, fecha_v, salesman):
      while result_submenu4.isdigit() == True:
        if result_submenu4 == '2':
          print(f'''Las ventas actuales son:
 Ventas: {venta} \n Indice:   {indice_v[1:]}''')
          print('Consulte según índice')
          consult_v = input('Elige: ')
          if consult_v.isdigit() == True:
            int_consultv = int(consult_v)
            if int_consultv in indice_v:
              n = 1
              for item in range(n):
                if int_consultv <= len(indice_v):
                  int_consultv = int(consult_v)-1
                  print(f'''
  Venta: {venta[int_consultv]}
  Fecha: {fecha_v[int_consultv]}
  Consulta: {salesman}
---------------------------------''')
                  return result_menu1
            else:
              print('ERROR - NO HAY VENTAS REGISTRADAS')
              print('////////////////////////////////////')
              return result_menu1
          else:
            print('OPCION NO VALIDA')
            print('////////////////////////////')
        elif result_submenu4 == '3':
          print(f'''Las ventas actuales son:
 Ventas: {venta} \n Indice:   {indice_v[1:]}''')
          print('Actualice según índice')
          consult_v = input('Elige: ')
          if consult_v.isdigit() == True:
            int_consultv = int(consult_v)
            if int_consultv in indice_v:
              n = 1
              for item in range(n):
                if int_consultv <= len(indice_v):
                  int_consultv = int(consult_v)-1
                  if int_consultv >= 0:
                    new_value = int(input('Ingrese nuevo valor de venta sin puntos ni comas: '))
                    print('------------------------------------')
                    venta.insert(int_consultv, new_value)
                    del venta[int_consultv+1]
                    new_date = input('Nueva fecha: ')
                    print('------------------------------------')
                    fecha_v.insert(int_consultv, new_date)
                    del fecha_v[int_consultv+1]
                    print(f''' VENTA ACTUALIZADA:
  Venta: {venta}
  Fecha: {fecha_v}
  Actualizada por: {salesman}
  ------------------------------------''')
                    return result_menu1
            else:
              print('ERROR - NO HAY VENTAS REGISTRADAS')
              print('////////////////////////////////////')
              return result_menu1
          else:
            print('OPCION NO VALIDA')
            print('////////////////////////////')
        elif result_submenu4 == '4':
          print(f'''Las ventas actuales son:
 Ventas: {venta} \n Indice:   {indice_v[1:]}''')
          print('Elimine según índice')
          del_v = input('Elige: ')
          if del_v.isdigit() == True:
            int_del_v = int(del_v)
            if int_del_v in indice_v:
              n = 1
              for item in range(n):
                if int_del_v <= len(indice_v):
                  del venta[int_del_v-1]
                  del fecha_v[int_del_v-1]
                  del indice_v[-1]
                  print(f''' LISTA ACTUALIZADA:
  Venta:           {venta}
  Fecha:           {fecha_v}
  Número:          {indice_v[1:]}
  Por: {salesman}
---------------------------------''')
                  return result_menu1
            else:
              print('ERROR - ESE INDICE NO EXISTE')
              print('/////////////////////')
              return result_menu1
        elif result_submenu4 == '5':
          print('VOLVIENDO AL MENU PRINCIPAL')
          print('//////////////////////////////')
          return result_menu1
        else:
          print('OPCION NO VALIDA')
          print('///////////////////////')
          return result_menu1
      if result_submenu4.isdigit() == False:
        print('''
OPCION NO VALIDA
/////////////////////////////''')
        return result_menu1