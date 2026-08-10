Title: Create windows service from an application
Date: 2016-06-06 19:16
Author: mohanad
Category: Application, howto, Servers
Tags: nssm, service, system
Slug: create-windows-service-from-an-application
Status: published
Direction: rtl

<span dir="ltr">في هذه المقالة سوف أقوم بشرح كيفية إنشاء [system service</span> على نظام التشغيل ويندوز.]

<span dir="ltr">[**في البداية ماهي [system services</span>؟!**]]

<span dir="ltr">[System services</span> هي نوع خاص من التطبيقات تم إعدادها لكي تعمل في الخلفية، أحياناً حتى قبل أن يقوم المستخدم بتسجيل دخول.]

<span dir="ltr">لن أتحدث هنا بالتفصيل عن [windows services</span> يمكن الإطلاع عليها لو أحب القارئ من المصادر في آخر المقالة [\[1\]].]

<span dir="ltr">حديثي في هذه المقالة حول كيفية إنشاء [service</span> بسهولة، سنتعامل مع برنامج اسمه **<span dir="ltr">nssm</span>**، واسمه اختصار لـ <span dir="ltr">non-sucking service </span>][manager]..<span dir="ltr"> [J</span> من اسمه نلاحظ أنه سهل الاستخدام يحاول تخفيف تعقيدات التعامل مع الخدمات]

سأفترض أنه يوجد برنامج جاهز تريد فقط أن تقوم بتحويله إلى خدمة،

1.  <span dir="ltr">قم بتحميل البرنامج من خلال صفحة التحميل الخاصة بالموقع: [[https://nssm.cc/download</span>](https://nssm.cc/download)]
2.  بعد أن قمت بتحميله، عليك أن تقوم بفك ضغط المجلد
3.  <span dir="ltr">يمكن تشغيل البرنامج والتعامل معه إما من خلال سطر الأوامر أو يمكن استخدام الواجه المرئية [GUI</span> الخاصة به (بالنسبة لي أفضل استخدام الواجهة المرئية)]
4.  لتشتغيل الواجهة المرئية، من سطر الأوامر قم بتحويل المسار ليوافق مسار البرنامج
5.  <span dir="ltr">بعدها قم بتنفيذ التعليمة: [nssm.exe install \<servicename\></span>]
6.  [بتنفيذ هذه التعليمة سوف تفتح لك الواجهة لتقوم بإضافة البرنامج الذي تريد تحويله إلى خدمة، كما هو موضح بالشكل التالي: [![install\_application](../../static/images/create-windows-service-from-an-application/install_application-300x171.png)](../../static/images/create-windows-service-from-an-application/install_application.png)]
7.  <span dir="ltr">قم بتحديد مسار البرنامج، واختيار اسم للخدمة وقم بالضغط على زر [install service</span>]
8.  <span dir="ltr">الآن تم إنشاء الخدمة، كل ما عليك فعله هو تشغيلها من خلال الذهاب إلى [services</span>]

 

الآن تحول برنامجك إلى خدمة تعمل في الخلفية بدون الحاجة لتسجيل الدخول وتشغيلها بشكل يدوي.

 

<u>[**المصادر:**</u>]

1.  <span dir="ltr">[[https://en.wikipedia.org/wiki/Windows\_service</span>](https://en.wikipedia.org/wiki/Windows_service)]
2.  <span dir="ltr">[[https://nssm.cc</span>](https://nssm.cc)]

 

 
