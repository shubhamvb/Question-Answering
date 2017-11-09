from nltk.tag.stanford import StanfordNERTagger

#gets the NER tags for a probable answer setnence
def get_ner_tags(answer):

	#download teh stanford ner zip file and extract it .
	#Change the directory location in the folllowing path
	st = StanfordNERTagger('/Users/shubhambarhate/Desktop/project3/stanford-ner-2017-06-09/classifiers/english.all.3class.distsim.crf.ser.gz',
           '/Users/shubhambarhate/Desktop/project3/stanford-ner-2017-06-09/stanford-ner.jar')

	return st.tag(context_list[0].split())