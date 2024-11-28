from perceptron import Perceptron
from nearest import Nearest

IMGS_FILE = 'mnist-x.data'
CHARS_FILE = 'mnist-y.data'


def main():
    """
    Implement the perceptron algorithm in the Perceptron class. After that you can try out the
    values of different number pairs by changing the values of the 'target_char' and
    'opposite_char' variables.
    """
    perc = Perceptron(IMGS_FILE, CHARS_FILE)
    perc.train('4', '9', 100)
    print(perc.test('4', '9'))
    perc.save_weights('weights.bmp') # 1 and 7 sometimes give around 0.5 score, 8 and 0 are very easy to classify with success rate over .88 consistently
    # near = Nearest(IMGS_FILE, CHARS_FILE)
    # print(near.test('4', '9'))

if __name__ == '__main__':
    main()
