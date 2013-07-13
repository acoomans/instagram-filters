import math
from instagram_filters.filter import Filter

class Vignette(Filter):
	def vignette(self, color_1 = 'none', color_2 = 'black', crop_factor = 1.5):
		crop_x = math.floor(self.image().size[0] * crop_factor)
		crop_y = math.floor(self.image().size[1] * crop_factor)
		 
		self.execute("convert \( {filename} \) \( -size {crop_x}x{crop_y} radial-gradient:{color_1}-{color_2} -gravity center -crop {width}x{height}+0+0 +repage \) -compose multiply -flatten {filename}",
			crop_x = crop_x,
			crop_y = crop_y,
			color_1 = color_1,
			color_2 = color_2,
		)
