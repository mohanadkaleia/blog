Title: You might not have permission to use this network resource
Date: 2013-07-24 15:29
Author: admin
Category: maintenance, Servers
Slug: you-might-not-have-permission-to-use-this-network-resource
Status: published

[![ITvenn](../../static/images/you-might-not-have-permission-to-use-this-network-resource/ITvenn-300x208.png){.aligncenter .size-medium .wp-image-280 width="300" height="208"}](../../static/images/you-might-not-have-permission-to-use-this-network-resource/ITvenn.png)

[بقلم: م. مهند شب قلعية]{style="background-color:#D3D3D3;"}

قبل البدء بالحديث عن المشكلة أحب أن أوضح بنية الشبكة الموجودة، الشبكة تتألف من سيرفر Windows server 2008 وأجهزة clients تتنوع أنظمتها بين windows 7 و windows xp، طبعاً يوجد Domain controller و active directory، للتحكم بالمستخدمين وصلاحياتهم على المجلدات.

[[ماهي المشكلة؟!!]{style="font-size:20px;"}]{style="color:#FF8C00;"} 
====================================================================

[المشكلة التي ظهرت هي عدم قدرة أحد الأجهزة بنظام ويندوز 7 على الوصول لموارد السيرفر من المجلدات المشاركة مع العلم أن الجهاز يستطيع الوصول للسيرفر من خلال عملية ping سواء للعنوان المنطقي أو لاسم السيرفر، ويمكن لهذا الجهاز الوصول لموارد الشبكة الأخرى غير السيرفر مثل الوصول للمجلدات المشاركة على أجهزة أخرى.]{style="font-size: 13px;"}

[ملاحظة في اللحظات الأولى لإقلاع الجهاز يمكنه الوصول لموارد السيرفر، ولكن بعد دقائق لا يعود قادر على الوصول وتظهر رسالة الخطأ التالية:]{style="font-size: 13px;"}

[![8117.SNAGHTML127e72fe\_thumb\_7E43F3AC](../../static/images/you-might-not-have-permission-to-use-this-network-resource/8117.SNAGHTML127e72fe_thumb_7E43F3AC-e1374668502566.png){.aligncenter .size-full .wp-image-324 width="600" height="195"}](../../static/images/you-might-not-have-permission-to-use-this-network-resource/8117.SNAGHTML127e72fe_thumb_7E43F3AC.png)

[حل المشكلة:]{style="color:#FF8C00;"} 
=====================================

بداية قم بإيقاف firewall سواء من مضاد الفايروسات أو الافتراضي الموجود في ويندوز. فربما تكون المشكلة في الفايروول، في حال لم ينجح الأمر قم بمشاهدة الفيديو التالي، فيه الطريقة التي نجحت معي لحل هذه المشكلة:

 

 

هل تم حل المشكلة؟!!  تهانينا :)

في حال لم يتم حل المشكلة لا تيأس قم بوضع تعليق فيمكن أن أستطيع مساعتدك.
