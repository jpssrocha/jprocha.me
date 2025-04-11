+++
date = '2025-02-23T14:34:16-03:00'
draft = false
title = 'Medindo tempo elegantemente em Python - ft. context managers!'
+++

Frequentemente, ao testar diferentes algoritmos e estratégias, precisamos
executar algum tipo de *benchmarking* em blocos do programa. Há algum tempo,
precisei fazer isso para as várias etapas de uma simulação e refleti sobre uma boa
estrutura de temporização. Embora ferramentas tradicionais como o cProfile
sejam boas para uma visão geral, quando é necessário um controle mais refinado
do tempo em blocos de código, geralmente acabamos usando manualmente algo como
a biblioteca `time` para fazer algo assim:

```python
from time import time

tic = time()

# Código aqui

toc = time()

print(f"Demorou: {toc - tic}")
```

Embora funcione, isso pode se tornar bem trabalhoso ao rastrear muitos blocos
(e às vezes gerar erros). Recentemente, estava fazendo isso e percebi que
poderia ser muito mais elegante usando funcionalidades do Python.

---

# Dica nº 1: Use `perf_counter`

No exemplo acima, usei a função `time` de propósito porque vejo muitas pessoas
a utilizando quando deveriam usar `perf_counter`. A função `time` não é
adequada para *profiling*, pois é destinada a marcações temporais devido à sua
implementação (veja [1] para detalhes). O código correto seria:

```python
from time import perf_counter

tic = perf_counter()

# Código aqui

toc = perf_counter()

print(f"Demorou: {toc - tic}")
```

---

# Dica nº 2: Use um gerenciador de contexto

Agora, imagine fazer o rastreamento acima com múltiplos pontos de teste?
Teríamos muitos blocos envolvendo chamadas de `perf_counter` – que coisa feia!
Mas não se preocupe: os idiomas do Python resolvem isso.

Para cronometrar elegantemente, podemos usar um dos recursos mais elegantes do
Python: um **gerenciador de contexto**. Gerenciadores de contexto são comumente
usados para recursos como arquivos ou conexões de banco de dados, mas também
podem ser usados para qualquer contexto, como medir tempos de execução.

Eles podem ser definidos de duas formas: como geradores ou como classes com
métodos `__enter__` e `__exit__`. Vejamos o primeiro caso:

```python
from contextlib import contextmanager

@contextmanager
def timer():
    try:
        tic = perf_counter()
        yield
    finally:
        print(f"Demorou: {perf_counter() - tic}")
```

Aqui, usamos o decorador `contextmanager` para converter a função em um objeto
compatível com o modelo de dados do Python. Uso:

```python
with timer():
    sleep(0.1)  # Código aqui!
```

Para implementações rápidas, essa abordagem é ideal. Mas recentemente
experimentei a segunda forma e vi seu potencial.

---

### Dica nº 3: Defina o gerenciador de contexto como classe para funcionalidades extras

Com um gerenciador de contexto definido como classe, ganhamos flexibilidade,
aproveitando todos os truques da orientação a objetos! Veja uma implementação
básica:

```python
from dataclasses import dataclass

@dataclass
class Timer:
    _elapsed_time: float = 0

    def __enter__(self):
        self._current_time = perf_counter()

    def __exit__(self, type, value, traceback):
        self._elapsed_time += perf_counter() - self._current_time

    def get_elapsed_time(self):
        return self._elapsed_time
```

Neste exemplo, usei outra funcionalidade útil do Python: **dataclasses**. Por
ser uma classe, o decorador `dataclass` facilita o gerenciamento do estado
interno. Essa ferramenta permite cronometrar blocos de código de forma
elegante. Por exemplo, em um loop complexo:

```python
t = Timer()
t2 = Timer()

for i in range(100):
    with t:
        sleep(0.1)
    
    with t2:
        sleep(0.05)
    
    with t:
        sleep(0.1)

print(t.get_elapsed_time())
print(t2.get_elapsed_time())
```

Imagine os recursos extras possíveis: temporizadores que rastreiam múltiplos
pontos em um dicionário ou geram *DataFrames* do pandas para análise
estatística. As possibilidades são infinitas!

---

# Resumo

1. **Prefira `perf_counter` em vez de `time`** para medições precisas, pois é projetado para *profiling*.
2. **Use gerenciadores de contexto** para encapsular a lógica de temporização, reduzindo código repetitivo e melhorando legibilidade.
3. **Implemente gerenciadores de contexto baseados em classe** para casos avançados, permitindo temporização cumulativa, gerenciamento de estado fácil e personalização.

Adotando essas práticas, desenvolvedores podem obter medições de desempenho
mais limpas, reutilizáveis e precisas, mantendo o código organizado.

---

# Referências

- [1] [perf_counter no Python](https://www.geeksforgeeks.org/time-perf_counter-function-in-python/)
