Title: Oracle TNS Listener service not starting
Date: 2014-03-08 21:44
Author: mohanad
Category: Database, maintenance, Servers
Tags: host name, oracle, TNS listener, XE
Slug: oracle-tns-listener-service-not-starting
Status: published

![Oracle\_Database](http://mycodee.com/wp-content/uploads/2014/03/Oracle_Database-150x150.jpg){.aligncenter .size-thumbnail .wp-image-361 width="150" height="150"}

من فترة صادفتني مشكلة عند تعاملي مع قاعدة البيانات أوراكل، قبل أن أبدأ النسخة التي أعمل عليها هي oracle XE 10g، المشكلة هي أنني لا استطيع الاتصال بقاعدة البيانات ولا حتى فتح واجهة الإدارة من المتصفح!!

المشكلة حدثت بالضبط بعد أن قمت بتغيير اسم السيرفر، وهذه هي المشكلة، فعلياً إعدادات الأوراكل ترتبط باسم السيرفر الذي تعمل عليه، وفي حال تغير هذا الاسم يجب عندها أن نقوم بتغييره أيضاً من ملف الإعدادات الخاص بأوراكل وإلا فإن الخدمة Oracle TNS service لن تعمل أبداً، وهي الخدمة المسؤولة عن الاستماع لطلبات قاعدة البيانات.

الآن سنتعلم طريقة إصلاح هذه المشكلة:

1.  قم بفتح موجه الأوامر CMD
2.  قم بكتابة التعليمة التالية: lsnrctl
3.  والآن قم بكتابة start

هذه التعليمات مسؤولة عن تشغيل الخدمة TNS listener وفي حال حدوث خطأ كما هو الحال عندي فيجب أن تظهر الرسالة التالية:

> ``` {style="border: 0px; font-family: 'Courier 10 Pitch', Courier, monospace; font-size: 13px; margin-top: 0px; margin-bottom: 1.625em; outline: 0px; padding: 0.75em 1.625em; vertical-align: baseline; background-color: rgb(244, 244, 244); line-height: 1.5; overflow: auto; color: rgb(55, 55, 55); text-align: left;"}
> LSNRCTL> start
> System parameter file is
>   C:\oracle\product\10.2.0\db_1\network\admin\listener.ora
> Error listening on:
>   (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=wrong_name)(PORT=1521)))
> TNS-12545: Connect failed because target host or object does not exist
>  TNS-12560: TNS:protocol adapter error
>   TNS-00515: Connect failed because target host or object does not exist
>     32-bit Windows Error: 1004: Unknown error
> ```

الآن لو ظهرت معك رسالة شبيهة فيمكن حل هذه المشكلة من خلال تعديل الملف:

[C:\\oracle\\product\\10.2.0\\db\_1\\network\\admin\\listener.ora]{style="color: rgb(55, 55, 55); font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 15px; line-height: 24px;"}

بحيث يصبح في حقل Host اسم السيرفر الصحيح:

> ``` {style="border: 0px; font-family: 'Courier 10 Pitch', Courier, monospace; font-size: 13px; margin-top: 0px; margin-bottom: 1.625em; outline: 0px; padding: 0.75em 1.625em; vertical-align: baseline; background-color: rgb(244, 244, 244); line-height: 1.5; overflow: auto; color: rgb(55, 55, 55); text-align: left;"}
> LISTENER =
>   (DESCRIPTION_LIST =
>     (DESCRIPTION =
>       (ADDRESS = (PROTOCOL = TCP)(HOST = good.betweengo.com)(PORT = 1521))
>       (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC0))
>     )
>   )
> ```

الآن قم بإعادة تشغيل الأوراكل وقم بتشغيل خدمة TNS lisener .. تهانينا لقد عادت للعمل من جديد :)
