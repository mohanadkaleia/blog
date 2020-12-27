Title: كيفية اتصال برنامج جافا بقاعدة البيانات أوراكل
Date: 2011-06-17 22:26
Author: admin
Category: Code, Database
Slug: java-connection-with-oracle
Status: published

[[ربط الجافا مع قاعدة البيانات أوراكل]{style="font-family:AlBattar;"}]{style="color:#c90016;"}

![](http://download.oracle.com/javaee/images/Java_clr_hori.gif "java with oracle database"){.aligncenter width="172" height="121"}

[سنتناول اليوم طريقة ربط برنامج مكتوب بلغة الجافا مع قاعدة البيانات أوراكل ]{style="font-family:Tahoma;"}.

[قبل أن نبدأ علينا أن نعرف أنه لكي يتمكن أي برنامج جافا من الاتصال بقاعدة البيانات أوراكل يجب أن يتوفر ]{style="font-family:Tahoma;"}**driver** [خاص اسمه ]{style="font-family:Tahoma;"}**jdbc** [والذي يهتم بإدارة عمليات الاتصال والاستعلامات وغيرها من العمليات مع القاعدة]{style="font-family:Tahoma;"}.. [المهم يمكن تحميله من موقع أوراكل مباشرة باتباع الرابط التالي واختيار مدير القاعدة المناسب ]{style="font-family:Tahoma;"}:

<http://www.oracle.com/technetwork/database/features/jdbc/index-091264.html>

[[[**الخطوة الأولى** ]{style="font-size:medium;"}]{style="font-family:Tahoma;"}[**-** ]{style="font-size:medium;"}[[**إنشاء مشروع جديد**]{style="font-size:medium;"}]{style="font-family:Tahoma;"}[**:**]{style="font-size:medium;"}]{style="color:#c90016;"}

[لنقم الآن بإنشاء مشروع جديد مثلاً يمكن اختيار ]{style="font-family:Tahoma;"}java application.

[[[**الخطوة الثانية – إضافة وسيط الاتصال**]{style="font-size:medium;"}]{style="font-family:Tahoma;"}[**:**]{style="font-size:medium;"}]{style="color:#c90016;"}

[حيث نقوم بالضغط بالزر اليمين على القائمة ]{style="font-family:Tahoma;"}Library [واختيار “]{style="font-family:Tahoma;"}add jar file” [وبعدها نقوم بإضافة وسيط الربط ]{style="font-family:Tahoma;"}class12.jar.

[![](../../static/images/java-connection-with-oracle/add_library1.png "add_library"){.aligncenter .size-full .wp-image-105 width="238" height="204"}](../../static/images/java-connection-with-oracle/add_library1.png)

[[[**الخطوة الثالثة – كود الاتصال**]{style="font-size:medium;"}]{style="font-family:Tahoma;"}[**:**]{style="font-size:medium;"}]{style="color:#c90016;"}

علينا أولاً أن نقوم باستيراد مكتبة الاتصال كما يلي:

**[import java.sql.\*;]{style="color:#339966;"}**

[لم يتبق لنا الآن سوى كتابة كود الاتصال لكي نتمكن من الاتصال بالقاعدة ]{style="font-family:Tahoma;"}:

**[try{]{style="font-size:small;color:#339966;"}**

**[[// load oracle driver  line 1]{style="color:#3366ff;"}  
]{style="font-size:small;color:#339966;"}**

**[Class.forName("oracle.jdbc.driver.OracleDriver"); [// line 2]{style="color:#3366ff;"}  
]{style="font-size:small;color:#339966;"}**

**[[//connect using Thin driver // line 3]{style="color:#3366ff;"}  
]{style="font-size:small;color:#339966;"}**

**[Connection con = DriverManager.getConnection("jdbc:oracle:thin:\@localhost:1521:xe","hr","hr"); [// line 4]{style="color:#3366ff;"}  
]{style="font-size:small;color:#339966;"}**

**[System.out.println("Connected Successfully To Oracle");[ // line  5]{style="color:#3366ff;"}  
]{style="font-size:small;color:#339966;"}**

**[Statement stmt = con.createStatement();[ // line 6]{style="color:#3366ff;"}  
]{style="font-size:small;color:#339966;"}**

**[ResultSet rset = stmt.executeQuery("select sysdate from dual"); [// line 7]{style="color:#3366ff;"}  
]{style="font-size:small;color:#339966;"}**

**[ while (rset.next()) [// line 8]{style="color:#3366ff;"}  
]{style="font-size:small;color:#339966;"}**

**[System.out.println (rset.getString(1)); [//  line 9 Print col 1]{style="color:#3366ff;"}]{style="font-size:small;color:#339966;"}**

**[stmt.close();]{style="font-size:small;color:#339966;"}**

**[con.close(); ]{style="font-size:small;color:#339966;"}**

**[}]{style="font-size:small;color:#339966;"}**

**[catch(Exception e)]{style="font-size:small;color:#339966;"}**

**[{]{style="font-size:small;color:#339966;"}**

**[System.out.println(“Error , can't connect to the database !”);]{style="font-size:small;color:#339966;"}**

**[}]{style="font-size:small;color:#339966;"}**

[  
]{style="font-size:small;"}

[[شرح الكود]{style="font-family:Tahoma;"}:]{style="color:#c90016;"}

[في السطر رقم ]{style="font-family:Tahoma;"}2 [قمنا بتعريف وسيط الاتصال]{style="font-family:Tahoma;"}[.]{style="font-size:x-small;"}

[في السطر رقم ]{style="font-family:Tahoma;"}[3 ]{style="font-size:x-small;"}[قمنا بالاتصال بالقاعدة و علينا تزويد المعلومات التالية ]{style="font-family:Tahoma;"}:

[[اسم السيرفر ]{style="text-decoration:underline;"}]{style="font-family:Tahoma;"}[:]{style="text-decoration:underline;"} [رقم ]{style="font-family:Tahoma;"}IP [أو اسم الجهاز الذي يحتوي القاعدة ، في حالتي هنا فهو ]{style="font-family:Tahoma;"}localhost.

[[اسم قاعدة البيانات ]{style="text-decoration:underline;"}]{style="font-family:Tahoma;"}[:]{style="text-decoration:underline;"} [عندي اسمها ]{style="font-family:Tahoma;"}xe.

[[اسم المستخدم ]{style="text-decoration:underline;"}]{style="font-family:Tahoma;"}[:]{style="text-decoration:underline;"} [اسم المستخدم الذي أريد أن أدخل للقاعدة من خلاله ]{style="font-family:Tahoma;"}"hr” ([ملاحظة لن يتم الاتصال في حال استخدام اسم المستخدم ]{style="font-family:Tahoma;"}sys [هنا ، لا أعرف ما السبب ربما لأغراض أمنية]{style="font-family:Tahoma;"}).

[[كلمة المرور ]{style="text-decoration:underline;"}]{style="font-family:Tahoma;"}[:]{style="text-decoration:underline;"} [كلمة مرور المستخدم وفي حالتي فهي ]{style="font-family:Tahoma;"}"hr”.

[في حال أن الاتصال قد نجح عندها فإنه سيكمل وإلا فإنه سيقوم بإرسال استثناء ]{style="font-family:Tahoma;"}throw exeption

[وبعدها قمنا بإنشاء استعلام يقوم بجلب ساعة النظام للتأكد من أن الاتصال قد تم بنجاح]{style="font-family:Tahoma;"}.

[أرجو أن يكون الشرح واضحاً]{style="font-family:Tahoma;"}..
