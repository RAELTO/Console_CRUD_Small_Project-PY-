# CAMBIOS DE VARIABLE
'''Funciones para renombrar variables en main.py
y que sean usadas en las tablas de detalles'''
def marca_b(marca, indice, productos, result_menu1):
  if marca.isdigit() == True:
    int_marca = int(marca)
    if int_marca in indice:
      n = 1
      for item in range(n):
        if int_marca <= len(indice):
              marca=productos[int_marca-1]
        else:
          marca = 'ERROR'
          return result_menu1
    else:
      return result_menu1
  else:
    print('OPCION NO VALIDA')
    return result_menu1
  return marca

def tipo_b(marca, indice, productos, result_menu1, tipo):
  if marca.isdigit() == True:
    int_marca = int(marca)
    if int_marca in indice:
      n = 1
      for item in range(n):
        if int_marca <= len(indice):
              tipo_bic=tipo[int_marca-1]
        else:
          tipo_bic = 'ERROR'
          return result_menu1
    else:
      return result_menu1
  else:
    print('OPCION NO VALIDA')
    return result_menu1
  return tipo_bic

def iva_bici(tipob):
  if tipob == 'NAL':
    IVA = 0.1
  elif tipob == 'IMP':
    IVA = 0.2
  return IVA

def color_bici(color):
  if color == '1':
    color = 'Roja'
  elif color == '2':
    color = 'Negra'
  elif color == '3':
    color = 'Roja-Negra'
  else:
    color = 'Error'
  return color

def tamaño_bici(tamaño):
  if tamaño == '1' or tamaño == 'S' or tamaño == 's':
    tamaño = 'S'
  elif tamaño == '2' or tamaño == 'M' or tamaño == 'm':
    tamaño = 'M'
  elif tamaño == '3' or tamaño == 'L' or tamaño == 'l':
    tamaño = 'L'
  elif tamaño == '4' or tamaño == 'XL' or tamaño == 'xl':
    tamaño = 'XL'
  else:
    tamaño = 'Error'
  return tamaño