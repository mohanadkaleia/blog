Title: Create view error - permission denied
Date: 2014-06-03 22:06
Author: mohanad
Category: Database
Slug: create-view-error-permission-denied
Status: published

مرحباً أصدقائي .. 

من فترة كنت عبعمل استيراد لقاعدة بيانات mysql من خلال phpmyadmin على الاستضافة.. وإذا بيطلع خطأ [command denied to user]{style="color: rgb(0, 0, 0); font-family: monospace; font-size: 11px; line-height: normal; background-color: rgb(255, 192, 203);"}

[هي المشكلة بتظهر عند الرغبة باستيراد view.. شو سبب المشكلة مابعرف.. بس بعرف شلون الحل :)]{style="font-size: 13px;"}

[الحل بملف sql بتبحث عن ]{style="font-size: 13px;"}DEFINER = \`root\`@\`localhost\` وبتحذفه..

جرب مرة تانية تعمل استيراد .. اوك مشي الحال..
