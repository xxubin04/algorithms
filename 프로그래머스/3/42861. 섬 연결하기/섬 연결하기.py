def solution(n, costs):
    parent = [i for i in range(n)]

    # x가 속한 집합의 대표 노드 찾기
    # 연결되어 있는지 확인
    def find(x):
        # 대표자가 아니라면 부모의 부모를 계속 찾아가서
        # 최종 대표자를 찾는 것
        if parent[x] != x: 
            parent[x] = find(parent[x])
        return parent[x]

    # a와 b가 속한 집합 합치기
    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        
        # 둘 중 작은 대표자를 최종 대표자로 만듦
        if root_a < root_b:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b

    # 비용이 작은 간선부터 확인
    costs.sort(key=lambda x: x[2])

    answer = 0  # 선택한 다리 비용의 총합
    edge_count = 0  # 선택한 다리 개수 

    for a, b, cost in costs:
        # 아직 서로 연결되지 않은 섬이라면(부모가 다르다면)
        # 연결해도 사이클 안 생김 
        if find(a) != find(b):
            union(a, b)
            answer += cost
            edge_count += 1

            # n개의 섬을 연결하려면 n-1개의 간선이면 충분
            if edge_count == n - 1:
                break

    return answer