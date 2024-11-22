TEMPLATE_FIELD = '|e|e|e|\n|e|e|e|\n|e|e|e|\n'
HUGE_NUMBER = 1000000


class AlphaBetaNode(object):
    def __init__(self):
        pass

    def generate_children(self):
        pass

    def is_max_node(self):
        pass

    def is_end_state(self):
        pass

    def value(self):
        pass


class TicTacToe(AlphaBetaNode):
    """Class that contains current state of the game and implements AlphaBetaNode methods
    :attr state: Current state of the board (str)
    :attr state: Indicates whose turn it is (Boolean)
    """

    def __init__(self, state, crosses_turn):
        super().__init__()
        self.state : str = state
        self.crosses_turn = crosses_turn
        self.best_child = None

    def is_end_state(self):
        return ('?' not in self.state) or self.won('x') or self.won('o')

    def won(self, c):
        triples = [self.state[0:3], self.state[3:6], self.state[6:9], self.state[::3], self.state[1::3],
                   self.state[2::3], self.state[0] + self.state[4] + self.state[8],
                   self.state[2] + self.state[4] + self.state[6]]
        combo = 3 * c
        return combo in triples

    def __str__(self):
        field = TEMPLATE_FIELD
        for c in self.state:
            field = field.replace('e', c, 1)

        return field

    def is_max_node(self):
        return self.crosses_turn

    def generate_children(self):
        """
        Generates list of all possible states after this turn
        :return: list of TicTacToe objects
        """
        # Implement me
        children = list()
        for i in range(9):
            if self.state[i] == '?':
                if self.crosses_turn:
                    newstate = self.state[:i] + 'x' + self.state[i+1:]
                else:
                    newstate = self.state[:i] + 'o' + self.state[i+1:]
                children.append(TicTacToe(newstate, not self.crosses_turn))
        return children

    def value(self):
        """
        Current score of the game (0, 1, -1)
        :return: int
        """
        # Implement me
        if self.won('o'):
            return -1
        elif self.won('x'):
            return 1
        else:
            return 0


def alpha_beta_value(node : TicTacToe):
    """Implements the MinMax algorithm with alpha-beta pruning
    :param node: State of the game (TicTacToe)
    :return: int
    """
    if node.is_max_node():
        ret = max_value(node, -1, 1)
    else:
        ret = min_value(node, -1, 1)
    print('optimal move')
    print(node.best_child)
    return ret
    # Implement me


def max_value(node : TicTacToe, alpha, beta):
    # Implement me
    if node.is_end_state():
        return node.value()
    v = -HUGE_NUMBER
    for child in node.generate_children():
        # print(child)
        mv = min_value(child, alpha, beta) 
        if mv > v:
            node.best_child = child
            v = mv
        # v = max(v, min_value(child, alpha, beta))
        alpha = max(alpha, v)
        if alpha >= beta:
            return v
    # print(node.best_child)
    return v


def min_value(node : TicTacToe, alpha, beta):
    # Implement me
    if node.is_end_state():
        return node.value()
    v = HUGE_NUMBER
    for child in node.generate_children():
        mv = max_value(child, alpha, beta)
        if mv < v:
            v = mv
            node.best_child = child
        # v = min(v, max_value(child, alpha, beta))
        beta = min(beta, v)
        if alpha >= beta:
            return v
    # print(node.best_child)
    return v
