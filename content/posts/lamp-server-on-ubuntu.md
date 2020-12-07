Title: ٍStep by step LAMP server on Ubuntu
Date: 2011-01-14 14:38
Author: admin
Category: Servers
Slug: lamp-server-on-ubuntu
Status: published

[![lamp](http://mycodee.com/wp-content/uploads/2011/01/lamp.jpg){.aligncenter .size-full .wp-image-241 width="250" height="127"}](http://mycodee.com/wp-content/uploads/2011/01/lamp.jpg)

إن كنت من مطوري الويب فلابد وأنك قد سمعت أو احتجت لتحويل جهازك إلى مخدم ويب لاستضافة مشاريعك الخاصة على جهازك المحلي قبل أن تقوم بتصديرهم للسيرفر الرئيسي،  سنشرح الآن كيفية تنصيب LAMP سيرفر على أبونتو، طبعاً LAMP هي اختصار Linux - Apache - Mysql - PHP.

[[الخطوة الأولى - تنصيب Apache:]{.underline}]{style="color:#FF8C00;"} 
---------------------------------------------------------------------

قم بفتح التيرمينال terminal واكتب فيه التعليمة التالية والتي تقوم بتنصيب الأباتشي:

> **sudo apt-get install apache2**

بعد الانتهاء من تنصيب الأباتشي يمكنك تجريبه من متصفح الويب من خلال كتابة عنوان جهازك المحلي <http://localhost/>، وانظر النتيجة التي ستظهر لك، الصفحة التي ظهرت لك هي الصفحة الرئيسية في الأباتشي ويمكنك تغييرها لاحقاً.

![](http://tech.mobiletod.com/wp-content/uploads/2010/12/Screenshot-7.png "Apache it's work"){.aligncenter} 
-----------------------------------------------------------------------------------------------------------

[الخطوة الثانية - تنصيب قاعدة البيانات mysql:]{.underline} 
----------------------------------------------------------

الآن علينا تنصيب قاعدة البيانات mysql، أيضاً قم بكتابة التعليمة التالية في التيرمينال terminal:

> ***sudo apt-get install mysql-server***

أثناء تنصيب قاعدة البيانات سيطلب منك إدخال كلمة المرور الخاصة بالمستخدم root للقاعدة، قم بإدخالها وتذكرها جيداً.

[الخطوة الثالثة - تنصيب PHP:]{.underline} 
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

![](http://tech.mobiletod.com/wp-content/uploads/2010/12/Screenshot-8.png "PHPinfo"){.aligncenter}

<div>

 

</div>

<div>

 

</div>

<div>

[PHPMyAdmin:]{.underline} 
-------------------------

</div>

<div>

تهانينا الآن أصبح لديك مخدم ويب LAMP وتستطيع البدء بتطوير مشاريعك الخاصة على جهازك فوراً، ولكن قبل الانتهاء سنقوم بتنصيب أداة لإدارة قاعدة البيانات وهذه الأداة هي الأشهر تقريباً لمطوري الويب واسمها PHPMyAdmin، الآن اكتب في التيرمينال التعليمة التالية:

</div>

> ::: {style="text-align: left;"}
> ***sudo apt-get install phpmyadmin***[ ]{style="line-height: 1.6em;"}
> :::

أثناء التنصيب سيظهر لك نافذة لاختيار مخدم الويب ليتم ضبط الإعدادات عليه قم باختيار [**apache**]{style="color:#FF8C00;"}.

[![choose web server](http://mycodee.com/wp-content/uploads/2011/01/choose-web-server-.png){.aligncenter .size-full .wp-image-244 width="664" height="462"}](http://mycodee.com/wp-content/uploads/2011/01/choose-web-server-.png)

 

[بعدها سيطلب منك أن يقوم بضبط قاعدة بيانات من أجل phpMyAdmin مع dbconfig-common قم باختيار [**NO.**]{style="color:#FF8C00;"}]{style="line-height: 1.6em;"}

[![database config](http://mycodee.com/wp-content/uploads/2011/01/database-config.png){.aligncenter .size-full .wp-image-245 width="481" height="122"}](http://mycodee.com/wp-content/uploads/2011/01/database-config.png)

[الآن عليك أن تقوم بنسخ ملف ضبط الإعدادات من خلال كتابة التعليمة التالية في التيرمينال:]{style="line-height: 1.6em;"}

> ***sudo cp /etc/phpmyadmin/apache.conf /etc/apache2/conf.d/***

الآن قم بعمل restart للأباتشي مرة ثانية من خلال التعليمة التالية في التيرمينال:

> **sudo /etc/init.d/apache2 restart**

جرب الآن phpMyAdmin من خلال الرابط التالي <http://localhost/phpmyadmin/>.

تهانينا الآن LAMP سيرفر جاهز للعمل :)

 
