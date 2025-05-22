+++
date = '2025-05-22T08:44:16-03:00'
draft = true
title = 'Surrogate_modelling_and_PIML'
+++

I've been studying Physics Informed Machine Learning for my master thesis
currently, i knew intuitively that these machine learning models are very useful
for surrogate modeling, nonetheless i didn't knew how widely used surrogates
were.

For those who don't know, surrogate modeling (or meta modeling), is the
practice of constructing an approximated model out of a high fidelity model -
that can be computationally very expensive. They go from the basic idea that
you can evaluate the expensive model a few times, and then use a statistical
learning process over these results to interpolate a model that is much more
cheaper to evaluate. This is very important for tasks such as optimization,
parameter calibration, parametric studies, online evaluation (such as is digital
twins), uncertainty quantification, and others - because these applications requires
often thousands of model executions.

This makes these models **extremely** important, because such applications
are crucial for smart decision making, and the intelligent systems/machinery
that forms the basis of modern society.

And it happens that PIML algorithms are perfect for the task of getting
surrogate models while solving many of the issues that the traditional methods
have, for example by leveraging the symbolic differentiation on the input
as a way to construct the differential equations from a model and use it
as a constraint on the statistical learning process of the surrogate we get
improvements on the problems related to the curse of dimensionality - since
we effectively reduce the dimensionality of the problem by constraining it to
the manifold that the differential equations live, and by the same reason we
get a better approximation on the borders of the domain (and a little bit of
extrapolation power) because it informs proper gradients on the borders.

Will be trying to explore this lens more closely on the future.
