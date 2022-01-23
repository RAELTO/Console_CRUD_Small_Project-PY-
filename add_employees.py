#FUNCIÓN PARA AÑADIR, MODIFICAR, ELIMINAR, CONSULTAR EMPLEADOS EN LA LISTA
def add_employees(result_menu1, result_submenu2, employees, indice_e, code_e):
      while result_submenu2.isdigit() == True:
        if result_submenu2 == '1':
          n = 1
          i = indice_e[-1]
          name = input('Ingrese el nombre del empleado: ')
          code = input('Asigne el código del empleado: ')
          for item in range(n):
            employees.append(name)
            code_e.append(code)
            i+=1
            indice_e.append(i)
            print(f'''Los datos se guardaron correctamente:
 Empleado: {employees} \n Código:   {code_e} \n Indice:   {indice_e[1:]}''')
            return result_submenu2
        elif result_submenu2 == '2':
          print(f'''Los empleados actuales son:
 Empleado: {employees} \n Indice:   {indice_e[1:]}''')
          print('Consulte según índice')
          consult_e = input('Elige: ')
          if consult_e.isdigit() == True:
            int_consultem = int(consult_e)
            if int_consultem in indice_e:
              n = 1
              for item in range(n):
                if int_consultem <= len(indice_e):
                  int_consultem = int(consult_e)-1
                  print(f'''
  Nombre: {employees[int_consultem]}
  Código: {code_e[int_consultem]}
---------------------------------''')
                  return result_menu1
            else:
              print('ERROR - NO HAY EMPLEADOS REGISTRADOS')
              print('////////////////////////////////////')
              return result_menu1
          else:
            print('OPCION NO VALIDA')
            print('////////////////////////////')
        elif result_submenu2 == '3':
          print(f'''Los empleados actuales son:
 Empleado: {employees} \n Código: {code_e} \n Indice:   {indice_e[1:]}''')
          print('Actualice según índice')
          consult_e = input('Elige: ')
          if consult_e.isdigit() == True:
            int_consultem = int(consult_e)
            if int_consultem in indice_e:
              n = 1
              for item in range(n):
                if int_consultem <= len(indice_e):
                  int_consultem = int(consult_e)-1
                  if int_consultem >= 0:
                    new_name = input('Ingrese nuevo nombre: ')
                    print('------------------------------------')
                    employees.insert(int_consultem, new_name)
                    del employees[int_consultem+1]
                    new_code = input('Nuevo código: ')
                    print('------------------------------------')
                    code_e.insert(int_consultem, new_code)
                    del code_e[int_consultem+1]
                    print(f''' LISTA ACTUALIZADA:
  Nombre: {employees}
  Código: {code_e}
  ------------------------------------''')
                    return result_menu1
        elif result_submenu2 == '4':
          print(f'''Los empleados actuales son:
 Empleado: {employees} \n Código: {code_e} \n Indice:   {indice_e[1:]}''')
          print('Elimine según índice')
          del_e = input('Elige: ')
          if del_e.isdigit() == True:
            int_del_e = int(del_e)
            if int_del_e in indice_e:
              n = 1
              for item in range(n):
                if int_del_e <= len(indice_e):
                  del employees[int_del_e-1]
                  del code_e[int_del_e-1]
                  del indice_e[-1]
                  print(f''' LISTA ACTUALIZADA:
              Nombre: {employees}
              Código: {code_e}
              Número: {indice_e[1:]}
---------------------------------''')
                  return result_menu1
            else:
              print('ERROR')
              print('/////////////////////')
              return result_menu1
        elif result_submenu2 == '5':
          return result_menu1
        else:
          print('OPCION NO VALIDA')
          print('///////////////////////')
      if result_submenu2.isdigit() == False:
        print('''
OPCION NO VALIDA
/////////////////////////////''')
        return result_menu1