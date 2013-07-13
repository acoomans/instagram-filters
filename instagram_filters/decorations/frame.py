from instagram_filters.filter import Filter

import os, inspect

class Frame(Filter):
				
	def frame(self, frame):
		path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
		self.execute("convert {filename} \( '{frame}' -resize {width}x{width}! -unsharp 1.5x1.0+1.5+0.02 \) -flatten {filename}",
			frame = os.path.join(path, "frames", frame)
		)