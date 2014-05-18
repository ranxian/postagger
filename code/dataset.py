# -*- coding: utf-8 -*-


class Dataset:
    """
    self.words
    self.tagged_words
    self.sents
    self.tagged_sents
    """
    def __init__(self, wrd_file, pos_chk_file, srl_file):
        wrd = open(wrd_file, 'r')
        pos_chk = open(pos_chk_file, 'r')
        srl = open(srl_file, 'r')


        self.sents = []
        self.tagged_sents = []
        self.chked_sents = []
        self.words = []
        self.tagged_words = []
        self.vocabulary = []
        self.tag_set = []

        self.srl_tokens = []

        sent = []
        tagged_sent = []
        chked_sent = []

        while True:
            word = wrd.readline()
            line = pos_chk.readline()
            predicate = srl.readline()

            if word == '\n' or word == '':
                if len(sent) > 0:
                    self.sents.append(sent)
                if len(tagged_sent) > 0:
                    self.tagged_sents.append(tagged_sent)
                if (len(chked_sent) > 0):
                    self.chked_sents.append(chked_sent)
                sent = []
                tagged_sent = []
                chked_sent = []
                if word == '\n':
                    continue
                else:
                    break

            word = word.rstrip('\n')
            tag, chunk = line.rstrip('\n').split('\t')
            predicate = predicate.split('\t')[0]
            if not '-' in predicate:
                word = '*' + word
            sent.append(word)
            tagged_sent.append((word, tag))
            chked_sent.append((word, tag, chunk))

            self.words.append(word)
            self.tagged_words.append((word, tag))

        self.vocabulary = set(self.words)
        self.tag_set = set(tag for (word, tag) in self.tagged_words)

        print len(self.sents), 'sentences,', len(self.words), 'words'

def read_words(path, tgtpath):
    f = open(path, 'r')
    f2 = open(tgtpath, 'r')

    sents = []
    sent = []
    while True:
        line = f.readline()
        line2 = f2.readline()
        if line == '':
            break
        word = line.rstrip('\n')
        predicate = line2.rstrip('\n')

        if word == '':
            sents.append(sent)
            sent = []
        else:
            if predicate != '-':
                word = '*' + word
            sent.append((word, None))

    return sents

def read_word_pos(path):
    f = open(path, 'r')
    tagged_sents = []
    sent = []
    while True:
        line = f.readline()
        if line == '':
            break

        line = line.rstrip('\n')
        if line == '':
            tagged_sents.append(sent)
            sent = []
        else:
            word, pos = line.split('\t')
            sent.append((word, pos, None))

    return tagged_sents


    self.vocabulary = set(self.words)
    self.tag_set = set(tag for (word, tag) in self.tagged_words)

def read_word_pos_chk(wordpath, tgt_path, poschkpath):
    wordf = open(wordpath, 'r')
    poschkf = open(poschkpath, 'r')
    tgtf = open(tgt_path, 'r')
    chked_sents = []
    sent = []
    while True:
        line = wordf.readline()
        line2 = tgtf.readline()
        line3 = poschkf.readline()
        if line == '':
            break
        line = line.rstrip('\n')
        line2 = line2.rstrip('\n')
        line3 = line3.rstrip('\n')

        predicate = line2
        pos, chk = line3.split('\n')


train = Dataset('../data/trn.wrd', '../data/trn.pos-chk', '../data/trn.props')
develop = Dataset('../data/dev.wrd', '../data/dev.pos-chk', '../data/dev.props')