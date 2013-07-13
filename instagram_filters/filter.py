# inspired from http://net.tutsplus.com/tutorials/php/create-instagram-filters-with-php/

import subprocess
import Image
import math

class Filter:
	
	def __init__(self, filename):
		self.filename = filename
		self.im = False
		
	def image(self):
		if not self.im:
			self.im = Image.open(self.filename)
		return self.im
	
	def execute(self, command, **kwargs):
		default = dict(
			filename=self.filename,
			width = self.image().size[0],
			height = self.image().size[1]
		)
		format = dict(default.items() + kwargs.items())
		command = command.format(**format)
		error = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
		return error
		
	def colortone(self, color, level, type = 0):
		
		arg0 = level
		arg1 = 100 - level
		if type == 0:
			negate = '-negate'
		else:
			negate = ''

		self.execute("convert {filename} \( -clone 0 -fill '{color}' -colorize 100% \) \( -clone 0 -colorspace gray {negate} \) -compose blend -define compose:args={arg0},{arg1} -composite {filename}",
			color = color,
			negate = negate,
			arg0 = arg0,
			arg1 = arg1
		)
