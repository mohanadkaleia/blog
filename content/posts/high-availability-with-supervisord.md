Title: High Availability with Supervisord
Date: 2020-12-29
Author: Mohanad Kaleia
Category: Software Engineering
Tags: supervisord, availability
Slug: high-availability-with-supervisord
Direction: rtl
Cover: ../../static/images/high-availability-with-supervisord/supervisord.png

![](../../static/images/high-availability-with-supervisord/supervisord.png)

في عالم هندسة البرمجيات، يوجد معيار هام جداً لتحديد فيما إذا كانت البرمجية أو الخدمة (سمها ما شئت) موثوقة أم لا، هذا المعيار هو الجاهزية availability، بحيث أن النظام أو الخدمة يجب أن تكون متوفرة وجاهزة للاستعمال في أي وقت كان. مثلاً في حال كان لديك خدمة بريد الكتروني، هذه الخدمة يجب أن تكون متوفرة بشكل دائم بحيث أي زبون حاول الاتصال بهذه الخدمة يجب أن يستطيع الوصول واستعمال هذه الخدمة. 

في تدوينتنا اليوم، سوف نتكلم عن كيف يمكن أدارة برنامج بسيط بحيث يحقق جاهزية عالية حتى في حال حدوث أخطاء، بشكل خاص سوف نتلكم عن أداة لأدارة ومراقبة المعالجات Supervisord. 


![](https://media.giphy.com/media/3oKHW8JB6ItMjIqXcs/giphy.gif)


--- 

# Availability الجاهزية

لا بأس في البداية من توضيح مفهوم الجاهزية. بالتعريف الجاهزية هي نسبة الوقت المتوقع فيه أن يعمل النظام لا بأس في البداية من توضيح مفهوم الجاهزية. بالتعريف الجاهزية هي نسبة الوقت المتوقع فيه أن يعمل النظام إلى الزمن الحقيقي الذي عمل فيه النظام. مثلاً لو أخذنا مثال برنامج طبي يراقب نبضات القلب لمريض، هذا النظام مطلوب منه جهوزية عالية جداً. فمثلاً  لو تم القياس على يوم كامل، لو عمل النظام بشكل فعال بدون أخطاً خلال هذا اليوم نقول أن الجاهزية هي 100٪.

    :::python
    availability = uptime / operatin cycle
    availability = 3600 / 3600 = 1

ولكن في حال أن النظام حدث فيه خطأ لنقل لمدة خمس دقائق، فأن هذه النسبة سوف تنقص لتصبح 0.998% 
    
    :::python
    availability = 3595 / 3600 = 0.998

 %99.8 ربما تبدو هذه النسبة عالية، ولكن في حالة الأجهزة الطبية ربما تعتبر خطيرة جداً وغير مقبولة.
وغير مقبولة.

--- 
# Supervisord

في هذه التدوينة، سوف نناقش مثال بسيط، بالتأكيد لن نتطرق لأمثلة خدمة البريد الالكتروني، أو أي أجهزة طبية (تأمين جاهزية عالية لهكذا أنظمة يعتبر قصة مختلفة تماماً). في هذه التدوينة، سوف نطرح برنامج بسيط، مثل Chat bot، وسوف نقوم باستعمال أداة تدعى Supervisord لأدارة المعالجة process الخاص ببرنامجنا بحيث تقوم بمراقبته وتضمن أن هذا البرنامج يعمل بشكل دائم، وتقوم بأعادة تشغيله في حال حدوث أخطاً وتوقف البرنامج عن العمل. 

سوبرفايزردي، هي برمجية مجانية ومفتوحة المصدر، تقوم بمراقبة وأدارة المعالجات Processes، على أنظمة Unix ومن الجدير بالذكر أن هذه الأداة تم بناءها باستخدام لغة البايثون. سوبرفايزرد تعتبر مثالية في السيناريوهات التالية:

1. تشغيل خدمة أو برنامج بشكل آلي عند تشغيل \ أعادة أقلاع الجهاز (السيرفر)
2. أعادة تشغيل الخدمة \ البرنامج عند حدوث خطأ ما (يمكن ضبط أعادة المحالة حتى عدد معين من المرات)

السيناريوهات السابقة تعتبر أساسية لضمان جاهزية عالية لأي خدمة. 

في الفقرات القادمة سنقوم بشرح كيفية تنصيب برمجية Supervisord، ثم سوف نطرح برنامج بسيط كمثال ونقوم بتهيئة وضبط Supervisord للعمل على مراقبة وتشغيل برنامجنا.

--- 

# The Script

لتوضيح فكرة عمل Supervisord سنقوم باستعمال برنامج بسيط جداً، هو عبارة عن خادم ويب يقوم بأرجاع جملة “Hello World” عندما يتم إرسال طلب له. البرنامج مكتوب بلغة البايثون:


    # Note I got this gist from here: https://bit.ly/2KKUB1e
    import http.server
    import socketserver
    from http import HTTPStatus
    
    
    class Handler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            self.send_response(HTTPStatus.OK)
            self.end_headers()
            self.wfile.write(b'Hello world')
    
    
    httpd = socketserver.TCPServer(('', 8000), Handler)
    httpd.serve_forever()

لاحظ أننا استعملنا هنا مكتبة http، وهي أحدى المكتبات الأساسية في البايثون، بغية تبسيط المثال اكثر. الآن قم بنسخ هذا الكود إلى جهازك المحلي ثم قم بتجربة تشغيله كما يلي (على فرض أننا أسمينا الملف app.py):

```
:::python
python3 app.py
```

من خلال المتصفح، أو حتى من خلال سطر الأوامر لو قمت باستعمال cURL، يمكننا تجربة أرسال طلب GET للسيرفر كما يلي:

```
:::python
curl localhost:8000
Hello world
```
--- 
# تنصيب Supervisord

لتنصيب Supervisord يمكننا استعمال مدير الحزم في أبونتو كما يلي: 

    :::python
    sudo apt-get install -y supervisor

بعد ذلك يمكننا معاملته على أساس خدمة في النظام وتشغيله كما يلي: 

    :::python
    sudo service supervisor start



# ضبط الأعدادات في Supervisord

علينا الآن أخبار Supervisord عن البرنامج الذي قمنا بكتابته ليقوم بإدارته ومراقبة عمله. من الجدير بالذكر أن Supervisord يقوم بقراءة جميع الإعدادات الموجودة في المسار `/etc/supervisor/conf.d/` لذلك كل ما علينا هو أنشاء ملف جديد داخل هذا المسار وكتابة إعدادات برنامجنا فيه. 


> ملاحظة سريعة: عرفنا مسار الإعدادات من خلال ملف الأعدادات الأساسية الموجود في `/etc/supervisor/supervisord.conf`   حيث لو فتحته لوجدت أنه يتم تضمين جميع الملفات الموجودة ضمن مسار conf.d كما يلي: 
> 
    [include]
    files = /etc/supervisor/conf.d/*.conf

قم بإنشاء ملف لإعدادات برنامجنا كما يلي: 

    :::python
    sudo touch /etc/supervisor/conf.d/hello_world.conf

وبعدها قم بالدخل إلى هذا الملف باستخدام محرر النصوص المفضل لديك (nano, vim, …) ثم أكتب الأعدادات التالية:


    [program:hello_world]
    command=python3 app.py 
    directory=/home/ubuntu/hello_world
    autostart=true
    autorestart=true
    startretries=3
    strerr_logfile=/home/ubuntu/hello_world/out.log
    stdout_logfile=/home/ubuntu/hello_world/out.log
    user=www-data

الآن لنشرح قليلاً الأعدادات التي قمنا بكتابتها:

- السطر الأول قمنا بتعريف اسم البرنامج الذي سيقوم supervisord بإدارته، في مثالنا hello_world
- في السطر الثاني، الأمر الذي سيتم تنفيذه لتشغيل البرنامج
- السطر الثالث، المسار الذي سيقوم supervisord بتشغيل الأمر فيه
- السطر الرابع، autostart=true لكي يتم تشغيل البرنامج عند تشغيل السيرفر
- السطر الخامس مهم جداً، هنا autorestart=true، معناها أن البرنامج سيتم إعادة تشغيله بشكل تلقائي في حال حدوث خلل ما أثناء عمله
- السطر السادس، startretries=3، يوضح عدد المرات التي سيتم محاولة تشغيل البرنامج قبل أن يتم اعتبار أن حالة التشغيل فاشلة
- السطر السابع والثامن، هنا تم ضبط الملف الذي سيتم كتابة خرج البرنامج عليه
- السطر التاسع، يوضح المستخدم الذي سيقوم بتشغيل هذا البرنامج


# تحديث الأعدادات في Supervisord

في الفقرة السابقة قمنا بكتابة ملف الأعدادات الذي من خلاله يمكن لـ supervisord أن يتعرف ويقوم بتشغيل البرنامج الذي قمنا بكتابته، ولكن قبل ذلك علينا أن نقوم بتحديث الأعدادات لنخبر Supervisord أننا قمنا بعمل تغيير في الأعدادات. يمكن ذلك من خلال تنفيذ أمر `reread` وبعده أمر `update` كما يلي:

    :::python
    sudo supervisorctl reread
    sudo supervisorctl update

الآن برنامجنا يجب أن يكون يعمل، يمكننا سؤال supervisord أن يقوم بعرض البرامج التي يقوم بإدارتها من خلال: 

    :::python
    sudo supervisorctrl status

وسوف تظهر لنا النتيجة: 

    :::python
    hello_world                      RUNNING   pid 180772, uptime 0:01:31

ولو أردنا أيضاً أن نقوم بإرسال طلب للسيرفر من المتصفح أو من خلال سطر الأوامر كما فعلنا سابقاً: 
    
    :::python
    curl localhost:8000
    Hello world

نلاحظ أن البرنامج يعمل كما هو متوقع. 

الآن بالإضافة إلى تعليمة `status` التي رأيناها يمكننا أيضاً أرسال عدة أوامر ل supervisord، يمكننا معرفة الأوامر المتاحة من خلال help كما يلي:

    sudo supervisorctl help
    
    default commands (type help <topic>):
    =====================================
    add    exit      open  reload  restart   start   tail   
    avail  fg        pid   remove  shutdown  status  update 
    clear  maintail  quit  reread  signal    stop    version

فمثلاً يمكننا أيقاف البرنامج من خلال تعليمة `stop` أو أعادة تشغيلها `restart` أو تشغيل الخدمة في حال لم تكن تعمل `start`. يمكنك استكشاف جميع هذه التعليمات المفيدة لو أحببت عزيزي القارئ. 

الآن فأن برنامجنا يعمل في الخلفية على شكل خدمة، تعمل بشكل تلقائي عند إقلاع الجهاز، وتعيد تشغيل نفسها في حال حدوث خلل ما أثناء التشغيل. 


![يحيى الذكاء](https://paper-attachments.dropbox.com/s_F82AF820B646632230135620136434F83C872EE7E557CDE6832B7D6CE7A9015D_1609311922315_image.png)

--- 

# الخاتمة

في هذه التدوينة، قمنا بالتعرف على مفهوم الجاهزية Availability، كما تعرفنا على برمجية Supervisord، والتي تقوم بمراقبة وإدارة المعالجات لتحقيق جاهزية عالية. قمنا ببناء مثال بسيط عن ويب سيرفر يقوم بطباعة جملة `hello world` عند إرسال طلب له. وقمنا بضبط Supervisord ليقوم بتشغيل هذا السيرفر بشكل تلقائي. 

أتمنى أن تكون هذه التدوينة مفيدة للجميع. 



# بعض المراجع المفيدة 

- [Supervisord](http://supervisord.org/)
- https://serversforhackers.com/c/monitoring-processes-with-supervisord
-  https://learning.oreilly.com/library/view/software-architecture-in/9780132942799/ch05.html
-  https://www.opensourceforu.com/2019/10/how-to-run-multiple-services-inside-a-single-container-using-supervisord/
