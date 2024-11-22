from alphabeta import TicTacToe
from alphabeta import alpha_beta_value
import time


def play(state : TicTacToe):
    """Makes turn and prints the result of it until the game is over
    :param state: The initial state of the game (TicTacToe)
    """
    print(alpha_beta_value(state))
    # Implement me

def main():
    """You need to implement the following functions/methods:
    play(state): makes turn and prints the result of it until the game is over
    value() in TicTacToe class: returns the current score of the game
    generate_children() in TicTacToe class: returns a list of all possible states after this turn
    alpha_beta_value(node): implements the MinMax algorithm with alpha-beta pruning
    max_value(node, alpha, beta): implements the MinMax algorithm with alpha-beta pruning
    min_value(node, alpha, beta):implements the MinMax algorithm with alpha-beta pruning
    """
    # empty_board = 3 * '???'
    empty_board = "?????????"
    state = TicTacToe(empty_board, False)
    print(state)
    time0 = time.time_ns()
    play(state)
    print("time spent:", time.time_ns() - time0)


if __name__ == '__main__':
    main()
