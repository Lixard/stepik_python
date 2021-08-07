namespaces: dict = {
    'global': {'parent': None, 'vars': []}
}


def main():
    req_count = int(input())
    for i in range(req_count):
        cmd, namespace, arg = input().split()

        if cmd == "create":
            create(namespace, arg)
        if cmd == "add":
            add(namespace, arg)
        if cmd == "get":
            get(namespace, arg)


def create(namespace: str, parent: str):
    global namespaces
    namespaces.update({namespace: {'parent': parent, 'vars': []}})


def add(namespace: str, arg: str):
    global namespaces

    array: [] = namespaces.get(namespace).get('vars')
    array.append(arg)


def get(namespace: str, arg: str):
    curr_namespace = namespace
    while True:
        namespace_dict = namespaces.get(curr_namespace)
        namespace_args = namespace_dict.get('vars')
        if arg in namespace_args:
            print(curr_namespace)
            break
        curr_namespace = namespace_dict.get('parent')
        if curr_namespace is None:
            print("None")
            break


main()
