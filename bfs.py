from hanoi import HanoiState


def bfs():
    # def initial node, explored nodes and the next node need to explore
    initial_state = HanoiState(disks=5)
    explored_nodes = []
    next_node = [initial_state]
    # the nodes generated during the search
    generated = 0
    # show path
    final_path = []

    # The node started, pop the first node
    current_state = next_node.pop(0)

    # doing the search
    while not current_state.is_goal_state():
        explored_nodes.append(current_state)
        actions = current_state.possible_actions()

        for action in actions:
            generated += 1
            new_state = current_state.next_state(action[0], action[1])
            if new_state not in explored_nodes and new_state not in next_node:
                next_node.append(new_state)

            if len(next_node) == 0:
                return None

        current_state = next_node.pop(0)

    print(f"explored {len(explored_nodes)} nodes")
    print(f"Generated {generated} nodes.")
    solution = current_state

    while current_state.parent is not None:
        final_path.append(current_state)
        current_state = current_state.parent

    final_path.append(current_state)

    for state in reversed(final_path):
        if state.action is not None:
            print(f"Move disk from peg {state.action[0]} to {state.action[1]}")
        print(state)

    return solution


# run bfs
final_solution = bfs()

if final_solution is None:
    print("No solution found!")
else:
    print("solution found!")
    print(final_solution)
