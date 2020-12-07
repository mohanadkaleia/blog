Title: SQL Group BY
Date: 2014-06-30 18:59
Author: mohanad
Category: Database
Tags: group by, SQL
Slug: sql-group-by
Status: published

[![sql](http://mycodee.com/wp-content/uploads/2014/06/sql.png){.aligncenter .size-full .wp-image-429 width="256" height="256"}](http://mycodee.com/wp-content/uploads/2014/06/sql.png)معظم البرامج اليوم تستخدم قواعد البيانات لحفظ البيانات، طبعاً لابد عزيزي القارئ في حال وصولك لهذه المقالة أنك تعرف ولو قليلاً عن لغة التعامل مع قواعد البيانات **SQL**، لن أتحدث في هذه المقالة عن الاستعلامات البسيطة وإنما سأتحدث عن **GROUP BY** ماهي وكيف يمكن أن تفيدنا وكيف يمكننا استعمالها.. 

[السيناريو المقترح]{style="color:#000080;"} 
-------------------------------------------

لنفترض أن لدينا جدول يمثل معلومات موظفين في شركة، اسم الموظف - القسم التابع له - الراتب الشهري، الصورة التالية تمثل جزء من البيانات في هذا الجدول:

[![employee](http://mycodee.com/wp-content/uploads/2014/06/employee.png){.aligncenter .size-full .wp-image-430 width="774" height="132"}](http://mycodee.com/wp-content/uploads/2014/06/employee.png)

حسناً فرضاً أردنا الحصول على متوسط رواتب كل قسم باستعلام واحد، كيف يمكننا فعل ذلك!! .. لو فكرنا قليلاً ما يجب علينا فعله هو أن نقوم بتجزئة هذه النتائج (المجموعة الكبيرة) إلى مجموعة من النتائج الجزئية وفقاً للقسم وبعدها نقوم بتطبيق عملية **AVG** المتوسط الحسابي على حقل الراتب وذلك بالنسبة لكل مجموعة جزئية أي بالنسبة لكل قسم.. ولكن كيف يمكننا فعل ذلك.

[تابع التجميع Group BY]{style="color:#000080;"} 
-----------------------------------------------

يمكننا تابع التجميع Group by من تجميع النتائج في مجموعات جزئية وتطبيق عملية ما على هذه المجموعات الجزئية، ما نريده هنا هو تجميع النتائج بالنسبة لماذا؟ بالنسبة لحقل القسم **department**، وتطبيق عملية المتوسط الحسابي على حقل الراتب، سنرى كيف نقوم بذلك في الاستعلام التالي:

[![employee](http://mycodee.com/wp-content/uploads/2014/06/employee1.png){.aligncenter .size-full .wp-image-434 width="774" height="132"}](http://mycodee.com/wp-content/uploads/2014/06/employee1.png)

> Select departmet , AVG(salary) as dept\_salary
>
> from employee
>
> Group By department

نلاحظ هنا كيف قمنا بالبداية بالاستعلام عن اسم القسم واستخدمنا عملية المتوسط الحسابي AVG على حقل الراتب Salary، وفي آخر الاستعلام قمنا بتجميع النتائج على حقل department.. والنتيجة عند تنفيذ هذا التابع هي:

[![dept\_salary](http://mycodee.com/wp-content/uploads/2014/06/dept_salary.png){.aligncenter .size-full .wp-image-432 width="392" height="75"}](http://mycodee.com/wp-content/uploads/2014/06/dept_salary.png)

نلاحظ في التنائج كيف تم تجميع الجدول الكبير فقط على الأقسام، وإظهار المتوسط الحسابي لرواتب كل قسم على حدا..

 

سهلة وممتعة، وليست معقدة كما يعتقد البعض ومفيدة جداً في كثير من الحالات..  

ملاحظة إن **Group By** لا تتحسس لأسماء الحقول المستعارة  **alias** لذلك يجب تمرير الاسم كما هو
