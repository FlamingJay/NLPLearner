# _*_ coding: UTF-8 _*_
#Author jay
"""
使用正向最大匹配算法实现中文分词
"""


def load_dict(path):
    """
    :param path: 字典文件路径
    :return: word_dict
    """
    word_dict = []  # 存储加载好的词典
    max_dict_word_len = 0
    with open(path, "r", encoding="utf8") as dict_input:
        for word in dict_input:
            if len(word) > max_dict_word_len:
                max_dict_word_len = len(word)
            word_dict.append(word.strip())

    return word_dict, max_dict_word_len

# 实现正向最大匹配算法中的切词方法
def cut_words(raw_sentence, word_dict, max_dict_word_length):
    sentence = raw_sentence.strip()
    # 统计序列长度
    words_length = len(raw_sentence)
    # 存储切分好的词语
    cut_word_list = []
    while words_length > 0:
        max_cut_length = min(max_dict_word_length, words_length)
        subSentence = sentence[0:max_cut_length]
        while max_cut_length > 0:
            if subSentence in word_dict:
                cut_word_list.append(subSentence)
                break
            elif max_cut_length == 1:
                cut_word_list.append(subSentence)
                break
            else:
                max_cut_length -= 1
                subSentence = sentence[0:max_cut_length]
        sentence = sentence[max_cut_length:]
        words_length = words_length - max_cut_length
    words = "/".join(cut_word_list)
    return words


if __name__ == '__main__':
    path = "G:/NLPLearner/corpous/30wdict_utf8.txt"
    word_dict, max_dict_word_length = load_dict(path=path)
    sentence = "今天天气非常好，我想出去走走。"
    res = cut_words(sentence, word_dict=word_dict, max_dict_word_length=max_dict_word_length)
    print(res)