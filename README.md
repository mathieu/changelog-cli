# changelog-cli

This tool is aiming at reducing conflicts in trunk-based or feature-based git developement.

## Install

```shell
> pip install cli_changelog
```

## Usage

```text
usage: changelog [-h] [-c message] [-r version] [-f FILENAME]

Changelog administration tool.

optional arguments:
  -h, --help            show this help message and exit
  -c message, --create message
                        creates an entry with this actual message to be added
                        to the changelog
  -r version, --release version
                        releases the changelog byt gathering all entries
  -f FILENAME, --filename FILENAME
                        the filename to put the message in if you don't want
                        to use the branch name
  -t, --commit          commit the created/deleted/modified files by this
                        command
```

## Flow example 

```shell
> changelog -c "Initial import" -f init
> changelog -c "Added readme content" -f readme
```

will give this layout

```text
├── CHANGELOG.md
├── README.md
├── changelog.py
└── changelogs/
│  └──── unreleased/
│     ├──── init.md
│     └──── readme.md
└── requirements.txt
```

And now releasing version 1.0.0 like this

```shell
> changelog -r 1.0.0
```

will give this layout

```text
├── CHANGELOG.md
├── README.md
├── changelog.py
└── requirements.txt
```

## Requirements

* tested with python3
