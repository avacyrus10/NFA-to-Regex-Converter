from NFA import NFA


def nfa_to_regex(nfa: NFA) -> str:
    """
    Performs the algorithm.

    First it replaces the final state and in a loop we eliminate states until
    the only states left are the start state and the final state. There will be
    only one transition remaining, and its label will be a regular expression for
    the language recognized by the original NFA.
    :param nfa:
    :return: the regex of the language
    """
    nfa.add_final_state_with_epsilon_transitions()
    nfa.merge_transitions()

    states_to_eliminate = set(range(1, nfa.states_num - 1))
    for state in states_to_eliminate:
        nfa.eliminate_state(state)

    initial_state = 0
    final_state = nfa.terminals[0]

    self_loops = [a for (i, a, j) in nfa.transitions if i == initial_state and j == initial_state]
    if self_loops:
        self_loop_regex = f"({self_loops[0]})*"
    else:
        self_loop_regex = ""

    for (i, a, j) in nfa.transitions:
        if i == initial_state and j == final_state:
            return self_loop_regex + a

    return ""


def main():
    nfa = NFA.create_nfa()
    regex = nfa_to_regex(nfa)
    print(regex)


if __name__ == '__main__':
    main()
