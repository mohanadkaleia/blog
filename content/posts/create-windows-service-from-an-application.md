Title: Create windows service from an application
Date: 2016-06-06 19:16
Author: mohanad
Category: Application, howto, Servers
Tags: nssm, service, system
Slug: create-windows-service-from-an-application
Status: published
Direction: rtl

[في هذه المقالة سوف أقوم بشرح كيفية إنشاء [system service]{dir="LTR"} على نظام التشغيل ويندوز.]{style="font-size:14px;"}

[[**في البداية ماهي [system services]{dir="LTR"}؟!**]{.underline}]{style="font-size:14px;"}

[[System services]{dir="LTR"} هي نوع خاص من التطبيقات تم إعدادها لكي تعمل في الخلفية، أحياناً حتى قبل أن يقوم المستخدم بتسجيل دخول.]{style="font-size:14px;"}

[لن أتحدث هنا بالتفصيل عن [windows services]{dir="LTR"} يمكن الإطلاع عليها لو أحب القارئ من المصادر في آخر المقالة [\[1\]]{dir="LTR"}.]{style="font-size:14px;"}

[حديثي في هذه المقالة حول كيفية إنشاء [service]{dir="LTR"} بسهولة، سنتعامل مع برنامج اسمه **[nssm]{dir="LTR"}**، واسمه اختصار لـ [non-sucking service ]{dir="LTR"}]{style="font-size:14px;"}[[manager]{style="font-size:14px;"}]{dir="LTR"}[..]{style="font-size:14px;"}[ [J]{dir="LTR"} من اسمه نلاحظ أنه سهل الاستخدام يحاول تخفيف تعقيدات التعامل مع الخدمات]{style="font-size:14px;"}

[سأفترض أنه يوجد برنامج جاهز تريد فقط أن تقوم بتحويله إلى خدمة،]{style="font-size:14px;"}

1.  [قم بتحميل البرنامج من خلال صفحة التحميل الخاصة بالموقع: [[https://nssm.cc/download]{dir="LTR"}](https://nssm.cc/download)]{style="font-size:14px;"}
2.  [بعد أن قمت بتحميله، عليك أن تقوم بفك ضغط المجلد]{style="font-size:14px;"}
3.  [يمكن تشغيل البرنامج والتعامل معه إما من خلال سطر الأوامر أو يمكن استخدام الواجه المرئية [GUI]{dir="LTR"} الخاصة به (بالنسبة لي أفضل استخدام الواجهة المرئية)]{style="font-size:14px;"}
4.  [لتشتغيل الواجهة المرئية، من سطر الأوامر قم بتحويل المسار ليوافق مسار البرنامج]{style="font-size:14px;"}
5.  [بعدها قم بتنفيذ التعليمة: [nssm.exe install \<servicename\>]{dir="LTR"}]{style="font-size:14px;"}
6.  [بتنفيذ هذه التعليمة سوف تفتح لك الواجهة لتقوم بإضافة البرنامج الذي تريد تحويله إلى خدمة، كما هو موضح بالشكل التالي: [![install\_application](../../static/images/create-windows-service-from-an-application/install_application-300x171.png){.aligncenter .size-medium .wp-image-623 width="300" height="171"}](../../static/images/create-windows-service-from-an-application/install_application.png)]{style="font-size:14px;"}
7.  [قم بتحديد مسار البرنامج، واختيار اسم للخدمة وقم بالضغط على زر [install service]{dir="LTR"}]{style="font-size:14px;"}
8.  [الآن تم إنشاء الخدمة، كل ما عليك فعله هو تشغيلها من خلال الذهاب إلى [services]{dir="LTR"}]{style="font-size:14px;"}

 

[الآن تحول برنامجك إلى خدمة تعمل في الخلفية بدون الحاجة لتسجيل الدخول وتشغيلها بشكل يدوي.]{style="font-size:14px;"}

 

[[**المصادر:**]{.underline}]{style="font-size:14px;"}

1.  [[[https://en.wikipedia.org/wiki/Windows\_service]{dir="LTR"}](https://en.wikipedia.org/wiki/Windows_service)]{style="font-size:14px;"}
2.  [[[https://nssm.cc]{dir="LTR"}](https://nssm.cc)]{style="font-size:14px;"}

 

 
