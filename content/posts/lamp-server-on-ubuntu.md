Title: ٍStep by step LAMP server on Ubuntu
Date: 2011-01-14 14:38
Author: admin
Category: Servers
Slug: lamp-server-on-ubuntu
Status: published

[![lamp](../../static/images/lamp-server-on-ubuntu/lamp.jpg)](../../static/images/lamp-server-on-ubuntu/lamp.jpg)

إن كنت من مطوري الويب فلابد وأنك قد سمعت أو احتجت لتحويل جهازك إلى مخدم ويب لاستضافة مشاريعك الخاصة على جهازك المحلي قبل أن تقوم بتصديرهم للسيرفر الرئيسي،  سنشرح الآن كيفية تنصيب LAMP سيرفر على أبونتو، طبعاً LAMP هي اختصار Linux - Apache - Mysql - PHP.

<u>[الخطوة الأولى - تنصيب Apache:</u>]
---------------------------------------------------------------------

قم بفتح التيرمينال terminal واكتب فيه التعليمة التالية والتي تقوم بتنصيب الأباتشي:

> **sudo apt-get install apache2**

بعد الانتهاء من تنصيب الأباتشي يمكنك تجريبه من متصفح الويب من خلال كتابة عنوان جهازك المحلي <http://localhost/>، وانظر النتيجة التي ستظهر لك، الصفحة التي ظهرت لك هي الصفحة الرئيسية في الأباتشي ويمكنك تغييرها لاحقاً.

![](http://tech.mobiletod.com/wp-content/uploads/2010/12/Screenshot-7.png "Apache it's work")
-----------------------------------------------------------------------------------------------------------

<u>الخطوة الثانية - تنصيب قاعدة البيانات mysql:</u>
----------------------------------------------------------

الآن علينا تنصيب قاعدة البيانات mysql، أيضاً قم بكتابة التعليمة التالية في التيرمينال terminal:

> ***sudo apt-get install mysql-server***

أثناء تنصيب قاعدة البيانات سيطلب منك إدخال كلمة المرور الخاصة بالمستخدم root للقاعدة، قم بإدخالها وتذكرها جيداً.

<u>الخطوة الثالثة - تنصيب PHP:</u>
-----------------------------------------

لتنصيب PHP قم بإدخال التعليمة التالية في التيرمينال:

> **sudo apt-get install php5 libapache2-mod-php5**

بعد الانتهاء من التنصيب قم بإعادة تشغيل الأباتشي من خلال التعليمة التالية:

> **sudo /etc/init.d/apache2 restart**

الآن لنتأكد من أن التنصيب قد تم بنجاح قم بإنشاء ملف وسمه phpinfo.php وقم بحفظه في المسار /var/www، لعمل ذلك قم بكتابة التعليمة التالية في التيرمينال:

> **sudo gedit /var/www/phpinfo.php**

وقم بكتابة التعليمات التالية ضمن الملف (هذه التعليمات ستظهر لك معلومات حول PHP):

> \<?php
>
>               phpinfo();
>
> ?\>

وقم بحفظ الملف ثم افتح متصفح الويب وقم بكتابة عنوان جهازك المحلي واتبعه باسم الملف <http://localhost/phpinfo.php> ، يجب أن تظهر لك معلومات عن PHP كما في الصورة التالية:

![](http://tech.mobiletod.com/wp-content/uploads/2010/12/Screenshot-8.png "PHPinfo")


 



 



<u>PHPMyAdmin:</u>
-------------------------



تهانينا الآن أصبح لديك مخدم ويب LAMP وتستطيع البدء بتطوير مشاريعك الخاصة على جهازك فوراً، ولكن قبل الانتهاء سنقوم بتنصيب أداة لإدارة قاعدة البيانات وهذه الأداة هي الأشهر تقريباً لمطوري الويب واسمها PHPMyAdmin، الآن اكتب في التيرمينال التعليمة التالية:


> ***sudo apt-get install phpmyadmin*** 

أثناء التنصيب سيظهر لك نافذة لاختيار مخدم الويب ليتم ضبط الإعدادات عليه قم باختيار **apache**.

[![choose web server](../../static/images/lamp-server-on-ubuntu/choose-web-server-.png)](../../static/images/lamp-server-on-ubuntu/choose-web-server-.png)

 

بعدها سيطلب منك أن يقوم بضبط قاعدة بيانات من أجل phpMyAdmin مع dbconfig-common قم باختيار [**NO.**]

[![database config](../../static/images/lamp-server-on-ubuntu/database-config.png)](../../static/images/lamp-server-on-ubuntu/database-config.png)

الآن عليك أن تقوم بنسخ ملف ضبط الإعدادات من خلال كتابة التعليمة التالية في التيرمينال:

> ***sudo cp /etc/phpmyadmin/apache.conf /etc/apache2/conf.d/***

الآن قم بعمل restart للأباتشي مرة ثانية من خلال التعليمة التالية في التيرمينال:

> **sudo /etc/init.d/apache2 restart**

جرب الآن phpMyAdmin من خلال الرابط التالي <http://localhost/phpmyadmin/>.

تهانينا الآن LAMP سيرفر جاهز للعمل :)

 
