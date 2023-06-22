from lxml import etree
import pathlib
import argparse


def validate(file, schema):
    relaxng_doc = etree.parse(schema)
    relaxng = etree.RelaxNG(relaxng_doc)
    doc = etree.parse(file)
    tei_relaxng = relaxng.validate(doc)
    try:
        relaxng.assert_(doc)
    except AssertionError as err:
        print('TEI validation error:', err)
    return tei_relaxng


def validate_all(args):
    path_to_tei_files = args.vedaweb_rigveda_tei
    files = pathlib.Path(path_to_tei_files).glob('*rv_book*')
    for f in files:
        valid = validate(str(f), path_to_tei_files + '/vedaweb.rng')
        print(f, valid)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('vedaweb_rigveda_tei',
                        help='path to vedaweb_rigveda_tei')
    args = parser.parse_args()
    validate_all(args)
