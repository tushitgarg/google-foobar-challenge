# DON'T GET VOLUNTEERED

def solution(src,dest):
	def convert_postition(pos):
		x=-1
		y=-1
		while(pos>=0):
			x+=1
			y=-1
			while(y<7 and pos>=0):
				y+=1
				pos-=1
		return (x,y)
	src_x,src_y = convert_postition(src)
	dest_x,dest_y = convert_postition(dest)
	visited = [[0 for i in range(8)] for j in range(8)]
	x_moves = [2, 2, -2, -2, 1, 1, -1, -1] 
	y_moves = [1, -1, 1, -1, 2, -2, 2, -2]
	queue = []
	lst = []
	queue.append([src_x,src_y,0])
	visited[src_x][src_y] = 1
	while(len(queue)!=0):
		q = queue[0]
		queue.pop(0)
		if(q[0] == dest_x and q[1]==dest_y):
			return q[2]
		for i in range(8):
			x = q[0] + x_moves[i]
			y = q[1] + y_moves[i]
			if(x>=0 and x<8 and y>=0 and y<8 and visited[x][y]!=1):
				visited[x][y]=1
				queue.append([x,y,q[2]+1])
	return -1
print(solution(0,1))
print(solution(19,36))
