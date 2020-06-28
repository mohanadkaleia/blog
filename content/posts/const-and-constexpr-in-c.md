Title: Const and constexpr in C++
Date: 2016-07-19 04:55
Author: mohanad
Category: Code
Tags: C++
Slug: const-and-constexpr-in-c
Status: published

In C++, there is two type of constant, a constant expression which can be determine at compilation time, and normal const which takes its value during running time, 

> const int i = 20; [// This is const expression ,]{style="color:#008000;"}
>
> const int j = i;[ // This is const expression, ]{style="color:#008000;"}
>
> const int k = getSize(); [// This constant can't be constant expression because the value of getSize can't be detected else of running time]{style="color:#008000;"}

 

Note: in C++11 we can define a function to be const expression, but this function should be simple enough so the compiler can get its output during compilation

 

...

Mohanad Kaleia, 

C++ Primer
