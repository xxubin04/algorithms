from itertools import product
from collections import deque 

def solution(n, infection, edges, k):
    graph = {}
    for s, e, p in edges:
        for a, b in [(s, e), (e, s)]:
            graph.setdefault(a, {})[b] = p
    
    def spread(infected, pipe_type):
        q = deque(infected)
        new_infected = set(infected)
        while q:
            node = q.popleft()
            for end, p in graph.get(node, {}).items():
                if p == pipe_type and end not in new_infected:
                    new_infected.add(end)
                    q.append(end)
        return new_infected
    
    max_infect = 0
    for actions in product([1, 2, 3], repeat=k):
        infected = {infection}
        for pipe_type in actions:
            infected = spread(infected, pipe_type)
        max_infect = max(max_infect, len(infected))
    
    return max_infect