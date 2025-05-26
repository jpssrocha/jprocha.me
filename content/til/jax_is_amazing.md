+++
date = '2025-05-26T19:31:41-03:00'
draft = false
title = 'Jax is Amazing!'
+++

It has a long time that i've been hearing about the jax framework but i've never
come to use it, since i've always thought it was just a deep learning framework, and i
was used to use PyTorch for it. But yesteday i was wanting to play with autograd
for coding a linear regression to learn more about the ins and outs of autograd,
and since i was just playing i've choosed jax for doing so.

When i was reading the documentation and coding the structure i've realized that
it could be used in a way very close to numpy (they even give a numpy-like api
over jax.numpy), in general the other libraries felt a little cumbersome to do
the stuff i usually do with numpy (maybe because i'm used to it), but with jax
it felt quite natural with a few caveats.

So far, so good, but the really great part was ... The thing was very fast. Then
i discovered the jit decorator that come by default, and it became **blanzingly
fast**. Then by coincident i've accessed nvtop to check some GPU information,
and saw that the process had allocated memory in the GPU, it was transparenly
sending some operations to the GPU without any prior configuration! In my
toy regression problem the jit accelerated version was getting about a 20000x
speedup!

So in summary, jax is not only a deep learning framework, but a viable numeric
core (such as numpy) to accelerate many numerical computing tasks with little
effort, that comes prepacked with autograd. Basically if you take your numpy
import from `import numpy as np` to `import jax.numpy as np` it is possible that
with little effort you can accelerate your numerical computations by a lot! (for
those curious the toy code is bellow)

```python
xs = jnp.linspace(-1, 1, 100)
ys = 2.1*xs + 1 + np.random.normal(size=xs.shape)

def cost_fn(a, b):
    return jnp.mean(((a*xs + b) - ys)**2)

@jax.jit
def optimize_1(a, b):
    lr = 0.01
    for _ in range(100):
        df_a, df_b = grad(cost_fn, 0)(a, b), grad(cost_fn, 1)(a, b)
        a, b = a - lr*df_a,  b - lr*df_b
```
