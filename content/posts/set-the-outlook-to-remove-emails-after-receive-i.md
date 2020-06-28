Title: ضبط برنامج الآوتلوك لحذف الرسائل من السيرفر بعد استقبالها
Date: 2013-06-29 16:26
Author: admin
Category: howto, maintenance
Slug: set-the-outlook-to-remove-emails-after-receive-i
Status: published

[![mail\_remove](http://mycodee.com/wp-content/uploads/2013/06/mail_remove-150x150.png){.aligncenter .size-thumbnail .wp-image-306 width="150" height="150"}](http://mycodee.com/wp-content/uploads/2013/06/mail_remove.png)[بقلم: م. مهند شب قلعية]{style="background-color:#D3D3D3;"}

[تكلمنا سابقاً عن كيفية نقل الآوتلوك من جهاز لجهاز، بعد أن تم النقل ظهرت معي مشكلة وهي أن الرسائل المستقبلة تبقى موجودة على السيرفر ولا يتم حذفها مع العلم أن البروتوكول المستخدم هو POP. قبل أن نتكلم عن تفاصيل المشكلة سنتحدث قليلاً عن البروتوكول POP و Imap المستخدم في الرسائل.]{style="line-height: 1.6em;"}

بشكل عام لاستقبال الرسائل يوجد بروتوكلين هما POP3 و IMAP، يتميز بروتوكل POP بأنه يقوم بحذف الرسائل من السيرفر بعد أن يتم استقبال الرسالة أما IMAP فإنه يقوم بالاحتفاظ بنسخة من الرسائل على السيرفر.

الآن نعود لمشكلتنا لدينا حساب بريدي معرف على برنامج outlook 2010 ويتم إرسال واستقبال الرسائل بشكل صحيح، المشكلة هي أنه لا يتم حذف الرسائل من السيرفر بعد استقبالها مع العلم أن البرتوكول المستخدم للاستقبال هو POP.

 

حل هذه المشكلة بسيط جداً، إن برنامج outlook يحتوي على خيار للاحتفاظ بالرسائل على السيرفر لعدد معين من الأيام قبل أن يتم حذفها، هذه الميزة تكون مفعلة بشكل افتراضي على outlook 2010 ولإلغاء تفعيلها بكل بساطة نذهب لضبط إعدادات الحساب. ننقر عليه نقرتين بالفأرة.

[![leavemsg\_outlook10\_7](http://mycodee.com/wp-content/uploads/2013/06/leavemsg_outlook10_7.png){.aligncenter .size-full .wp-image-307 width="392" height="432"}](http://mycodee.com/wp-content/uploads/2013/06/leavemsg_outlook10_7.png)الآن من النافذة advanced نقوم بإلغاء تفعيل الخيار Leave a copy of messages on the server. ثم نضغط OK وبعدها Next ليقوم بحفظ الإعدادات.  
  
الآن سيتم حذف الرسائل من السيرفر بمجرد استقبالها.
