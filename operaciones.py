#OPERACIONES PARA SUBTOTAL, IVA, TOTAL A PAGAR Y COMISION

def p_subtotal(precio_bici, cantidad):
  precio_sbt = precio_bici*cantidad
  return precio_sbt

def valor_iva(IVA, cantidad, precio_bici):
  t_iva = IVA*precio_bici*cantidad
  return t_iva

def p_final(subtotal, total_iva):
  total = subtotal+total_iva
  return total

def bono_vendedor(subtotal):
  if subtotal >= 200000 and subtotal <= 800000:
    comision = subtotal*0.05
  elif subtotal >= 800000 and subtotal <= 1500000:
    comision = subtotal*0.1
  elif subtotal > 1500000:
    comision = subtotal*0.15
  return comision

def tipo_bono(subtotal):
  if subtotal >= 200000 and subtotal <= 800000:
    msg = 'Tipo A'
  elif subtotal >= 800000 and subtotal <= 1500000:
    msg = 'Tipo B'
  elif subtotal > 1500000:
    msg = 'Tipo C'
  return msg
