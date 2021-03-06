# מפרט מסמך - _xAI Vision_ #
שי קמחי ויותם סלמון

## תכונות ותהליכים עיקריים ##

### הוספת קטגוריה ###

**גרסת ההדגמה הגרפית** של *xAI Vision* תספק טופס להוספת קטגוריה חדשה. לטופס הפשוט תהיה תיבת טקסט, שבה המשתמש יזין מזהה קטגוריה, ותיבת טקסט שנייה שבה המשתמש יזין את שם התצוגה המקדימה של הקטגוריה. מתחת לזה יהיה כפתור להוספת הקטגוריה. התוכנה תבדוק כי יש את אותו מזהה קטגוריה אינו קיים עדיין, ואם כן - הודעת שגיאה יוצגו. אחרת, המערכת תוסיף את הקטגוריה לאחסון ותנתב את המשתמש לטופס הראשי.

**בגירסת API**, פונקציה תצוין ליצירת קטגוריה חדשה `classifier.add_category (id: string, name: string): void`. ממשק ה- API של REST יספק אפשרות 'POST `לבקשה' / Categories / add`** ** endpoint פנימי כדי להוסיף מרחוק קטגוריה.

**ממשק האינטרנט  **עבור ממשק ה- API של REST יחזיק טופס להזנת קטגוריה, אותו ממשק משתמש כמו גרסת ההדגמה. Differene היא כי הגירסה מבוססת אינטרנט מוסיף את הקטגוריה ברחבי העולם, ואת גירסת הדגמה מוסיף אותו באופן מקומי.

* לא נגיש למפתחים להשתמש. ממשק ה- API הציבורי לא יספק דרך להוסיף קטגוריה לביטחון.

### הוספת תמונה לקטגוריה ###

** הגרסה ההדגמה הגרפית ** תספק טופס להוספת תמונות בודדות / מרובות ולסווג אותן לקטגוריה מסוימת. הטופס יכיל קלט קובץ עבור תמונה.
אם נבחרה תמונה אחת, תופיע תיבת הסימון של השלמה אוטומטית ורשימת תיבות, ותאפשר למשתמש להזין קטגוריות מרובות מתוך הקטגוריות הקיימות. אם נבחרה יותר מתמונה אחת,
המשתמש יוכל לבחור קטגוריה משותפת להחלת תמונות אלה. לאחר לחיצה על כפתור "סיום", התוכנה תכשיר את הרשת באמצעות התמונה.

** גרסת ממשק ה- API ** תחתום על הפונקציה 'classifier.sign_category (תמונה: image, category: string): void` ועומס יתר' classifier.sign_category (image: image, categories: string []): void` צלם תמונה וקטגוריה / ותאמן את הרשת באמצעות התמונה.

** בגרסת האינטרנט ** יהיה טופס דומה לצורת הרשת המקומית כדי להעלות תמונה אחת או מספר תמונות. בנוסף, יהיה טופס עם אפשרות לקבל תמונה אקראית ולהחיל תגים על זה.

### סידור תמונה ###

** בגרסת ההדגמה הגרפית של GUI **, יהיה טופס עם אפשרות לשלוח תמונה. לאחר טעינת תמונה, יופיע מתחתיה טבלה, המציינת את הקטגוריות הרלוונטיות ביותר המסווגות עבורה ואת האמון בכל אחת מהקטגוריות (מספר בין 0 ל -1 המייצג את האפשרות לתשובה נכונה).

** גרסת ממשק ה- API תספק פונקציה 'classifier.classify (image: image): dict`, שיחזיר מילון עם הקטגוריות כמפתחות ורמת הביטחון כערכים.

** גרסת האינטרנט ** תהיה בדיוק כמו גירסת ההדגמה הגרפית.

### מסה מסווג ###

_xAI Vision_ יהיה משחק קטן, בצורה של יישום סלולרי. מטרת המשחק היא ליצור קבוצה עשירה של קטגוריות ו מסווגים עבור ה- API. שחקנים מרובים ימסרו בו זמנית תמונות ויהיו חייבים להיכנס למה שהם חושבים שהאחרים חושבים עליו. ככל שיש להם קטגוריות יותר במשותף, כך הם מקבלים יותר נקודות. זה יעזור לנו לסווג תמונות אקראיות מהאינטרנט לקטגוריות שאנחנו כבר יודעים, ותיצור מטא נתונים עשירים של מסווגים. מידע נוסף על GUI של המשחק בקטע הדמיה של ממשק המשתמש.

תכונות זה יהיה:
+ כניסה למערכת רישום
+ מערכת מזומנים עם אפשרויות פרופיל
+ משחק אקראי
+ חנות קוסמטיקה

### מסך התחברות ###

מסך המציג טופס כניסה עם לוגו לאימות של Facebook. בחלק העליון, הלוגו של היישום יופיע. מתחת, 2 תיבות טקסט, `שם משתמש` ו` סיסמה`, אשר ידרוש את המידע של המשתמש. מתחת, כפתור 'התחברות'. על אישורי הכניסה הנכונים, יועברו לטופס היישום הראשי. באישורים שגויים, תופיע הודעה שתודיע על שגיאה.

טופס ההתחברות יכלול גם לחצן כניסה ל- Facebook, שיחתום אוטומטית על המשתמש באמצעות אישורי הפייסבוק או החשבון שלהם.

מתחת לכל, תהיה תווית שכותרתה _ אין לך חשבון? הרשם! _ כי על קליק יעביר את המשתמש לדף ההרשמה.

### מסך הרשמה ###

האם רשימת תיבות בשם `שם משתמש`,` סיסמה`, `אישור סיסמה`,` דוא"ל` ו`` מדינה`. מתחת יהיה כפתור רישום. בעת שליחת מידע שגוי, תתריע על הודעת שגיאה. אחרת, תוסיף את המשתמש לאחסון ותפנה מחדש את המשתמש לתהליך האימות באימייל.

דרישות מידע:
+ שם המשתמש חייב להיות 8 תווים לפחות
+ שם המשתמש יכול להיות לכל היותר 30 תווים
+ הסיסמה צריכה להיות לפחות 8 תווים
+ הסיסמה יכולה להיות לכל היותר 50 תווים
+ הסיסמה חייבת להכיל מספר
+ הסיסמה חייבת להכיל אות רישית
+ הסיסמה חייבת להכיל אות קטנה
+ אישור הסיסמה חייב להיות זהה לסיסמה
+ כתובת האימייל חייבת להיות כתובת דוא"ל חוקית
+ המדינה חייבת לכלול מדינה קיימת

### מסך ראשי ###

במסך הראשי יהיו 3 לחצנים: 'Play`, `Store` ו-` Profile`. Play ינותב מחדש למסך המשחק, החנות תציג את לוח החנות, והפרופיל יאפשר למשתמש לערוך את הגדרות הפרופיל שלו, לשנות את תמונת הפרופיל שלו וכו '(במסך הפרופיל).

להלן תהיה תמונה של השחקן, ומתחתיו כפתור אדום שכותרתו 'התנתק', שיחתום על המשתמש מחוץ ליישום וייקח את המשתמש חזרה למסך ההתחברות.

### הפעל מסך ###

עוד כדי להיות מפורט על זה מאוחר יותר. ניתן לראות בקטע הדמיה של ממשק המשתמש


# # ממשק משתמש הדמיה ##

### גרסת WF ###

** הוספת תמונה לקטגוריה **

! [העלאת תמונה] (https://github.com/yotam180/xAI/blob/master/docs/xAI%20Vision/images/Uploading%20Picture.PNG?raw=true)


** אימות תמונות מהאינטרנט **

! [הורדת תמונה] (https://github.com/yotam180/xAI/blob/master/docs/xAI%20Vision/images/Download1.PNG?raw=true)

! [הורדת תמונה] (https://github.com/yotam180/xAI/blob/master/docs/xAI%20Vision/images/Download2.PNG?raw=true)

** הוספת קטגוריה **

[הגדרת קטגורי] (https://github.com/yotam180/xAI/blob/master/docs/xAI%20Vision/images/AddCatagory.PNG?raw=true)

** הסתר תמונה **

! [בדיקה] (https://github.com/yotam180/xAI/blob/master/docs/xAI%20Vision/images/Test.PNG?raw=true)

### יישום ###

** מסך כניסה **

! [מסך כניסה] (https://raw.githubusercontent.com/yotam180/xAI/master/docs/xAI%20Vision/images/first_form.png)

** תהליך ההרשמה **

! [הרשמה] (https://raw.githubusercontent.com/yotam180/xAI/master/docs/xAI%20Vision/images/signup.png)

**מסך ראשי**

! [מסך ראשי] (https://raw.githubusercontent.com/yotam180/xAI/master/docs/xAI%20Vision/images/main_form.png)

** הצג מסך **

! [הצג מסך] (https://raw.githubusercontent.com/yotam180/xAI/master/docs/xAI%20Vision/images/play.png)

## דרישות לא פונקציונליות ##

### לשימוש בממשק GUI ###

1. NET Framework (אפשרי עם. Core Core)
2. חיבור לאינטרנט

### לשימוש בממשק ה- API ###

1. Python 2.7 / 3 ** OR ** C ++ ** או **. NET Framework
2. חיבור לאינטרנט (עבור שיחות REST API)

### עבור ממשק האינטרנט ###

1. דפדפן (עם HTML 5 ו- JavaScript תמיכה)
2. חיבור לאינטרנט
3. SSL לאבטחת תקשורת באינטרנט

### ליישום ###

1. Android 4 או יותר * (TBD)
2. מקום פנוי בדיסק
3. חיבור לאינטרנט
