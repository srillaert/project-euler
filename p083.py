# Very much based upon the nice Python solution at https://betaprojects.com/solutions/project-euler/project-euler-problem-083-solution/
from heapq import heappop, heappush

def get_minimal_path_sum(rows):
	n = len(rows)
	dist = [[float('inf')] * n for _ in range(n)]
	dist[0][0] = rows[0][0]
	heap = [(rows[0][0], 0, 0)]
	while heap:
		cost, x, y = heappop(heap)
		for nx, ny in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
			if 0 <= nx < n and 0 <= ny < n:
				ncost = cost + rows[nx][ny]
				if ncost < dist[nx][ny]:
					dist[nx][ny] = ncost
					heappush(heap, (ncost, nx, ny))
	return dist[-1][-1]

def get_minimal_path_sum_from_file(filename):
	with open(filename) as f:
		rows = [list(map(int, line.strip().split(','))) for line in f]
	return get_minimal_path_sum(rows)

if __name__ == "__main__":
	solution = get_minimal_path_sum_from_file('p083.input')
	print(solution)