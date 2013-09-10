from setuptools import setup

config = {
	'name': 'instagram-filters',
	'version': '0.1',
	'description': 'Instagram-like image filters',
	'license': 'LICENSE.txt',
	'url': 'https://github.com/acoomans/instagram-filters',
	'author': 'Arnaud Coomans',
	'author_email': 'arnaud.coomans@gmail.com',
	'install_requires': ['PIL'],
	'packages': ['instagram_filters', 'instagram_filters.filters', 'instagram_filters.decorations'],
	'data_files' : [
		('instagram_filters/decorations/frames', ['instagram_filters/decorations/frames/Kelvin.jpg', 'instagram_filters/decorations/frames/Nashville.jpg'])
	],
	'zip_safe': False
}

setup(**config)