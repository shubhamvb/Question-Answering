from CosineSimilarity import getCosineSimilarity
from NERTags import get_ner_tags

window_length = 14

#generated list of paragraph strings of a particular window length
def get_sliding_window(para):

	a=para.split()
	b = [a[i:i+window_length] for i in range(len(a)- (window_length -1))]
	c = []
	for i  in b:
		c.append(" ".join(i))
	
	return c



def get_most_probable_answer(probable_ans):
	
	ner = get_ner_tags(probable_ans)
	print(ner)
	return probable_ans

#Uses Cosine Similarity to get the most probable sentenc, where we expect to discover our answer
def get_answer(window, q):
	maxSimilarity = -float("inf")
	for i in window:
		if getCosineSimilarity(i, q) > maxSimilarity:
			maxSimilarity = getCosineSimilarity(i, q)
			probable_ans = i

	#probable_ans = get_most_probable_answer(probable_ans)
	return probable_ans

#calls the get_answer method for every questions and stores the answer sentence corresponding to every Question id
def get_para_answer(index, para, q_dict):
	output_dict = dict()

	window =get_sliding_window(para)
	
	for i in q_dict:
		id = q_dict[i]
		output_dict[id] = get_answer(window, i)

	return output_dict
	