Title: No Internet on Windows server 2008
Date: 2014-03-06 21:43
Author: mohanad
Category: maintenance, Servers
Tags: 0.0.0.0, gate way address, no internet connection
Slug: no-internet-on-windows-server-2008
Status: published

![no-internet-connection-300x300](../../static/images/no-internet-on-windows-server-2008/no-internet-connection-300x300-300x300.jpg){.size-medium .wp-image-357 .aligncenter width="192" height="192"}

هل واجهتك مشكلة عدم قدرة ويندوز سيرفر 2008 (أو حتى ويندوز فيستا أو 7) من الاتصال بالنت؟!!! جربت أن تعمل **ping** على إحدى المواقع فتحصل على عنوان IP المقابل ولكن لا يمكن الوصول للموقع!!

وربما جربت الذهاب لموجه الأوامر CMD وكتابة تعليمة ipconfig /all وترى أن default gate way address قد تم وضعه على العنوان 0.0.0.0 مع أنك لم تقم بذلك وحتى لو ذهبت لضبط إعدادات الشبكة فلن تجد هذا العنوان!!!

لو حصلت معك هذه الأعرض فإن السيرفر لن يتمكن من الوصول للانترنت لأنه يتوجه دوماً لطلب الاتصال من العنوان 0.0.0.0 ولن يتمكن من الوصول لشبكة الانترنت أبداً. لحل هذه المشكلة يجب إعادة ضبط عنوان gate way كما يلي:

1.  قم بفتح موجه الأوامر CMD
2.  أكتب التعليمة التالية: [route delete 0.0.0.0]{style="font-family: 'Century Gothic', serif; font-size: 16px; line-height: 24px; background-color: rgb(242, 242, 242);"}
3.  الآن لقد تم حذف العنوان الخاطئ، عليك الآن الذهاب إلى إعدادات الشبكة للقيام بضبط إعادات gate way مرة أخرى بشكل صحيح.

هذا هو كل شيء .. :)
