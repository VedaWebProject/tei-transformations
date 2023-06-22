import sys
import json
import csv
import pickle
import collections
import pandas as pd
from string import punctuation

csv.field_size_limit(sys.maxsize)

def rec_dd():
    return collections.defaultdict(rec_dd)


def read_zurich(xls_file):
    print("... reading " + xls_file)
    df = pd.read_excel(xls_file)
    # avoid NaN values with ''
    df = df.fillna('')
    j = (df.groupby(['VERS_NR', 'PADA_NR'])
         .apply(lambda x: x.to_dict('records')))
    d = rec_dd()
    for i, r in j.iteritems():
        verse_id = i[0].split('.')
        d[verse_id[0]][verse_id[1]][verse_id[2]][i[1]] = r
    return d

def read_csv_to_dict(filename):
    #csv.field_size_limit = sys.maxsize
    with open(filename) as csv_data:
        #problem with csv.reader-method! --> old school readlines()
        data = list(csv_data.readlines())
        d={}
        for i, row in enumerate(data):
            data[i] = data[i].strip("\n")
            data[i] = data[i].split("\t")
        len_row = len(data[i])
        #read files without subverses i.e. files containing only 2 columns


        for row in data:

            vers_id = row[0]

            # read files without subverses i.e. files containing only 2 columns
            if len_row == 2:
                try:
                    text = row[1]
                    d[vers_id] = text
                except:
                    print("Cannot read the following row: " + str(row))

            # read files with subverses i.e. files containing 3 columns
            elif len_row == 3:
                try:
                    pada_count = row[1]
                    text = row[2]

                    #read rows without subverses
                    if pada_count == "-":
                        d[vers_id] = row[2]

                    # read rows with subverses:
                    else:
                        if pada_count == "1" or pada_count=="a":
                            d[vers_id]=[[pada_count, text]]
                        else:
                            d[vers_id].append([pada_count, text])

                except:
                    print("Cannot read the following row: "+str(row))
        print("... reading", filename, "("+str(len(d))+" stanzas)")
        return d

def read_grassmann_corrections(filename):
    print("... reading " + filename)
    #csv.field_size_limit = sys.maxsize
    with open(filename, "r", encoding="utf-8") as csv_data:
        #problem with csv.reader-method! --> old school readlines()
        reader_list = list(csv.DictReader(csv_data))
        d = {}
        for entry in reader_list:
            lemma = entry["zurich_lemma"]
            if not entry.get("gra_lemma_rank") or entry["gra_lemma_rank"]=="1":
                gra_lemma_id_1 = entry["gra_lemma_id"]
                d[lemma] = {"gra_lemma_id_1": gra_lemma_id_1}
            elif entry["gra_lemma_rank"] == "2":
                gra_lemma_id_2 = entry["gra_lemma_id"]
                d[lemma] = {"gra_lemma_id_1":gra_lemma_id_1, "gra_lemma_id_2": gra_lemma_id_2 }
            else:
                print(lemma)
    return d

def read_json(filename):
    print("... reading " + filename)
    with open(filename) as json_data:
        d = json.load(json_data)
        return d

def write_json(data, filename):
    with open(filename, mode='w', encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=3, ensure_ascii=False)


def serialize(data, filename):
    with open(filename, mode='wb') as outfile:
        pickle.dump(data, outfile, pickle.HIGHEST_PROTOCOL)


def deserialize(filename):
    with open(filename, mode='rb') as input:
        return pickle.load(input, encoding='utf-8')

def clean_up_morpho_info(key):
    key = str(key)
    # for 1.0 digits a la padas
    key = key.strip()
    key = key.rstrip('.0')
    key = key.lower()
    key = key.strip(punctuation)
    return key


