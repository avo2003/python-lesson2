class Snake:
	def __init__(self, name):
		self.name = name

	def modify_name(self, name):
		self.name = name

snake = Snake('python')
print(snake.name)
snake.modify_name('Shoghakat')
print(snake.name)
