Title: Windows 7 no longer boots
Date: 2014-03-13 22:20
Author: mohanad
Category: maintenance
Tags: bootloader, bootrec, No SLIC, repair
Slug: windows-no-longer-boots
Status: published

[![IMG-20140309-WA0002](../../static/images/windows-no-longer-boots/IMG-20140309-WA0002-300x225.jpg)](../../static/images/windows-no-longer-boots/IMG-20140309-WA0002.jpg)

من فترة واجهتني مشكلة أن الويندوز 7 لم يعد يستطيع الإقلاع ولم يعد يستطيع الدخول إلى الويندوز، وتظهر الخيارات التالية:

> Booting Windows 7/Vista/Server (No SLIC - Pointer)
>
> Booting Windows 7/Vista/Server (No SLIC)
>
> Booting Windows NT/2000/XP
>
> Booing Enter Command Line 

سبب المشكلة
-------------------------------------

بشكل عام تظهر هذه المشكلة بسبب نسخ الويندوز الغير شرعية، فعندما تتم عملية activate أو تحديث يمكن أن تظهر هذه المشكلة ولا يعود الجهاز قادر على الدخول لبيئة ويندوز، حيث يعطب محمل الإقلاع boot loader، ولحل هذه المشكلة يجب علينا إصلاح محمل الإقلاع boot loader باستخدام قرص ويندوز في نمط الإصلاح repair.

 

حل المشكلة
------------------------------------

1.  قم بوضع قرص windows 7 في السواقة.
2.  قم بالإقلاع من قرص الويندوز.
3.  بعد أن تقلع من القرص قم باختيار اللغة والوقت وقم بالضغط على زر next
4.  إضغط على زر repair your computer
5.  (الآن سيقوم بعملية تحديد أنظمة التشغيل الموجودة لديك) قم باختيار نظام التشغيل.
6.  الآن من خيارات الإصلاح قم باختيار آخر خيار Command Prompt
7.  قم الآن بكتابة التعليمات التالية (بعد كل تعليمة قم بضغط زر enter):

> Bootrec.exe /FixMbr
>
> Bootrec.exe /FixBoot
>
> Bootrec.exe /RebuildBcd

بعد الانتهاء من تنفيذ هذه التعليمات بنجاح قم بإغلاق موجه الأوامر command prompt وبعدها قم بعمل إعادة تشغيل للجهاز.

مبروووووووك الآن تم إصلاح محمل الأقلاع boot loader وتستطيع أن تدخل للويندوز من جديد :)
