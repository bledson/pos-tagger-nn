import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--min-length',
                    default=0,
                    help='Sentences with size n or less will be ignored.',
                    metavar='n',
                    type=int)
args = parser.parse_args()

interim_prefix_path = '../../data/interim/'
processed_prefix_path = '../../data/processed/'

filenames = ['macmorpho-train.txt', 'macmorpho-dev.txt', 'macmorpho-test.txt']


for f in filenames:
    tsv_file = f.split('.')[0] + '.tsv'
    if not os.path.exists(processed_prefix_path + tsv_file):
        with open(interim_prefix_path + f) as text, \
                open(processed_prefix_path + tsv_file, 'w+') as out:
            for sentence in text:
                tokens_tags = sentence.split()
                if len(tokens_tags) > args.min_length:
                    for token_tag in tokens_tags:
                        token, tag = token_tag.split('_')
                        out_str = token + '\t' + tag + '\n'
                        out.write(out_str)
                    out.write('\n')
