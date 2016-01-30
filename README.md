# Scrollin
Scrollin' is a script written in Python that lets you output scrolling text on your i3 bar.

Obs! Scrollin's scrolling speed is restricted by the inverval time of i3 & i3blocks.

Current features:

	Static text
	Dates

In development:

	Music
	Static text

Dependencies:

	i3
	i3blocks
	
# How to use
Run the script from your i3blocks config, example:

```bash
[scrollin]
command=python ~/.config/i3blocks/scripts/scrollin/scroll.py
label=
interval=1
```

For date just add #date in config.txt, example:

```txt
#date
```

For static text add your text into cache.txt and make sure that config.txt is empty, example:

```txt
This static text will scroll
```

