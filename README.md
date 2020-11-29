# Blog

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

With no strong reason, I decided to move my own blog from being on WordPress to be a simple Python managed blog, where all posts are written in Markdown format. During this transition, I tried to use Pelican as a static website generator. I found it really interesting, but at the same time a bit limited. So decided to build a very simple blog using Python. I open-sourced this work, so anyone can fork it and build his own blog as well. 

## Architecture
The blog will be built using the following stack: Flask - Python - Markdown (no database will be used). With server-rendered HTML pages. 

The point here is to make the blog as simple as possible, taking into consideration that not too many people would bother reading it :D

## Development 
If you want to run this blog locally, you can do that by the following:

1. Install the dependecies, I always prefer to use virtual env to isolate dependecies
```
pip3 install -r requiremenets.txt
```

2. Run the app
```
python3 run.py
```

## Note
This work is still in progress, it is not intended to be forked and copied by others. But if you decided to fork it please don't copy the content directory which contains my posts. I will figure out a way for that later but for now just don't :D 

## License 
Please note that the content here is copyrighted, so pleaes don't copy it :) 
