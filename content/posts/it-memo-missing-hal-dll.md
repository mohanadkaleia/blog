Title: مذكرات IT - مشكلة في أقلاع ويندوز xp الملف hal.dll
Date: 2013-06-15 19:57
Author: admin
Category: maintenance, windows xp
Slug: it-memo-missing-hal-dll
Status: published

[![ITvenn](http://mycodee.com/wp-content/uploads/2013/06/ITvenn-300x208.png){.aligncenter .size-medium .wp-image-280 width="300" height="208"}](http://mycodee.com/wp-content/uploads/2013/06/ITvenn.png)

[بقلم: م.مهند شب قلعية]{style="background-color:#D3D3D3;"}

في هذه السلسلة سأقوم بطرح جميع المشاكل التي واجهتني في عملي كمهندس حواسيب في إحدى الشركات وكيفية حلها. وسيتم طرح المشكلة وفق تصانيف محددة، هذا العمل هو جزء من مقالات حلول كومبيوتك [Computech](http://computech-sy.com) solution حيث يمكن أن تجد هذه المقالة مكتوبة في موقع كومبيوتك أيضاً.

[[ماهي المشكلة:]{.underline}]{style="color:#FF8C00;"} 
-----------------------------------------------------

في ويندوز XP وعند الأقلاع تظهر رسالة بأنه يوجد ملف ناقص هو hal.dll، كما في الصورة التالية:

[![windowsxpsp2\_virtualpc](http://mycodee.com/wp-content/uploads/2013/06/windowsxpsp2_virtualpc.jpg){.aligncenter .size-full .wp-image-281 width="520" height="86"}](http://mycodee.com/wp-content/uploads/2013/06/windowsxpsp2_virtualpc.jpg)

> Windows could not start because the following file is missing or currupted:
>
> \<windows root\>\\system32\\hal.dll
>
> please re-install a copy of the above file

 

[[شرح المشكلة:]{.underline}]{style="color:#FF8C00;"} 
----------------------------------------------------

يمكن أن يتسبب في هذه المشكلة فيروس ما، حيث يتعثر الوصول للملف hal.dll خاصة وفعلياً ما حدث معي هو عدم القدرة على الوصول للقرص c بالكامل، حتى مع محاولاتي للدخول على القرص من خلال قرص UBUNTU إقلاعي إلا أن جميع المحاولات تفشل حيث يظهر رسالة تفيد في أنه غير ممكن الوصول للقرص.

 

[[كيفية حل المشكلة:]{.underline}]{style="color:#FF8C00;"} 
---------------------------------------------------------

بعد العديد من المحاولات الفاشلة توصلت لحل المشكلة كما يلي:

1.  ضع قرص Windows xp في السواقة.

2.  قم بالإقلاع من السواقة.

3.  نختار خيار Repair.

4.  بعد الوصول لسطر الأوامر الخاص بعملية الإصلاح repair prompt command line، نكتب التعليمة التالية:

    ``` {style="font-family: inherit; margin-top: 1.5em; margin-bottom: 1.5em; margin-left: 3em; padding: 0px; text-decoration: inherit; white-space: pre-wrap; line-height: 18px;"}
    chkdsk /r
    ```

5.  مهمة هذه التعليمة هي إصلاح واسترجاع الملفات المعطوبة، بعد الانتهاء من عملية الاسترجاع قم بكتابة تعليمة **exit**.

6.  أخرج قرص الويندوز من السواقة وقم بالإقلاع من الهارد.

7.  تهانينا لقد تم حل المشكلة.

في حال لم ينجح الحل قم بكتابة تعليق كي أتمكن من مساعدتك في حل المشكلة.

في رعاية الله.

 
