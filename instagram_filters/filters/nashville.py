from instagram_filters.filter import Filter
from instagram_filters.decorations import Frame

import inspect, os


class Nashville(Filter, Frame):
	
	def apply(self):
		self.colortone('#222b6d', 50, 0);
		self.colortone('#f7daae', 120, 1);
		self.execute("convert {filename} -contrast -modulate 100,150,100 -auto-gamma {filename}");
		self.frame("Nashville.jpg");
		