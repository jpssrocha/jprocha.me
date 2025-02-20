+++
date = '2025-02-17T10:30:35-03:00'
draft = true
title = 'RAG for Scientists and Science Students'
+++

Some time ago I've saw the internet be flooded with the term **RAG**, which
stands for *Retrieval Augmented Generation*. At the time i didn't paid a lot of
attention, since it was related with the much hyped subject of Generative AI
and LLMs (Large Language Models), so I've thought it wasn't that useful and
people was talking about it just because it was aligned with the hype cycle.

Nonetheless, yesterday I've took a look at it ... And discovered that i was
wrong, this thing is highly useful (specially for ADHD people like myself).
After some time reflecting about my attitude of judging the book by it's cover,
I've researched a bit about more the subject and started to think about the
possibilities (i'll leave the resources i've found useful at the bottom). I'll now
share with you the core idea of it and then some i've had that i think will be
useful for scientist and science students (like me). I'll be focusing on RAGs
for text data, still, it can be used with other types of media, the idea is
roughly the same, with some asterisks.

# The concepts around RAG

The term "Retrieval Augmented Generation" (or RAG) may sound fancy, but the
main idea is quite simple and elegant (once you have access to a trained LLM).
For context lets return to the basics - speaking in simple terms - LLMs operates
as next word guessers (or more precisely: next token guessers), which means
that in their training process they basically "read" a lot of text while trying
to guess the next word (for more details the 3B1B series on LLM's is amazing!
Link bellow), the more they learn to get the next token right, the knowledge
and pattern of that text gets "imprinted" on the weights of it's neural
network. This process is done to extremely huge amounts of text so that the
model learns a lot about a broad spectrum. Nonetheless, when you want to know
something about an specific document, audio, etc the neural net obviously can't
know anything about it if it wasn't on the body of data it was trained on and
if you ask for it the LLM may even hallucinate it ... Therefore when a company
or individual want a that can answer queries about an specific body of that they
have 2 main options (that i'm aware of ...):

- Fine Tuning
- Retrieval Augmented Generation

The process of fine tuning consists of taking an already trained model and
training it again on a smaller more targeted data set - that can be for example
a set of papers for a research project, or the documentation of your favorite
tools - making the model learn new information from it and improve performance
on tasks related to that data set. Despite being very useful, it comes with its
pros and cons, a big con is that it is ineffective to use with real time data
such as papers being published in a fast moving field, or monitoring news,
postings, and other sources of this kind. Since each time a new source comes
one would need to train the network again generating a new version, which is
highly costly both in compute and storage. 

This kind of scenario is where RAG systems shine! These can be used directly
with an out-of-the-box LLM or in combination with fine tuned ones. Let's talk
about then now!

# The concept of RAG

Retrieval Augmented Generation is quite simple, basically it is the practice
of enhancing the input for an LLM with text you recover from some data source.
Breaking it down it would be something like:

1. You write a query (or queries) for the LLM with a place for inputting new context
2. You retrieve this context data from somewhere
3. You send the query to the LLM so it can generate output

That's it ... The concept behind RAG is so simple that I've already started using it without
even realizing, for examples, some times i would write text and ask for chatgpt or deepseek 
to help me improve it. The queries would be something like:

```
Read the text between quotes bellow:

"
{TEXT}
"

Now please, help me improving the structure of this text rearranging the ideas
so they flow more naturally while keeping the style. Show me the complete new
suggested text under quotes and then explain me the reason for changing each 
paragraph.
```

In this example i have (1) a query with a placeholder, (2) a customized information
i'll input into it (by hand in this case), (3) i send it to the LLM over the chat.
In this case, off course the LLM don't know about my text i've just written, it would 
be overkill to do fine-tuning for such task, that's a perfect example of the essence 
of RAG. 

Despite the basic idea being simple this can get quite elaborate, for example,
(1) the input query could be multiple ones with different purposes to be later
combined, or be done in sequence, (2) the contextual information could come
from a vector database, internet search, SQL database, or even multiple sources
combined that have to be updated and managed daily, and (3) the generation
process could require sophisticated control logic for combining many results
into an output.

Some examples of sophisticated RAG systems that i use daily are
[perplexity](perplexity.ai) and [consensus](consensus.app) (imagine if
perplexity fine tuned a model every time something new is indexed by google and
other search engines ...). However this could be used in simple daily tasks to
automate boring stuff and improve productivity. A good way of doing so for
researchers and students is by utilizing, structured outputs.
 
# A RAG superpower - Structured Outputs

A common task for research (be scientific or not) is to feed spreadsheets and
databases by painstakingly reading papers, documents and things of this nature
(the ADHD nightmare) ... but fear not RAG systems are perfect for that ... By simply
asking an LLM to output it's generated content in a given form, it will do so! Then
you can simply parse it with you favorite tool! For me this looks like, asking the 
neural net to output the content into JSON, parsing into with Python's native
JSON engine and then using the result to instantiate the most adequate data structure 
for the job (mostly pandas dataframes).

This saves ages of hustle cause you can then take these formatted outputs and do
what you need inside an easy to automate environment! (the ADHD dream!).

# A word of caution

Despite all these positive points bear in mind that LLM's are still LLM's even
when aided by RAG, so they can hallucinate, even tough the amount of
hallucinations are less. Since RAG systems became so popular there are many
guidelines one can follow in order to improve the situation such as keeping the
context input small, actively instructing the model not to create information
and reducing the LLM temperature parameters. It's always a good idea to test
your system against a validation data set to see if things are working
properly and use some hallucination evaluation tools (link bellow).


# Some ideas


# Useful links

- [A Helping Hand for LLMs (RAG) - Computerphile](https://youtu.be/of4UDMvi2Kw?si=-Vqic8KKT3OR1mW6)
- [Large Language Models Explained Briefly - 3Blue1Brown](https://youtu.be/LPZh9BOjkQs?si=W2H2UkKEjngwZ-Sj)
- [RAG Isn’t Immune to LLM Hallucination](https://towardsdatascience.com/detecting-hallucination-in-rag-ecaf251a6633/)
