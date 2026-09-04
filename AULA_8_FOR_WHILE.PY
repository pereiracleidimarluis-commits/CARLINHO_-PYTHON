AULA_8_FOR_WHILE.PY 
python
  
for item in colecao:
    # código que repete
 
 
-  for  = para cada
-  item  = variável que guarda o valor da vez
-  in  = em / dentro de
-  :  = obrigatório no final!
- Indentação = o código repetido tem que ter um recuo (4 espaços)
 
✅ A função  range()  — 3 formas:
 
1.  range(5)  → 0, 1, 2, 3, 4 (começa do 0)
2.  range(1, 6)  → 1, 2, 3, 4, 5 (define início e fim)
3.  range(2, 11, 2)  → 2, 4, 6, 8, 10 (início, fim, passo)
 
✅ Exercícios pra gente resolver:
 
- 🎯 Exercício 1 — Tabuada de 1 a 10
- 🎯 Exercício 2 — Contador regressivo (10 até 0) → "Decolar! 🚀"
- 🎯 Exercício 3 — Verificar aprovados (nota ≥ 6 = Aprovado)
 
 
✅ O que é o  while ?
 
-  while  = "enquanto" → repete enquanto a condição for verdadeira
- Diferença do  for :
- 🔹  for  → quando sabemos quantas vezes repetir
- 🔹  while  → quando NÃO sabemos quantas vezes vai repetir (depende de uma condição mudar)
 
✅ Os 3 passos OBRIGATÓRIOS do  while :
 
python
  
# 1️⃣ Inicializar a variável de controle
contador = 1

# 2️⃣ Testar a condição
while contador <= 5:
    print(contador)
    
    # 3️⃣ Atualizar a variável (ESSENCIAL! Sem isso → loop infinito ❌)
    contador = contador + 1
 
 
⚠️ Nunca esqueça o passo 3! Sem ele, o programa trava em loop infinito!
 
✅ Exemplos práticos:
 
- Contagem simples → conta até chegar no limite
- Validar senha → pede senha até acertar (não sabemos quantas tentativas)
- Menu interativo → usa  break  pra sair:  while True:  +  break 
 
 
 
🎯 Exercícios pra gente resolver:
 
Exercício O que fazer 
1 — Contagem Regressiva Conta de 10 até 0 → no final: "Fogo! 🚀" 
2 — Somador de Números Digita números, soma tudo → para quando digitar 0 
3 — Jogo da Adivinhação Número secreto = 7 → pede palpites até acertar → "Parabéns! 🎉" 
 
 
 
