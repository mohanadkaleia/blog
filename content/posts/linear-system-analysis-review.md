Title: Linear System Analysis - Review
Date: 2017-01-23 05:46
Author: mohanad
Category: Academic
Tags: analysis, approximate solution, Linear
Slug: linear-system-analysis-review
Status: published

![](http://mycodee.com/wp-content/uploads/2017/01/main-qimg-1269ba0ad2c22a1a2501a7158cd7d1b8-c-300x190.jpg){.aligncenter .size-medium .wp-image-710 width="300" height="190"}

Hello everyone,

As a student at Oklahoma University in Electrica and Computer Engineering, I took a course of **Linear Analysis**. The course material was available online from Stanford. Honestly, it was one of the best courses, very helpful and enjoyable. In this post, I'm gonna write about my experience and what I've learned from this course. (Note this post will be updated by adding more details later on).

In this course we took a look at the linear dynamical systems, it starts with a general overview on linear algebra including basis, dimension, null space of a matrix, range of a matrix, rank of a matrix, conservation of dimension, orthogonal and orthonormal set of vectors, QR factorization.

Then the course covered the following headlines:

-   Least squares approximate solution of over-determined equations,
-   Least norm solutions of undetermined equations
-   Singular value decomposition
-   Eigenvalues and Eigenvectors
-   Stability of a system
-   impulse response
-   transfer matrix

I got really useful information of how to identify a system, write a transfer matrix of it, find an approximate solution using least squares, or least norm solution. SVD and PCA give a very nice idea of how to reduce the dimensions of a system and to find the most important features of a system.

I really liked this course and advice Electrical and Computer Engineering students to take a look on this course, it is free and available at Stanford \[2\]

Below I’m gonna write a very brief overview about keywords covered in Linear Analysis class, of course, more detailed information can be found on the course homepage.

[**Basis**]{.underline}: a set of vectors \[v1, v2, .. vn\] called to be a basis for a set V, if those vectors span V and they are independent, in another word the whole set V can be generated from that set of vectors.

[**Null space**]{.underline}: is the space that would give 0 solutions for all input values. Having zero null space means you don’t have a zero mapping between the input and the output, which means your system is deterministic. Mapping from x to Ax is one-to-one different x’s map to different y’s.

[**Range space**]{.underline}: is on the reverse of null space, is the set where we can get a solution by mapping y=Ax

We always try to have a full rank range space and a zero rank null space, that would be the best

[**QR**]{.underline} [**decomposition**]{.underline}: is to factorize transfer matrix A into two matrices Q and R, A = QR, where Q is orthogonal basis of R(A), it yields to orthogonalize the transfer matrix, also to find the pseudo inverse in SVD

[**Least squares error**]{.underline}: is a method to find the approximate solution of overdetermined equations, by defining the residuals r = Ax – y, in order to find x that minimize r, it has a lot of applications, the most popular one is in regression analysis in machine learning

Least norm solutions: provide a solution of underdetermined equations where A is fat, where there are more variables than equations, that leads to have many choices for x that leads to the same y, we try to minimize the norm of x subjected to Ax = y, we aim to have A(x − xln) = 0, xln has the smallest norm of any solution

[**Singular Value Decomposition**]{.underline}: is a decomposition of A into three matrices, where A = UDV\^T, is very useful when trying to reduce the dimension without losing information,

**Eigenvalues/vectors**: Av = lambda\*v, v called to be eigenvectors where the changes of Ax does not affect the direction, but only magnitude which called lambda

 

[**Resource:**]{style="text-decoration: underline;"}

\[1\] Image in the post from https://www.quora.com/topic/Singular-Value-Decomposition

\[2\] Stanford course https://see.stanford.edu/Course/EE263
