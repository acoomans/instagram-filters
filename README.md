Instagram-filters
=================

Instagram-like image filters.

Can be used in conjunction with the [instagram-client](https://bitbucket.org/acoomans/instagram-client) to upload the image after applying a filter.

## Install

	python setup.py install


## Usage

First, import the client:

	from instagram_filters.filters import *

Instanciate a filter and apply it:

	f = Nashville("image.jpg")
	f.apply()

Available filters: 

- Gotham
- Kelvin
- Lomo
- Nashville
- Toaster

**Note** The filters change the image in-place. Be sure to copy it before applying any filter if you want to copy the original image.


# Tests

Run the tests with:

	cd tests
	python test.py
	
## Credits

This library is inspired from the ["Create instagram filters with php" tutsplus tutorial](http://net.tutsplus.com/tutorials/php/create-instagram-filters-with-php/).