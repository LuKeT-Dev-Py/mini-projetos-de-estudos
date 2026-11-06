# Checklist de Estudos

Aplicação de terminal para cadastrar duas tarefas de estudo, acompanhar quais estão pendentes e marcá-las como concluídas. Desenvolvida por João Antônio durante a prática de Python com funções, módulos, listas e dicionários.

## O que esta versão faz

- Solicita dois títulos válidos, removendo espaços nas extremidades e preservando acentos e maiúsculas.
- Rejeita títulos vazios e permite uma nova tentativa.
- Lista os títulos com a situação **Pendente** ou **Concluída**.
- Permite concluir uma tarefa pelo número: `1` para a primeira e `2` para a segunda.
- Trata entradas que não são números e seleções fora do intervalo.
- Encerra o menu com `0`.

As tarefas ficam apenas na memória. Ao encerrar o programa, elas são descartadas.

## Como executar

É necessário **Python 3.12 ou superior**. Não há dependências externas.

A partir da raiz deste repositório:

```bash
cd checklist-de-estudos
python3 tarefas.py
```

No Windows, dentro da mesma pasta, use `py tarefas.py` ou `python tarefas.py`, com Python 3.12 ou superior instalado.

O arquivo de entrada desta aplicação é `tarefas.py`.

## Exemplo de uso

1. Informe `Revisar Git` como primeiro título.
2. Informe `Praticar Python` como segundo título.
3. O programa mostra:

```text
Revisar Git - Pendente
Praticar Python - Pendente
```

4. Na pergunta sobre qual tarefa mudar, digite `2`. A listagem passa a ser:

```text
Revisar Git - Pendente
Praticar Python - Concluída
```

5. Digite `0` para sair.

Um título formado apenas por espaços é recusado e não ocupa uma das duas posições. Na seleção, letras ou números fora do intervalo geram um aviso e permitem nova tentativa.

## Organização dos arquivos

| Arquivo | Responsabilidade |
| --- | --- |
| `tarefas.py` | Cadastro pelo terminal, seleção da tarefa, listagem e saída. |
| `imports.py` | Funções para validar o título, adicionar a tarefa, descrever a situação e marcar a conclusão. |

### Funções principais

| Função | Comportamento |
| --- | --- |
| `titulo_valido(titulo)` | Retorna um dicionário com o título limpo e `concluida=False`, ou `False` para título vazio. |
| `adicionar_se_criada(tarefas, tarefa)` | Adiciona o dicionário à lista e retorna `True`; se receber `False`, preserva a lista e retorna `False`. |
| `situacao_tarefa(tarefa)` | Retorna `"Pendente"` ou `"Concluída"`, sem modificar o registro. |
| `marcar_concluida(tarefas, numero)` | Valida a numeração a partir de 1, altera somente a tarefa escolhida e informa o resultado com um booleano. |

O campo `"concluida": False` representa uma tarefa existente e pendente. Ele é diferente do retorno `False` usado quando um título vazio impede a criação.

## Conferências

O autor confirmou os testes durante o desenvolvimento. Na preparação desta publicação, também foram executados cenários com **Python 3.12.14**:

- Cadastro de dois títulos, conclusão da segunda tarefa e preservação da primeira como pendente.
- Rejeição de títulos vazios ou formados apenas por espaços.
- Tratamento de letras, zero, números negativos e números acima da quantidade de tarefas, conforme o contexto de cada entrada.
- Saída sem concluir tarefas e preservação de acentos e do título limpo.
- Verificação direta dos retornos das funções e das seleções inválidas.

Essas conferências não constituem uma suíte automatizada incluída no projeto.

## Escopo e próximos passos

O cadastro atual é de exatamente duas tarefas por execução, seguido do menu de conclusão. A listagem não apresenta números ao lado dos títulos: a seleção segue a ordem de cadastro.

Possíveis melhorias futuras são exibir essa numeração e permitir cadastrar novas tarefas pelo menu. Essas melhorias ainda não estão implementadas.
