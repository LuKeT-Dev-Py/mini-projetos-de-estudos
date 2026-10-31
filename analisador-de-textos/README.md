# Analisador de textos

Aplicação de terminal em Python para contar palavras e caracteres. Permite analisar vários textos na mesma execução e trata opções inválidas do menu.

## Como executar

Requer **Python 3.12 ou superior**, pela sintaxe de f-strings utilizada em `main.py`. Não há dependências externas. Execução verificada com Python 3.12.14.

A partir da raiz do repositório:

```bash
cd analisador-de-textos
python3 main.py
```

No Windows, dentro da mesma pasta: `py main.py` ou `python main.py`. Confira se o interpretador é 3.12 ou superior.

Escolha `1` para analisar e `0` para sair. Se digitar texto vazio ou somente espaços, o programa solicita outra entrada. Opções não numéricas ou inexistentes retornam ao menu com aviso.

## Exemplo

Informe `  Git e Python  `:

```text
Palavras: 3
Caracteres: 12
```

O menu reaparece para permitir outra análise. O exemplo foi conferido por execução em Python 3.12.14.

## Regra de contagem

`strip()` remove os espaços em branco das extremidades. `split()` separa as palavras por espaços em branco, e `len()` conta as palavras obtidas e os caracteres do texto tratado.

Espaços internos entram na contagem de caracteres. A pontuação continua no trecho da palavra; maiúsculas e acentos são preservados. A função também trata tabulações e quebras de linha recebidas como string, embora a entrada interativa com `input()` leia uma linha por vez.

Para consultar a função diretamente, dentro desta pasta:

```bash
python3 -c "from Analisar_txt import analisar_texto; print(analisar_texto('  Olá Python  '))"
```

Resultado:

```python
{'palavras': 2, 'caracteres': 10}
```

A função aceita uma string vazia e retorna contagens zeradas; a entrada interativa exige texto preenchido.

## Organização e aprendizado

| Arquivo | Responsabilidade |
| --- | --- |
| [main.py](main.py) | Menu e apresentação dos resultados. |
| [Analisar_txt.py](Analisar_txt.py) | Funções `analisar_texto()` e `pedir_texto()`. |
| [conferir_analise.py](conferir_analise.py) | Auxiliares `resultados_iguais()` e `opcao_permitida()`. |

Mantenha as maiúsculas de `Analisar_txt.py`, pois o import usa esse nome. O projeto pratica strings, listas, dicionários, funções e retorno, módulos, laços, condicionais e tratamento de `ValueError`.

## Limitações e verificação

Os resultados aparecem no terminal e não são salvos. Não há uma suíte de `unittest` incluída; executar `conferir_analise.py` isoladamente apenas define funções auxiliares.

<details>
<summary>Verificações registradas na publicação de 30/10/2026</summary>

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

</details>
