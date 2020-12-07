Title: تنصيب بيئة MPI على نظام أبونتو
Date: 2013-10-15 11:58
Author: mohanad
Category: GNULinux, howto
Tags: install, mpi, parallel programming, ubuntu
Slug: how-to-install-mpi-on-ubuntu
Status: published

[بعد أن بدأت بإعطاء سلسلة دروس برمجة تفرعية باستخدام مكتبة ]{style="line-height: 1.6em;"}**MPI**[ أحببت أن أضع بعض الدروس على مدونتي.]{style="line-height: 1.6em;"}

طبعاً طالما أنني أعمل على بيئة لينوكس فأحب أن أضع شرحاً لكيفية تنصيب وبدء العمل على بيئة **MPI** باستخدام نظام أبونتو.

لتنصيب مكتبة MPI فقط نكتب في التيرمينال التعليمة التالية:

> sudo apt-get install libcr-dev mpich2 mpich2-doc

بعد الانتهاء من تنصيب المكتبة لنقم الآن بكتابة برنامج صغير يطبع عبارة hello world على كل عقدة من عقد الحوسبة.

> \#include \<stdio.h\>  
>   
> \#include \<mpi.h\>
>
> void main()  
>   
> {  
>   
>     MPI\_Init(NULL , NULL);  
>   
>       
>   
>     printf("Hello world!\\n");  
>   
>       
>   
>     MPI\_Finalize();  
>   
> }

والآن لترجمة وتنفيذ البرنامج يمكننا ذلك كما يلي:

> mohanad\@mohanad-laptop:\~/Desktop/mpi\$ mpicc hello\_world.c -o hello\_world  
>   
> mohanad\@mohanad-laptop:\~/Desktop/mpi\$ mpirun -np 2 ./hello\_world  
>   
> Hello world!  
>   
> Hello world!  
>   
> mohanad\@mohanad-laptop:\~/Desktop/mpi\$

 

تهانينا الآن يمكنك كتابة ما تشاء من البرامج التفرعية :) 
