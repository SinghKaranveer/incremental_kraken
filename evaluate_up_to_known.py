import os
import pickle
import sys
from functools import reduce
from os import path
import numpy as np

import matplotlib.pyplot as plt


def get_directory_structure(rootdir):
    dir = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = reduce(dict.get, folders[:-1], dir)
        parent[folders[-1]] = subdir
    return dir['training_data']

if path.exists("NCBI_cache.pickle"):
    with open("NCBI_cache.pickle", "rb") as handle:
        h = pickle.load(handle)
else:
    h = {}

with open('nodes.pickle', 'rb') as handle:
    n = pickle.load(handle)

dir_struct = get_directory_structure('/scratch/djd378/training_data/')

def find_accuracies(path, year, fold):
    counts = \
            {
                'no rank': 0,
                'species': 0,
                'genus': 0,
                'family': 0,
                'order': 0,
                'class': 0,
                'phylum': 0,
                'superkingdom': 0,
                'subspecies': 0,
                'subphylum': 0,
                'suborder': 0,
                'species subgroup': 0,
                'subclass': 0,
                'tribe': 0,
                'subfamily': 0,
                'subgenus': 0,
                'species group' : 0
            }
    totals = \
            {
                'no rank': 1,
                'species': 1,
                'genus': 1,
                'family': 1,
                'order': 1,
                'class': 1,
                'phylum': 1,
                'superkingdom': 1,
                'subspecies': 1,
                'subphylum': 1,
                'suborder': 1,
                'species subgroup': 1,
                'subclass': 1,
                'tribe': 1,
                'subfamily': 1,
                'subgenus': 1,
                'species group' : 1
            }
    skipped = 0
    U_miss = 0
    with open(path) as f:
        for line in f:
            
            l = line.split()
            if  (l[0] == 'C' or  l[0] == 'U') and is_valid_misclass(l[1], year):
                if l[0] == 'C':
                    actual = l[1] 
                    predicted = l[2]
                    
                    if predicted == '0':
                        skipped += 1
                        continue
        
                    tree = []
                    actual_parent = 0
                    while actual_parent != '1':
                        if actual == "1049581":
                            actual = "293387"
                        elif actual == "330":
                            actual = "301"
                        elif actual == "2172536":
                            actual = "2698682"
                        elif actual == "2109625":
                            actual = "2605946"
                        elif actual == "2480923":
                            actual = "2674991"
                        elif actual == "2183547":
                            actual = "998844"
                        elif actual == "2016518":
                            actual = "2016517" 
                        elif actual == "2494549":
                            actual = "2707005" 
                        elif actual == "2016519":
                            actual = "2016517" 
                        actual_parent, actual_level = n[actual]
                        if actual_parent != '1':
                            tree.append((actual_parent, actual_level))
                        actual = actual_parent
        
                    pred_parent = 0
                    while pred_parent != '1': 
                        pred_parent, pred_level = n[predicted]
                        if pred_parent != '1':
                            if (pred_parent, pred_level) in tree:
                                if pred_level in counts.keys():
                                    counts[pred_level] += 1
                                    totals[pred_level] += 1
                            else:
                                # first check if present in training data
                                #if is_valid_misclass(l[1], year):
                                #    for level in totals.keys():
                                #totals[level] += 1
                                totals[pred_level] += 1

                        predicted = pred_parent
                
                if l[0] == 'U':
                    #for level in totals.keys():
                    #    totals[level] += 1
                    for level in totals.keys():
                        totals[level] += 1
                        U_miss += 1

    for level, count in counts.items():
        print('level:{}'.format(level))
        print(count/totals[level])
    print('species: {} '.format(totals['species']))
    print('skipped:')
    print(skipped)
    print('missed Us: {}'.format(U_miss))
    return(counts, totals)

def evaluate_fold(path):
    years = []
    scores = []
    for subdir, dirs, files in os.walk(path):
        for file in files:
            ext = file.split('.')[-1]
            if ext != "sh":
                year = file.split('_')[2][:4]
                years.append(year)
                print(year)
                fold = sys.argv[1][:-1]
                counts, totals = find_accuracies(os.path.join(subdir, file), year, fold)
                print("")
                scores.append((counts, totals))
    print(len(scores))
    plt.figure()
    print(scores[0][0])
    species = []
    genus = []
    phylum = []
    family = []
    order = []
    class_ = []
    year_list = []
    for i in range(1999, 2020):
        idx = years.index(str(i))
        year_list.append(str(i))
        genus.append(scores[idx][0]['genus'] / scores[idx][1]['genus'])
        species.append(scores[idx][0]['species'] / scores[idx][1]['species'])
        phylum.append(scores[idx][0]['phylum'] / scores[idx][1]['phylum'])
        family.append(scores[idx][0]['family'] / scores[idx][1]['family'])
        order.append(scores[idx][0]['order'] / scores[idx][1]['order'])
        class_.append(scores[idx][0]['class'] / scores[idx][1]['class'])
    plt.plot(year_list, species, label = "Species")
    plt.plot(year_list, genus, label = "Genus")
    plt.plot(year_list, phylum, label = "Phylum")
    plt.xlabel("Year")
    plt.ylabel("Accuracy")
    plt.legend()
    #plt.show()
    return (species, genus, phylum, family, order, class_)

def is_valid_misclass(taxid, max_year):
    for year in range(1999, int(max_year) + 1):
        year = str(year)
        for year_child in dir_struct[year].keys():
            if year_child.startswith('fold'):
                for fold_child in dir_struct[year][year_child].keys():
                    if fold_child == taxid:
                        return True
    return False

def in_training_data(tax, max_year):
    training_path = "/lustre/scratch/djd378/training_data/"
    for year in range(1999, int(max_year)+1):
        if os.path.isdir(training_path + str(year)+ '/fold1/' + str(tax)) == True:
            return True
        if os.path.isdir(training_path + str(year)+ '/fold2/' + str(tax)) == True:
            return True
        if os.path.isdir(training_path + str(year)+ '/fold3/' + str(tax)) == True:
            return True
        if os.path.isdir(training_path + str(year)+ '/fold4/' + str(tax)) == True:
            return True
        if os.path.isdir(training_path + str(year)+ '/fold5/' + str(tax)) == True:
            return True
    return False

if __name__ == "__main__":
    species_scores = []
    phylum_scores = []
    genus_scores = []
    family_scores = []
    order_scores = []
    class_scores = []
    for i in range(1, len(sys.argv)):
        print("Fold : {}\n".format(sys.argv[i]))
        species, genus, phylum, family, order, class_= evaluate_fold(sys.argv[i])
        species_scores.append(species)
        phylum_scores.append(phylum)
        genus_scores.append(genus)
        family_scores.append(family)
        order_scores.append(order)
        class_scores.append(class_)
    species_scores = np.array(species_scores)
    genus_scores = np.array(genus_scores)
    phylum_scores = np.array(phylum_scores)
    family_scores = np.array(family_scores)
    order_scores = np.array(order_scores)
    class_scores = np.array(class_scores)
    np.savetxt("species.txt", species_scores, delimiter=',')
    np.savetxt("genus.txt", genus_scores, delimiter=',')
    np.savetxt("phylum.txt", phylum_scores, delimiter=',')
    np.savetxt("family.txt", family_scores, delimiter=',')
    np.savetxt("order.txt", order_scores, delimiter=',')
    np.savetxt("class.txt", class_scores, delimiter=',')
    print("2019 MEAN = {}".format(np.mean(species_scores[:,-1])))
