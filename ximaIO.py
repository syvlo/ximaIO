import numpy as np
import os.path
import struct

def imaread(imgName):
	"""Reads a *ima file. ImgName can be with or without extension"""
	if imgName.endswith('.ima'):
		imgName = os.path.splitext(imgName)[0]

	return _imaread(imgName)

def _imaread(imgName):
	"""Reads a *.ima file. ImgName should come with no extension"""
	with open(imgName + '.dim') as f:
		tmp = f.readline().split()
		w = int(tmp[0])
		h = int(tmp[1])

	img = np.empty([h, w])
	with open(imgName + '.ima') as f:
		for i in range(0, h):
			for j in range(0, w):
				img[i, j] = struct.unpack('B', f.read(1))[0]

	return img