1.  upper() 
 
O que faz: Transforma TODAS as letras do texto em MAIÚSCULAS.
 
python
  
texto = "python"
print(texto.upper())
# Saída: PYTHON
 
 
2.  lower() 
 
O que faz: Transforma TODAS as letras do texto em minúsculas.
 
python
  
texto = "PYTHON"
print(texto.lower())
# Saída: python
 
 
3.  strip() 
 
O que faz: Tira os espaços sobrando no começo e no final do texto.
 
python
  
texto = "  Olá, Mundo!  "
print(texto.strip())
# Saída: Olá, Mundo!
 
 
4.  replace(antigo, novo) 
 
O que faz: Troca um pedaço do texto por outro.
 
python
  
texto = "Gosto de Java"
print(texto.replace("Java", "Python"))
# Saída: Gosto de Python
 
 
5.  split() 
 
O que faz: Corta o texto em partes, virando uma lista. Onde corta? No que você escolher (vírgula, espaço...).
 
python
  
texto = "maçã,banana,uva"
print(texto.split(","))
# Saída: ['maçã', 'banana', 'uva']
 
 
6.  join() 
 
O que faz: Junta uma lista de palavras num texto só, colocando o que você quiser entre elas.
 
python
  
frutas = ['maçã', 'banana', 'uva']
print(", ".join(frutas))
# Saída: maçã, banana, uva
 
 
7.  find() 
 
O que faz: Diz em qual posição começa o pedaço procurado. Se não achar, devolve  -1 .
 
python
  
texto = "Aprender Python é legal"
print(texto.find("Python"))
# Saída: 9
 
 
8.  index() 
 
O que faz: Igual ao  find() , mas dá erro se não achar o texto procurado.
 
python
  
texto = "Aprender Python é legal"
print(texto.index("Python"))
# Saída: 9
 
 
9.  startswith() 
 
O que faz: Verifica se o texto começa com aquele pedaço. Responde  True  (sim) ou  False  (não).
 
python
  
texto = "Python 3.10"
print(texto.startswith("Py"))
# Saída: True
 
 
10.  endswith() 
 
O que faz: Verifica se o texto termina com aquele pedaço. Responde  True  ou  False .
 
python
  
arquivo = "relatorio.pdf"
print(arquivo.endswith(".pdf"))
# Saída: True
 
 
11.  count() 
 
O que faz: Conta quantas vezes um pedacinho aparece no texto.
 
python
  
texto = "banana"
print(texto.count("a"))
# Saída: 3
 
 
12.  capitalize() 
 
O que faz: Deixa só a primeira letra da frase em maiúscula e o resto tudo em minúscula.
 
python
  
texto = "olá MUNDO"
print(texto.capitalize())
# Saída: Olá mundo
 
 
13.  title() 
 
O que faz: Deixa a primeira letra de CADA palavra em maiúscula.
 
python
  
texto = "bem-vindo ao curso de python"
print(texto.title())
# Saída: Bem-Vindo Ao Curso De Python
 
 
14.  isalpha() 
 
O que faz: Verifica se tem só letras — sem número, sem espaço, sem símbolo.  True  ou  False .
 
python
  
print("Python".isalpha())   # True
print("Python3".isalpha())  # False
 
 
15.  isdigit() 
 
O que faz: Verifica se tem só números.  True  ou  False .
 
python
  
print("12345".isdigit())  # True
print("123a".isdigit())   # False
 
 
