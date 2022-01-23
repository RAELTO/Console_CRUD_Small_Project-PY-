# INICIAR SESION - FINALIZADO
def user_code(code, code_e):
  if '@' in code or '+' in code or '=' in code or '&' in code:
    msg = 'No usar los siguientes carácteres: @ + = &'
  elif len(code) < 8 or len(code) >8:
    msg = 'invalid code'
  elif code[0] == code[7] and code[2] == '*' and len(code) == 8 and code in code_e:
    msg = 'valid code'
  else:
    msg = 'invalid code'
  return msg