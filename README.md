# make-vim-help
Create beautifully formatted Vim helpfiles from markdown files.

## Installation
Clone this repository (or just download `mvh.py`).

## Usage
Run `mvh.py`, with the following options:

| option          | what it does                                           |
|-----------------|--------------------------------------------------------|
| `--input`       | `.markdown` file to convert (default is `./README.md`) |
| `--output`      | name of output file (**required**)                     |
| `--name`        | name of your plugin (**required**)                     |
| `--description` | description of your plugin                             |
| `--tag-prefix`  | "prefix" name for the helpfile tags                    |
| `--author`      | the author's name                                      |
| `--licence`     | the name of the licence for your plugin                |

### Examples
`example.txt` in this repo was created with the following call:

```zsh
py mvh.py --output "example.txt" --name "example.vim" --description "this is a very interesting plugin" --author "PerpetualCreativity" --licence "MIT Licence" --tag-prefix "example-"
```

## Contributing
If you'd like to contribute, please open an issue or a pull request.

