Title: Install Zend server
Date: 2011-02-19 13:23
Author: admin
Category: Servers
Slug: zend-server
Status: published

![zend server](http://ww1.prweb.com/prfiles/2009/10/19/3077094/gI_0_zendcolorlogo.gif.jpg "zend server"){.aligncenter width="250" height="118"}

::: {dir="rtl"}
السلام عليكم ورحمة الله وبركاته

سنقوم اليوم بشرح كيفية تنصيب [Zend server]{style="color:#333399;"} على أنظمة جنولينوكس دبيان ومشتقاتها...

ولكن قبل أن نبدأ سنقوم بتعريف بسيط لهذا المخدم:

Zend server هو مخدم لتطبيقات الويب حيث يقوم بتشغيل وإدارة التطبيقات المكتوبة بلغة PHP ، كما يوفر هذا المخدم بيئة جيدة لبرمجة تطبيقات الويب بالإضافة إلى العديد من الإضافات التي تساعد PHP على الاتصال بمديري قواعد البيانات مثل أوراكل ، أحد هذه الإضافات هي OCI الضرورية للاتصال بأوراكل..

الآن لنبدأ بخطوات تنصيب هذا المخدم :

[**الخطوة الأولى - إضافة المستودعات المطلوبة:**]{style="color:#008000;"}

علينا أن نقوم بإضافة مستودع لملف الـ source.list حيث يمكننا فتحه بتطبيق التعليمة التالية:

**`#gedit /etc/apt/sources.list `**

ومن ثم نقوم بإضافة المستودع التالي إلى آخر الملف :

**`deb http://repos.zend.com/zend-server/deb server non-free `**

[**الخطوة الثانية - إضافة مفتاح public key:**]{style="color:#008000;"}

نقوم بتنفيذ التعليمة التالية :

**`# wget http://repos.zend.com/zend.key -O- |apt-key add - `**

` #wget http://repos.zend.com/zend.key -O- | sudo apt-key add -`

[**الخطوة الثالثة - تحديث المستودعات:**]{style="color:#008000;"}

**`# aptitude update `**

**[الخطوة الرابعة - تنصيب Zend server:]{style="color:#008000;"}**

**`# aptitude install zend-server-php-5.3`**

بعد الانتهاء من التنصيب يمكنك الدخول لصفحة المخدم من خلال العنوان التالي:  
http://localhost:10081/ZendServer

المصدر : [http://files.zend.com/help/Zend-Serv...stallation.htm](http://files.zend.com/help/Zend-Server/zend-server.htm#deb_installation.htm)  
بالتوفيق وأرجو أن يكون الشرح واضحاً..
:::
