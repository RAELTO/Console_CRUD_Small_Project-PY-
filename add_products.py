#FUNCIÓN PARA AÑADIR, MODIFICAR, ELIMINAR, CONSULTAR PRODUCTOS EN LA LISTA
def add_products(result_menu1, result_submenu1, productos, tipo, indice):
      while result_submenu1.isdigit() == True:
        if result_submenu1 == '1':
          i = indice[-1]
          n = input('|Ingrese la cantidad de nuevos productos que desea agregar: ')
          print('--------------------------------------------------')
          while n.isdigit() == True:
            i+=1
            converter = int(n)
            while converter > 0:
              product = input('|Ingrese el nombre del producto: ')
              print('--------------------------------------------------')
              tipo_p = input('''Ingrese el tipo de producto: 
              [1] NAL (Nacional)
              [2] IMP (Importado)
              : ''')
              if tipo_p == '1':
                productos.append(product)
                tipo.append('NAL')
                indice.append(i)
                converter-=1
                i+=1
              elif tipo_p == '2':
                productos.append(product)
                tipo.append('IMP')
                indice.append(i)
                converter-=1
                i+=1
              else:
                print('Opción no válida')
                print('///////////////////////////////')
                return result_menu1
              print(f'|El producto se guardó correctamente en la lista: \n {productos} \n {tipo} \n {indice}')
              if converter == 0:
                print('---------------------------------------------')
                return result_menu1
            if converter == 0:
              print('No ha ingresado ningún producto')
              return result_menu1
          if n.isdigit() == False:
            print('Ha ingresado una opción no válida...')
            return add_products(result_menu1, result_submenu1, productos, tipo, indice)
        elif result_submenu1 == '2':
          print(f'Los productos que puede CONSULTAR son: \n Productos ---> {productos} \n Tipo --->      {tipo} \n Indice --->    {indice}')
          print('Consulte según índice')
          consulta_p = input('Elige: ')
          if consulta_p.isdigit() == True:
            int_consultap = int(consulta_p)
            if int_consultap <= len(indice):
              int_consultap = int(consulta_p)-1
              print(f'''
              Marca: {productos[int_consultap]}
              Tipo: {tipo[int_consultap]}
---------------------------------''')
              break
            else:
              print('ERRROR')
              break
          else:
            print('ERROR')
            print('/////////////////////////////////')
            return add_products(result_menu1, result_submenu1, productos, tipo, indice)
        elif result_submenu1 == '3':
          print(f'Los productos que puede ACTUALIZAR son: \n Productos ---> {productos} \n Tipo --->      {tipo} \n Indice --->    {indice}')
          print('''Actualice según índice
------------------------------------''')
          upd_p = input('Elige: ')
          print('------------------------------------')
          if upd_p.isdigit() == True:
            int_updt = int(upd_p)
            if int_updt <= len(indice):
              int_updt = int(upd_p)-1
              if int_updt >= 0:
                new_name = input('Ingrese nuevo nombre: ')
                print('------------------------------------')
                productos.insert(int_updt, new_name)
                del productos[int_updt+1]
                new_tipo = input('Nuevo tipo: ')
                print('------------------------------------')
                tipo.insert(int_updt, new_tipo)
                del tipo[int_updt+1]
                print(f''' LISTA ACTUALIZADA:
              Marca: {productos}
              Tipo: {tipo}
              Número: {indice}
---------------------------------''')
                break
              else:
                break
            else:
              print('ERRROR')
              break
          else:
            print('''
OPCIÓN NO VÁLIDA
//////////////////////////''')
            break
        elif result_submenu1 == '4':
          print(f'Los productos que puede ELIMINAR son: \n Productos ---> {productos} \n Tipo --->      {tipo} \n Indice --->    {indice}')
          print('''Elimine según índice
------------------------------------''')
          del_p = input('Elige: ')
          print('------------------------------------')
          if del_p.isdigit() == True:
            int_del = int(del_p)-1
            if int_del <= len(indice):
                del productos[int_del]
                del tipo[int_del]
                del indice[-1]
                print(f''' LISTA ACTUALIZADA:
              Marca: {productos}
              Tipo: {tipo}
              Número: {indice}
---------------------------------''')
                break
            else:
              print('ERRROR')
              break
        elif result_submenu1 == '5':
          return result_menu1
        else:
          print('''
|OPCIÓN NO VÁLIDA
/////////////////////////////////////////''')
          return result_menu1