classes = {}


def main():
    cls_count = int(input())
    read_cls_configs(cls_count)

    req_count = int(input())
    comp_req(req_count)


def read_cls_configs(cls_count: int) -> None:
    global classes
    for i in range(cls_count):
        conf = input().split(" : ")
        parent_cls, sub_cls = conf[0], conf[1].split() if len(conf) == 2 else []

        if parent_cls in classes:
            classes.get(parent_cls).extend(sub_cls)
        else:
            classes[parent_cls] = [*sub_cls]


def comp_req(req_count: int) -> None:
    for i in range(req_count):
        is_parent(*input().split())


def deep_first_search(graph: dict, start: str, search: str) -> bool:
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            if search == vertex:
                return True
            visited.add(vertex)
            stack.extend(set(graph[vertex]) - visited)
    return False


def is_parent(sub_cls: str, parent_cls: str) -> None:
    print("Yes") if deep_first_search(classes, parent_cls, sub_cls) else print("No")


main()
