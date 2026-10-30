# Analisador de Textos no Terminal

Aplicação de terminal em Python para contar palavras e caracteres de um texto. O programa permite realizar várias análises na mesma execução, com validação das opções do menu e das entradas de texto.

## Funcionalidades

- Menu com as opções **1 — Analisar texto** e **0 — Sair**.
- Contagem de palavras e de caracteres.
- Nova tentativa quando o texto está vazio ou contém somente espaços.
- Aviso e retorno ao menu para opções inválidas, incluindo entradas que não são números.
- Preservação de maiúsculas e acentos no texto tratado.

## Requisitos

- **Python 3.12 ou superior**, compatível com a sintaxe utilizada no código.
- Apenas a biblioteca padrão do Python; não há dependências externas para instalar.

## Como executar

A partir da raiz do repositório:

```bash
cd analisador-de-textos
python3 main.py
```

Escolha `1`, informe o texto e consulte as contagens. O menu reaparece após cada análise. Escolha `0` para encerrar.

### Exemplo

Ao informar `  Git e Python  `, o programa apresenta:

```text
Palavras: 3
Caracteres: 12
```

## Como a contagem funciona

1. `strip()` remove os espaços em branco das extremidades.
2. `split()` separa as palavras por espaços em branco, incluindo espaços repetidos, tabulações e quebras de linha.
3. `len()` conta as palavras obtidas e os caracteres do texto tratado.

Espaços internos e quebras de linha entram na contagem de caracteres. Cada trecho separado por espaços em branco conta como uma palavra; a pontuação continua fazendo parte desse trecho.

A função de análise aceita uma string vazia e devolve contagens zeradas. Na entrada interativa, o programa pede outro texto até receber conteúdo preenchido.

Os resultados ficam na memória durante a execução e são apresentados no terminal.

## Organização

```text
analisador-de-textos/
├── Analisar_txt.py
├── conferir_analise.py
├── main.py
└── README.md
```

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Menu, escolha da operação e apresentação dos resultados |
| `Analisar_txt.py` | Funções `analisar_texto()` e `pedir_texto()` |
| `conferir_analise.py` | Funções auxiliares `resultados_iguais()` e `opcao_permitida()` |

Os nomes dos arquivos devem ser mantidos, incluindo as maiúsculas de `Analisar_txt.py`.

## Conferência

Para consultar diretamente o retorno da função, execute dentro da pasta do projeto:

```bash
python3 -c "from Analisar_txt import analisar_texto; print(analisar_texto('  Olá Python  '))"
```

Resultado esperado:

```python
{'palavras': 2, 'caracteres': 10}
```

### Casos verificados na revisão para publicação

Em **30/10/2026**, foram executadas oito verificações independentes em uma cópia do projeto, com **Python 3.12.14**. Todos os casos passaram após a correção do retorno ao menu no tratamento de `ValueError`.

| Texto | Palavras | Caracteres |
|---|---:|---:|
| `"  Olá Python  "` | 2 | 10 |
| `"Git   Python"` | 2 | 12 |
| `"   "` | 0 | 0 |
| `"Git\nPython"` | 2 | 10 |

No último caso, `\n` representa uma quebra de linha, contada como um caractere interno.

Também foram conferidos quatro cenários do menu:

- Sair imediatamente com `0`, sem solicitar texto.
- Informar letra, entrada vazia e opção numérica inválida, recuperando o menu.
- Rejeitar textos vazios e realizar duas análises na mesma execução.
- Informar uma letra depois de uma análise, sem reutilizar a escolha anterior.

`conferir_analise.py` fornece funções auxiliares e não executa uma bateria de casos ao ser chamado isoladamente. As oito verificações acima correspondem à revisão de publicação; não há uma suíte de `unittest` incluída nesta versão.

## Conhecimentos aplicados

Manipulação de strings, listas e dicionários; funções e retorno; importação de módulos; condicionais e laços; validação de entrada; tratamento de `ValueError`.

