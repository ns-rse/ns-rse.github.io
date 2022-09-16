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

[`bat`](https://github.com/sharkdp/bat) is "_A `cat(1)` clone with wings._". It automatically uses syntax highlighting
and integrates with git if a file is version controlled to show changes and lots more. You can pipe input to it,
including from e.g. `curl -s https://server.com/some_file`


#### Examples

``` bash
❱ bat pyproject.toml
───────┬──────────────────────────────────────────────
       │ File: pyproject.toml
───────┼──────────────────────────────────────────────
   1   │ [build-system]
   2   │ requires = [
   3   │   "setuptools",
   4   │   "versioneer==0.26",
   5   │   "wheel"]
   6   │ build-backend = "setuptools.build_meta"
   7   │
   8   │ [tool.black]
   9   │ line-length = 120
  10   │ target-version = ['py38', 'py39', 'py310']
  11   │ include = '\.pyi?$'
───────┴──────────────────────────────────────────────
```

#### Aliases

N/A - no aliases required, just use `bat` instead of `cat` it will by default recognise file types and print with
appropriate syntax highlighting.

#### Configuration

You can generate a default configuration file with

``` bash
bat --generate-config-file
```

This will be saved at `~/.config/bat/config` and you can edit it as desired


### `cheat`

[`cheat`](https://opensource.com/article/22/6/linux-cheat-command) is actually a web-service that returns short "cheats"
for command line programmes which will often cover many use cases and save you having to read the rather dry `man` pages
for functions.

#### Examples

``` bash
❱ cheat cheat
 cheat:cheat
# To see example usage of a program:
cheat <command>

# To edit a cheatsheet
cheat -e <command>

# To list available cheatsheets
cheat -l

# To search available cheatsheets
cheat -s <command>

# To get the current `cheat' version
cheat -v

 tldr:cheat
# cheat
# Create and view interactive cheat sheets on the command-line.
# More information: <https://github.com/cheat/cheat>.

# Show example usage of a command:
cheat command

# Edit the cheat sheet for a command:
cheat -e command

# List the available cheat sheets:
cheat -l

# Search available the cheat sheets for a specified command name:
cheat -s command

# Get the current cheat version:
cheat -v
```

#### Aliases

``` bash

```

### `duf`

[duf](https://github.com/muesli/duf)

#### Examples

``` bash

```
#### Aliases

``` bash

```

### `exa`

#### Examples

``` bash

```
#### Aliases

``` bash

```

#### Examples

``` bash

```
#### Aliases

``` bash

```

### `fd`

[`fd`](https://github.com/sharkdp/fd) is an alternative to `find` that is easier to use. It is "opinionated"
(i.e. decisions have been made about default options that you may not agree with) but purportedly covers ~80% of use
cases.

#### Examples

``` bash

```
#### Aliases

``` bash

```

### `lsd`

[`lsd`](https://github.com/Peltoche/lsd) is `ls`Deluxe and is very similar to [`exa`](#exa) but with a few additions
such as icons.

#### Examples

``` bash
❱ l
.rw-r--r-- neil neil  144 B  Sun Aug 14 19:56:53 2022  #.gitlab-ci.yml#
drwxr-xr-x neil neil  4.0 KB Thu Sep 15 22:21:25 2022  .
drwxrwxr-x root users 4.0 KB Tue Aug 30 20:46:37 2022  ..
drwxr-xr-x neil neil  4.0 KB Thu Sep 15 22:21:56 2022  .git
drwxr-xr-x neil neil  4.0 KB Sun Aug 14 21:51:03 2022  .github
.rw-r--r-- neil neil  613 B  Sun Aug 14 21:44:38 2022  .gitignore
.rw-r--r-- neil neil  151 B  Sun Aug 14 19:56:13 2022  .gitlab-ci.yml
drwxr-xr-x neil neil  4.0 KB Thu Sep 15 22:21:25 2022  .quarto
.rw-r--r-- neil neil  386 B  Thu Sep 15 22:05:23 2022  _quarto.yaml
.rw-r--r-- neil neil  263 B  Sun Aug 14 10:59:13 2022  _quarto.yml~
drwxr-xr-x neil neil  4.0 KB Thu Sep 15 22:05:24 2022  _site
.rw-r--r-- neil neil  1.1 KB Thu Sep 15 22:05:23 2022  about.qmd
.rw-r--r-- neil neil  455 B  Sun Aug 14 11:02:13 2022  about.qmd~
drwxr-xr-x neil neil  4.0 KB Thu Sep 15 22:05:23 2022  img
.rw-r--r-- neil neil  185 B  Sun Aug 14 22:22:04 2022  index.qmd
.rw-r--r-- neil neil  191 B  Sun Aug 14 10:59:13 2022  index.qmd~
.rw-r--r-- neil neil   34 KB Sun Aug 14 21:14:38 2022  LICENSE
.rw-r--r-- neil neil  1.7 KB Thu Sep 15 22:05:23 2022  links.qmd
.rw-r--r-- neil neil  237 B  Thu Sep 15 21:46:30 2022  links.qmd~
drwxr-xr-x neil neil  4.0 KB Wed Sep 14 20:24:25 2022  posts
.rw-r--r-- neil neil  378 B  Thu Aug 25 23:20:16 2022  README.md
.rw-r--r-- neil neil   13 B  Sun Aug 14 21:58:38 2022  requirements.txt
.rw-r--r-- neil neil   17 B  Sun Aug 14 21:24:35 2022  styles.css
drwxr-xr-x neil neil  4.0 KB Thu Aug 25 23:20:16 2022  www
```

#### Aliases

``` bash
alias ls='lsd'
alias l='ls -lha'
alias lla='ls -la'
alias lt='ls --tree'
```

### `tldr`


#### Examples

``` bash

```

#### Aliases

``` bash

```

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
```

### Windows

**WARNING** None of these have been tested I do not have access to a Windows system running PowerShell. They use
[Scoop](https://scoop.sh/) a command-line installer for Windows.

``` bash
scoop install lsd
```

## Links

* [bat](https://github.com/sharkdp/bat)
* [cheat](https://opensource.com/article/22/6/linux-cheat-command)
* [duf](https://github.com/muesli/duf)
* [exa](https://the.exa.website/)
* [fd](https://github.com/sharkdp/fd)
* [lsd](https://github.com/Peltoche/lsd)
* [tldr](https://tldr.sh/)
