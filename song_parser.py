'''
See def main() docstring
'''

import argparse


def main():
    '''
    Takes a single argument - a filepath and name of a text file
    which in this current project are in folder raw/song_name
    and retuns a printout of the song parsed for e-songbooks
    @todo: make the output write to a out/song_name file
    '''
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('filenames', metavar='N', type=str, nargs='+',
                        help='file to be done')

    args = parser.parse_args()

    for filename in args.filenames:
        print filename
        with open(filename, 'r') as file_handle:
            raw_text = file_handle.readlines()

        output = []
        for line in raw_text:
            if line[0] == '#':
                output.append('<i>{}</i><br>'.format(line[1:]))
            elif raw_text[0] == line:
                title = line
                output.append('<h2 id=''>{}</h2>'.format(line))
            elif line == '\n':
                output.append('\n</p><p>')
            else:
                output.append('{}<br>'.format(line))

        with open('out/{}.out'.format(title), 'w') as fh_out:
            for line in output:
                fh_out.write(line)

main()
if __name__ == '__main__':
    main
