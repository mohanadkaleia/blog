Title: How to solve winload.exe missing problem
Date: 2014-07-14 18:47
Author: mohanad
Category: howto, maintenance, Servers
Tags: boot, missing, windows server 2008, winload.exe
Slug: how-to-solve-winload-exe-missing-problem
Status: published

[![winload\_exe\_vista\_missing\_or\_corrupt](http://mycodee.com/wp-content/uploads/2014/07/winload_exe_vista_missing_or_corrupt-300x196.jpg){.aligncenter .size-medium .wp-image-439 width="300" height="196"}](http://mycodee.com/wp-content/uploads/2014/07/winload_exe_vista_missing_or_corrupt.jpg)

ظهرت معي مشكلة في سيرفر عليه نظام تشغيل windows server 2008 بأنه لم يعد يقلع وتظهر رسالة خطأ التالية:

> ``` {style="box-sizing: border-box; margin-top: 0px; margin-bottom: 24px; font-family: Menlo, Monaco, Consolas, 'Courier New', monospace; font-size: 13px; white-space: pre-wrap; word-wrap: break-word; line-height: 22px; word-break: break-all; background-color: rgb(247, 247, 247); border: 1px solid rgb(229, 229, 229); padding: 20px; color: rgb(56, 56, 56);"}
> Windows Boot Manager
>
> Windows failed to start. A recent hardware or software change might be the cause. To fix the problem:
>
> 1. Insert your Windows installation disc and restart your computer.
> 2. Choose your language settings, and then click "Next."
> 3. Click "Repair your computer."
>
> If you do not have this disc, contact your system administrator or computer manufacturer for assistance
>
> File: \Windows\system32\winload.exe
>
> Status: 0xc000000f
>
> Info: The selected entry could not be loaded because the application is missing or corrupt
> ```

هذه المشكلة يمكن أن تحدث بسبب انقطاع التيار الكهربائي بشكل مفاجئ على السيرفر، يمكن حلها من خلال الاستعانة بقرص windows server 2008، من خلال الدخول على repaire وإعادة تهيئة بيانات الإقلاع من جديد كما في الخطوات التالية:

1.  قم بإدخال قرص ويندوز windows server 2008 في السواقة.
2.  أعد إقلاع الجهاز وقم بالإقلاع من القرص وذلك من خلال ضبط إعدادات تسلسل الإقلاع في BIOS.
3.  قم بالضغط على خيار **Repaire Your Computer،** وذلك بعد اختيار اللغة والوقت ولوحة المفاتيح.
4.  الآن سيقوم بالبحث عن القرص الموجود عليه نظام التشغيل قم باختياره واضغط next.
5.  قم باختيار Command Prompt.
6.  ثم قم بكتابة التعليمة التالية:

> ``` {style="box-sizing: border-box; margin-top: 0px; margin-bottom: 24px; font-family: Menlo, Monaco, Consolas, 'Courier New', monospace; font-size: 13px; white-space: pre-wrap; word-wrap: break-word; line-height: 22px; word-break: break-all; background-color: rgb(247, 247, 247); border: 1px solid rgb(229, 229, 229); padding: 20px; color: rgb(56, 56, 56);"}
> bootrec /rebuildbcd
> ```

بعد الانتهاء قم بالخروج من خلال كتابة تعليمة exit، وقم بإعادة تشغيل الجهاز.

الآن يجب أن يكون قد تم حل المشكلة، في حال لم تحل المشكلة قم بكتابة تعليق لأقوم بمساعدتك :)
