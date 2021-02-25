from hanoi import HanoiState


def dfs():
    # set initial state, explored nodes and the node next
    initial_state = HanoiState(disks=5)
    explored_nodes = []
    next_node = [initial_state]

    # the nodes number generated
    generated = 0

    current_state = next_node.pop(0)

    while not current_state.is_goal_state():
        explored_nodes.append(current_state)
        actions = current_state.possible_actions()
        for action in actions:
            generated += 1
            new_state = current_state.next_state(action[0], action[1])
            if new_state not in explored_nodes and new_state not in next_node:
                next_node.append(new_state)

            if len(next_node) == 0:
                print("No solution found!")
                return None

        current_state = next_node.pop()

    print("solution found!")
    print(current_state)
    print(f"Explored {len(explored_nodes)} nodes")
    print(f"Generated {generated} nodes")

    # show the search path
    final_path = []
    while current_state.parent is not None:
        final_path.append(current_state)
        current_state = current_state.parent

    final_path.append(current_state)

    for state in reversed(final_path):
        if state.action is not None:
            print(f"Move disk from peg {state.action[0]} tp {state.action[1]}")
        print(state)


dfs()







