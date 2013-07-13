import instagram_filters
from instagram_filters.filters import *

import shutil
import inspect
import os


def applyOne():
	f = Nashville("test.jpg")
	f.apply()
	
def applyAll():
	d = "results"
	if not os.path.exists(d):
		os.makedirs(d)
		
	for name, obj in inspect.getmembers(instagram_filters.filters):
		if inspect.isclass(obj):
			filename = os.path.join(d, name+".jpg")
			shutil.copyfile("test.jpg", filename)
			f = obj(filename)
			f.apply()

if __name__ == "__main__":
	applyAll()