Motivation
==========

Mercurial seems to be missing a grep command. A command which invokes
grep over files under version control. Since ``git-grep`` is pretty good,
let's use it.

Installation
============

Clone this repo, and put the following in `~/.hgrc`::

  [extensions]
  hgrep = ...path-to-repo/hggitgrep.py

Usage
=====

::

  hg gitgrep <pattern>
