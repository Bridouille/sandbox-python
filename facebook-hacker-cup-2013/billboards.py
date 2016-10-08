#!/usr/bin/env python3

import sys, math

# This function test if the words in the words list can fit in a billboard of mWidth and mHeight with a font size of fontSize
def textIsFitting(words, fontSize, mWidth, mHeight):
	currentWidth, currentHeight = 0, fontSize # we start at the beginning of the line, the beginning height is 1 * fontSize for the first line

	# -- Dummy check to see if the sum of the letters > total space
	if fontSize == 0 or len(''.join(words)) > (mHeight // fontSize) * (mWidth // fontSize):
		return False

	for i, word in enumerate(words):
		if currentWidth + len(word) * fontSize <= mWidth: # Prefect, the word is fitting on the line
			currentWidth += (len(word) + 1) * fontSize

			if currentWidth >= mWidth: # The limit on the current line has been reached, we change the line
				currentWidth = 0
				currentHeight += fontSize
				if currentHeight > mHeight and len(words) > i + 1: # if the height is to high and we still have words, it doesn't fit
					return False

		else: # we try to make it fit to the next line
			currentWidth = 0
			currentHeight += fontSize
			if currentHeight > mHeight: # We have a word to fit and we're already too high
				return False

			if currentWidth + len(word) * fontSize <= mWidth: # The word fit on the next line
				currentWidth += (len(word) + 1) * fontSize
			else: # if it doesn't fit on a new line, if won't fit because all lines have the same width
				return False

	return True

# This function try to find the biggest font size that must be 1 <= maxFontSize <= min(maxWidth, maxHeight)
# Using the Bisection method
def resolve(words):
	maxWidth, maxHeight, found, fontSize = int(words[0]), int(words[1]), False, 0

	minValue, maxValue = 0, min(maxWidth, maxHeight) # 1 <= maxFontSize <= min(maxWidth, maxHeight)
	if maxValue == 0:
		return 0
	pivot = minValue + math.ceil((maxValue - minValue) / 2)
	while not found:
		if textIsFitting(words[2:], pivot, maxWidth, maxHeight):
			minValue = pivot
		else:
			maxValue = pivot - 1

		if minValue == maxValue: # if the minValue == the maxValue, we have the good value for the maximum font size
			fontSize = minValue
			found = True
		pivot = minValue + math.ceil((maxValue - minValue) / 2) # we don't have the good value, re-calculate the next midpoint

	return fontSize

if __name__ == '__main__':
	lines = [line.strip() for line in sys.stdin.readlines()]
	for i, line in enumerate(lines[1:]):
		print("Case #{}: {}".format(i + 1, resolve(line.split(' '))))
