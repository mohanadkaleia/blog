Title: إخفاء الكيبورد في تطبيقات IOS
Date: 2014-08-06 10:30
Author: mohanad
Category: Code, IOS
Tags: app, hide, ios, keyboard
Slug: how-to-hide-keyboard-in-ios-app
Status: published

[![twitter-keyboard-100056244-large](../../static/images/how-to-hide-keyboard-in-ios-app/twitter-keyboard-100056244-large-300x201.png){.aligncenter .size-medium .wp-image-490 width="300" height="201"}](../../static/images/how-to-hide-keyboard-in-ios-app/twitter-keyboard-100056244-large.png)

 

هل بدآت بتعلم  برمجة IOS ..؟!! لابد وأنك واجهت مشكلة ان لوحة المفاتيح لا تختفي بشكل تلقائي عند النقر على زر Return.. نعم السبب انه اخفاءها يتم بشكل برمجي (يدوي) وليس افتراضي من نظام التشغيل.. لذلك سنتعلم اليوم كيفية اخفاء الكيبورد في نظام IOS

سنقوم الآن بإنشاء مشروع بسيط جداً بحيث نقوم بإخفاء الكيبورد بطريقتين الطريقة الأولى من خلال النقر على زر Return، والطريقة الثانية من خلال النقر على أي مكان فارغ بالشاشة.

 

### [أولاً - قم بإنشاء مشروع جديد]{style="color:#800080;"} 

قم بإنشاء مشروع جديد من نوع [Single View based وقم بتسمية المشروع بأي اسم مثلاً HideKeyboard، وبعدها قم بسحب عنصر text box من المكتبة.]{style="color: rgb(0, 0, 0); font-family: sans-serif; font-size: 13px; line-height: 19.0499992370605px;"}

الآن بعد أن أصبح لدينا واجهة تحتوي على حقل نصي يجب علينا أن نقوم بإنشاء outlet في  view controller ونربطه مع هذا الحقل النصي، يمكن القيام بهذا من خلال إظهار Assistant editor واختيار ملف .h، وبعدها نقوم بالضغط على زر control وسحب العنصر إلى قسم interface، كما يجب أن نقوم بتعريف تابع لإخفاء الكيبورد، الآن يجب أن يكون شكل الملف كالتالي:

> ``` {style="padding: 1em; border: 1px dashed rgb(47, 111, 171); color: rgb(0, 0, 0); line-height: 1.1em; background-color: rgb(249, 249, 249);"}
> #import <UIKit/UIKit.h>
>
> @interface HideKeyboardViewController : UIViewController 
>
> @property (strong, nonatomic) IBOutlet UITextField *textField;
> -(IBAction)textFieldReturn:(id)sender;
> @end
> ```

 

### [ثانياً - كتابة الملف التنفيدي .m]{style="color:#800080;"} 

نقوم بفتح الملف التنفيذي implementation file .m، ونقوم بكتابة التابع الذي قمنا بتعريفه سابقاً بحيث يصبح شكل الملف كما يلي:

``` {dir="ltr" style="padding: 1em; border: 1px dashed rgb(47, 111, 171); color: rgb(0, 0, 0); line-height: 1.1em; background-color: rgb(249, 249, 249);"}
#import "HideKeyboardViewController.h"

@interface HideKeyboardViewController ()

@end

@implementation HideKeyboardViewController

-(IBAction)textFieldReturn:(id)sender
{
    [sender resignFirstResponder];
}
.
.
.
@end
```

في الكود السابق قمنا باستدعاء التابع resignFirstResponder للعنصر الذي يقوم بالحدث، وهو في حالتنا هذه الكيبورد، أي قم باخفاء الكيبورد..

ولكن كيف سيتم تنفيذ هذا التابع، يجب علينا ربطه مع الحدث المناسب ليتم استدعاءه في الوقت المناسب، يمكن أن نقوم بعملية الربط من خلال Interface builder، حسناً قم الآن باختيار Main.storyboard.

الآن قم باختيار الحقل النصي الذي قمنا بإضافته مسبقاً text field ثم قم باختيار نافذة connection inspector من الجهة اليمنى، وقم بالنقر على الدائرة على اليمين للحدث Did end on exit واسحبه إلى أسفل View controller  كما هو مبين بالشكل وافلته وقم باختيار التابع HideKeyboardViewController الذي قمنا بكتابته مسبقاً:

[![Xcode\_5\_connection\_to\_viewcontroller](../../static/images/how-to-hide-keyboard-in-ios-app/Xcode_5_connection_to_viewcontroller.png){.aligncenter .size-full .wp-image-492 width="796" height="713"}](../../static/images/how-to-hide-keyboard-in-ios-app/Xcode_5_connection_to_viewcontroller.png)

الآن لو جربنا تشغيل البرنامج إذا نقرنا على الحقل النصي لإظهار الكيبورد يمكننا الآن إخفاءه من خلال النقر على زر Return.

 

### [إخفاء الكيبورد من خلال النقر على الخلفية]{style="color:#800080;"} 

الآن قمنا بإخفاء الكيبورد عند النقر على زر Return ولكن من الشائع أيضاً أن يقوم المستخدم بإخفاء الكيبورد عند النقر على أي مكان بالشاشة خارج الكيبورد، يمكننا فعل ذلك أيضاً بسهولة من خلال بناء التابع touchBegan في  التالي:

``` {dir="ltr" style="padding: 1em; border: 1px dashed rgb(47, 111, 171); line-height: 1.1em; background-color: rgb(249, 249, 249);"}
- (void)touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event {

    UITouch *touch = [[event allTouches] anyObject];
    if ([_textField isFirstResponder] && [touch view] != _textField) {
        [_textField resignFirstResponder];
    }
    [super touchesBegan:touches withEvent:event];
}
```

في التابع السابق قمنا باختبار فيما إذا كان العنصر الفعال هو الحقل النصي، والعنصر الذي ننقر عليه ليس الحقل النصي إذا قم بإخفاء الكيبورد.

 

الآن قم بتشغيل البرنامج وتجربته، جرب أن تقوم بالنقر على أي مكان بالشاشة بعد ان تقوم بإظهار الكيبورد، لقد اختفى الكيبورد :)

 

المصدر: <http://www.techotopia.com/index.php/Writing_iOS_7_Code_to_Hide_the_Keyboard>

 
