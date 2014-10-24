import sfml as sf
import math as m
import time

opt = {
	"xSize" : 300,
	"ySize" : 300,
	"game" : [[0, 0 ,0],
			[0, 0, 0],
			[0, 0, 0]],
	"player" : 1,
	"crossColor" : sf.Color(81, 45, 168),
	"circleColor" : sf.Color(232, 78, 54),
	"bgColor" : sf.Color(115, 143, 254),
	"linesColor" : sf.Color(42, 54, 177)
}

class Morpion():
	def __init__(self, opt):
		self.game = opt["game"]
		self.xSize = opt["xSize"]
		self.ySize = opt["ySize"]
		self.xPad = self.xSize // 3
		self.yPad = self.ySize // 3
		self.player = opt["player"]
		self.crossColor = opt["crossColor"]
		self.circleColor = opt["circleColor"]
		self.bgColor = opt["bgColor"]
		self.linesColor = opt["linesColor"]
		self.player = opt["player"]

		self.w = sf.RenderWindow(sf.VideoMode(self.xSize, self.ySize), "SFML")
		self.image = sf.Image.create(self.xSize, self.ySize, sf.Color(50, 50, 50))
		self.texture = sf.Texture.from_image(self.image)
		self.sprite = sf.Sprite(self.texture)
		self.refresh()
		self.mainLoop()

	def drawCross(self, i, j):
		size = self.xPad
		for x in range(size // 6, size - size // 6):
			for y in range(size // 6, size - size // 6):
				for r in range(3):
					if x == y - r or x == size - y + r:
						self.image[i + x, j + y] = self.crossColor

	def drawCercle(self, i, j):
		size = self.xPad // 2
		size_r = size // 1.5
		for x in range(-size, size):
			for y in range(-size, size):
				if x**2 + y**2 < size_r**2 and x**2 + y**2 > size_r**2 - size_r * 5:
					self.image[i + x + size, j + y + size] = self.circleColor

	def drawGame(self):
		game = self.game
		xPad = self.xPad
		yPad = self.yPad
		for i in range(self.xSize):
			for j in range(self.ySize):
				self.image[i, j] = self.bgColor
				if i in [xPad, xPad * 2] or j in [yPad, yPad * 2]:
					self.image[i, j] = self.linesColor

		for i in range(len(game)):
			for j in range(len(game[i])):
				if game[i][j] == 1:
					self.drawCercle(i * xPad, j * yPad)
				elif game[i][j] == 2:
					self.drawCross(i * xPad, j * yPad)

	def endGame(self):
		game = self.game
		for i in range(3): # check lines
			if game[0][i] == game[1][i] and game[1][i] == game[2][i] and game[0][i] != 0:
				return True
		for i in range(3): # check columns
			search = game[0][i];
			if [game[i][0], game[i][1], game[i][2]] == [search, search, search] and search != 0:
				return True
		if game[0][0] == game[1][1] == game[2][2] != 0 or game[2][0] == game[1][1] == game[0][2] != 0: # check diago
			return True
		return False

	def pat(self):
		game = self.game
		for line in game:
			for square in line:
				if square == 0:
					return False
		return True

	def refresh(self):
		self.drawGame()
		self.texture = sf.Texture.from_image(self.image)
		self.sprite = sf.Sprite(self.texture)

	def mainLoop(self):
		while self.w.is_open:
			for event in self.w.events:
				if type(event) is sf.CloseEvent:
					self.w.close()
				if event == sf.MouseButtonEvent and event.released:
					x, y = m.floor(event.position[0] / self.xPad), m.floor(event.position[1] / self.yPad)
					if self.game[x][y]:
						continue
					self.game[x][y] = 1 if self.player % 2 else 2
					self.refresh()
					self.player = not self.player

			self.w.clear()
			self.w.draw(self.sprite)
			self.w.display()

			if self.endGame():
				print("Player {} Win !".format(self.player + 1))
				time.sleep(3)
				self.w.close()
			if self.pat():
				print("Partie egale")
				time.sleep(3)
				self.w.close()

if __name__ == "__main__":
	m = Morpion(opt)