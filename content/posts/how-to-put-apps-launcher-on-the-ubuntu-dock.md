Title: كيفية إضافة أي برنامج إلى شريط يونيتي في أبونتو
Date: 2013-06-04 16:46
Author: admin
Category: Application, GNULinux, howto
Slug: how-to-put-apps-launcher-on-the-ubuntu-dock
Status: published

[![unity launcher](../../static/images/how-to-put-apps-launcher-on-the-ubuntu-dock/unity-launcher.jpg){.aligncenter .size-full .wp-image-261 width="285" height="177"}](../../static/images/how-to-put-apps-launcher-on-the-ubuntu-dock/unity-launcher.jpg)

يؤمن مشغُل يونيتي  Unity launcher في أبونتو الوصول السريع للتطبيقات من خلال الاختصارات الموجودة عليه، بشكل عام يمكن إضافة أي برنامج إلى هذا المشغل عن طريق تشغيله أولاً وبعدها النقر بالزر اليمين على أيقونته على مشغل يونيتي ونختار lock to launcherK، ولكن بعض التطبيقات لا نستطيع تطبيق هذا الأمر معها، إحدى هذه التطبيقات هي [Aptana](http://www.aptana.com/) 

[الخطوة الأولى - إنشاء ملف التشغيل:]{style="color:#800080;"} 
------------------------------------------------------------

إذهب إلى مسار مجلد البرنامج مثلاً home/mohanad/programs/aptana وقم بإنشاء ملف نصي بداخله (حالياً اتركه باسمه الافتراضي ولا تغير اسمه).. ثم اكتب بداخل هذا الملف النصي التالي:

> \[Desktop Entry\]  
>   
> Type=Application  
>   
> StartupNotify=True  
>   
> Name=Aptana  
>   
> Comment=Aptana Studio 3  
>   
> Icon=/home/mohanad/programs/Aptana\_Studio\_3/icon.xpm  
>   
> Exec=/home/mohanad/programs/Aptana\_Studio\_3/AptanaStudio3   
>   
> Terminal=false  
>   
> Categories=Development;IDE;

 

أهم سطرين في النص السابق هو مسار أيقونة البرنامج ومسار ملف تشغيل البرنامج، قم بتعديلها لتصبح حسب المسار في جهازك.

[الخطوة الثانية - إضافته على مشغل يونيتي:]{style="color:#800080;"} 
------------------------------------------------------------------

الآن قبل أن نقوم بإضافته على شريط يونيتي قم بتغيير اسم الملف النصي إلى aptana.desktop ثم ومن التيرمينال أعطه صلاحيات التشغيل كما في التعليمة التالية:

> chmod +x aptana.desktop

بعد الانتهاء قم بتجربته عن طريق النقر عليه نقرتين، تهانينا لقد اشتغل معك البرنامج، الآن لم يبقى لنا سوى إضافته على شريط يونيتي وذلك من خلال سحبه وإفلاته على الشريط.. أو بعد أن يتم تشغيل قم بالنقر عليه في شريط يونتي واختر lock to launcher.

 

 
