import os
import tarfile
import urllib.request as request
import zipfile

raw_prefix_path = '../../data/raw/'
interim_prefix_path = '../../data/interim/'

urlmacmorpho = 'http://www.nilc.icmc.usp.br/macmorpho/macmorpho-v3.tgz'
urlskip300 = 'http://143.107.183.175:22980/download.php?file=embeddings/word2vec/skip_s300.zip'


def maybe_download(filename, url, expected_bytes):
    local_filename = raw_prefix_path + filename
    if not os.path.exists(local_filename):
        local_filename, _ = request.urlretrieve(url, local_filename)
    statinfo = os.stat(local_filename)
    if statinfo.st_size == expected_bytes:
        print('Found and verified', filename)
    else:
        print(statinfo.st_size)
        raise Exception('Failed to verify ' + local_filename +
                        '. Can you get to it with a browser?')
    return local_filename


macmorpho = maybe_download('macmorpho-v3.tgz', urlmacmorpho, 2463485)
word2vec = maybe_download('skip_s300.zip', urlskip300, 964026201)


def extract_from(filename):
    extension = filename.split('.')[-1]
    if extension == 'tgz':
        tar = tarfile.open(filename)
        for archive in tar.getnames():
            if not os.path.exists(interim_prefix_path + archive):
                tar.extract(archive, interim_prefix_path)
    elif extension == 'zip':
        zip = zipfile.ZipFile(filename)
        for archive in zip.namelist():
            if not os.path.exists(interim_prefix_path + archive):
                zip.extract(archive, interim_prefix_path)


extract_from(macmorpho)
extract_from(word2vec)
