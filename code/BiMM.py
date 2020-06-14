# _*_ coding:utf-8 _*_
# author:jay
import FMM
import BMM

def load_dict(path):
    """
    加载词典，返回词典列表和词典中最长词的长度
    :param path:
    :return:
    """
    word_dict = []
    max_dict_word_length = 0
    with open(path, "r", encoding="utf8") as dict_input:
        for word in dict_input:
            if len(word) > max_dict_word_length:
                max_dict_word_length = len(word)
            word_dict.append(word)

    return word_dict, max_dict_word_length

def cut_words(raw_sentence, word_dict, max_dict_word_length):
    """
    实现双向最长匹配算法进行分词
    :param raw_sentence:
    :param word_dict:
    :param max_dict_word_length:
    :return:
    """
    bmm_word_list = BMM.cut_words(raw_sentence, word_dict, max_dict_word_length).split("/")
    fmm_word_list = FMM.cut_words(raw_sentence, word_dict, max_dict_word_length).split("/")
    bmm_len = len(bmm_word_list)
    fmm_len = len(fmm_word_list)
    if bmm_len != fmm_len:
        if bmm_len < fmm_len:
            return "/".join(bmm_word_list)
        else:
            return "/".join(fmm_word_list)
    else:
        FSingle = 0
        BSingle = 0
        isSame = True
        for i in range(bmm_len):
            if bmm_word_list[i] != fmm_word_list[i]:
                isSame = False
            if len(bmm_word_list[i]) == 1:
                BSingle += 1
            if len(fmm_word_list[i]) == 1:
                FSingle += 1
        if isSame:
            return "/".join(bmm_word_list)
        if BSingle < FSingle:
            return "/".join(bmm_word_list)
        else:
            return "/".join(fmm_word_list)

if __name__ == '__main__':
    path = "G:/NLPLearner/corpous/30wdict_utf8.txt"
    word_dict, max_dict_word_length = load_dict(path=path)
    sentence = "今天天气非常好，我想出去走走。"
    res = cut_words(sentence, word_dict=word_dict, max_dict_word_length=max_dict_word_length)
    print(res)