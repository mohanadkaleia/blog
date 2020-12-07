Title: كيفية الوصول لكرت الذاكرة في أندرويد 4 من أبونتو
Date: 2013-03-28 07:29
Author: admin
Category: Application, GNULinux, howto
Slug: how-to-properly-mount-android-4-0-devices-in-ubuntu-using-go-mtpfs
Status: published

![Enable-MTP-on-Linux](http://mycodee.com/wp-content/uploads/2013/03/Enable-MTP-on-Linux-300x136.jpg){.aligncenter .size-medium .wp-image-171 width="300" height="136"}

لابد وأن كل من حصل على هاتف أو جهاز لوحي بنظام اندرويد 4 قد لاحظ عدم إمكانية ابونتو من الوصول والتعامل مع الملفات الموجودة في كرت الذاكرة، فعلياً يمكنه فقط عرض الملفات دون القدرة على الحذف أو التعديل والإضافة، والسبب في ذلك هو استخدام اندرويد لنظام نقل الملفات [MTP](http://en.wikipedia.org/wiki/Media_Transfer_Protocol) الغير متوافق مع لينوكس، لذلك ولجعل أبونتو يتمكن من التعامل مع هذا البروتوكل لابد من الاستعانة ببرنامج وسيط، البرنامج الذي تعاملت معه اسمه [**Go-mtpfs**]{style="color:#FF8C00;"}، سأشرح الآن كيفية تنصيبه خطوة خطوة (طبعاً هذا الشرح موجه لأنظمة أبونتو):

> ``` {.western style="margin-left: 0.1in; background-color: transparent; border: none; padding: 0in; line-height: 0.21in; text-align: left;"}
> sudo add-apt-repository ppa:webupd8team/unstable
> sudo apt-get update
> sudo apt-get install go-mtpfs
> ```

والآن بعد أن تم الانتهاء من تنصيب البرنامج سنقوم بإضافة أيقونة له على شريط يونيتي unity luncher كما يلي:

> ``` {.western style="margin-left: 0.1in; background-color: transparent; border: none; padding: 0in; line-height: 0.21in; text-align: left;"}
> sudo apt-get install go-mtpfs-unity
> ```

والآن كل شيء أصبح جاهزاً، يجب أن يظهر على شريط يونتي أيقونة البرنامج كما في الصورة التالية:

[![go-mtpfs-quicklists\_thumb](http://mycodee.com/wp-content/uploads/2013/03/go-mtpfs-quicklists_thumb-300x157.png){.aligncenter .size-medium .wp-image-176 width="300" height="157"}](http://mycodee.com/wp-content/uploads/2013/03/go-mtpfs-quicklists_thumb.png)

لتشغيل البرنامج قم بوصل هاتفك أو جهازك اللوحي بالكمبيوتر وبعدها قم بالنقر بالزر الأيمن على أيقونة البرنامج واختر mount android devices، ستظهر لك رسالة تخبرك بنجاح العملية وسيظهر لك مجلد جديد أو سواقة جديدة اسمها my android يوجد بداخلها محتويات ذاكرة جهازك، كما في الصورة التالية:

[![go-mtpfs-nautilus](http://mycodee.com/wp-content/uploads/2013/03/go-mtpfs-nautilus-300x194.png){.aligncenter .size-medium .wp-image-177 width="300" height="194"}](http://mycodee.com/wp-content/uploads/2013/03/go-mtpfs-nautilus.png)

تهانينا الآن يمكنك الإضافة أو الحذف كما تريد :)

 

> ملاحظة:
>
> تم تجربة هذا الحل على أبونتو 12.04 مع samsung galaxy tab2.

المصدر:

<http://www.webupd8.org/2012/12/how-to-mount-android-40-ubuntu-go-mtpfs.html>
