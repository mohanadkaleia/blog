Title: تضمين خطوط ويندوز في أبونتو
Date: 2011-05-11 12:27
Author: admin
Category: GNULinux
Slug: include-windows-fonts-in-ubuntu
Status: published

**اسم التوزيعة:ubuntuDebian**
**  
تصنيف المشكلة:** خطوط بشعة ![](http://www.alhasebat.net/vb/images/smilies/new/nono.gif "Nono")  
**  
الوصف:  
**يمكن أن يلاحظ من استخدم أنظمة جنو لينوكس أن الخطوط العربية بشعة وقليلة مقارنة بخطوط ويندوز الكثيرة جداً..  
حسناً هل يمكن جعل خطوط لينوكس مثل ويندوز ..  
**  
الحل:**  
نعم حيث يمكننا استيراد خطوط ويندوز نفسها ![](http://www.alhasebat.net/vb/images/smilies/smile.gif "Smile")  
ولفعل ذلك اتبع الخطوات التالية:

1.  إذهب إلى القرص الموجود عليه نظام ويندوز - مجلد windows - انسخ المجلد Fonts
2.  انسخه وقم بوضعه على مسار /home/username
3.  قم بتغيير اسمه إلى :

    .fonts

4\. من التيرمينال نفذ الأمر التالي :

    fc-cache -vf

وهكذا نكون قد ضمّنا خطوط ويندوز..![](http://www.alhasebat.net/vb/images/smilies/055.gif ":aywa:")
