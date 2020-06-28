Title: Why can't install OSx on PC
Date: 2015-07-19 12:36
Author: mohanad
Category: Uncategorized
Tags: install, intel, osx, PC, pwoerPC, System managment controller
Slug: why-cant-install-osx-on-pc
Status: published

![](http://www.winbeta.org/sites/default/files/news/BootcampWindows.jpg){.aligncenter width="744" height="399"}

هل تحب تجربة نظام التشغيل OSX ولكن ليس لديك ماكنتوش .. هل حاولت تنصيبه على جهازك PC؟ .. هل فشلت في تنصيبه؟!.. 

سأخبرك عزيزي القارئ لم تنصيب نظام التشغيل OSX صعب جداً على الحواسيب الشخصية PC .. 

> ### [OSX supporting intel]{style="color:#A9A9A9;"} 
>
> نعم هذا صحيح الآن أجهزة الماكنتوش تأتي بمعالجات انتل .. (حيث كانت من قبل تأتي مدعومة بمعالج PowerPC) .. ولكن حتى بعد أن تم دعم معالجات انتل المماثلة لمعالج جهازك عزيزي القارئ إلا أنه لا يزال تنصيب النظام صعب جداً .. ولكنه أعطى بعض الأمل للGeeks .. 

السبب وراء ذلك أن أنظمة أبل تقوم بفحص وجود شريحة خاصة وفي حال عدم وجودها فإن النظام لا يقوم بمتعابعة التنصيب أو الإقلاع، بشكل أدق فإن هذه العملية مقادة بواسطة [System Managment Controller](https://en.wikipedia.org/wiki/System_Management_Controller)، بشكل عام فإن SMC مسؤول عن عدة مهام .. مثل التحكم بالتبريد .. عمليات Sleep wake .. وأيضاً بالإضافة للتحقق من أن الهارد وير الذي يعمل عليه هو هارد وير خاص من أبل.

طبعاً بالإضافة أيضاً إلى أن دعم نظام OSX لتعاريف القطع محدود جداَ من كروت الشاشة .. وتعاريف كرت الصوت وغيره مما يزيد من صعوبة الأمر.

[الحلول البديلة]{style="color:#800080;"} 
----------------------------------------

طبعاً يوجد حلول بديلة اليوم تمكنك من تشغيل نظام الماك على جهازك الشخصي، وإحدى أسهل هذه الحلول هي باستخدام المحاكي Virtual Machine والذي يقوم بتهيئة بيئة عمل مماثلة لأجهزة الماكنتوش بحيث يمكن تنصيب نظام OSX عليها .. 

ولقد قمت مسبقاً بكتابة مقالة عن كيفية تنصيب نظام يمكنك مشاهدتها من هنا:

<http://mycodee.com/how-to-install-mac-on-vmware/>

أيضاً يمكن تجربته تنصيب Hackintosh ومتابعة مقالاتهم عن كيفية تنصيبه .. 

<http://www.hackintosh.com/>

 

المصادر:

http://www.howtogeek.com/178031/why-is-it-still-so-difficult-to-install-os-x-on-pcs/

https://en.wikipedia.org/wiki/System\_Management\_Controller

 
