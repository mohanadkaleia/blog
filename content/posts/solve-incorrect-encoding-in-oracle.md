Title: حل مشكلة ظهور اللغة العربية "؟؟؟" في أوراكل 
Date: 2011-04-08 23:41
Author: admin
Category: Database
Slug: solve-incorrect-encoding-in-oracle
Status: published

السلام عليكم ورحمة الله وبركاته.

**شرح المشكلة :**

المشكلة تحدث عند إدخال أو قراءة المعلومات في أوراكل XE حيث تظهر اللغة العربية بشكل ???? غير مقروءة.

**حل المشكلة بإذن الله:**

1.  **تحميل نسخة Oracle XE universal لكي تدعم الترميز العربي ، حيث يمكن تحميلها من موقع أوراكل (بالنسبة للسوريين يمكن تحميلها من موقع www.no403.net).**
2.  **ضبط خيارات اللغة للنظام المضيف كالتالي:**
    1.  من لوحة التحكم --\> خيارات إقليمية :[![](../../static/images/solve-incorrect-encoding-in-oracle/regional-option.png "regional option")](../../static/images/solve-incorrect-encoding-in-oracle/regional-option.png)
    2.  نقوم بإضافة اللغة العربية كما في الصورة التالية :[![](../../static/images/solve-incorrect-encoding-in-oracle/1-1.png "1.1")](../../static/images/solve-incorrect-encoding-in-oracle/1-1.png)
    3.  بعدها من التبويبة advanced نقوم بإضافة ترميز اللغة العربية للنظام كما في الصورة التالية:[![](../../static/images/solve-incorrect-encoding-in-oracle/22.png "2")](../../static/images/solve-incorrect-encoding-in-oracle/22.png)
    4.  بعدها من التبويبة language :[![](../../static/images/solve-incorrect-encoding-in-oracle/3.png "3")](../../static/images/solve-incorrect-encoding-in-oracle/3.png)
    5.  بعدها من details نقوم بتفعيل خيار compatibility configuration  كما في الصورة التالية :[![](../../static/images/solve-incorrect-encoding-in-oracle/4.png "4")](../../static/images/solve-incorrect-encoding-in-oracle/4.png)
3.  **تغيير خيار اللغة في الريجيستيري nls\_lang:**
    1.  من القائمة إبدأ - Run نقوم بكتابة regedit كما في الصورة:[![](../../static/images/solve-incorrect-encoding-in-oracle/reg-edit.png "reg edit")](../../static/images/solve-incorrect-encoding-in-oracle/reg-edit.png)
    2.  [![](../../static/images/solve-incorrect-encoding-in-oracle/regedit2.png "regedit2")](../../static/images/solve-incorrect-encoding-in-oracle/regedit2.png)[![](../../static/images/solve-incorrect-encoding-in-oracle/regedit3.png "regedit3")](../../static/images/solve-incorrect-encoding-in-oracle/regedit3.png)وبعدها نقوم بالبحث عن nls\_lang وتغييرها من  AMERICAN\_AMERICA.WE8MSWIN1256 إلى القيمة AMERICAN\_AMERICA.AR8MSWIN1256[![](../../static/images/solve-incorrect-encoding-in-oracle/regeidt4.png "regeidt4")](../../static/images/solve-incorrect-encoding-in-oracle/regeidt4.png)[![](../../static/images/solve-incorrect-encoding-in-oracle/regedit5.png "regedit5")](../../static/images/solve-incorrect-encoding-in-oracle/regedit5.png)
4.  **كتابة التعليمة التالية في الـ cmd:**  
   `set nls_lang=american_america.ar8mswin1256`
5.  **في حال التعامل مع القاعدة من خلال لغات مثل php يجب التأكد من أن يكون الترميز المكتوب به الصفحات هو UTF8 with out bom.**

والآن بإذن الله ستكون مشكلة اللغة العربية قد حلت..

أرجو أن أكون قد وفقت في طرح الموضوع..

 
