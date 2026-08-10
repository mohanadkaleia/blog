Title: كيفية نقل حساب المستخدم من صلاحية standard إلى صلاحية administrator في أبونتو
Date: 2012-10-14 16:17
Author: admin
Category: GNULinux, howto
Slug: move-user-from-standard-to-administrator-in-ubunut-12-04
Status: published

[![root](../../static/images/move-user-from-standard-to-administrator-in-ubunut-12-04/root-300x188.jpg)](../../static/images/move-user-from-standard-to-administrator-in-ubunut-12-04/root.jpg)

مؤخراً قمت بالخطأ بتحويل حساب المستخدم الأساسي لنظام أبونتو من administrator إلى standard :( .. وبعدها لم أتمكن من فعل أي عمل يتطلب صلاحيات الأدمن، مثل تنصيب برامج وغيرها .. وحتى لم أتمكن من الانتقال لحساب الرووت من خلال تعليمة sudo su!!

فقط لتعرف كيفية تحويل نمط الحساب من adminstrator إلى standard فكل ما عليك فعله هو الذهاب إلى User Account وبعدها قم بتعمل Account type من  adminstrator إلى standard.

المهم لإعادة صلاحيات الحساب إلى administrator اتبع الخطوات التالية:

الخطوة الأولى: 
--------------

قم بإعادة تشغيل جهازك للدخول في grub (للدخول لقائمة grub قم بالضغط على زر **shift** بشكل مستمر بينما تتم عملية إعادة التشغيل) ثم قم باختيار الخيار "**recovery mode**".

الخطوة الثانية: 
---------------

قم باختيار "root" من قائمة recovery، عندها ستفتح لديك terminal في أسفل الشاشة قم بكتابة التعليمات التالية:

> mount -o remount,rw /
>
> sudo addgroup your-username sudo

قم بتبديل "your-username" باسم المستخدم الذي تريد تحويل حسابه، مثلاً عندي اسم المستخدم هو "mohanad".

 الخطوة الثالثة: 
----------------

قم بإعادة تشغيل الجهاز من خلال الضغط على CTRL+D وبعدها قم باختيار "resume" من قائمة recovery.

انتهينا .. هذا كل مافي الأمر :)
