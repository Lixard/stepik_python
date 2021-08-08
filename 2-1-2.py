inh_conf = {}


def deep_search(graph: dict, node: str, queue: set) -> bool:
    visited, stack = set(), [*graph[node]]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            if vertex in queue:
                return True
            visited.add(vertex)
            stack.extend(set(graph[vertex]) - visited)
    return False


ex_init_count = int(input())
for _ in range(ex_init_count):
    ex_input = input().split()
    inh_conf[ex_input[0]] = inh_conf.get(ex_input[0], []) + ex_input[2:]

req_count = int(input())
ex_queue = []
result = []
for _ in range(req_count):
    ex_queue.append(input())

while ex_queue:
    value = ex_queue.pop()
    if deep_search(inh_conf, value, set(ex_queue)):
        result.append(value)

result.reverse()
print(*result, sep='\n')
