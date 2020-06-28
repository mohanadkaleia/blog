# Blog

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

Theb blog uses [**Pelican**](https://github.com/getpelican/pelican), a static generator library, to generate the blog's static pages.

## Content type:

1. Posts: for articles that are listed in the blog section
2. Activity: articles under `Activity` directory are listed under `Recent update` Section
3. tbd

## Create new article

Pelican is a static generator library that generates static pages. It takes `markdown` as an input and generates `html` as an output. 

Based on the content type, create a `.md` file under `content/[posts|activities]`, then run pelican to generate the output:

`pelican -lr -s pelicanconf.py -o output -t theme content`

This will keep listning to any change in the conent directory and generates output.

A Python http server can be used to serve the generated pages, first change the directory to the `output` directory. Then run the following command: 

`python -m http.server  ` 

Oh.. forgot that you will need to install requirements: 

`pip install requirements.txt` 



## Deployment

Deployment into aws S3


## License 
Please note that the content here is copyrighted, so pleaes don't copy it :) 
