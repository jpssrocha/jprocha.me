+++
date = '2025-06-01T18:53:53-03:00'
draft = false
title = 'Physics Informed Machine Learning for Modelling Natural Circulation Applied to Nuclear Safety'
+++

As the world races to decarbonize energy systems, advanced nuclear reactors
emerge as a critical solution, delivering reliable, carbon-free power. A key
innovation in these reactors is the use of natural circulation, a naturally
ocurring phenomena that happens in fluids in the presence of a gravitational
field without any external incluence, this phenomena can be leveraged in the
reactor design to passively cool down reactors without the use of mechanical
pumps, making then inherently safer.

Nonetheless due to the complex, non-linear, multi-physics interactions that
governs this fluid flow phenomena, the computational simulations of such systems
are often very computationally expensive, making it challenging do design and
monitor reactors that leverage such phenomena.

That's why in my current research project, being conducted as part of my
Masters at the **National Laboratory for Scientific Computing**, we aim to study
the possibility of using techniques from the emerging field of Physics Informed
Machine Learning (PIML) to model the natural circulation phenomena, so we can
measure the possible speedups and develop implementation strategies.

For that we're using experimental data collected at the **Institute for Nuclear
Engineering** (IEN, :brazil:) from the Natural Circulation Circuit experiment,
which is a 4:1 scale in height model inspired by the AP600 reactor, as well
as numerical data simulated using the OpenFOAM suite, to train and validate
different architectures of PIML models such as PINNs and DeepOnets using Machine
Learning frameworks like **PyToch, Jax, and DeepXDE**.

<!-- ![Natural Circulation Circuit on the Institute for Nuclear Engineering](/vista_geral.jpg) -->

{{< figure src="/vista_geral.jpg" title="Natural Circulation Circuit on the Institute for Nuclear Engineering" height="700" alt="Natural Circulation loop at IEN">}}
