# Lista de leituras

Aplicação de terminal para cadastrar títulos, consultar a lista e recuperar os registros em uma nova execução. É o mini projeto desta coleção que demonstra persistência em JSON.

## Funcionalidades

- Cadastro de títulos preenchidos, removendo espaços das extremidades e preservando acentos e maiúsculas.
- Listagem dos títulos e da quantidade cadastrada.
- Menu com tratamento de entradas não numéricas e opções inexistentes.
- Carregamento dos registros ao iniciar e gravação da lista completa após cada cadastro válido.
- Tratamento de arquivo ausente e JSON vazio ou malformado.

## Como executar

Requer Python 3, sem dependências externas. Execução verificada com Python 3.12.14.

A partir da raiz do repositório:

```bash
cd lista-de-leituras
python3 main.py
```

No Windows, dentro da mesma pasta: `py main.py` ou `python main.py`.

Execute a partir da pasta que contém `main.py`: o caminho do JSON é relativo à pasta atual do terminal.

| Opção | Ação |
| --- | --- |
| `1` | Cadastrar um título |
| `2` | Listar títulos e quantidade |
| `0` | Sair |

## Experimente a persistência

O arquivo incluído começa com o título fictício `Python`.

1. Escolha `1` e cadastre `Introdução ao Git`.
2. Escolha `2`. Em uma cópia inicial, a saída inclui:

```text
['Python', 'Introdução ao Git']
Quantidade cadastrada: 2
```

3. Escolha `0` para sair.
4. Execute novamente e escolha `2`: os dois títulos continuam disponíveis.

O ciclo de cadastro, gravação e recuperação acima foi conferido em Python 3.12.14.

## Arquivo de dados e limites

Os títulos ficam em `leituras_treino_quarta.json`, como uma lista de strings em UTF-8. Após um cadastro válido, o programa grava a lista completa com os registros anteriores.

| Situação | Comportamento |
| --- | --- |
| JSON válido com títulos | Recupera a lista e abre o menu. |
| `[]` | Abre com lista vazia. |
| Arquivo ausente | Avisa, começa em memória e cria o arquivo somente após um cadastro válido. |
| Arquivo sem conteúdo ou JSON malformado | Avisa, não abre o menu e preserva o conteúdo. |

Sair sem cadastrar e digitar opções inválidas não provocam gravação. Um arquivo vazio é diferente de `[]`, que representa uma lista vazia válida.

A estrutura esperada é uma lista de títulos em texto. A validação dessa estrutura após a leitura e o tratamento de falhas de gravação ainda não estão implementados. Também não há edição nem exclusão de títulos.

## Organização

| Arquivo | Responsabilidade |
| --- | --- |
| [main.py](main.py) | Carregamento inicial, menu e chamadas de gravação. |
| [Modulos/titulo.py](Modulos/titulo.py) | Solicitação e validação do título. |
| [Modulos/persistencia.py](Modulos/persistencia.py) | Leitura e gravação JSON. |
| [leituras_treino_quarta.json](leituras_treino_quarta.json) | Dados fictícios de exemplo. |

O exercício pratica funções, módulos, listas, condicionais, laços, entrada de dados, strings, exceções e persistência em JSON.

<details>
<summary>Verificações registradas na publicação de 23/10/2026</summary>

As conferências desta publicação foram executadas em **23/10/2026**, com **Python 3.12.14**, em cópias isoladas do projeto e com dados fictícios. Os nove cenários abaixo passaram.

| Cenário e entrada | Resultado observado |
|---|---|
| Arquivo válido contendo `["Python"]`; listar e sair | Exibiu o título e quantidade `1`, sem modificar o arquivo |
| Lista inicial com `Python`; cadastrar `Introdução ao Git` e `Funções em Python`, incluindo tentativas vazias e espaços nas extremidades; reiniciar | Rejeitou títulos vazios, preservou acentos e maiúsculas e recuperou os três títulos sem duplicar os anteriores |
| Arquivo contendo `[]`; listar | Abriu o menu e informou que não havia títulos |
| Arquivo inexistente; listar e sair sem cadastrar | Informou a criação de uma lista nova em memória e terminou sem criar arquivo |
| Arquivo inexistente; cadastrar `Lógica de Programação` | Criou o JSON com o primeiro título válido |
| Arquivo sem conteúdo | Avisou, não abriu o menu e manteve o arquivo sem alterações |
| JSON malformado, `["Python",]` | Avisou, não abriu o menu e preservou os bytes do arquivo |
| Letra `x` no menu | Mostrou o aviso de número inválido e permitiu continuar, preservando os registros |
| Opção numérica inexistente, `9` | Mostrou o aviso de opção inválida e permitiu continuar, preservando os registros |

Para repetir cenários de erro, use cópias separadas de laboratório e mantenha o mesmo `caminho` nas chamadas de leitura e gravação.

</details>
