def divide(number):
  try:
    value = 5/number
  except ZeroDivisionError:
    print('Por zero não né')
    value = 1
  return value

def divide_if(number):
  if number > 0:
    value = 5/number
  else:
    value = 1
    print('valor menor ou igual a zero')
  return value