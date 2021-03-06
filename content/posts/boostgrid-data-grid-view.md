Title: boostGrid: data grid view
Date: 2013-05-24 17:17
Author: admin
Category: Application, Website
Slug: boostgrid-data-grid-view
Status: published
Cover:../../static/images/boostGrid.png
Direction: rtl

![boostGrid](../../static/images/boostGrid.png)


إن إسلوب عرض البيانات للمستخدم هو من أهم الأمور التي يجب أن يراعيها المبرمج أثناء كتابته لبرامجه، ولعل من أهم وأسهل وسائل عرض كتل البيانات الضخمة من قواعد البيانات هي جداول البيانت أو كما يعرفها المبرمجون data grid view والتي تقوم بإظهار البيانات على شكل أسطر كل سطر هو عبارة عن سجل من سجلات قاعدة البيانات.

بالنسبة لمبرمجي الويب فيوجد العديد من الخيارات لاستعمال هذه الأدارة ولعل أبسطها وأقلها تعقيداً هو استعمال الوسم \<table\> وعرض البيانات بداخله، ولكن مع ازدياد حجم البيانات يصبح هناك حاجة أكبر لقدرات وميزات لا يمكن أن يقوم هذا الوسم بعمله، مثل القدرة على الترتيب والبحث والتنقل بين صفحات من البيانات بدلاً من عرضها كصفحة واحدة كبيرة.

بالنسبة لي جربت الكثير والكثير من data grid view ولكل واحدة منها ميزاتها وعيوبها ولكن أهم عيب وعائق واجهني في كل ما تعاملت معه هو ضعف توثيق الكود وقلة الشروحات التي تشرح هذه الأداة. لذا قررت أن أقوم بعمل واحدة من الصفر تجمع كل الميزات التي احتجت إليها خلال سنوات عملي كمطور ويب على تماس مع متطلبات المستخدمين وانتهيت الآن من النسخة الأولى (التجريبية) من هذه الأداة والتي أسميتها [boostGrid](https://mohanadkaleia.com/boostgrid/).

**بعض ميزات boostGrid**:

-   تم بناءها اعتماداً على لغة PHP وموجهة لبيئة codeIgniter.
-   AJAX based: حيث يتم تحديث البيانات دون الحاجة لتحديث الصفحة كاملة.
-   تأخذ مصفوفة كمصدر للبيانات.
-   تذكر الصفحات السابقة.
-   تريتيب البيانات اعتماداً على العمود.
-   بحث ديناميكي على كل الحقول المعروضة.
-   إضافة حقول تحكم (مثل الحذف أو التعديل)
-   دعم الكتابة من اليمين لليسار وبالعكس.
-   تعمل تحت رخصة [LGPL](http://www.gnu.org/licenses/lgpl.html).

يمكن تجربة boostGrid من خلال الذهاب للرابط التالي جربني](https://mohanadkaleia.com/boostgrid).]

كما يمكن تحميل نسخة منها من خلال مستودع [git](https://github.com/mohanadkaleia/boostgrid).

سيتم قريباً طرح دليل المطور بالإضافة لدليل المستخدم، كما سيتم تحسينها من خلال إضافة ميزات جديدة عليها. في حال وجود أخطاء يرجى إبلاغي عنها فوراً ليتم تصحيحها.. وشكراً
