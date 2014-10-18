#!/usr/bin/python3.3

import sys, os, re

class bsq:
   def  __init__(self, filename):
      try:
         self.file = open(filename, "r")
      except IOError as e:
         printErr("{}: {}: {}".format(sys.argv[0], filename, os.strerror(e.errno)))

   def __del__(self):
      try:
         self.file.close()
      except:
         pass

   def readFile(self):
      self.lines = [line.strip() for line in self.file.readlines()]
      self.verifFormat()

   def verifFormat(self):
      if len(self.lines) < 2:
         printErr("File is not well formated : missing number of lines")
         sys.exit(1)
      try:
         self.size = int(self.lines[0])
      except:
         printErr("File is not well formated : missing number of lines")
         sys.exit(1)
      del self.lines[0]
      self.sizeLine = len(self.lines[0])
      for line in self.lines:
         if len(line) != self.sizeLine:
            printErr("File is not well formated : lines length does not match size")
            sys.exit(1)
         if re.match("^(\.|o)*$", line) is None:
            printErr("File is not well formated : lines contains other caracters then \".\" and \"o\": \"{}\"".format(line))
            sys.exit(1)

   def placeSquare(self, size, x, y):
      toFind = "." * size
      if len(self.lines[0]) <= x + size or len(self.lines) <= y + size:
         return False
      for i in range(0, size):
         for j in range(0, size):
            if self.lines[y + i][x + j] != ".":
               return False
         i += 1
      return True

   def printSquare(self):
      self.squareSize = 0
      self.x = 0
      self.y = 0

      for y in range(0, len(self.lines) - 1):
         for x in range(0, len(self.lines[y])):
            while self.placeSquare(self.squareSize + 1, x, y) == True:
               self.squareSize += 1
               self.y = y;
               self.x = x;
            x += 1
         y += 1
      self.printResult()


   def printResult(self):
      y = 0
      print(str(self.size))
      for line in self.lines:
         if y >= self.y and y < self.y + self.squareSize:
            line = line[:self.x] + "x" * self.squareSize + line[self.x + self.squareSize:]
         print(line)
         y += 1

def printErr(errMsg):
   print(errMsg, file = sys.stderr)

if __name__ == "__main__":
   if len(sys.argv) < 2:
      printErr("Usage : {} filename".format(sys.argv[0]))
   else:
      bsq = bsq(sys.argv[1])
      bsq.readFile()
      bsq.printSquare()
