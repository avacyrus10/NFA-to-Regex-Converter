from typing import List, Tuple


class NFA:
    def __init__(self, states_num: int, transitions: List[Tuple[int, str, int]], terminals: List[int]):
        self.states_num = states_num
        self.transitions = transitions
        self.terminals = terminals

    @staticmethod
    def create_nfa() -> 'NFA':
        """
        Get input from the user in the specified format and create the NFA of it.
        :return: NFA obj
        """
        states_num = int(input().strip())
        transitions_num = int(input().strip())

        transitions = []
        for _ in range(transitions_num):
            i, a, j = input().strip().split()
            if a == '0':
                a = '()'
            transitions.append((int(i), a, int(j)))

        terminals_num = int(input().strip())
        terminals = list(map(int, input().strip().split()))

        return NFA(states_num, transitions, terminals)

    def add_final_state_with_epsilon_transitions(self):
        """
        Add a new final state with an epsilon transition from all old final states.
        """
        final_state = self.states_num
        self.states_num += 1
        for t in self.terminals:
            self.transitions.append((t, '()', final_state))
        self.terminals = [final_state]

    def merge_transitions(self):
        """
        Replace multiple edges between any pair of states A and B with one edge
        labeled with the union of the labels of the original edges.
        """
        new_transitions = {}
        for (i, a, j) in self.transitions:
            if (i, j) not in new_transitions:
                new_transitions[(i, j)] = a
            else:
                existing = new_transitions[(i, j)]
                if existing != a:
                    new_transitions[(i, j)] = f"({existing}|{a})"
                else:
                    new_transitions[(i, j)] = existing
        self.transitions = [(i, a, j) for ((i, j), a) in new_transitions.items()]

    def eliminate_state(self, state: int):
        """
        Eliminates a state from the NFA and updates transitions accordingly.

        This method removes a given state from the NFA and reconnects the incoming
        and outgoing transitions through the eliminated state, effectively bypassing it.
        It also handles self-loops by incorporating them into the transition labels.

        :param state: The state to be eliminated from the NFA.
        """
        incoming = [(i, a, j) for (i, a, j) in self.transitions if j == state]
        outgoing = [(i, a, j) for (i, a, j) in self.transitions if i == state]
        self_loop = [(i, a, j) for (i, a, j) in self.transitions if i == state and j == state]

        self.transitions = [(i, a, j) for (i, a, j) in self.transitions if i != state and j != state]

        r_self = self_loop[0][1] if self_loop else ''

        for (i, rin, _) in incoming:
            for (_, rout, j) in outgoing:
                if r_self:
                    new_label = f"{rin}({r_self})*{rout}"
                else:
                    new_label = f"{rin}{rout}"
                self.transitions.append((i, new_label, j))

        self.merge_transitions()
