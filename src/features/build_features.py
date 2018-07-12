import os

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
                for token_tag in tokens_tags:
                    token, tag = token_tag.split('_')
                    out_str = token + '\t' + tag + '\n'
                    out.write(out_str)
                out.write('\n')
