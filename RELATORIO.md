## Relatório
## Histórico de commit
@luiztcn78 ➜ /workspaces/AtividadeAula (main) $ git log --oneline
fbbb95b (HEAD -> main) mensagem importante
7bd92f4 ADD feat: Multiplicação
0fd6b6c (tag: v1.4, tag: v1.3) Att de variáveis
5f7f440 feat: adicionada função de divisão
1d7b7b8 (tag: v1.2, tag: v1.1) Update de todas as funções
e0e256f feat: adicionada função de soma
4fcebc9 feat: adicionado mini menu para calculadora
dee20bb (tag: v1.0) Create Main.py



## Diferenças entre versão inicial e final
@luiztcn78 ➜ /workspaces/AtividadeAula (main) $ git diff v1.0 v1.4
diff --git a/Main.py b/Main.py
index 19d0339..95e950a 100644
--- a/Main.py
+++ b/Main.py
@@ -1 +1,33 @@
 ## Atividade aula
+
+UserChoice = int(input("Digite a operação que você quer (1 - soma, 2 - multiplicação, 3 - subtração, 4 - divisão): "))
+Number1 = int(input("Digite o primeiro número que você quer manipular: "))
+Number2 = int(input("Digite o segundo numero que você quer manipular: "))
+## print(UserChoice)
+
+## Atividade aula
+
+x = int(input("Digite um número:"))
:


## Auditoria do Arquivo
@luiztcn78 ➜ /workspaces/AtividadeAula (main) $ git blame Main.py
^dee20bb (luiztcn78       2025-09-08 09:55:22 -0300  1) ## Atividade aula
fbbb95b9 (luiztcn78       2025-09-08 13:44:36 +0000  2) ##se tiver pouco commit de luiz é porque agnt quebrou o codigo muitas vezes
5f7f4409 (Pedro Delgado   2025-09-08 13:32:05 +0000  3) UserChoice = int(input("Digite a operação que você quer (1 - soma, 2 - multiplicação, 3 - subtração, 4 - divisão): "))
e0e256fe (Pedro Delgado   2025-09-08 13:19:53 +0000  4) Number1 = int(input("Digite o primeiro número que você quer manipular: "))
e0e256fe (Pedro Delgado   2025-09-08 13:19:53 +0000  5) Number2 = int(input("Digite o segundo numero que você quer manipular: "))
e0e256fe (Pedro Delgado   2025-09-08 13:19:53 +0000  6) ## print(UserChoice)
e0e256fe (Pedro Delgado   2025-09-08 13:19:53 +0000  7) 
1d7b7b82 (Marcus Vinícius 2025-09-08 13:26:36 +0000  8) ## Atividade aula
1d7b7b82 (Marcus Vinícius 2025-09-08 13:26:36 +0000  9) 
1d7b7b82 (Marcus Vinícius 2025-09-08 13:26:36 +0000 10) x = int(input("Digite um número:"))
1d7b7b82 (Marcus Vinícius 2025-09-08 13:26:36 +0000 11) y = int(input("Digite outro número:"))





:
