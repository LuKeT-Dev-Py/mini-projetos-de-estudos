# Mini projetos de estudos em Python

Quatro aplicações de terminal desenvolvidas por João Antônio (LuKeT-Dev-Py) durante a prática de Python. Cada projeto tem código próprio, exemplos de uso e instruções de execução.

## Escolha um projeto

| Projeto | O que faz | Conceitos aplicados | Armazenamento |
| --- | --- | --- | --- |
| [Lista de Leituras](lista-de-leituras/) | Cadastra títulos e os recupera ao reabrir. | Funções, módulos, validação, exceções e arquivos JSON. | JSON |
| [Analisador de Textos](analisador-de-textos/) | Conta palavras e caracteres e permite novas análises. | Strings, dicionários, funções, módulos e tratamento de entradas. | Sem histórico salvo |
| [Registro de Estudos](registro-de-estudos/) | Registra sessões e soma o tempo estudado. | Listas, dicionários, funções, laços e validações. | Memória |
| [Quiz no Terminal](quiz-no-terminal/) | Apresenta duas perguntas e calcula pontuação e entradas inválidas. | Condicionais, laços, contadores e normalização de strings. | Memória |

Para observar persistência entre execuções, comece pela Lista de Leituras. Para uma demonstração rápida de validação e fluxo no terminal, experimente o Registro de Estudos.

## Como executar

Não há dependências externas. Os exemplos foram conferidos com Python 3.12.14; o Analisador de Textos exige **Python 3.12 ou superior** pela sintaxe utilizada. Veja os requisitos individuais nos READMEs.

Clone uma vez e entre na pasta do projeto escolhido:

```bash
git clone https://github.com/LuKeT-Dev-Py/mini-projetos-de-estudos.git
cd mini-projetos-de-estudos
cd registro-de-estudos
python3 main.py
```

No Windows, dentro da mesma pasta, use `py main.py` ou `python main.py`. Para executar outro projeto, volte à raiz do repositório e entre na pasta correspondente.

## Escopo

São exercícios de aprendizado com funcionalidades pequenas. Os READMEs apresentam o comportamento atual, as limitações e os exemplos conferidos. Os registros de verificações manuais não equivalem a uma suíte automatizada incluída.

Novos mini projetos serão acrescentados ao índice conforme forem concluídos e conferidos.
