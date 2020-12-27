Title: Windows 7 no longer boots
Date: 2014-03-13 22:20
Author: mohanad
Category: maintenance
Tags: bootloader, bootrec, No SLIC, repair
Slug: windows-no-longer-boots
Status: published

[![IMG-20140309-WA0002](../../static/images/windows-no-longer-boots/IMG-20140309-WA0002-300x225.jpg){.aligncenter .size-medium .wp-image-365 width="300" height="225"}](../../static/images/windows-no-longer-boots/IMG-20140309-WA0002.jpg)

[من فترة واجهتني مشكلة أن الويندوز 7 لم يعد يستطيع الإقلاع ولم يعد يستطيع الدخول إلى الويندوز، وتظهر الخيارات التالية:]{style="line-height: 1.6em;"}

> [Booting Windows 7/Vista/Server (No SLIC - Pointer)]{style="color: rgb(0, 0, 0); font-family: verdana, geneva, lucida, 'lucida grande', arial, helvetica, sans-serif; font-size: 13px; line-height: normal; background-color: rgb(245, 245, 255);"}
>
> [Booting Windows 7/Vista/Server (No SLIC)]{style="color: rgb(0, 0, 0); font-family: verdana, geneva, lucida, 'lucida grande', arial, helvetica, sans-serif; font-size: 13px; line-height: normal; background-color: rgb(245, 245, 255);"}
>
> [Booting Windows NT/2000/XP]{style="color: rgb(0, 0, 0); font-family: verdana, geneva, lucida, 'lucida grande', arial, helvetica, sans-serif; font-size: 13px; line-height: normal; background-color: rgb(245, 245, 255);"}
>
> [Booing Enter Command Line ]{style="color: rgb(0, 0, 0); font-family: verdana, geneva, lucida, 'lucida grande', arial, helvetica, sans-serif; font-size: 13px; line-height: normal; background-color: rgb(245, 245, 255);"}

[سبب المشكلة]{style="color:#800080;"} 
-------------------------------------

بشكل عام تظهر هذه المشكلة بسبب نسخ الويندوز الغير شرعية، فعندما تتم عملية activate أو تحديث يمكن أن تظهر هذه المشكلة ولا يعود الجهاز قادر على الدخول لبيئة ويندوز، حيث يعطب محمل الإقلاع boot loader، ولحل هذه المشكلة يجب علينا إصلاح محمل الإقلاع boot loader باستخدام قرص ويندوز في نمط الإصلاح repair.

 

[حل المشكلة]{style="color:#800080;"} 
------------------------------------

1.  قم بوضع قرص windows 7 في السواقة.
2.  قم بالإقلاع من قرص الويندوز.
3.  بعد أن تقلع من القرص قم باختيار اللغة والوقت وقم بالضغط على زر next
4.  إضغط على زر repair your computer
5.  (الآن سيقوم بعملية تحديد أنظمة التشغيل الموجودة لديك) قم باختيار نظام التشغيل.
6.  الآن من خيارات الإصلاح قم باختيار آخر خيار [Command Prompt]{style="color: rgb(0, 0, 0); font-family: verdana, geneva, lucida, 'lucida grande', arial, helvetica, sans-serif; font-size: 13px; line-height: normal; background-color: rgb(245, 245, 255);"}
7.  قم الآن بكتابة التعليمات التالية (بعد كل تعليمة قم بضغط زر enter):

> [Bootrec.exe /FixMbr]{style="color: rgb(0, 0, 0); font-family: verdana, geneva, lucida, 'lucida grande', arial, helvetica, sans-serif; font-size: 13px; line-height: normal; background-color: rgb(245, 245, 255);"}
>
> [Bootrec.exe /FixBoot]{style="color: rgb(0, 0, 0); font-family: verdana, geneva, lucida, 'lucida grande', arial, helvetica, sans-serif; font-size: 13px; line-height: normal; background-color: rgb(245, 245, 255);"}
>
> [Bootrec.exe /RebuildBcd]{style="color: rgb(0, 0, 0); font-family: verdana, geneva, lucida, 'lucida grande', arial, helvetica, sans-serif; font-size: 13px; line-height: normal; background-color: rgb(245, 245, 255);"}

بعد الانتهاء من تنفيذ هذه التعليمات بنجاح قم بإغلاق موجه الأوامر command prompt وبعدها قم بعمل إعادة تشغيل للجهاز.

مبروووووووك الآن تم إصلاح محمل الأقلاع boot loader وتستطيع أن تدخل للويندوز من جديد :)
