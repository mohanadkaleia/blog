Title: Cross Compilation of QT/C++ application for Windows under Linux
Date: 2016-07-25 18:58
Author: mohanad
Category: Code, howto
Tags: C++, cross-platform, mxe, qt, qt creator, windows
Slug: cross-compilation-of-qtc-application-for-windows-under-linux
Status: published
Direction: rtl

السلام عليكم ورحمة الله

من المعروف أن لغة C++ هي من بين اللغات التي يمكن أن تعمل على مختلف أنظمة التشغيل .. والتي تسمى cross-platform language، حيث يمكنك ان تقوم بكتابة برنامج وبناءه ليعمل على نظام تشغيل Windows و Linux وحتى على الموبايل..

في هذه المقالة سأشرح كيف نقوم ببناء مشروع QT based application على نظام Ubuntu بحيث يعمل على نظام Windows

## الأدوات المستخدمة

-   نظام التشغيل Ubuntu 16.04
-   بيئة التطوير: Qt Creator 4.0.3 Based on Qt 5.7.0
-   معمارية المعالج: Intel 64bit
-   أداة الترجمة التي سيتم استخدامها: MXE
-   نظام التشغيل الهدف Windows 10 64bit
-   C++11

## تنصيب أدارة الترجمة

قبل أن نقوم بتنصيب الأداة لنأخذ لمحة عنها، MXE هي أداة تستعمل مترجم Mingw لترجمة المكتبات والبرامج على مختلف بيئات وأنظمة التشغيل. تعمل هذه الأداة على أنظمة تشغيل Unix.

الآن لتنصيب الأداة لنقم بالبداية بتحميلها، ملاحظة أنا أفضل أن يتم تحميل الأداة مباشرة في مكان التنصيب، عندي أفضل تنصيبه ضمن مجلد /opt

```
git clone https://github.com/mxe/mxe.git
```

الآن قبل أن نقوم بعملية التنصيب علينا أن نقوم بتنصيب جميع الاعتماديات اللازمة:

```
apt-get install autoconf automake autopoint bash bison bzip2 flex gettext git g++ gperf intltool libffi-dev libgdk-pixbuf2.0-dev libtool libltdl-dev libssl-dev libxml-parser-perl make   
openssl p7zip-full patch perl pkg-config python ruby scons sed unzip wget xz-utils

apt-get install g++-multilib libc6-dev-i386

apt-get install libtool-bin
```
 

الآن علينا أن نقوم ببناء الأداة كما يلي:

```
cd mxe && make MXE_TARGETS=x86_64-w64-mingw32.static qt5
```

الآن علينا تضمين مسار مجلد البرامج التنفيذية bin لمتحول البيئة PATH كما يلي:

> ``` {.prettyprint}
> export PATH=/opt/mxe/usr/bin:$PATH
> ```

 

[قم ببناء برنامجك الآن ]{style="color: #800080;"} {#قم-ببناء-برنامجك-الآن dir="rtl"}
-------------------------------------------------

الآن كل شيء أصبح جاهز لنقوم ببناء برنامجنا ليعمل على بيئة ويندوز، سأفترض أنه لديك برنامج جاهز لعملية البناء، كل ما عليك فعله الآن هو أن تقوم بالذهاب إلى مسار برنامجك، وتوليد ملف make كمايلي:

> ``` {.prettyprint}
> /opt/mxe/usr/bin/x86_64-w64-mingw32.static-qmake-qt5
> ```

هل كل شيء سار على مايرام؟ الآن قم بتنفيذ تعليمة make:

> ``` {.prettyprint}
> make
> ```

لا يوجد أخطاء؟ رائع! .. الآن برنامج التنفيذي أصبح جاهز وموجود ضمن مجلد release، يمكنك تجربته على بيئة ويندوز، أو يمكن مباشرة أن تقوم بتجربته من خلال المحاكي Wine

 

في حال وجود استفسارات أرجو ترك رد.. بالتوفيق

 

[**المصادر:**]{.underline}

http://stackoverflow.com/questions/14170590/building-qt-5-on-linux-for-windows/14170591

http://www.neologix.ae/cross-platform.html

http://mxe.cc/
