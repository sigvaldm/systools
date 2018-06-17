# systools
Linux command line tools for home system administration.

These tools are written for myself because I needed them and comes with no guarantee whatsoever.

## Installation
Clone (or download) this folder and put the `bin` subfolder in `$PATH`. For instance if you downloaded to `~/systools`, you could put the following line in your `~/.bashrc` file (or `~/.zshrc.local` if you use Zsh):

```
export PATH=$PATH:$HOME/systools/bin
```

## Overview of commands

| Command   | Description                                          |
|-----------|------------------------------------------------------|
| `dupdir`  | Lists duplicate* subdirectories in a given directory |
| `diffidir`  | Lists the differences between two directories         |

\* Only the names of files are checked. Not their contents.
