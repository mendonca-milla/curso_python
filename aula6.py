# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1'))) #<class 'int'>
print(float('1.2') + 1) #2.2
print(type(float('1') + 1)) #<class 'float'>
print(bool(' ')) #True (string vazia = False / string mesmo com espaço = True)
print(bool('')) #False
print(str(11)+ 'b') # 11b (concatenou duas strings)