#FUNCIÓN PARA AÑADIR, MODIFICAR, ELIMINAR, CONSULTAR CLIENTES EN LA LISTA
def add_clients(result_menu1, result_submenu3, indice_c, clients, cc):
      while result_submenu3.isdigit() == True:
        if result_submenu3 == '1':
          n = 1
          i = indice_c[-1]
          name = input('Ingrese el nombre del cliente: ')
          code = input('ingrese el ID del cliente: ')
          for item in range(n):
            clients.append(name)
            cc.append(code)
            i+=1
            indice_c.append(i)
            print(f'''Los datos se guardaron correctamente:
 Cliente: {clients} \n    ID:   {cc} \n Indice:  {indice_c[1:]}''')
            return result_submenu3
        elif result_submenu3 == '2':
          print(f'''Los clientes actuales son:
 Cliente: {clients} \n Indice:   {indice_c[1:]}''')
          print('Consulte según índice')
          consult_c = input('Elige: ')
          if consult_c.isdigit() == True:
            int_consultc = int(consult_c)
            if int_consultc in indice_c:
              n = 1
              for item in range(n):
                if int_consultc <= len(indice_c):
                  int_consultc = int(consult_c)-1
                  print(f'''
  Nombre: {clients[int_consultc]}
  ID: {cc[int_consultc]}
---------------------------------''')
                  return result_menu1
            else:
              print('ERROR - NO HAY CLIENTES REGISTRADOS')
              print('////////////////////////////////////')
              return result_menu1
          else:
            print('OPCION NO VALIDA')
            print('////////////////////////////')
        elif result_submenu3 == '3':
          print(f'''Los CLIENTES actuales son:
 Nombre: {clients} \n     ID: {cc} \n Indice: {indice_c[1:]}''')
          print('Actualice según índice')
          consult_c = input('Elige: ')
          if consult_c.isdigit() == True:
            int_consultc = int(consult_c)
            if int_consultc in indice_c:
              n = 1
              for item in range(n):
                if int_consultc <= len(indice_c):
                  int_consultc = int(consult_c)-1
                  if int_consultc >= 0:
                    new_name = input('Ingrese nuevo nombre: ')
                    print('------------------------------------')
                    clients.insert(int_consultc, new_name)
                    del clients[int_consultc+1]
                    new_id = input('Nuevo ID: ')
                    print('------------------------------------')
                    cc.insert(int_consultc, new_id)
                    del cc[int_consultc+1]
                    print(f''' LISTA ACTUALIZADA:
  Nombre: {clients}
  ID: {cc}
  ------------------------------------''')
                    return result_menu1
            else:
              print('ERROR - NO HAY CLIENTES REGISTRADOS')
              print('////////////////////////////////////')
              return result_menu1
          else:
            print('OPCION NO VALIDA')
            print('////////////////////////////')
        elif result_submenu3 == '4':
          print(f'''Los CLIENTES actuales son:
 Nombre: {clients} \n     ID: {cc} \n Indice: {indice_c[1:]}''')
          print('Elimine según índice')
          del_c = input('Elige: ')
          if del_c.isdigit() == True:
            int_del_c = int(del_c)
            if int_del_c in indice_c:
              n = 1
              for item in range(n):
                if int_del_c <= len(indice_c):
                  del clients[int_del_c-1]
                  del cc[int_del_c-1]
                  del indice_c[-1]
                  print(f''' LISTA ACTUALIZADA:
              Nombre: {clients}
              ID: {cc}
              Número: {indice_c[1:]}
---------------------------------''')
                  return result_menu1
            else:
              print('ERROR - ESE INDICE NO EXISTE')
              print('/////////////////////')
              return result_menu1
        elif result_submenu3 == '5':
          print('''
          VOLVIENDO AL MENU PRINCIPAL
          ///////////////////////////////////''')
          return result_menu1
        else:
          print('OPCION NO VALIDA')
          print('///////////////////////')
          return result_menu1
      if result_submenu3.isdigit() == False:
        print('''
OPCION NO VALIDA
/////////////////////////////''')
        return result_menu1