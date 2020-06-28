Title: Install and setup ftp server on ubuntu
Date: 2013-06-03 18:03
Author: admin
Category: GNULinux, howto, Servers
Slug: install-and-setup-ftp-server-on-ubuntu
Status: published

[![offSiteFTP\_B](http://mycodee.com/wp-content/uploads/2013/06/offSiteFTP_B-300x104.png){.aligncenter .size-medium .wp-image-249 width="300" height="104"}](http://mycodee.com/wp-content/uploads/2013/06/offSiteFTP_B.png)

قبل أن أبداً بشرح كيفية تنصيب مخدم الملفات FTP server، لنتحدث باختصار شديد عن ماهو مخدم الملفات. [بداية FTP هي اختصار File transfer protocol أي بروتوكول نقل الملفات، ومن خلاله يمكن تبادل البيانات في الشبكة بين المخدم والأجهزة العادية. وطبعاً ftp server هو المخدم الذي يتم فيه حفظ البيانات.]{style="line-height: 1.6em;"}

[الخطوة الأولى - تنصيب مخدم vsftp:]{style="color:#800080;"} 
-----------------------------------------------------------

لتنصيب مخدم الملفات vsftp نقوم بفتح terminal ونكتب فيها تعليمة التنصيب:

> sudo apt-get install vsftpd

 

[الخطوة الثانية - ضبط الإعدادات:]{style="color:#800080;"} 
---------------------------------------------------------

بعد الانتهاء من التنصيب سيصبح جهازك مخدم ملفات، ولكن علينا أن نقوم بضبط بعض الإعدادات، نقوم بفتح ملف الإعدادات من خلال terminal كما يلي:

> sudo gedit /etc/vsftpd.conf

الآن بعد أن ظهر لك ملف الإعدادات عليك أن تقوم بالبحث عن الخيارات التالية، واجعلها كما يلي:

> [anonymous\_enable=NO]{style="line-height: 1.6em;"}
>
> [local\_enable=YES]{style="font-family: Georgia, Times, 'Times New Roman', serif; font-size: 13px; font-style: italic;"}
>
> write\_enable=YES

أي قمنا بمنع المستخدم المجهول من الدخول للسيرفر، الخيار الثاني هو للسماح بالدخول على السيرفر من خلال معلومات المستخدمين المحليين على السيرفر، أما الخيار الثالث فهو للسماح بكتابة المعلومات على السيرفر، [**انتبه يجب أن تكون هذه الخيارات غير معلقة أي لا يجب أن يسبقها رمز \#.**]{style="color:#A52A2A;"}

 

[الخطوة الثالثة - إعادة تشغيل خدمة الملفات:]{style="color:#800080;"} 
--------------------------------------------------------------------

لم يتبقى علينا الآن سوى أن نكتب التعليمة التالية في terminal:

> sudo service vsftpd restart

تهانينا الآن أصبح جهازك مخدم للملفات :)
