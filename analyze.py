from khaiii import KhaiiiApi
api = KhaiiiApi()


def get_nouns_from_sentences(sentences):
    noun_list = []
    for word in api.analyze(sentences):
	    for morph in word.morphs:
                if morph.tag in ['NNG','NNP']:
                    noun_list.append(morph.lex)
    return noun_list 

print(get_nouns_from_sentences('이게 무슨일 인가 자네'))