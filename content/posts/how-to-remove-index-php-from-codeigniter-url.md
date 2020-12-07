Title: How to remove index.php from Codeigniter URL
Date: 2012-10-05 14:28
Author: admin
Category: Code, howto, Servers, Website
Slug: how-to-remove-index-php-from-codeigniter-url
Status: published

 

[![codeIgniter](http://mycodee.com/wp-content/uploads/2012/10/codeig_ote-300x216.png){.aligncenter .size-full .wp-image-199 width="300" height="216"}](http://mycodee.com/wp-content/uploads/2012/10/codeig_ote-300x216.png)

[في حال كنت مطور ويب وتعاملت مع بيئة [codeIgniter](http://ellislab.com/codeigniter) لابد وأنك قد لاحظت أن الرابط URL الافتراضي يحتوي على الجزء **index.php** وربما قد أزعجك وجوده مثلي بشكل دائم، ولابد أنك تريد تغييره وحذفه وإلا لما وصلت لهذه الصفحة ![wink](http://mycodee.com/wp-content/plugins/ckeditor-for-wordpress/ckeditor/plugins/smiley/images/wink_smile.gif "wink"){width="20" height="20"}.]{style="font-size:14px;"}

> [before:]{style="font-size:14px;"}
>
> [localhost/backmeup/[index.php]{style="color:#FF8C00;"}/dashboard]{style="font-size:14px;"}
>
> [after:]{style="font-size:14px;"}
>
> [[localhost/backmeup/]{style="font-family: Georgia, Times, 'Times New Roman', serif; font-style: italic;"}[dashboard]{style="font-family: Georgia, Times, 'Times New Roman', serif; font-style: italic;"}]{style="font-size:14px;"}

 

[لإزالته فقط اتبع الخطوات التالية:]{style="font-size:14px;"}

1.  [قم بفتح ملف **config.php** من **system/application/config **وقم بحذف index.php من الخيار **\$config\['index\_page'\]**.]{style="font-size:14px;"}
2.  [قم بإنشاء ملف **.htaccess** في مسار الجذر (بنفس مستوى مجلد application و system) وقم بوضع الكود التالي بداخله:]{style="font-size:14px;"}

> [RewriteEngine on]{style="color: rgb(68, 68, 68); font-family: Verdana; line-height: 20px;"}  
>
> [RewriteCond \$1 !\^(index\\.php\|resources\|robots\\.txt)]{style="color: rgb(68, 68, 68); font-family: Verdana; line-height: 20px;"}  
>
> [RewriteCond %{REQUEST\_FILENAME} !-f]{style="color: rgb(68, 68, 68); font-family: Verdana; line-height: 20px;"}  
>
> [RewriteCond %{REQUEST\_FILENAME} !-d]{style="color: rgb(68, 68, 68); font-family: Verdana; line-height: 20px;"}  
>
> [RewriteRule \^(.\*)\$ index.php/\$1 \[L,QSA\]]{style="color: rgb(68, 68, 68); font-family: Verdana; line-height: 20px;"}

 

[في حال كان mod\_rewrite غير مفعل لديك كما هو الحال في أنظمة أبونتو، عندها يجب عليك أن تقوم بتفعليه كما يلي:]{style="font-size:14px;"}

[نكتب التعليمة التالية في التيرمينال:]{style="font-size:14px;"}

> [[sudo a2enmod rewrite]{style="font-family: Menlo, Monaco, 'Andale Mono', 'lucida console', 'Courier New', monospace; line-height: 18.850000381469727px; white-space: pre;"}]{style="font-size:14px;"}

[التعليمة السابقة تقوم بتفعيل مود rewrite في الأباتشي، ولكن مهلاً لم ننتهي بعد يجب علينا أن نقوم بتعديل خيار [AllowOverrides]{style="color: rgb(34, 34, 34); font-family: Lato, sans-serif; line-height: 24px; text-align: justify;"} ملف الإعدادات في الأباتشي والذي يسمح بتغيير إعدادات الأباتشي بناء على ملف htaccess، نقوم بتعديله كما يلي:]{style="font-size:14px;"}

نفتح ملف الإعدادات من خلال أي محرر نحبه مثلاً gedit:

> sudo gedit /etc/apache2/sites-available/default

الآن بعد أن فتح معك الملف ابحث عن [[“AllowOverride None” وقم بتعديله ليصبح “AllowOverride All”.]{style="color: rgb(34, 34, 34); font-family: Lato, sans-serif; line-height: 24px; text-align: justify;"}]{style="font-size:14px;"}

لقد انتهينا لم يتبقى سوى عمل إعادة تشغيل لخدمة الأباتشي من خلال التعليمة التالية في التيرمينال:

> [service apache2 restart]{style="font-family: Menlo, Monaco, 'Andale Mono', 'lucida console', 'Courier New', monospace; font-size: 13px; line-height: 18.850000381469727px; white-space: pre;"}

تهانينا لقد أصبح عنوان URL خالي من index.php المزعجة للمستخدم ولمحركات البحث ![wink](http://mycodee.com/wp-content/plugins/ckeditor-for-wordpress/ckeditor/plugins/smiley/images/wink_smile.gif "wink"){width="20" height="20"}

 

[تنويه: تم تجربة الحل بنجاح على أبونتو 12.04]{style="color:#EE82EE;"}
