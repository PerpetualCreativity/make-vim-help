'''
Make Vim Help. Create beautifully formatted vim helpfiles from markdown files.

Usage:
    mvh.py --output=output --name=name [--input=input_file] [--description=description] [--tag-prefix=tag_prefix] [--author=author] [--licence=licence]
    mvh.py --help

Options:
    --help                      Output this information.
    --output=output             The output file. Required.
    --name=name                 Name of your plugin. Required.
    --input=input_file          The input file. Default is ./README.md.
    --description=description   Description of your plugin.
    --tag-prefix=tag_prefix     The prefix name for your helpfile tags. Default is equal to name.
    --author=author             The author's name.
    --licence=licence           The name of the licence for your plugin.
'''

import re
import textwrap
from docopt import docopt

args = docopt(__doc__)

def main():
    output_file = args['--output']
    name        = args['--name']
    input_file  = args['--input'] or './README.md'
    description = args['--description'] or None
    tag_prefix  = args['--tag-prefix'] or ''
    author      = args['--author'] or None
    licence     = args['--licence'] or None

    with open(output_file, 'w') as o:
        if description:
            o.write(f'*{name}*\t{description}\n')
        else:
            o.write(f'*{name}*\n')
        o.write('\n')
        if author:
            o.write(f'Author: {author}\n')
        if licence:
            o.write(f'Licence: {licence}\n')
        o.write('\n')
        with open(input_file, 'r') as i:
            codeline = False
            header = False
            for line in i:
                # header detection
                if (header := re.search(r"(#{1,2}) (.*)", line)):
                    line = f"{'='*80}\n{header.group(2).upper()}{' '*((78-2*len(header.group(2))-len(tag_prefix)))}*{tag_prefix}{header.group(2).lower()}*\n"
                    header = True
                if (header := re.search(r"(#{3,6}) (.*)", line)):
                    line = f"{'-'*80}\n{header.group(2).upper()}{' '*((78-2*len(header.group(2))-len(tag_prefix)))}*{tag_prefix}{header.group(2).lower()}*\n"
                    header = True
                # link detection
                if (link := re.search(r"(\[.*?\])(\(.*?\))", line)):
                    if (local_link := re.search("(#)(.*?)", link.group(2))):
                        line = replace(r"(\[.*\])(\(.*\))", f"|{tag-prefix}{local_link.group(2).lower()}|", line)
                    else:
                        line = replace(r"(\[.*\])(\(.*\))", f"{link.group(1)} ({link.group(2)})", line)
                if (re.match(r"```\s*", line) and codeline):
                    codeline = False
                    o.write("\n")
                    continue
                if (re.match(r"```", line)):
                    codeline = True
                    continue
                if line[0] != '|' and not header and not codeline:
                    line = textwrap.fill(line, width=80)+'\n'
                if codeline:
                    o.write(f"\t{line}")
                else:
                    o.write(f"{line}")

    print(f'Output is at {output_file}.')

if __name__ == '__main__':
    main()

