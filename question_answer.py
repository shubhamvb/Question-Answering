from CosineSimilarity import getCosineSimilarity
from nltk.tag.stanford import StanfordNERTagger

def get_sliding_window(para):

	a=para.split()
	b = [a[i:i+12] for i in range(len(a)-11)]
	c = []
	for i  in b:
		c.append(" ".join(i))
	
	return c

def get_ner_tags(answer):

	st = StanfordNERTagger('/Users/shubhambarhate/Desktop/project3/stanford-ner-2017-06-09/classifiers/english.all.3class.distsim.crf.ser.gz',
           '/Users/shubhambarhate/Desktop/project3/stanford-ner-2017-06-09/stanford-ner.jar')

	return st.tag(context_list[0].split())


def get_most_probable_answer(probable_ans):
	
	ner = get_ner_tags(probable_ans)
	print(ner)
	return probable_ans

def get_answer(window, q):
	maxSimilarity = -float("inf")
	for i in window:
		if getCosineSimilarity(i, q) > maxSimilarity:
			maxSimilarity = getCosineSimilarity(i, q)
			probable_ans = i

	#probable_ans = get_most_probable_answer(probable_ans)
	return probable_ans

def get_para_answer(index, para, q_dict):
	output_dict = dict()

	window =get_sliding_window(para)
	
	for i in q_dict:
		id = q_dict[i]
		output_dict[id] = get_answer(window, i)

	return output_dict
	