# Tipos int e float
# int -> Número inteiro
# O tipo int representa qualquer número positivo ou negativo. 
# int sem sinal é considerado positivo.
print(11) # int
print(-11) # int
print(0)


# float -> Número com ponto flutuante
# O tipo float representa qualquer número positivo ou negativo com ponto flutuante.
# float sem sinal é considerado positivo.
print(1.1, 10.11) #float
print(0.0, -1.5) #float

# A função type mostra o tipo que o Python
# inferiu ao valor.
print(type('Camilla'))
print(type(0))
print(type(1.1), type(-1.1), type(0.0))


"""
conclusão: tem casa decimal é float não tem casa decimal é inteiro

print(   type('Camilla')    ) = me diz qual é a class - string, interiro etc

print(type('Camilla'))
print(type(0))
print(type(1.1), type(-1.1), type(0.0))

<class 'str'>
<class 'int'>
<class 'float'> <class 'float'> <class 'float'>
"""