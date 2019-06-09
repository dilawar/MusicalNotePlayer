"""main.py: 
Play a note.
"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import sys
import os
import helper

def main(**kwargs):
    n = helper.find_note(kwargs['note'])
    print( n )
    pass


if __name__ == '__main__':
    import argparse
    # Argument parser.
    description = '''Play a note or midi file using aplay'''
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--note', '-n'
        , required = True
        , help = 'Name of the note'
        )
    parser.add_argument('--duration', '-d'
        , required = False, default = 1.0
        , help = 'Duration of playback (sec).'
        )
    class Args: pass 
    args = Args()
    parser.parse_args(namespace=args)
    main( **vars(args) )
