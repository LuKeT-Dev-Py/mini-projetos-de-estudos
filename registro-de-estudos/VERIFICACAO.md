# Verificação do Registro de Estudos

Conferido em 09/10/2026 por execução do programa de terminal.

| Caso | Resultado observado |
|---|---|
| Listar antes do cadastro | Mensagem de ausência e total 0 min |
| Assunto só com espaços | Nova tentativa |
| Duração abc, 0, -5 e depois 20 | Só o valor positivo foi aceito |
| Duas sessões: 20 e 15 minutos | Registros independentes e total 35 min |
| Terceira sessão: 10 minutos | Cadastro permitido e total 45 min |
| Opção 9 | Erro e retorno ao menu |
| Opção abc | ValueError tratado e retorno ao menu |
| Opção 0 | Encerramento normal |
| Nova execução | Lista vazia; dados não persistem |

## Preparação para publicação

A implementação foi recuperada das três capturas finais enviadas em 08/10. Foram aplicados os dois ajustes já apontados na revisão: remoção do parâmetro sem uso de cadastrar_sessao e correção da mensagem do menu para 0, 1 ou 2. As aspas externas da f-string de listagem foram ajustadas para manter compatibilidade com Python 3.10 e 3.11, sem alterar a lógica. O arquivo Modulos/__init__.py e o .gitignore foram acrescentados na preparação. README e este registro foram preparados com apoio de IA.

Os testes acima correspondem ao código deste pacote. A publicação no GitHub não é comprovada por esta verificação.
