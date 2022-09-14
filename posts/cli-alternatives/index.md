---
title: "Linux Command Line Alternatives"
author: "Neil Shephard"
date: "2022-09-18"
categories: [code, linux, bash]
image: "https://live.staticflickr.com/3793/12059147393_1b75269246_k.jpg"
---

The command line is my second home when sat at a computer ([Emacs](https://www.gnu.org/software/emacs/) is my first ;-)
and the [UNIX Philosophy](https://en.wikipedia.org/wiki/Unix_philosophy) is the key to the huge amount of highly
productive tools that are available under UNIX, GNU/Linux, BSD, OSX, PowerShell etc.

Many of these tools work and have done for many years, but there are some new alternatives that are coming through that
build and modernise on these tools without breaking the core functionality. Here I detail some of the tools and why you
might want to use them. Each tool has a brief introduction with some example output shown and then some `aliases` listed
that you can drop into `~/.bash_aliases` or `~/.oh-my-zsh/custom/aliases` to use on your system.


## Alternatives

### `bat`

[`bat`](https://github.com/sharkdp/bat) is "_A `cat(1)` clone with wings._"

### `cheat`

[`cheat`](https://opensource.com/article/22/6/linux-cheat-command) is actually a web-service that returns short "cheats"
for command line programmes which will often cover many use cases and save you having to read the rather dry `man` pages
for functions.

### `duf`

### `exa`

### `fd`

[`fd`](https://github.com/sharkdp/fd) is an alternative to `find` that is easier to use. It is "opinionated"
(i.e. decisions have been made about default options that you may not agree with) but purportedly covers ~80% of use
cases.

### `lsd`

[`lsd`](https://github.com/Peltoche/lsd) is `ls`Deluxe and is very similar to [`exa`](#exa) but with a few additions
such as icons. You c

### `tldr`


## Installation

Most of these programmes will be available in your systems package manager.

### Linux

``` bash
# Gentoo
emerge -av bat duf exa fd lsd tldr

# Arch
pacman -Syu bat duf exa fd lsd tldr

# Ubuntu
sudo apt-install bat duf exa fd lsd tldr
```

### OSX

``` bash
brew install bat duf exa fd lsd tldr
``**

### Windows

**WARNING** None of these have been tested I do not have access to a Windows system running PowerShell. They use
[Scoop](https://scoop.sh/) a command-line installer for Windows.

``` bash
scoop install lsd
```

## Links

* [bat: A cat(1) clone with wings.](https://github.com/sharkdp/bat)
* [cheat](https://opensource.com/article/22/6/linux-cheat-command)
* [duf: Disk Usage/Free Utility - a better 'df' alternative](https://github.com/muesli/duf)
* [exa · a modern replacement for ls](https://the.exa.website/)
* [fd](https://github.com/sharkdp/fd)
* [lsd](https://github.com/Peltoche/lsd)
* [tldr](https://tldr.sh/)
