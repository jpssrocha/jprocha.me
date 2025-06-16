+++
date = '2025-06-15T21:00:57-03:00'
draft = false
title = 'New cool tool detected: Entr'
+++

Found a new useful tool today! Lately it has become increasingly difficult for
me to find new useful tools for improving my productivity at the command line,
so I'm happy to find it! This tool is `entr`!

It is a tool that will live rerun a given command if a list of files given on
the standard input gets changed and print the outputs. Quite simple but very
useful since it allows the user to do live rerun any generic command line tool,
combine that with a build system like `make` and you have a system that can
rerun smart pipelines whatever a file changes. For example to rerun a recipe to
compile a C project defined as a Makefile from the project folder you can use:

```bash
$ ls *.c | entr make
```

Simple as that! It can also reload a given process if you're using some program
that spawns a server or similar process but don't have a builtin option to watch
by passing the `-r` flag. For example:

```bash
$ ls *.js | entr -r "node app.js"
```

It has many more options but these are the main ones! 
