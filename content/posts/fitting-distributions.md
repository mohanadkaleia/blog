Title: FITTING DISTRIBUTIONS
Date: 2017-01-29 05:34
Author: mohanad
Category: Academic
Tags: analytics, data, distribution, fitting
Slug: fitting-distributions
Status: published

When you got a statistical data and you need to describe your data in a mathematical function, you need then to fit a distribution with your data. In general four steps in fitting distributions:

1.  Choose a function that you think fits the more with your data
2.  Estimate parameters
3.  Evaluate the quality of the fit
4.  Do statistical test

This article, in general, is not aimed to give information how to fit a distribution with a specific language, although you can do that very easily using R, or Python.

Data Exploratory
----------------

Since you need to fit a distribution with your data, then you really need to explore and know your data. Get statistics about your data, for example, mean, standard deviation, skewness, ..etc. Taking iris data as an example, where there are four variables in iris dataset, Sepal width/length, and Petal width/length. Drawing the histogram for your data would also give a good hand to choose the best distribution.

![](http://mycodee.com/wp-content/uploads/2017/01/1-300x242.png){.aligncenter .wp-image-715 width="460" height="371"}

Choosing a Distribution
-----------------------

Now the graphical analysis of your data should give you the good sense to choose a distribution, figure 2 below could help you in choosing it, I found it so useful.

![](http://mycodee.com/wp-content/uploads/2017/01/Distribution-1024x452.png){.aligncenter .size-large .wp-image-716 width="1024" height="452"}

So, for example in iris dataset, we can found that the variable Sepal width, fit with Normal distribution.

**Although,** you can obtain a good distribution that could fit your data the most, but sometimes graphical judgment is not enough or not so trusted. There are other methods that can be used based on analytical expression such as Pearson’s K criterion. Actually, I don’t know much about this method, but I will update this post when I read or use this criterion.

 

**References:**

\[1\] FITTING DISTRIBUTIONS WITH R by Vito Ricci

\[2\] Intelligent Data Analytics online course from Oklahoma University

\[3\] PROBABILISTIC APPROACHES: SCENARIO ANALYSIS, DECISION TREES AND SIMULATIONS
