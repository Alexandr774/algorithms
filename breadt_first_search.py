from collections import deque

graph = {}

graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = ['jhon', "mia", "robert"]


def search_bredit_first():
    search_queue = deque()
    search_queue += graph["you"]
    while search_queue:
        person = search_queue.popleft()
        # print(graph)
        if person_is_seller(person):
            print(person + " yes")
            return True
        else:
            if person in graph.keys():
                search_queue += graph[person]
    return False


def person_is_seller(name):
    return name[-1] == 'm'


search_bredit_first()
