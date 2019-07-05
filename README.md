# changelog-cli

This tool is aiming at reducing conflicts in trunk-based or feature-based git developement.

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

```

