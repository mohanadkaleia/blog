Title: format your code on git pre-commit hooks
Date: 2021-10-17
Author: mohanad
Category: Howto
Tags: python, git, lint
Slug: format-your-code-on-git-pre-commit-hooks
Status: published
Cover: https://media.giphy.com/media/LQ3yYk351QJgm4rQwg/giphy.gif

Code formatting and linting is one of the essential part in writing a clean code. Instead of wasting lots of time doing it manually or to waste other people’s time reviewing ugly code. You MUST use some automation tools that does the job for you! (yay for automation) 

![This gif is taken from Slam Dunk when Hanamichi Sakuragi got his new fancy shoes kinda not related to this article but I don’t care 😛](https://media.giphy.com/media/LQ3yYk351QJgm4rQwg/giphy.gif)

This article will be targeting Python coding flow, same ideas may be applied of course to other languages like Go or Javascript, but we gonna use tools written for Python.

Before we start, lets review few terminologies that would be helpful to fully grasp before integrating tools into your code flow. 


> Lint, or a linter, is a static code analysis tool used to flag programming errors, bugs, stylistic errors and suspicious constructs (wikipedia)


> Git hooks: Git has a way to fire off custom scripts when certain important actions occur. (source)

What we are going to do is before we commit any changed piece of code, we run the linter to check the new changes, make sure the code does not have any errors or stylistic problems, make changes when possible. 


There are many linting tools written for Python, I can say one of the most famous ones are Flake8, PyLint and Black


## Black

 I used Black in many of my project and I love it, so you better use too 😛. It even has a playground demo if you want to see it in action before actually using it. 
 
 To install it run: (or if you want just follow the read me page of the project)
 
```python
pip install black
```

You got it installed? try it out quickly! 

```python
black <path to a python file or directory>
```
Cool, you got it up and running, now instead of you running this command every time you make a change, let Git handle this for you by using git pre-commit hook. 


## Pre-commit 

If you have your project initialized with Git, you can navigate to the .git directory and see your pre-commit hooks `.git/hooks`

Hmmm this seems a bit complicated hah.. in order to add Black to be called before committing any change you will need to modify `pre-commit` file. 

We are not doing that, that is why I’m writing this blog post. We will use a simple tool written for Python called pre-commit (yeah I use this tool too so you better using it as well 😎) 

With pre-commit tool, you can easily manage the hooks you want to run by defining them in a yaml file. (easy peasy) 

Install it simply like this (man I still remember how painful it was installing Linux libraries and packages and compile them from their source — glad with Python we can just use its package manager to install everything phew):

```python
pip install pre-commit
```

Add `pre-commit` configurations should be added to your project, here is a sample (no this is not a sample this is my actual pre commit configurations to run Black before committing a change. 

```yaml
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files
    -   id: check-ast
    -   id: check-byte-order-marker
    -   id: check-case-conflict
-   repo: https://github.com/psf/black
    rev: 19.3b0
    hooks:
    -   id: black
-   repo: https://gitlab.com/pycqa/flake8
    rev: 3.9.2
    hooks:
    -   id: flake8
        additional_dependencies: [flake8-typing-imports==1.10.0]
```

Woohoo! that looks so beautiful!! (and yeah of course it is beautiful because it is my code silly).. anyway lets add some explanations on the above configs:

First, there are soooo many hooks that we can use (you can pick and choose what ever you like) for example, you can prevent committing large files into your Git tree. 

In my configurations version, you can see all the hooks I’m using, (Just copy and paste it — I decided not to explain it 😝)

Oh forgot to say, save the configurations in a file and name it `.pre-commit-config.yaml` 

## Put them all together

Now remember the ugly file that we saw in the directory `.git/hooks/pre-commit` yeah.. it was so ugly that we could not even look at it (actually did you bother opening it? or you just lazy? you seem like so lazy!!) 

Anyway, we need to let the `pre-commit` tool to read the yaml config file that you created earlier and write it into `.git/hooks/pre-commit` file. 

You can do that simply using:

```perl
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```
All done! thank me! 


![Another pic from Slam Dunk, that really does not add any value to this article but could not fine better lol](https://media.giphy.com/media/dzHzdMctT3jNu/giphy.gif)


P.S
Note, the `.pre-commit-config.yaml` file should be committed so if other people are also contributing to your project they can also run `pre-commit install` to add the hooks to their `.git` hooks.

I would also add `Black and pre-commit` to the virtual environment so other developers can install those dependencies as well. 

