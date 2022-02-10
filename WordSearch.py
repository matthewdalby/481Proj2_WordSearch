from collections import deque
# Below lists detail all eight possible movements from a cell
row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]
result=[]

# Function to check if it is possible to go to position next
# from the current position. The function returns false if next is
# not in a valid position, or it is already visited
def isValid(mat, x, y, path):
	return (0 <= x < len(mat)) and (0 <= y < len(mat[0])) and (x, y) not in path


def DFS(mat, word, i, j, path=[], index=0):


	if index == len(word):
		if [(word[i], path[i]) for i in range(0, len(word))] not in result:
			result.append([(word[i], path[i]) for i in range(0, len(word))])
		return
	if (isValid(mat,i,j,path) and mat[i][j]==word[index]):
		path.append((i,j))
		for k in range(len(row)):
			DFS(mat,word,i+row[k],j+col[k],path,index+1)
		path.remove((i,j))
	else:
		return
			
	


def WordSearch(mat, word):
	# base case
	if not mat or not len(mat) or not len(word):
		return

	for i in range(len(mat)):
		for j in range(len(mat[0])):
			DFS(mat, word, i, j)


if __name__ == '__main__':

	mat = [
		['A', 'D', 'E', 'B', 'C'],
		['O', 'O', 'C', 'A', 'X'],
		['S', 'C', 'D', 'K', 'C'],
		['O', 'D', 'E', 'H', 'L']
	]
	word = 'CODE'

	WordSearch(mat, word)

	for row in result:
		print(row)

