# Apex Legends voicelines

[[_TOC_]]

## What is this package?

I love Apex Legends voice lines so much that I wanted to use it as my window title of my text editor so I created this.

You can also use it in your terminal too. 

Just run `apex-voicelines` in the terminal and it will randomly print one voiceline.

## Install

This package is available on [PyPI](https://pypi.org/project/apex-legends-voicelines/).

Recommended way to install is by using [pipx](https://github.com/pipxproject/pipx/).

Pipx will add isolation so that your system is always unaffected.

```sh
pipx install apex-legends-voicelines
```

But you can also install using your standard `pip`.

```sh
python3 -m pip install apex-legends-voicelines # or pip3 install apex-legends-voicelines
```

### Prerequsities

You need Python 3. 

Recommended version is Python 3.8.

## Usage

To use just run `apex-voicelines`

Example:

```sh
$ apex-voicelines
My squad must be very proud - MRVN aka Pathfinder                                                                                               
```

---

**TODO** Legend selection

Maybe some time later, I will work on specifying which Legend voicelines you need as some argument.

I am thinking of doing something like `apex-voicelines --legend wraith`.

---

**TODO** VSCode support

I don't use VSCode much so I don't know how to make it work with it. But maybe I will look into it.

---

*If anyone figured on how to use it for some other purpose let me know, I'm excited.*

### Using inside Emacs

These voicelines can be used inside Emacs.

You can use the voicelines as the frame title.

This is how I use it.

#### As frame title on startup

Add this to your config

```emacs-lisp
(setq frame-title-format (shell-command-to-string "apex-voicelines"))
```

#### Use interactively

You can also add this in your config and change the title on demand

```emacs-lisp
(defun change-emacs-title-apex ()
  (interactive)
  (setq frame-title-format (shell-command-to-string "apex-voicelines")))
```

Just run `M-x change-emacs-title-apex` to do so.

## License

MIT License
