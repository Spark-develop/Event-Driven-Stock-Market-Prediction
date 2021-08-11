from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import textacy
import spacy
# import pickle


def SVO(filepath):
	all_lower_title = []
	with open(filepath, 'r',encoding="utf-8") as f:
		for line in f.readlines():
			line = line.split()
			all_lower_title.append(" ".join(line[4:]))
	model='en_core_web_lg'
	nlp = spacy.load(model)

	# start process
	svo_results = []
	len_titles = len(all_lower_title)

	for n,title in enumerate(all_lower_title):
		all_lower_title_unicode = title
		docs = nlp(all_lower_title_unicode)
		b = textacy.extract.subject_verb_object_triples(docs)
		svo = list(b)
		if len(svo) > 0:
			i = svo[0]
			svo_results.append([str(j) for j in i])
	print ("total sents:",len_titles,"extracted sents:",len(svo_results),
		"extraction_rate:", len(svo_results)/float(len_titles))
	f1 = open('datasets/entities.txt','w')
	f2 = open('datasets/relations.txt','w')
	f3 = open('datasets/train_triplet.txt','w')
	for eni in range(len(svo_results)):
		print(svo_results[eni][0][1:-1].split()[0])
		try:
			f1.write("%s\n"%str(svo_results[eni][0][1:-1].split()[0]).replace(',',""))
			f1.write("%s\n"%str(svo_results[eni][2][1:-1].split()[0]).replace(',',""))
			f2.write("%s\n"%str(svo_results[eni][1][1:-1].split()[0]).replace(',',""))
			f3.write("%s %s %s\n"%(str(svo_results[eni][0][1:-1].split()[0]).replace(',',""),str(svo_results[eni][1][1:-1].split()[0]).replace(',',""),str(svo_results[eni][2][1:-1].split()[0]).replace(',',"")))
		except Exception:
			pass
	f1.close()
	f2.close()
	f3.close()


file_path = 'datasets/train.txt'
SVO(file_path)
