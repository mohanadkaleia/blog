Title: Working with prolog on ubuntu	
Date: 2013-06-05 21:54	
Author: admin	
Category: Application, GNULinux, howto	
Slug: working-with-prolog-on-ubuntu	
Status: published	

[![swipl](../../static/images/working-with-prolog-on-ubuntu/swipl.png){.aligncenter .size-full .wp-image-264 width="170" height="140"}](../../static/images/working-with-prolog-on-ubuntu/swipl.png)	

[بقلم: م.مهند شب قلعية.]{style="background-color:#cccccc;"}	

يوجد العديد من مفسرات لغة البرولوغ على بيئة ويندوز ومنها [visual prolog](http://www.visual-prolog.com/) ، ولكن القليل منها يعمل على بيئة لينوكس، سنتكلم على بيئة [SWI-Prolog](http://www.swi-prolog.org/) بعض ميزات هذه البيئة:	

-   مجاني ومفتوح المصدر.	
-   خفيف وسريع.	
-   يدعم تعدد الخيوط.	
-   يدعم أنظمة تشغيل WIndows - GUN/Linux - Mac	
-   ...	

[الخطوة الأولى - تنصيب swi-prolog:]{style="color:#800080;"} 	
-----------------------------------------------------------	

الآن لننتقل لتنصيب البيئة، أولاً قم بفتح التيرمينال terminal وقم بلصق الأسطر التالية فيها:	

> \% sudo apt-add-repository ppa:swi-prolog/devel  	
>   	
> % sudo apt-get update  	
>   	
> % sudo apt-get install swi-prolog	
هل انتهى التنصيب؟!!! تهانينا الآن بإمكانك كتابة برامج باستخدام لغة برولوغ	



[الخطوة الثانية - التجربة:]{style="color:#800080;"} 	
---------------------------------------------------	

لنقم بتجربة البرنامج، قبل أن نجرب البرنامج سنقوم بكتابة ملف يحتوي مجموعة صغيرة جداً من القواعد.. قم بنسخها أو قم بكتابة برنامج الخاص:	

> traffic\_light(red , no\_cars).  	
>   	
> traffic\_light(green , cars).	
الأسطر السابقة تمثل نظام إشارة مرور بسيط جداً، حيث تعطي إشارة **[حمراء]{style="color:#B22222;"}** في حال عدم تواجد سيارات في الشارع، لتسمح بالمشاة بالمرور، وتعطي إشارة **[خضراء]{style="color:#008000;"}** في حال تواجد سيارات. قم بحفظ الملف وتسميته [basic\_its\_system.pl]{style="font-family: Georgia, Times, 'Times New Roman', serif; font-size: 13px; font-style: italic;"}	

الآن لنقم بتشغيل البرنامج، من التيرمينال نكتب التعليمة التالية **swipl** ستظهر كتابات كتابات**،** ما سنقوم به هو استدعاء الملف الذي كتبناه لنقوم بإجراء استعلامات عليه كما يلي:	

قم بكتابة التعليمة التالية:	

> consult('/home/mohanad/Workspace/prolog/basic\_its\_system.pl').	
يجب أن تظهر الرسالة التالية لتخبرنا بإنه قد تم جلب الملف وترجمته بنجاح:	

> \% /home/mohanad/Workspace/prolog/basic\_its\_system.pl compiled 0.00 sec, 256 bytes  	
>   	
> true.	
الآن يمكننا إجراء استعلامات، فممكن مثلاً أن نقوم بالاستعلام التالي:	

> traffic\_light(X , no\_cars).	
ما النتيجة التي أعطاك إياها؟!!! :)	

تذكر يوجد بالموقع دليل استخدام قوي وسهل يمكن الاستعانة به في أي وقت.. اسمتمع :)Title: Working with prolog on ubuntu	
Date: 2013-06-05 21:54	
Author: admin	
Category: Application, GNULinux, howto	
Slug: working-with-prolog-on-ubuntu	
Status: published	

[![swipl](../../static/images/working-with-prolog-on-ubuntu/swipl.png){.aligncenter .size-full .wp-image-264 width="170" height="140"}](../../static/images/working-with-prolog-on-ubuntu/swipl.png)	

[بقلم: م.مهند شب قلعية.]{style="background-color:#cccccc;"}	

يوجد العديد من مفسرات لغة البرولوغ على بيئة ويندوز ومنها [visual prolog](http://www.visual-prolog.com/) ، ولكن القليل منها يعمل على بيئة لينوكس، سنتكلم على بيئة [SWI-Prolog](http://www.swi-prolog.org/) بعض ميزات هذه البيئة:	

-   مجاني ومفتوح المصدر.	
-   خفيف وسريع.	
-   يدعم تعدد الخيوط.	
-   يدعم أنظمة تشغيل WIndows - GUN/Linux - Mac	
-   ...	

[الخطوة الأولى - تنصيب swi-prolog:]{style="color:#800080;"} 	
-----------------------------------------------------------	

الآن لننتقل لتنصيب البيئة، أولاً قم بفتح التيرمينال terminal وقم بلصق الأسطر التالية فيها:	

> \% sudo apt-add-repository ppa:swi-prolog/devel  	
>   	
> % sudo apt-get update  	
>   	
> % sudo apt-get install swi-prolog	
هل انتهى التنصيب؟!!! تهانينا الآن بإمكانك كتابة برامج باستخدام لغة برولوغ	



[الخطوة الثانية - التجربة:]{style="color:#800080;"} 	
---------------------------------------------------	

لنقم بتجربة البرنامج، قبل أن نجرب البرنامج سنقوم بكتابة ملف يحتوي مجموعة صغيرة جداً من القواعد.. قم بنسخها أو قم بكتابة برنامج الخاص:	

> traffic\_light(red , no\_cars).  	
>   	
> traffic\_light(green , cars).	
الأسطر السابقة تمثل نظام إشارة مرور بسيط جداً، حيث تعطي إشارة **[حمراء]{style="color:#B22222;"}** في حال عدم تواجد سيارات في الشارع، لتسمح بالمشاة بالمرور، وتعطي إشارة **[خضراء]{style="color:#008000;"}** في حال تواجد سيارات. قم بحفظ الملف وتسميته [basic\_its\_system.pl]{style="font-family: Georgia, Times, 'Times New Roman', serif; font-size: 13px; font-style: italic;"}	

الآن لنقم بتشغيل البرنامج، من التيرمينال نكتب التعليمة التالية **swipl** ستظهر كتابات كتابات**،** ما سنقوم به هو استدعاء الملف الذي كتبناه لنقوم بإجراء استعلامات عليه كما يلي:	

قم بكتابة التعليمة التالية:	

> consult('/home/mohanad/Workspace/prolog/basic\_its\_system.pl').	
يجب أن تظهر الرسالة التالية لتخبرنا بإنه قد تم جلب الملف وترجمته بنجاح:	

> \% /home/mohanad/Workspace/prolog/basic\_its\_system.pl compiled 0.00 sec, 256 bytes  	
>   	
> true.	
الآن يمكننا إجراء استعلامات، فممكن مثلاً أن نقوم بالاستعلام التالي:	

> traffic\_light(X , no\_cars).	
ما النتيجة التي أعطاك إياها؟!!! :)	

تذكر يوجد بالموقع دليل استخدام قوي وسهل يمكن الاستعانة به في أي وقت.. اسمتمع :)