Title: كيفية اتصال برنامج جافا بقاعدة البيانات أوراكل
Date: 2011-06-17 22:26
Author: admin
Category: Code, Database
Slug: java-connection-with-oracle
Status: published

[ربط الجافا مع قاعدة البيانات أوراكل]

![](http://download.oracle.com/javaee/images/Java_clr_hori.gif "java with oracle database")

سنتناول اليوم طريقة ربط برنامج مكتوب بلغة الجافا مع قاعدة البيانات أوراكل .

قبل أن نبدأ علينا أن نعرف أنه لكي يتمكن أي برنامج جافا من الاتصال بقاعدة البيانات أوراكل يجب أن يتوفر **driver** خاص اسمه **jdbc** والذي يهتم بإدارة عمليات الاتصال والاستعلامات وغيرها من العمليات مع القاعدة.. المهم يمكن تحميله من موقع أوراكل مباشرة باتباع الرابط التالي واختيار مدير القاعدة المناسب :

<http://www.oracle.com/technetwork/database/features/jdbc/index-091264.html>

[[**الخطوة الأولى** ]**-** [**إنشاء مشروع جديد**]**:**]

لنقم الآن بإنشاء مشروع جديد مثلاً يمكن اختيار java application.

[[**الخطوة الثانية – إضافة وسيط الاتصال**]**:**]

حيث نقوم بالضغط بالزر اليمين على القائمة Library واختيار “add jar file” وبعدها نقوم بإضافة وسيط الربط class12.jar.

[![](../../static/images/java-connection-with-oracle/add_library1.png "add_library")](../../static/images/java-connection-with-oracle/add_library1.png)

[[**الخطوة الثالثة – كود الاتصال**]**:**]

علينا أولاً أن نقوم باستيراد مكتبة الاتصال كما يلي:

**import java.sql.\*;**

لم يتبق لنا الآن سوى كتابة كود الاتصال لكي نتمكن من الاتصال بالقاعدة :

**try{**

**[// load oracle driver  line 1
]**

**Class.forName("oracle.jdbc.driver.OracleDriver"); [// line 2
]**

**[//connect using Thin driver // line 3
]**

**Connection con = DriverManager.getConnection("jdbc:oracle:thin:\@localhost:1521:xe","hr","hr"); [// line 4
]**

**System.out.println("Connected Successfully To Oracle");[ // line  5
]**

**Statement stmt = con.createStatement();[ // line 6
]**

**ResultSet rset = stmt.executeQuery("select sysdate from dual"); [// line 7
]**

** while (rset.next()) [// line 8
]**

**System.out.println (rset.getString(1)); [//  line 9 Print col 1]**

**stmt.close();**

**con.close(); **

**}**

**catch(Exception e)**

**{**

**System.out.println(“Error , can't connect to the database !”);**

**}**

[  
]

[شرح الكود:]

في السطر رقم 2 قمنا بتعريف وسيط الاتصال.

في السطر رقم 3 قمنا بالاتصال بالقاعدة و علينا تزويد المعلومات التالية :

<u>[اسم السيرفر </u>]<u>:</u> رقم IP أو اسم الجهاز الذي يحتوي القاعدة ، في حالتي هنا فهو localhost.

<u>[اسم قاعدة البيانات </u>]<u>:</u> عندي اسمها xe.

<u>[اسم المستخدم </u>]<u>:</u> اسم المستخدم الذي أريد أن أدخل للقاعدة من خلاله "hr” (ملاحظة لن يتم الاتصال في حال استخدام اسم المستخدم sys هنا ، لا أعرف ما السبب ربما لأغراض أمنية).

<u>[كلمة المرور </u>]<u>:</u> كلمة مرور المستخدم وفي حالتي فهي "hr”.

في حال أن الاتصال قد نجح عندها فإنه سيكمل وإلا فإنه سيقوم بإرسال استثناء throw exeption

وبعدها قمنا بإنشاء استعلام يقوم بجلب ساعة النظام للتأكد من أن الاتصال قد تم بنجاح.

أرجو أن يكون الشرح واضحاً..
