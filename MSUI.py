import tkinter as tk
from collections import deque

def bfs_maze_solver(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None}
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        current = queue.popleft()
        
        if current == end:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]
        
        for direction in directions:
            row, col = current[0] + direction[0], current[1] + direction[1]
            if 0 <= row < rows and 0 <= col < cols and maze[row][col] == 0:
                neighbor = (row, col)
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    parent[neighbor] = current
    
    return []

class MazeSolverApp:
    def __init__(self, root, maze):
        self.root = root
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.cell_size = 40
        self.start = None
        self.end = None
        
        self.canvas = tk.Canvas(root, width=self.cols*self.cell_size, height=self.rows*self.cell_size)
        self.canvas.pack()
        
        self.draw_maze()
        self.canvas.bind("<Button-1>", self.set_start)
        self.canvas.bind("<Button-3>", self.set_end)
        
        self.solve_button = tk.Button(root, text="Solve Maze", command=self.solve_maze)
        self.solve_button.pack()
        
    def draw_maze(self):
        for row in range(self.rows):
            for col in range(self.cols):
                x1, y1 = col * self.cell_size, row * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                color = "white" if self.maze[row][col] == 0 else "black"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")
    
    def set_start(self, event):
        col, row = event.x // self.cell_size, event.y // self.cell_size
        if self.maze[row][col] == 0:
            if self.start:
                self.canvas.create_rectangle(
                    self.start[1] * self.cell_size,
                    self.start[0] * self.cell_size,
                    (self.start[1] + 1) * self.cell_size,
                    (self.start[0] + 1) * self.cell_size,
                    fill="white", outline="gray"
                )
            self.start = (row, col)
            self.canvas.create_rectangle(
                col * self.cell_size,
                row * self.cell_size,
                (col + 1) * self.cell_size,
                (row + 1) * self.cell_size,
                fill="green", outline="gray"
            )
    
    def set_end(self, event):
        col, row = event.x // self.cell_size, event.y // self.cell_size
        if self.maze[row][col] == 0:
            if self.end:
                self.canvas.create_rectangle(
                    self.end[1] * self.cell_size,
                    self.end[0] * self.cell_size,
                    (self.end[1] + 1) * self.cell_size,
                    (self.end[0] + 1) * self.cell_size,
                    fill="white", outline="gray"
                )
            self.end = (row, col)
            self.canvas.create_rectangle(
                col * self.cell_size,
                row * self.cell_size,
                (col + 1) * self.cell_size,
                (row + 1) * self.cell_size,
                fill="red", outline="gray"
            )
    
    def solve_maze(self):
        if not self.start or not self.end:
            print("Please set both start and end points.")
            return
        
        path = bfs_maze_solver(self.maze, self.start, self.end)
        if path:
            for (row, col) in path:
                self.canvas.create_rectangle(
                    col * self.cell_size,
                    row * self.cell_size,
                    (col + 1) * self.cell_size,
                    (row + 1) * self.cell_size,
                    fill="blue", outline="gray"
                )
        else:
            print("No path found.")

if __name__ == "__main__":
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    root = tk.Tk()
    app = MazeSolverApp(root, maze)
    root.mainloop()

