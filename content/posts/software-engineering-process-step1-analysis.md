Title: مراحل بناء مشروع برمجي خطوة بخطوة – الجزء الأول التحليل
Date: 2013-05-17 08:37
Author: admin
Category: Code, Uncategorized
Slug: software-engineering-process-step1-analysis
Status: published

![software\_engineering](http://mycodee.com/wp-content/uploads/2013/05/software_engineering-300x254.png){.aligncenter .size-medium .wp-image-216 width="300" height="254"}

[[[هل[ ]{lang="ar-SY"}فكرت[ ]{lang="ar-SY"}يوماً[ ]{lang="ar-SY"}أو[ ]{lang="ar-SY"}عملت[ ]{lang="ar-SY"}على[ ]{lang="ar-SY"}مشروع[ ]{lang="ar-SY"}ما؟]{lang="ar-SY"}]{lang="ar-SA"}[!! ]{lang="en-US"}[[قبل[ ]{lang="ar-SY"}البدء[ ]{lang="ar-SY"}بتنفيذ[ ]{lang="ar-SY"}أي[ ]{lang="ar-SY"}مشروع[ ]{lang="ar-SY"}لابد[ ]{lang="ar-SY"}من[ ]{lang="ar-SY"}القيام[ ]{lang="ar-SY"}بالتخطيط[ ]{lang="ar-SY"}المسبق[ ]{lang="ar-SY"}له،[ ]{lang="ar-SY"}فمثلاً[ ]{lang="ar-SY"}عندما[ ]{lang="ar-SY"}نرغب[ ]{lang="ar-SY"}ببناء[ ]{lang="ar-SY"}منزل[ ]{lang="ar-SY"}صغير[ ]{lang="ar-SY"}فإننا[ ]{lang="ar-SY"}قبل[ ]{lang="ar-SY"}أن[ ]{lang="ar-SY"}نمسك[ ]{lang="ar-SY"}المطرقة[ ]{lang="ar-SY"}والأخشاب[ ]{lang="ar-SY"}نقوم[ ]{lang="ar-SY"}برسم[ ]{lang="ar-SY"}مخطط[ ]{lang="ar-SY"}للمنزل]{lang="ar-SY"}[ ]{lang="ar-SY"}]{lang="ar-SA"}[blueprint. ]{lang="en-US"}[[كذلك[ ]{lang="ar-SY"}الأمر[ ]{lang="ar-SY"}عندما[ ]{lang="ar-SY"}نريد[ ]{lang="ar-SY"}بناء[ ]{lang="ar-SY"}أي]{lang="ar-SY"}[ ]{lang="ar-SY"}[مشروع]{lang="ar-SY"}[ ]{lang="ar-SY"}[برمجي]{lang="ar-SY"}[ ]{lang="ar-SY"}[فينبغي[ ]{lang="ar-SY"}علينا[ ]{lang="ar-SY"}المرور[ ]{lang="ar-SY"}بعدة[ ]{lang="ar-SY"}مراحل[ ]{lang="ar-SY"}لإتمام[ ]{lang="ar-SY"}المشروع[ ]{lang="ar-SY"}والالتزام[ ]{lang="ar-SY"}بهذه[ ]{lang="ar-SY"}المراحل[ ]{lang="ar-SY"}والمعايير[ ]{lang="ar-SY"}يضمن[ ]{lang="ar-SY"}نجاح[ ]{lang="ar-SY"}وحياة[ ]{lang="ar-SY"}أطول[ ]{lang="ar-SY"}للمشروع]{lang="ar-SY"}]{lang="ar-SA"}[.]{lang="en-US"}]{style="font-size:18px;"}

[[[بشكل[ ]{lang="ar-SY"}عام[ ]{lang="ar-SY"}لتطوير[ ]{lang="ar-SY"}أي[ ]{lang="ar-SY"}نظام[ ]{lang="ar-SY"}برمجي[ ]{lang="ar-SY"}فإننا[ ]{lang="ar-SY"}سنمر[ ]{lang="ar-SY"}بمرحلة]{lang="ar-SY"}[ ]{lang="ar-SY"}[[التحليل]{lang="ar-SY"}]{.underline}[،]{lang="ar-SY"}[ ]{lang="ar-SY"}[[التصميم]{lang="ar-SY"}]{.underline}[،]{lang="ar-SY"}[ ]{lang="ar-SY"}[[التنفيذ]{lang="ar-SY"}]{.underline}[،]{lang="ar-SY"}[ ]{lang="ar-SY"}[[الاختبار]{lang="ar-SY"}]{.underline}[ ]{lang="ar-SY"}[[والصيانة]{lang="ar-SY"}]{.underline}]{lang="ar-SA"}[. ]{lang="en-US"}[[سنتكلم[ ]{lang="ar-SY"}في[ ]{lang="ar-SY"}هذه[ ]{lang="ar-SY"}المقالة[ ]{lang="ar-SY"}عن[ ]{lang="ar-SY"}أولى[ ]{lang="ar-SY"}مراحل[ ]{lang="ar-SY"}التطوير[ ]{lang="ar-SY"}وهي[ ]{lang="ar-SY"}مرحلة]{lang="ar-SY"}[ ]{lang="ar-SY"}[[التحليل]{lang="ar-SY"}]{style="color:#0000FF;"}]{lang="ar-SA"}[.]{lang="en-US"}]{style="font-size:18px;"}

 

[[[[المرحلة[[ ]{lang="ar-SY"}]{.underline}**الأولى**]{lang="ar-SY"}]{.underline}]{lang="ar-SA"}[[:]{.underline} ]{lang="en-US"}[[[التحليل]{lang="ar-SY"}]{.underline}[[ ]{lang="ar-SY"}]{.underline}]{lang="ar-SA"}[[Analysis Phase]{.underline}]{lang="en-US"}]{style="color:#0000FF;"}

[![analysis](http://mycodee.com/wp-content/uploads/2013/05/analysis-300x254.png){.aligncenter .size-medium .wp-image-217 width="300" height="254"}](http://mycodee.com/wp-content/uploads/2013/05/analysis.png)

[[[تعتبر]{lang="ar-SY"}[ ]{lang="ar-SY"}[هذه]{lang="ar-SY"}[ ]{lang="ar-SY"}[المرحلة]{lang="ar-SY"}[ ]{lang="ar-SY"}[من]{lang="ar-SY"}[ ]{lang="ar-SY"}[أهم]{lang="ar-SY"}[ ]{lang="ar-SY"}[مراحل]{lang="ar-SY"}[ ]{lang="ar-SY"}[تصميم]{lang="ar-SY"}[ ]{lang="ar-SY"}[نظامك]{lang="ar-SY"}[ ]{lang="ar-SY"}[البرمجي]{lang="ar-SY"}[ ]{lang="ar-SY"}[وتأخذ]{lang="ar-SY"}[ ]{lang="ar-SY"}[هذه]{lang="ar-SY"}[ ]{lang="ar-SY"}[المرحلة]{lang="ar-SY"}[ ]{lang="ar-SY"}[الحيز]{lang="ar-SY"}[ ]{lang="ar-SY"}[الأكبر]{lang="ar-SY"}[ ]{lang="ar-SY"}[من]{lang="ar-SY"}[ ]{lang="ar-SY"}[العمل]{lang="ar-SY"}[ ]{lang="ar-SY"}[حيث]{lang="ar-SY"}[ ]{lang="ar-SY"}[نجاح]{lang="ar-SY"}[ ]{lang="ar-SY"}[التحليل]{lang="ar-SY"}[ ]{lang="ar-SY"}[يؤدي]{lang="ar-SY"}[ ]{lang="ar-SY"}[لنجاح]{lang="ar-SY"}[ ]{lang="ar-SY"}[المشروع،]{lang="ar-SY"}[ ]{lang="ar-SY"}[ويمكن]{lang="ar-SY"}[ ]{lang="ar-SY"}[تقسيم]{lang="ar-SY"}[ ]{lang="ar-SY"}[هذه]{lang="ar-SY"}[ ]{lang="ar-SY"}[المرحلة]{lang="ar-SY"}[ ]{lang="ar-SY"}[إلى]{lang="ar-SY"}[ ]{lang="ar-SY"}[خطوات]{lang="ar-SY"}[ ]{lang="ar-SY"}[جزئية]{lang="ar-SY"}[ ]{lang="ar-SY"}[كما]{lang="ar-SY"}[ ]{lang="ar-SY"}[في]{lang="ar-SY"}[ ]{lang="ar-SY"}[الشكل]{lang="ar-SY"}[ ]{lang="ar-SY"}[التالي]{lang="ar-SY"}]{lang="ar-SA"}:]{style="font-size:18px;"}

[![software engineering analysis phase](http://mycodee.com/wp-content/uploads/2013/05/software-engineering-analysis-phase-300x273.png){.aligncenter .size-medium .wp-image-218 width="300" height="273"}](http://mycodee.com/wp-content/uploads/2013/05/software-engineering-analysis-phase.png)

### [[**الخطوة**]{lang="ar-SY"}[** الأولىالتعرف على مجال العمل scope definition**]{lang="ar-SY"}]{lang="ar-SA"}**:**  {#الخطوة-الأولىالتعرف-على-مجال-العمل-scope-definition .western align="RIGHT" dir="RTL" style="line-height: 150%"}

[[[في هذه الخطوة المطلوب جمع معلومات عامة عن المجال سواء كانت من خبرتك الشخصية –أنت كمصمم النظام]{lang="ar-SY"}]{lang="ar-SA"}- [[أو من خلال الاطلاع على الأنظمة المشابهة، بالإضافة لتحديد الشريحة المستهدفة لاستخدام هذا النظام]{lang="ar-SY"}]{lang="ar-SA"}.]{style="font-size:18px;"}

 

[[[على سبيل المثال نحن نريد تصميم موقع جامعة ففي هذه الخطوة يكون علينا أن نجمع خبرتنا ]{lang="ar-SY"}]{lang="ar-SA"}([[من كوننا كنا طلاباً]{lang="ar-SY"}]{lang="ar-SA"}) [[ثم نقوم بالاطلاع على مواقع لجامعات أخرى، أما بالنسبة لشريحة المستخدمين المستهدفة لاستخدام هذا الموقع هم الطلاب والمدرسين والإداريين]{lang="ar-SY"}]{lang="ar-SA"}.]{style="font-size:18px;"}

[[[بانتهاء هذه المرحلة سيكون لدينا وثائق بإحدى اللغات الطبيعية ]{lang="ar-SY"}]{lang="ar-SA"}([[عربية، إنكليزية،]{lang="ar-SY"}]{lang="ar-SA"}...) [[نضع فيها أهم النقاط التي وجدناها في هذا المجال بالإضافة لوثائق أخرى على شكل أسئلة للأمور التي تكون غير واضحة بالنسبة لنا]{lang="ar-SY"}]{lang="ar-SA"}.]{style="font-size:18px;"}

 

[[**الخطوة**]{lang="ar-SY"}[ ]{lang="ar-SY"}[**الثانية**]{lang="ar-SY"}[ ]{lang="ar-SY"}[**جمع**]{lang="ar-SY"}[ ]{lang="ar-SY"}[**متطلبات**]{lang="ar-SY"}[ ]{lang="ar-SY"}[**النظام**]{lang="ar-SY"}[ ]{lang="ar-SY"}]{lang="ar-SA"}**Business Requirement:**

[[[هنا سنقوم بعمل مقابلات مع الأشخاص المسؤولين عن البرنامج المراد تصميمه بالطبع ستكون الوثائق التي نتجت عن المرحلة السابقة محور حديثنا، طبعاً لا ننسى أن للمقابلة آداب بالإضافة لاختيار الأسئلة بعناية ]{lang="ar-SY"}]{lang="ar-SA"}([[سيتم طرح مقالة خاصة عن المقابلات لاحقاً]{lang="ar-SY"}]{lang="ar-SA"}).[[سننتهي من هذه الخطوة لينتج لدينا توصيف –أيضا بأحد اللغات الطبيعية – لتفاصيل عمل النظام المطلوب]{lang="ar-SY"}]{lang="ar-SA"}.]{style="font-size:18px;"}

  
 

[[**الخطوة**]{lang="ar-SY"}[ ]{lang="ar-SY"}[**الثالثة**]{lang="ar-SY"}[ ]{lang="ar-SY"}[**رسم**]{lang="ar-SY"}[ ]{lang="ar-SY"}[**مخططات**]{lang="ar-SY"}[ ]{lang="ar-SY"}[**معيارية**]{lang="ar-SY"}[ ]{lang="ar-SY"}]{lang="ar-SA"}**UML:**

[[[بعد الانتهاء من مرحلة جمع المتطلبات علينا أن نقوم بترجمة هذه المتطلبات للغة معيارية تكون مفهومة من قبل المبرمجين من جهة ومن قبل مستخدمي النظام من جهة ثانية، هنا سنقوم برسيم مخططات ]{lang="ar-SY"}]{lang="ar-SA"}UML [[لتوصيف عمل النظام وأهم هذه المخططات هم ]{lang="ar-SY"}]{lang="ar-SA"}Class Diagram , Usecase , Sequence.]{style="font-size:18px;"}

[[[مخطط حالات الاستخدام ]{lang="ar-SY"}]{lang="ar-SA"}Usecase Diagram : [[يمثل تفاعل المستخدم مع النظام، يمكن لهذا المخطط ان يوضع الطرق المختلفة لتفاعل المستخدمين مع النظام]{lang="ar-SY"}]{lang="ar-SA"}.]{style="font-size:18px;"}

[[[مخطط الأصناف ]{lang="ar-SY"}]{lang="ar-SA"}Class Diagram : [[احد المخططات الساكنة التي تصف بنية النظام بإظهار أصناف النظام ]{lang="ar-SY"}]{lang="ar-SA"}Classes[[، خصائصه ]{lang="ar-SY"}]{lang="ar-SA"}Attributes [[عملياته ]{lang="ar-SY"}]{lang="ar-SA"}Operations [[والعلاقات بين الأصناف]{lang="ar-SY"}]{lang="ar-SA"}.]{style="font-size:18px;"}

[[[مخطط التتابع ]{lang="ar-SY"}]{lang="ar-SA"}Sequence: [[يوضح كيفية إنجاز وظائف النظام خطوة بخطوة وبترتيب زمني، بكلام آخر يوضح سيناريو إنجاز وظيفة ما، يتم رسم هذا المخطط للوظائف المعقدة]{lang="ar-SY"}]{lang="ar-SA"}]{style="font-size:18px;"}

[[[تعطي المخططات المعيارية صورة واضحة عن النظام وتشكل جسر بين الزبون وبينك]{lang="ar-SY"}]{lang="ar-SA"}.]{style="font-size:18px;"}

  
 

[[[**الخطوة**]{lang="ar-SY"}[ ]{lang="ar-SY"}[**الرابعة**]{lang="ar-SY"}[ ]{lang="ar-SY"}[**واجهات**]{lang="ar-SY"}[ ]{lang="ar-SY"}[**المستخدم**]{lang="ar-SY"}[ ]{lang="ar-SY"}]{lang="ar-SA"}**User Interface:**]{style="font-size:18px;"}

[[[في هذه الخطوة سنقوم برسم واجهات قريبة من واجهات نظامنا وذلك من اجل الأقسام الغير واضحة تماما ليتم عرض هذه الواجهات على الزبون]{lang="ar-SY"}]{lang="ar-SA"}.. [[إذا عدنا لمثالنا وهو موقع لإحدى الجامعات سيكون علينا مثلاً رسم واجهة توضح طريقة عرض النتائج الامتحانية وكيفية البحث عن نتيجة ما وفق معايير محددة]{lang="ar-SY"}]{lang="ar-SA"}.]{style="font-size:18px;"}

 

 

[[[نكون بانتهاء هذه الخطوة قد انتهينا من المرحلة الأولى مرحلة التحليل]{lang="ar-SY"}]{lang="ar-SA"}.]{style="font-size:18px;"}

 

================

بقلم: م.رامي عقاد و م.مهند شب قلعية
