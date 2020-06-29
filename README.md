# Apex Legends voicelines

[[_TOC_]]

## Install

Recommended way to install is by using [pipx](https://github.com/pipxproject/pipx/).

Pipx will add isolation so that your system is always unaffected.

```sh
pipx install apex-legends-voicelines
```

## Usage

To use just run

```sh
apex-voicelines
```

### Using inside Emacs

These voicelines can be used inside Emacs.

You can use the voicelines as the frame title.

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
