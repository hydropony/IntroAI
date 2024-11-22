import os
import math

SMALL_NUMBER = 0.00001


def get_occurrences(filename):
    results = {}
    dir_path = os.path.dirname(os.path.realpath(__file__))

    try:
        with open(os.path.join(dir_path, '..', filename)) as file:
            for line in file:
                count, word = line.strip().split(' ')
                results[word] = int(count)

        return results

    except FileNotFoundError:
        print("File %s was not found." % filename)
        raise
    except Exception as e:
        print("Something terrible happened: %s" % str(e))
        raise


def get_words(filename):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    try:
        with open(os.path.join(dir_path, '..', filename)) as file:
            words = [word for line in file for word in line.split()]

        return words

    except FileNotFoundError:
        print("File %s was not found." % filename)
        raise
    except Exception as e:
        print("Something terrible happened: %s", str(e))
        raise


class SpamHam:
    """ Naive Bayes spam filter
        :attr spam: dictionary of occurrences for spam messages {word: count}
        :attr ham: dictionary of occurrences for ham messages {word: count}
    """

    def __init__(self, spam_file, ham_file):
        self.spam = get_occurrences(spam_file)
        self.ham = get_occurrences(ham_file)
        self.spamNum = 75268
        self.hamNum = 290673

    def evaluate_from_file(self, filename):
        words = get_words(filename)
        return self.evaluate(words)

    def evaluate_from_input(self):
        words = input().split()
        return self.evaluate(words)

    def evaluate(self, words):
        """
        :param words: Array of str
        :return: probability that the message is spam (float)
        """
        # Implement me
        R = 1
        logR = 0
        for word in words:
            if word in self.spam:
                pWordWhenSpam = self.spam[word] / self.spamNum
            else:
                pWordWhenSpam = SMALL_NUMBER
            
            if word in self.ham:
                pWordWhenHam = self.ham[word] / self.hamNum
            else:
                pWordWhenHam = SMALL_NUMBER 
            
            R *= pWordWhenSpam / pWordWhenHam
            logR += math.log(pWordWhenSpam) - math.log(pWordWhenHam)
            # print(pWordWhenSpam, pWordWhenHam)
        
        spamprobability = R / (1 + R)
        R = math.exp(logR)
        spamprobability2 = R / (1 + R)
        return (spamprobability, spamprobability2)
