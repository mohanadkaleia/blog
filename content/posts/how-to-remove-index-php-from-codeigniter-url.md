Title: How to remove index.php from Codeigniter URL
Date: 2012-10-05 14:28
Author: admin
Category: Code, howto, Servers, Website
Slug: how-to-remove-index-php-from-codeigniter-url
Status: published

 

[![codeIgniter](../../static/images/how-to-remove-index-php-from-codeigniter-url/codeig_ote-300x216.png)](../../static/images/how-to-remove-index-php-from-codeigniter-url/codeig_ote-300x216.png)

[في حال كنت مطور ويب وتعاملت مع بيئة [codeIgniter](http://ellislab.com/codeigniter) لابد وأنك قد لاحظت أن الرابط URL الافتراضي يحتوي على الجزء **index.php** وربما قد أزعجك وجوده مثلي بشكل دائم، ولابد أنك تريد تغييره وحذفه وإلا لما وصلت لهذه الصفحة ![wink](../../static/images/how-to-remove-index-php-from-codeigniter-url/wink_smile.gif "wink").]

> before:
>
> localhost/backmeup/[index.php/dashboard]
>
> after:
>
> [localhost/backmeup/dashboard]

 

لإزالته فقط اتبع الخطوات التالية:

1.  [قم بفتح ملف **config.php** من **system/application/config **وقم بحذف index.php من الخيار **\$config\['index\_page'\]**.]
2.  قم بإنشاء ملف **.htaccess** في مسار الجذر (بنفس مستوى مجلد application و system) وقم بوضع الكود التالي بداخله:

> RewriteEngine on
>
> RewriteCond \$1 !\^(index\\.php\|resources\|robots\\.txt)
>
> RewriteCond %{REQUEST\_FILENAME} !-f
>
> RewriteCond %{REQUEST\_FILENAME} !-d
>
> [RewriteRule \^(.\*)\$ index.php/\$1 \[L,QSA\]]

 

في حال كان mod\_rewrite غير مفعل لديك كما هو الحال في أنظمة أبونتو، عندها يجب عليك أن تقوم بتفعليه كما يلي:

نكتب التعليمة التالية في التيرمينال:

> [sudo a2enmod rewrite]

التعليمة السابقة تقوم بتفعيل مود rewrite في الأباتشي، ولكن مهلاً لم ننتهي بعد يجب علينا أن نقوم بتعديل خيار [AllowOverrides ملف الإعدادات في الأباتشي والذي يسمح بتغيير إعدادات الأباتشي بناء على ملف htaccess، نقوم بتعديله كما يلي:]

نفتح ملف الإعدادات من خلال أي محرر نحبه مثلاً gedit:

> sudo gedit /etc/apache2/sites-available/default

الآن بعد أن فتح معك الملف ابحث عن [“AllowOverride None” وقم بتعديله ليصبح “AllowOverride All”.]

لقد انتهينا لم يتبقى سوى عمل إعادة تشغيل لخدمة الأباتشي من خلال التعليمة التالية في التيرمينال:

> service apache2 restart

تهانينا لقد أصبح عنوان URL خالي من index.php المزعجة للمستخدم ولمحركات البحث ![wink](../../static/images/how-to-remove-index-php-from-codeigniter-url/wink_smile.gif "wink")

 

تنويه: تم تجربة الحل بنجاح على أبونتو 12.04
