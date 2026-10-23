# Lista de Leituras

Aplicação de terminal em Python para cadastrar títulos, consultar a lista e recuperar os registros em uma nova execução. Miniprojeto desenvolvido durante as práticas de estudo de Python.

## Funcionalidades

- Cadastro de títulos com validação de entradas vazias ou formadas somente por espaços.
- Remoção de espaços nas extremidades, preservando acentos e maiúsculas.
- Listagem dos títulos e da quantidade cadastrada.
- Menu com tratamento de entradas não numéricas e opções inexistentes.
- Gravação da lista completa em JSON após cada cadastro válido.
- Recuperação dos títulos ao iniciar o programa.
- Tratamento de arquivo ausente, sem conteúdo ou com JSON malformado.

## Requisitos e execução

Requer Python 3. O projeto utiliza apenas a biblioteca padrão, sem instalação de dependências externas.

Na raiz deste repositório, execute:

```bash
cd lista-de-leituras
python3 main.py
```

Execute o programa a partir da pasta que contém `main.py`. O caminho do JSON é relativo à pasta atual do terminal.

| Opção | Ação |
|---|---|
| `1` | Cadastrar um título |
| `2` | Listar títulos e quantidade |
| `0` | Encerrar |

## Organização

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Carregamento inicial, menu, tratamento de erros e chamadas de gravação |
| `Modulos/titulo.py` | Solicitação e validação do título com `pedir_titulo()` |
| `Modulos/persistencia.py` | Leitura e gravação com `carregar_leituras()` e `salvar_leituras()` |
| `leituras_treino_quarta.json` | Dados fictícios de exemplo; inclui inicialmente o título `Python` |

## Persistência e tratamento de problemas

Os títulos são armazenados em `leituras_treino_quarta.json`, como uma lista JSON de strings. A gravação usa UTF-8, mantém os acentos legíveis e organiza o conteúdo com recuos.

Ao iniciar, o programa tenta carregar a lista antes de permitir novos cadastros. Após cada cadastro válido, salva a lista completa, incluindo os títulos recuperados.

| Situação do arquivo | Comportamento |
|---|---|
| JSON válido com títulos | Recupera os registros e abre o menu |
| Lista vazia válida, `[]` | Abre o menu com lista vazia |
| Arquivo inexistente | Avisa e começa uma lista nova; cria o arquivo somente após um cadastro válido |
| Arquivo sem conteúdo ou com JSON malformado | Mostra o caminho e um aviso, impede a abertura do menu e preserva o conteúdo |

Sair sem cadastrar não cria um arquivo ausente. Entradas inválidas no menu também não provocam gravação.

O formato esperado é uma lista JSON de títulos em texto. Um arquivo sem conteúdo é diferente de `[]`: o primeiro falha na interpretação; o segundo representa uma lista vazia válida.

## Exemplo de uso

1. Execute `python3 main.py`.
2. Escolha `1` e informe `Introdução ao Git`.
3. Escolha `2` para consultar os títulos e a quantidade.
4. Escolha `0` para sair.
5. Execute o programa novamente e escolha `2`: o título continua disponível, junto dos registros anteriores.

## Casos verificados

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

## Conhecimentos aplicados

Funções, módulos, listas, condicionais, laços, entrada de dados, métodos de string, tratamento de exceções e persistência em JSON.

