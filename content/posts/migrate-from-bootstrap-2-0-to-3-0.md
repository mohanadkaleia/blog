Title: الانتقال من Bootstrap النسخة الثانية للثالثة
Date: 2014-05-04 20:36
Author: mohanad
Category: Design, Website
Slug: migrate-from-bootstrap-2-0-to-3-0
Status: published

[![bootstrap\_logo](../../static/images/migrate-from-bootstrap-2-0-to-3-0/bootstrap_logo-300x64.png)](../../static/images/migrate-from-bootstrap-2-0-to-3-0/bootstrap_logo.png)

هل قمت باستخدام Bootstrap 2 في إحدى تصميماتك؟ نعم لقد تم إطلاق Bootstrap بنسخة الثالثة ويوجد الكثير من التغييرات، ولا يكفي فقط تضمين النسخة الجديدة، بل عليك أن تقوم بتعديل ملفاتك لكي تتمكن من الانتقال للنسخة الجديدة.. في هذه المقالة سوف أتحدث عن كيفية الانتقال من النسخة الثانية للنسخة الثالثة من [Bootstrap](http://getbootstrap.com).

بشكل عام الهدف الأساسي من Bootstrap هي قابلية التقييس حسب حجم شاشة العرض المستخدمة، من شاشات الموبايل لشاشات التابلت انتهاء بشاشات الحواسيب الكبيرة واللابتوب.

[![Screenshot from 2014-05-04 21:14:02](../../static/images/migrate-from-bootstrap-2-0-to-3-0/Screenshot-from-2014-05-04-211402-1024x118.png)](../../static/images/migrate-from-bootstrap-2-0-to-3-0/Screenshot-from-2014-05-04-211402.png)

ماذا أفعل؟!!
--------------------------------------

سنرى الآن كيف ماهي التغييرات التي يجب أن نعدلها حتى ننتقل من النسخة الثانية للثالثة، بشكل عام ما يهمك عزيزي القارئ هو ما هي أسماء الكلاسات التي تم استبدالها وتنسيقها وبما يجب عليك أن تستبدلها، الجدول التالي فيه كل صنف من النسخة الثانية وماهو الصنف الجديد الذي يجب أن تستبدله به:

  Bootstrap 2.x (القديم)                                                                                                                                                                                                                                                                                                                                                   Bootstrap 3.0 (الجديد)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `.container-fluid`   `.container`
  `.row-fluid`         `.row`
  `.span*`             `.col-md-*`
  `.offset*`           `.col-md-offset-*`
  `.brand`             `.navbar-brand`
  `.hero-unit`         `.jumbotron`
  `.icon-*`            `.glyphicon .glyphicon-*`
  `.btn`               `.btn .btn-default`
  `.btn-mini`          `.btn-xs`
  `.btn-small`         `.btn-sm`
  `.btn-large`         `.btn-lg`
  `.visible-phone`     `.visible-sm`
  `.visible-tablet`    `.visible-md`
  `.visible-desktop`   `.visible-lg`
  `.hidden-phone`      `.hidden-sm`
  `.hidden-tablet`     `.hidden-md`
  `.hidden-desktop`    `.hidden-lg`
  `.input-small`       `.input-sm`
  `.input-large`       `.input-lg`
  `.input-prepend`     `.input-group`
  `.input-append`      `.input-group`
  `.add-on`            `.input-group-addon`
  `.btn-navbar`        `.navbar-btn`
  `.thumbnail`         `.img-thumbnail`
  `ul.inline`          `.list-inline`

  
-

هل قمت بالاستبدال؟!! تهانينااااااا الآن أنت انتقلت بشكل كامل من Bootstrap2 إلى bootstrap3، والآن انتقل لصفحة [bootstrap](http://getbootstrap.com/) لتشاهد الميزات الجديدة وتبدأ باستخدامها في تصميمك.

 
