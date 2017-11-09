
# coding: utf-8

# In[102]:

import json
from nltk.tag.stanford import StanfordNERTagger
from question_answer import get_para_answer

def read_json(file):
    with open(file, 'r') as f:
        text = json.load(f)
    return text

def convert_input_to_dict(text):
    data_length = len(text['data'])
    context_list = list()
    test_dict = dict()
    for i in range(data_length):
        data = text['data'][i]
        para_length = len(data['paragraphs'])
        para = data['paragraphs']
        #print(para_length)
        
        for j in range(para_length):
            key = len(context_list)
            context_list.insert(key, para[j]['context'])
            if key not in test_dict:
                test_dict[key] = dict()
                
            qas_length = len(para[j]['qas'])
            qas = para[j]['qas']
            
            for k in range(qas_length):
                if qas[k]['question'] not in test_dict[key]:
                    test_dict[key][qas[k]['question']] = dict()
                test_dict[key][qas[k]['question']] = str(qas[k]['id'])
                #print(str(qas[k]['question']) +" : " +str(qas[k]['id']))
        
    return test_dict, context_list
    

def generate_output_json(dictionary):
    filename = "output.json"
    with open(filename, 'w') as f:
        json.dump(dictionary, f)
    


# In[103]:

def main():
    
    sample_file = "sample.json"
    train_file = "training.json"
    test_file = "testing.json"
    
    
    #sample_text = read_json(sample_file)
    #train_text = read_json(train_file)
    test_text = read_json(test_file)

    #test_dict contains the json text for testing.json
    test_dict, context_list = convert_input_to_dict(test_text)
    
    #ans_dict will have q id as key and answer phrase as the value
    ans_dict = dict()
    index = 0

    #this just gets answers for the questions associated with the first paragraph
    dictionary = get_para_answer(0, context_list[0], test_dict[0])
    ans_dict.update(dictionary)

    #generic loop for iterating through every paragraph and and getting answers for its questions
    '''
    for i in context_list:
        dictionary = get_para_answer(index, i, test_dict[index])
        ans_dict.update(dictionary)
        index += 1
    '''
    
    #Used to generate the output json file
    generate_output_json(ans_dict)
    
    '''
    st = StanfordNERTagger('/Users/shubhambarhate/Desktop/project3/stanford-ner-2017-06-09/classifiers/english.all.3class.distsim.crf.ser.gz',
           '/Users/shubhambarhate/Desktop/project3/stanford-ner-2017-06-09/stanford-ner.jar')
    print(st.tag(context_list[0].split()))
    '''
    
    
if __name__ == "__main__":
    main()


# In[ ]:



