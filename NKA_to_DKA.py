import networkx as nx
import matplotlib.pyplot as plt


def nka_to_dka(states, alphabet, connection_arr):
    new_states = [states[0]]
    new_connection_arr = []

    # Создаем новые вершины и связи между ними
    for new_state in new_states:
        for letter in alphabet:
            state_arr = set()
            for connection in connection_arr:
                if connection[0] in new_state and connection[1] == letter:
                    state_arr.add(connection[2])
            sorted_string = ''.join(sorted(state_arr))
            if sorted_string not in new_states:
                new_states.append(sorted_string)
            if sorted_string != '' and sorted_string not in new_state:
                new_connection_arr.append([new_state, letter, sorted_string])

    return new_connection_arr


if __name__ == "__main__":
    # Ввод вершин автомата
    states = input("input states: ").split()

    # Ввод символов
    alphabet = input("input alphabet: ").split()

    print(states)
    print(alphabet)

    connection_arr = []
    # Ввод связей между вершинами
    s = input()
    while s != '':
        connection = s.split()
        if len(connection) != 3 or connection[0] not in states or connection[2] not in states or connection[1] not in alphabet:
            print("что ты мне поришь?")
            break
        connection_arr.append(connection)
        s = input()

    print(connection_arr)

    new_connection_arr = nka_to_dka(states, alphabet, connection_arr)

    for connection in new_connection_arr:
        print(connection)

    # Создаем массивы свзяей на вывод
    output_connection_arr = []
    flag = False
    for connection in connection_arr:
        if output_connection_arr:
            for output_connection in output_connection_arr:
                if connection[0] == output_connection[0] and connection[2] == output_connection[2]:
                    flag = True
                    output_connection[1] += ',' + connection[1]
        if not flag:
            output_connection_arr.append(connection)
        flag = False

    output_new_connection_arr = []
    flag = False
    for connection in new_connection_arr:
        if output_new_connection_arr:
            for output_connection in output_new_connection_arr:
                if connection[0] == output_connection[0] and connection[2] == output_connection[2]:
                    flag = True
                    output_connection[1] += ',' + connection[1]
        if not flag:
            output_new_connection_arr.append(connection)
        flag = False

    # Создание первого графа
    G1 = nx.DiGraph()
    for connection in output_connection_arr:
        G1.add_edge(connection[0], connection[2], label=connection[1])

    # Визуализация первого графа
    plt.figure(1)  # Создание первого окна
    pos1 = nx.spring_layout(G1)
    nx.draw(G1, pos1, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
    edge_labels1 = nx.get_edge_attributes(G1, 'label')
    nx.draw_networkx_edge_labels(G1, pos1, edge_labels=edge_labels1)
    plt.title("Первый граф")

    # Создание второго графа
    G2 = nx.DiGraph()
    for new_connection in output_new_connection_arr:
        G2.add_edge(new_connection[0], new_connection[2], label=new_connection[1])

    # Визуализация второго графа
    plt.figure(2)  # Создание второго окна
    pos2 = nx.spring_layout(G2)
    nx.draw(G2, pos2, with_labels=True, node_color='lightgreen', node_size=2000, font_size=10, font_weight='bold')
    edge_labels2 = nx.get_edge_attributes(G2, 'label')
    nx.draw_networkx_edge_labels(G2, pos2, edge_labels=edge_labels2)
    plt.title("Второй граф")

    # Показать оба графа
    plt.show()
