# _*_ coding:UTF-8 _*_
# Author: jay

"""
使用后向最大匹配算法进行分词
"""


def load_dict(path):
    """
    加载词典，返回词典列表和最长词的长度
    :param path:
    :return:
    """
    word_dict = []
    max_dict_word_length = 0
    with open(path, "r", encoding="utf8") as dict_input:
        for word in dict_input:
            if len(word) > max_dict_word_length:
                max_dict_word_length = len(word)
            word_dict.append(word.strip())

    return word_dict, max_dict_word_length

def cut_words(raw_sentence, word_dict, max_dict_word_length):
    """
    基于后向最大匹配酸法进行分词
    :param raw_sentence:
    :param word_dict:
    :return:
    """
    sentence = raw_sentence.strip()
    words_length = len(sentence)
    cut_word_list = []

    while words_length > 0:
        max_cut_length = min(words_length, max_dict_word_length)
        subSentence = sentence[words_length - max_cut_length: words_length]
        while max_cut_length > 0:
            if subSentence in word_dict:
                cut_word_list.append(subSentence)
                break
            elif max_cut_length == 1:
                cut_word_list.append(subSentence)
                break
            else:
                max_cut_length = max_cut_length - 1
                subSentence = sentence[words_length - max_cut_length: words_length]
        words_length = words_length - max_cut_length
        sentence = sentence[:words_length]

    res = "/".join(reversed(cut_word_list))
    return res

if __name__=="__main__":
    path = r"G:\NLPLearner\corpous\30wdict_utf8.txt"
    word_dict, max_dict_word_length = load_dict(path=path)
    sentence = "今天天气非常好，我想出去走走。"
    res = cut_words(raw_sentence=sentence, word_dict=word_dict, max_dict_word_length=max_dict_word_length)
    print(res)