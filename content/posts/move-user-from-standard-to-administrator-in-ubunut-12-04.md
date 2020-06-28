Title: كيفية نقل حساب المستخدم من صلاحية standard إلى صلاحية administrator في أبونتو
Date: 2012-10-14 16:17
Author: admin
Category: GNULinux, howto
Slug: move-user-from-standard-to-administrator-in-ubunut-12-04
Status: published

[![root](http://mycodee.com/wp-content/uploads/2012/10/root-300x188.jpg){.aligncenter .size-medium .wp-image-196 width="300" height="188"}](http://mycodee.com/wp-content/uploads/2012/10/root.jpg)

مؤخراً قمت بالخطأ بتحويل حساب المستخدم الأساسي لنظام أبونتو من administrator إلى standard :( .. وبعدها لم أتمكن من فعل أي عمل يتطلب صلاحيات الأدمن، مثل تنصيب برامج وغيرها .. وحتى لم أتمكن من الانتقال لحساب الرووت من خلال تعليمة sudo su!!

[فقط لتعرف كيفية تحويل نمط الحساب من adminstrator إلى standard فكل ما عليك فعله هو الذهاب إلى User Account وبعدها قم بتعمل Account type من  adminstrator إلى standard.]{style="color:#cc3333;"}

المهم لإعادة صلاحيات الحساب إلى administrator اتبع الخطوات التالية:

الخطوة الأولى: 
--------------

قم بإعادة تشغيل جهازك للدخول في grub (للدخول لقائمة grub قم بالضغط على زر **shift** بشكل مستمر بينما تتم عملية إعادة التشغيل) ثم قم باختيار الخيار "**[recovery mode]{style="font-size: 13px;"}**".

الخطوة الثانية: 
---------------

قم باختيار "root" من قائمة recovery، عندها ستفتح لديك terminal في أسفل الشاشة قم بكتابة التعليمات التالية:

> [mount -o remount,rw /]{style="color: rgb(54, 49, 45); font-family: Consolas, Monaco, 'Lucida Console', monospace; font-size: 13px; line-height: 24px;"}
>
> [sudo addgroup your-username sudo]{style="font-family: monospace; font-size: 13px;"}

قم بتبديل "[your-username"]{style="font-family: monospace; font-size: 13px; font-style: italic;"} باسم المستخدم الذي تريد تحويل حسابه، مثلاً عندي اسم المستخدم هو "mohanad".

 الخطوة الثالثة: 
----------------

قم بإعادة تشغيل الجهاز من خلال الضغط على CTRL+D وبعدها قم باختيار "resume" من قائمة recovery.

انتهينا .. هذا كل مافي الأمر :)
