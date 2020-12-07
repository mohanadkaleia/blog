Title: How to steup XAMP with MSSQL server
Date: 2015-10-03 21:53
Author: mohanad
Category: Code, howto, Servers
Slug: how-to-steup-xamp-with-mssql-server
Status: published

تحتاج للترجمة للعربية، ولكن جربتها وهي ناجحة:

المصدر:

http://samalpramod.blogspot.com/2014/03/connect-sql-server-2008-from-xampp.html

https://gist.github.com/mycodee/f1616d3ff7cecdf90fb9

 

Troubleshoot

1\. ظهرت لي مشكلة بعد ان قمت بتضمين الملفات لم يعمل فكان الحل بتنصيب odbc نسخة 64 بت 

https://www.microsoft.com/en-us/download/details.aspx?id=36434

2\. ظهرت مشكلة ثانية هي أن من سطر الأوامر يظهر أن تعليمة الاتصال مع قاعدة البيانات غير معرفة .. سبب المشكلة ان ملف الاعدادات php.ini الخاص بسطر الاوامر غيره المستخدم من قبل المتصفح .. الحل يجب إضافة ملف الاعدادات إلى متغيرات النظام system environment Path

 
