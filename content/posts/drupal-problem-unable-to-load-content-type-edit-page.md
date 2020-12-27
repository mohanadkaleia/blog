Title: دروبال .. مشكلة وحل.. عدم القدرة على تحميل صفحة التعديل في content type
Date: 2013-06-20 16:58
Author: admin
Category: drupal
Tags: edit content type, token tweak
Slug: drupal-problem-unable-to-load-content-type-edit-page
Status: published

[![drupal-logo](../../static/images/drupal-problem-unable-to-load-content-type-edit-page/drupal-logo.gif){.aligncenter .size-full .wp-image-286 width="200" height="200"}](../../static/images/drupal-problem-unable-to-load-content-type-edit-page/drupal-logo.gif)

[بقلم م.مهند شب قلعية.]{style="background-color:#D3D3D3;"}

في هذه السلسلة سأقوم بطرح المشاكل والحلول الذي ظهرت معي وتم حلها عند التعامل مع Drupal، المشكلة التي واجهتني اليوم هي عندما أقوم بالنقر على رابط Edit في أي content type لا يتم تحميل الصفحة بشكل كامل وإنما تظهر على شكل plain text

، كما في الصورة التالية:

[![auto\_nodetitle](../../static/images/drupal-problem-unable-to-load-content-type-edit-page/auto_nodetitle.jpg){.aligncenter .size-full .wp-image-285 width="597" height="457"}](../../static/images/drupal-problem-unable-to-load-content-type-edit-page/auto_nodetitle.jpg)

[الحل:]{style="color:#FF8C00;"} 
-------------------------------

تحدث هذه المشكلة بسبب token module، ملاحظة قد لاتحدث على بعض السيرفرات حيث تحدث فقط عندما تكون الذاكرة المخصصة للدروبال صغيرة الحجم، ولحل هذه المشكلة نقوم بتنصيب [Token tweaks module](https://drupal.org/project/token_tweaks).

بعد الانتهاء من تنصيبه نقوم بالذهاب للقائمة configuration  وبعدها نذهب للخيار token، ونجعل الخيار [limiting the recursion [على القيمة 2.]{style="font-family:arial,helvetica,sans-serif;"}]{style="color: rgb(34, 34, 34); font-family: 'Lucida Grande', 'DejaVu Sans', 'Bitstream Vera Sans', Verdana, Arial, sans-serif; font-size: 13px; line-height: 17.984375px;"}

[[تهانينا لقد تم حل المشكلة، والآن أصبح لديك القدرة على تعديل content type بدون أن تحدث هذه المشكلة.]{style="font-family:arial,helvetica,sans-serif;"}]{style="color: rgb(34, 34, 34); font-family: 'Lucida Grande', 'DejaVu Sans', 'Bitstream Vera Sans', Verdana, Arial, sans-serif; font-size: 13px; line-height: 17.984375px;"}
