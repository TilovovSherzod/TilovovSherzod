from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

def start(update: Update, context: CallbackContext):
    try:
        keyboard = [[InlineKeyboardButton("Dasturlash tillari: ", callback_data='langs')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Assalomu alaykum hurmatli mijoz bizning dasturlash tillari haqida malumot beruvchi botimizga xush kelibsiz.', reply_markup=reply_markup)
    except Exception as e:
        print(f"Nomalum xatolik yuz berdi: {e}")

def langs(update: Update, context: CallbackContext):
    try:
        query = update.callback_query
        query.answer()

        keyboard = [
            [InlineKeyboardButton("Python", callback_data='lang_python'),InlineKeyboardButton("Java", callback_data='lang_java'), InlineKeyboardButton("C++", callback_data='lang_cpp')],
            [InlineKeyboardButton("C#", callback_data='lang_csharp'), InlineKeyboardButton("PHP", callback_data='lang_php') , InlineKeyboardButton("JavaScript", callback_data='lang_javascript')]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Dasturlash tillaridan birini tanlang:", reply_markup=reply_markup)
    except Exception as e:
        print(f"Nomalum xatolik yuz berdi: {e}")

def language_info(update: Update, context: CallbackContext):
    try:
        query = update.callback_query
        query.answer()

        lang = query.data
        keyboard = [
            [InlineKeyboardButton("Info", callback_data=f'info_{lang}'), InlineKeyboardButton("Libraries", callback_data=f'libraries_{lang}')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Info - til haqida ma'lumot, Libraries - tildagi bazi kutubxonalar :", reply_markup=reply_markup)
    except Exception as e:
        print(f"Nomalum xatolik yuz berdi: {e}")


def send_info(update: Update, context: CallbackContext):
    try:
        query = update.callback_query
        query.answer()

        lang_info = {
            'info_lang_python': """Python haqida ma'lumotlar quyidagilar \n:
Python ([ˈpʌɪθ (ə)n] — payton, piton) — turli sohalar uchun yuqori darajadagi umumiy maqsadli dasturlash tili. Uning dizayn falsafasi muhim chekinishdan foydalangan holda kodning oʻqilishiga urgʻu beradi. Uning til konstruksiyalari va obyektga yoʻnaltirilgan yondashuvi dasturchilarga kichik va yirik loyihalar uchun aniq, mantiqiy kod yozishda yordam berishga qaratilgan[4]. Shuningdek Python sunʼiy intellekt hamda maʼlumotlar muhandisiligi sohalarining tili hisoblanadi.

Python deyarli barcha platformalarda ishlay oladi, xususan Windows, Linux, Mac OS X, Palm OS, Mac OS va boshqalar shular jumlasidandir. Python Microsoft.NET platformasi uchun yozilgan realizatsiyasi ham mavjud boʻlib, uning nomi — IronPython dasturlash muhitidir.

Guido van Rossum 1980-yillarning oxirida ABC dasturlash tilining davomchisi sifatida Python ustida ishlay boshladi va birinchi marta 1991-yilda Python 0.9.0 versiyasini ommaga eʼlon qildi[5].

Python dasturlash tiliga boʻlgan talab yildan yilga oshib bormoqda. CodingDojo[6] portalining tadqiqotlariga koʻra, 2020—2021-yillarda aynan Python tilida dasturlovchi mutaxassislarga eng koʻp talab boʻlgan[7].


Guido van Rossum
Sintaksisi
Unda Lua tiliga oʻxshab, bir vaqtning oʻzida bir nechta oʻzgaruvchiga qiymat berish mumkin. Shuningdek, yangi oʻzgaruvchi kiritmasdan turib, ikkita oʻzgaruvchining qiymatlarini almashtirish mumkin:

 x, y = y, x
Va uni funksiyalaridan ham shunday turda qaytarishingiz mumkin:

def function():
    x = "Jimbo"
    y = "Wales"
    return x, y
Salom, dunyo seni men sevaman!
# -*- coding: utf-8 -*-
print("Salom, dunyo seni men sevaman!")
Ishlatilishi
Web dasturlash
Zope — CMS yaratish uchun server va veb dasturlar qilish uchun dastur.
Django — web dasturlash muhiti.
Turbogears — web yaratish qilish uchun dastur.
CherryPy — web yaratish qilish uchun dastur.
Plone — saytni muhofaza qilish uchun dastur.
Mailman — „Rassilka“ yaratish uchun dastur
MoinMoin — viki — dvijok internet va intranet uchun
PlanetPlanet — RSS oqimini sindikatsiyalash
Grafika
Skencil — Vektor grafikasi uchun dastur
Pythonni ishlatadigan dasturlar
Wikipedia — botlarni yozish uchun ishlatadi.
Civilization IV — Yaxshi strategiya oʻyin.
Pythonni ishlatadigan kompaniyalar
Kosmik teleskop instituti
NASA
Google
DreamWorks
Industrial Light & Magic
Firaxis Games
Apple Computer
CCP""",
            'info_lang_java': """Java haqida ma'lumotlar \n :
        Java qati’y va statik tipizatsiyaga ega boʻlgan va obyektga yoʻnaltirilgan umumiy maqsaddagi dasturlash tilidir. Avvaliga Sun Microsystems tomonidan ishlab chiqilgan, keyinchalik Oracle kompaniyasi tarafidan sotib olingan.

Tarixi
Java dasturlash tili Oak dasturlash tili asosida paydo boʻldi. Oak dasturlash tili 90-yillarning boshida Sun Microsystems tomonidan platformaga, yaʼni operatsion sistemaga bogʻliq boʻlmagan holda ishlovchi yangi avlod aqlli qurilmalarini yaratishni maqsad qilib harakat boshlagan edi. Bunga erishish uchun Sun xodimlari C++ni ishlatishni rejalashtirdilar, lekin baʼzi sabablarga koʻra bu fikridan voz kechishdi. Oak muvofaqiyatsiz chiqdi va 1995-yilda Sun uning nomini Java ga almashtirdi va uni WWW rivojlanishiga xizmat qilishi uchun maʼlum oʻzgarishlar qilishdi.

Tilning asosiy xususiyatlari
Java obyektga yoʻnaltirilgan dasturlash (inglizcha: OOP — Object Oriented Programming) tili va u C++ ga ancha oʻxshash. Eng koʻp yoʻl qoʻyildigan xatolarga sabab boʻluvchi qismlari olib tashlanib, Java dasturlash tili ancha soddalashtirildi.

Java kod yozilgan fayllar (*.java bilan nihoyalanuvchi) kompilatsiyadan keyin bayt kod (inglizcha: bytecode) ga oʻtadi va bu bayt kod Java Virtual Mashinasi JVM tomonidan oʻqib yurgizdiriladi.

Java afzalliklari:

WORA — (inglizcha: Write Once, Run Anywhere - portable). Platforma tanlamaydi;
xavfsizlik (ishonch yoʻq kodni xavfsiz ishga tushirish);
xotirani xavfsiz boshqarish (avtomat ravishda chiqindilarni yigʻadi);
tarmoq uchun dasturlar yozish ;
koʻp oqimli (inglizcha: Multi-thread) dasturlash;
dinamik & kengaytirish;
Class lar alohida fayllarda saqlanadi. Kerak boʻlsa ishlatiladi. Dinamik ravishda imkoniyatini oshirish xam mumkin kerak boʻlsa.
Java texnologiyalari
Java SE (inglizcha: Java Standart Edition) — serverda, shaxsiy kompyuterda desktoplarda ishlovchi dasturlar, appletlar yaratish uchun ishlatiladi. Bu texnologiya yordamida yaratilgan dasturlar deyarli barcha operatsion tizimlarda ishlay oladi (Windows NT, Macintosh, Linux va Solaris). Shu bilan birga JavaSE boshqa Java turlarining asosi hisoblanadi.
JVM (Java Virtual mashinasi) JVM ning vazifasi tarjimonlik ya’ni, dastlab biz yozgan *.java fayl kompilyator yordamida bayt kod ga o’giriladi va JVM yordamida esa mashina tiliga aylantiriladi. Bu degani JVM qaysi platformaga tegishli bo’lsa, kodlarni ham o’sha platformaga moslab beradi. JVM ni ko’pgina qurilmalar va dasturiy ta’minotlar uchun ishlatish mumkin. Har bir OT(operatsion tizim) uchun JVM JRE va JDK lar konfiguratsiyasi farq qiladi, chunki bular platformaga bog’liq. Lekin java mustaqil platforma hisoblanadi.
JVM ning amalga oshiradigan asosiy vazifalari

Loads code (kod yuklanishi)
Verifies code (kod tekshirilishi)
Executes code (kod bajarilishi)
Provides runtime environment (dasturni bajarilish muhitini ta’minlash)
JRE (Java bajarilish muhiti)
JRE – Java Runtime Environment
JRE – bu faqat dastur bajarilishi uchun kerak bo`lgan muhit xolos. Dasturchi bo`lmagan oddiy foydalanuvchilarga Java dasturlari bajarilishi uchun JRE yetarlidir.
JDK(Java Development Kid) - JDK tarkibida JRE va boshqa qo'shimcha dasturlash uskunalari bo'ladi.""",
            'info_lang_cpp': """C++ haqida ma'lumotlar. \n
        C++ dasturlash tili C tiliga asoslangan. C esa oʻz navbatida B va BCPL tillaridan kelib chiqqan. BCPL 1967-yilda Martin Richards tomonidan tuzilgan va operatsion sistemalarni yozish uchun moʻljallangan edi.

Ken Thompson oʻzining B tilida BCPL ning koʻp hossalarini kiritgan va B da UNIX operatsion sistemasining birinchi versiyalarini yozgan. BCPL ham, B ham tipsiz til boʻlgan. Yani oʻzgaruvchilarning maʼlum bir tili boʻlmagan — har bir oʻzgaruvchi kompyuter hotirasida faqat bir bayt yer egallagan. Oʻzgaruvchini qanday sifatda ishlatish esa, yani butun sonmi, kasrli sonmi yoki harfdekmi, dasturchi vazifasi boʻlgan.

C tilini Dennis Ritchie B dan keltirib chiqardi va uni 1972 yili ilk bor Bell Laboratoriyasida, DEC PDP-11 kompyuterida qoʻlladi. C oʻzidan oldingi B va BCPL tillarining juda koʻp muhim tomonlarini oʻz ichiga olish bilan bir qatorda oʻzgaruvchilarni tiplashtirdi va bir qator boshqa yangiliklarni kiritdi. Boshlanishda C asosan UNIX sistemalarida keng tarqaldi. Hozirda operatsion sistemalarning asosiy qismi C/C++ da yozilmoqda. C mashina arhitekturasiga bogʻlangan tildir. Lekin yahshi rejalashtirish orqali dasturlarni turli kompyuter platformalarida ishlaydigan qilsa boʻladi.

1983-yilda, C tili keng tarqalganligi sababli, uni standartlash harakati boshlandi. Buning uchun Amerika Milliy Standartlar Komiteti (ANSI) qoshida X3J11 tehnik komitet tuzildi. Va 1989-yilda ushbu standart qabul qilindi. Standartni dunyo boʻyicha keng tarqatish maqsadida 1990-yilda ANSI va Dunyo Standartlar Tashkiloti (ISO) hamkorlikda C ning ANSI/ISO 9899:1990 standartini qabul qilishdi. Shu sababli C da yozilgan dasturlar kam miqdordagi oʻzgarishlar yoki umuman oʻzgarishlarsiz juda koʻp kompyuter platformalarida ishlaydi.

C++ 1980 yillar boshida Bjarne Stroustrup tomonidan C ga asoslangan tarzda tuzildi. C++ juda koʻp qoʻshimchalarni oʻz ichiga olgan, lekin eng asosiysi u obyektlar bilan dasturlashga imkon beradi.

Dasturlarni tez va sifatli yozish hozirgi kunda katta ahamiyat kasb etmoda. Buni taʼminlash uchun ob’ektli dasturlash gʻoyasi ilgari surildi. Huddi 70-chi yillar boshida strukturali dasturlash kabi, programmalarni hayotdagi jismlarni modellashtiruvchi ob'ektlar orqali tuzish dasturlash sohasida inqilob qildi.

C++ dan tashqari boshqa koʻp ob’ektli dasturlshga yoʻnaltirilgan tillar paydo boʻldi. Shulardan eng koʻzga tashlanadigani Xerox ning Palo Altoda joylashgan ilmiy-qidiruv markazida (PARC) tuzilgan Smalltalk dasturlash tilidir. Smalltalk da hamma narsa ob’ektlarga asoslangan. C++ esa gibrid tildir. Unda C ga oʻhshab strukturali dasturlash yoki yangicha, ob’ektlar bilan dasturlash mumkin. Yangicha deyishimiz ham nisbiydir. Ob’ektli dasturlash falsafasi paydo boʻlganiga ham yigirma yildan oshayapti.

C++ funksiya va ob’ektlarning juda boy kutubhonasiga ega. Yani C++ da dasturlashni oʻrganish ikki qismga boʻlinadi. Birinchisi bu C++ ni oʻzini oʻrganish, ikkinchisi esa C++ ning standart kutubhonasidagi tayyor ob’ekt/funksiyalarni qoʻllashni oʻrganishdir.""",
            'info_lang_csharp': """C# haqida ma'lumotlar\n :
        C# (Si Sharp — deb talaffuz qilinadi) leksik jihatdan kengaytirilgan, imperativ, deklarativ, funksional, umumiy, obyektga yoʻnaltirilgan (sinfga asoslangan) va komponentlarga yoʻnaltirilgan dasturlash fanlarini oʻz ichiga olgan umumiy maqsadli, koʻp paradigmali dasturlash tili. U 2000-yilda Microsoft tomonidan .NET tashabbusi doirasida ishlab chiqilgan va keyinchalik Ecma (ECMA-334) va ISO (ISO / IEC 23270: 2018) tomonidan xalqaro standart sifatida tasdiqlangan.

Misol
Console.WriteLine("Salom, dunyo!");
C# tili tarixi
Kompyuter tillari oʻz-oʻzidan emas, balki oʻzaro bir-biriga bogʻliqlikda mavjud boʻladi. Har qanday yangi til u yoki bu shaklda oldingi yaratilgan tillarning xossalarini oʻziga meros qilib oladi, yaʼni ketma-ketlik prinsipi amalga oshiriladi. Natijada bitta tilning imkoniyatlari boshqalari tomonidan foydalaniladi (masalan, yangi xususiyatlar mavjud kontekstga birlashtiriladi, tilning eski tuzilishlari esa oʻchirib yuboriladi).
Kompyuter tillarining evolyutsiyasi shunday tarzda roʻy beradi va dasturlash mahorati takomillashtiriladi. C# tili yuqoridagilardan istisno emas, u boshqa dasturlash tillarining koʻplab foydali imkoniyatlarini meros qilib oldi va dunyoda eng koʻp qoʻllaniladigan ikkita kompyuter tillari — Ci, C++, shuningdek Java tili bilan uzviy bogʻliqdir.
C# tili 1972-yilda Nyu-Djersi shtatining Myurrey-xill shahrida Bell Laboratories kompaniyasining tizimli dastur tuzuvchisi Dennis Richie tomonidan yaratilgan. Bu til oʻzini shunchalik yaxshi koʻrsatdiki, oxir oqibatda unda Unix operatsion tizimlarining 90 % yadro kodlari yozildi (oldin quyi darajadagi til assemblerda yozilgan).
C# ning vujudga kelishidan oldinroq yaratilgan tillardan, (Pascal ulardan eng mashhuri hisoblanadi), yetarli darajada muvaffaqiyatli foydalanilgan, lekin aynan C# tili dasturlashning zamonaviy davri boshlanishini belgilab berdi. 1960-yillarda dasturlash texnologiyalaridagi strukturaviy dasturlashlarning paydo boʻlishiga olib kelgan inqilobiy oʻzgarishlar C# tilini yaratish uchun asosiy imkoniyatlarni belgilab berdi.
Strukturaviy dasturlashlarning paydo boʻlishiga qadar katta dasturlarni yozish qiyin boʻlgan, satr kodlari miqdorining oshishi sababli dasturlarning oʻtish joylari chalkash massalariga aylanib ketishiga olib keladi. Strukturaviy tillar dastur tuzuvchi instrumentariysiga shartli operatorlarni, lokal oʻzgaradigan tartiblarni va boshqa mukammallashtirishlarni qoʻshib bu muammoni hal qildi. Shunday tarzda nisbatan katta dasturlarni yozish imkoniyati vujudga keldi.
Aynan C# tili kuch, elegantlik va maʼnodorlikni oʻzida muvaffaqiyatli birlashtirgan birinchi strukturaviy til boʻldi. Uning boʻlishi mumkin boʻlgan xatolar masʼuliyatini tilga emas dastur tuzuvchi zimmasiga yuklaydigan prinsiplar bilan inobatga olgan holda sintaksisdan foydalanishdagi qisqalik va osonlik kabi xususiyatlari tezda koʻplab tarafdorlarini topdi. Bugungi kunda biz mazkur sifatlarni oʻz oʻzidan anglashiladigan deb hisoblaymiz, lekin S da birinchi marotaba dastur tuzuvchiga zarur boʻlgan ajoyib yangi imkoniyatlar mujassamlashtirilgan.
Natijada 1980 yillardan boshlab S strukturaviy dasturlash tillari orasida eng koʻp foydalaniladiganlaridan biri boʻlib qoldi. Biroq, dasturlashning rivojlantirish choralariga koʻra bundanda kattaroq dasturlarni qayta ishlash muammosi kelib chiqmoqda. Loyiha kodi maʼlum bir hajmga yetgan zahoti (uning raqamli ahamiyati dastur, dastur tuzuvchi, foydalanilgan instrumentlarga bogʻliq boʻladi, lekin taxminan 5000 satr kodlari nazarda tutilayapti) S-dasturlarini tushunish va kuzatib borishda qiyinchiliklar yuzaga keladi.
OYDning vujudga kelishi va C++ tilining yaratilishi
1970 yillar oxirida koʻplab loyihalar S strukturaviy dasturlash tili yordamida qayta ishlash uchun oson boʻlgan eng yuqori hajmga erishgan. Endi bularga yangicha munosabat talab qilina boshlandi va ushbu muammoni hal etish uchun dastur tuzuvchiga katta hajmdagi dasturlar bilan ishlash imkonini beruvchi obyektga yoʻnaltirilgan dasturlash (OYD) yaratildi. Hamonki, oʻsha vaqtda S eng ommabop til boʻlishiga qaramasdan OYD ni qoʻllab-quvvatlamadi, uning obyektga yoʻnaltirilgan (keyinchalik C++ deb atalgan) versiyasini yaratish zarurati tugʻildi.
Bu versiya oʻsha Bell Laboratories kompaniyasining xodimi Brian Straustrup tomonidan 1979-yil boshida ishlab chiqilgan. Dastlab yangi til „C sinflar bilan“ degan nom oldi, lekin 1983-yilda C++ deb qayta nomlangan. U oʻzida C tilini toʻla qamrab oladi (yaʼni, C C++ uchun poydevor boʻlib xizmat qiladi) va obyektga yoʻnaltirilgan dasturlashni qoʻllab-quvvatlash uchun moʻljallangan yangi imkoniyatlarni namoyon qiladi. Aslida C++ C tilining obyektga yoʻnaltirilgan versiyasi hisoblanadi, shuning uchun C ni biluvchi dastur tuzuvchi uchun C++ da dasturlashga oʻtishda yangi tilni emas, balki faqatgina OYD ning yangi konsepsiyasini oʻrganish kifoya qiladi.
C++ tili uzoq vaqt mobaynida sifatga etibor bermay, faqat miqdor oshirish, hajmni kengaytirish jihatidan rivojlandi va soya ostida qolib ketdi. 1990 yillar boshida u ommaviy ravishda qoʻllanila boshlandi va katta yutuqlarga erishdi, oʻn yillikning oxirida esa dasturiy taʼminotni qayta ishlashda eng keng foydalaniladigan va bugungi kunda ham peshqadamlik qilayotgan tilga aylandi. Shuni anglash muhimki, C++ ni ishlab chiqilishi yangi dasturlash tilini yaratishga intilish hisoblanmaydi, balki faqatgina etarli darajada muvaffaqiyatli tilni takomillashtirayapti va toʻldirayapti. Bunday qarash, hozirda ham kompyuter tillarini rivojlantirishning yangi yoʻnalishlarida qoʻllanilayapti.""",
            'info_lang_php': """PHP haqida ma'lumotlar.:\n
        PHP Ma'lumotlar turlari

PHP dasturlash tilida o'zgaruvchilar har xil turdagi ma'lumotlarni saqlashi mumkin va har xil ma'lumotlar turlari turli xil ishlarni bajarishi mumkin.

PHP dasturlash tilida quyidagi ma'lumot turlari mavjud.
String
Integer
Float (o'nli kasrlar - double deb ham ataladi.)
Boolean
Massiv
Object
NULL
Resource
PHP String
Satr - bu "Hello world!" kabi belgilar ketma-ketligi. Satr ni bayon qilish uchun siz bir yoki ikki tirnoqdan foydalanishinigiz mumkin.

<?php
$x = "Hello world!";
$y = 'Hello world!';

echo $x;
echo "<br>";
echo $y;
?>
Hello world!
Hello world!
PHP Integer
Butun sonli ma'lumotlar turi -2,147,483,648 va 2,147,483,647 oralig'idagi o'nlik bo'lmagan sondir. Butun sonlar uchun quyidagicha qoilarni keltirishimiz mumkin.

Butun sonda kamida bitta raqam bo'lishi kerak
Butun sonda kasr boʻlmasligi kerak
Butun son musbat yoki manfiy bo'lishi mumkin
Butun sonlar oʻnlik (asos 10), oʻn oltilik (asos 16), sakkizlik (8-asos) yoki ikkilik (2-asos) yozuvlarida koʻrsatilishi mumkin.
Quyidagi misolda $x butun sondir. PHP var_dump() funksiyasi maʼlumotlar turi va qiymatini qaytaradi:

<?php
$x = 5985;
var_dump($x);
?>
PHP Float
o'nli kasrlarni ifodalash uchun ishlatiladi. Misol uchun 13.15

<?php
$x = 13.15;
?>
PHP Boolean
Mantiqiy ikki mumkin bo'lgan holatni ifodalaydi: TRUE yoki FALSE.

$x = true;
$y = false;
PHP massiv
Massiv bir o'zgaruvchi tipiga tegishli o'zida bir nechta qiymatni saqlaydi.

<?php
$monopoliya = array("spark","gentra","tracker");
var_dump($monopoliya);
?>""",
            'info_lang_javascript': """JavaScript haqida ma'lumotlar: \n
        JavaScript - bu interaktiv va dinamik veb-saytlarni yaratish uchun keng qo'llaniladigan dasturlash tili. U birinchi marta 1995 yilda Brendan Eich tomonidan ishlab chiqilgan va hozirda ECMAScript standartlari organi tomonidan qo'llab-quvvatlanadi. JavaScript barcha asosiy veb-brauzerlar tomonidan qo'llab-quvvatlanadigan yuqori darajali, talqin qilingan dasturlash tilidir.

JavaScript asosan veb-brauzerda ishlaydigan mijoz tomoni skriptlarini yaratish uchun ishlatiladi. Bu shuni anglatadiki, u serverda emas, balki foydalanuvchining kompyuterida bajariladi. Bu foydalanuvchi tajribasini tezroq va sezgirroq qilish imkonini beradi, chunki kod to'g'ridan-to'g'ri brauzerda serverga borishni talab qilmasdan ishlashi mumkin. Bundan tashqari, JavaScript-dan Node.js kabi texnologiyalar yordamida server tomonidagi skriptlarni yaratish uchun foydalanish mumkin.



JavaScript-ning eng mashhur qo'llanilishidan biri bu interaktiv veb-sahifalarni yaratishdir. Masalan, JavaScript-dan ochiladigan menyular, tasvir slayderlarini yaratish va shaklni tekshirish uchun foydalanish mumkin. Bundan tashqari, animatsiyalar, qalqib chiquvchi oynalar va modal oynalar kabi dinamik effektlarni yaratish uchun ham foydalanish mumkin. Bundan tashqari, JavaScript vazifalar ro'yxati va kalendarlar kabi veb-ilovalarni yaratish uchun ishlatilishi mumkin.

JavaScript odatda HTML va CSS kabi boshqa veb-texnologiyalar bilan birgalikda ishlatiladi. HTML veb-sahifaning tuzilishini ta'minlaydi, CSS esa maket va dizaynni yaratish uchun ishlatiladi. JavaScript veb-sahifaga interaktivlik va dinamik xatti-harakatlarni qo'shish uchun ishlatilishi mumkin.



JavaScript o'rganish uchun nisbatan oson til bo'lib, barcha asosiy veb-brauzerlar tomonidan qo'llab-quvvatlanadi. Sintaksis C va Java kabi boshqa dasturlash tillariga o'xshaydi va JavaScript-ni o'rganish va boshlashga yordam beradigan ko'plab manbalar mavjud. Bundan tashqari, Angular, React va Vue.js kabi ko'plab ramkalar va kutubxonalar mavjud bo'lib, ular ishlab chiqish jarayonini soddalashtirish va murakkab ilovalarni yaratishni osonlashtirish uchun ishlatilishi mumkin.

Shuni ta'kidlash kerakki, JavaScript mijoz tomoni tilidir, shuning uchun u foydalanuvchi kompyuterida ishlaydi. Bu shuni anglatadiki, kod foydalanuvchiga ko'rinadi va ular xohlasa, uni ko'rishi va o'zgartirishi mumkin. Bu xavfsizlik bilan bog'liq bo'lishi mumkin, shuning uchun har qanday foydalanuvchi kiritgan ma'lumotlarni serverga yuborishdan oldin tekshirish va tozalash muhim ahamiyatga ega.

Xulosa qilib aytganda, JavaScript kuchli dasturlash tili bo'lib, interaktiv va dinamik veb-sahifalar va veb-ilovalarni yaratishda keng qo'llaniladi. Uni o'rganish oson va barcha asosiy veb-brauzerlar tomonidan qo'llab-quvvatlanadi va boshlashingizga yordam beradigan ko'plab manbalar va ramkalar mavjud. Biroq, mijoz tomonidan skript yaratish bilan bog'liq xavfsizlik muammolarini yodda tutish kerak.

JavaScript bilan ishlashda quyidagi bir nechta narsalarni yodda tutish kerak:

1) JavaScript voqealarga asoslangan tildir, ya'ni kod tugmani bosish yoki sahifa yuklanishi kabi muayyan hodisalarga javoban ishlaydi. Bu yanada interaktiv va sezgir foydalanuvchi tajribasiga imkon beradi.

2) JavaScript erkin terilgan tildir, ya'ni siz o'zgaruvchini e'lon qilganingizda uning ma'lumotlar turini ko'rsatishingiz shart emas. Bu kodni yanada moslashuvchan qilishi mumkin, lekin disk raskadrovkani ham qiyinlashtirishi mumkin.

3) JavaScript - bu ob'ektga yo'naltirilgan til, ya'ni siz kodingizni tartibga solish va tuzilish uchun ob'ektlar va sinflarni yaratishingiz mumkin. Bu prototiplar va konstruktorlar yordamida amalga oshiriladi.

4) JavaScript-da turli xil o'rnatilgan funktsiyalar va ob'ektlarni ta'minlovchi boy standart kutubxona mavjud. Bunga massivlar, satrlar va sanalar, shuningdek, muntazam ifodalar va taymerlar kabi kengaytirilgan xususiyatlar kiradi.

5) JavaScript ko'pincha dinamik veb-ilovalarni yaratish uchun AJAX va JSON kabi boshqa texnologiyalar bilan birgalikda ishlatiladi. AJAX asinxron veb-sahifalarni yaratishga imkon beradi, ular sahifani yangilamasdan yangilanishi mumkin. JSON - bu server va mijoz o'rtasida ma'lumotlarni uzatish uchun tez-tez ishlatiladigan engil ma'lumot almashish formati.

6) JavaScript-dan React Native va Electron kabi texnologiyalar yordamida platformalararo ilovalar yaratish uchun ham foydalanish mumkin.

7) JavaScript jonli va faol hamjamiyatga ega, ya'ni o'rganish va boshlashga yordam beradigan ko'plab manbalar va ramkalar mavjud. Bundan tashqari, boshqa ishlab chiquvchilar bilan bog'lanishingiz va so'nggi tendentsiyalar va eng yaxshi amaliyotlardan xabardor bo'lishingiz mumkin bo'lgan ko'plab konferentsiyalar va uchrashuvlar mavjud.

8) JavaScript-da juda ko'p uchinchi tomon kutubxonalari va ramkalari mavjud bo'lib, ular ishlab chiqish jarayonini soddalashtirish va murakkab ilovalarni yaratishni osonlashtirish uchun ishlatilishi mumkin, masalan, Jquery, Lodash, axios, Moment.js va boshqalar.

9) Nihoyat, JavaScript doimiy ravishda rivojlanib bormoqda, yangi xususiyatlar va yangilanishlar muntazam ravishda chiqariladi. Til imkoniyatlaridan to‘liq foydalanish uchun eng so‘nggi yangiliklardan xabardor bo‘lish muhim."""
        }

        lang = query.data
        info = lang_info.get(lang, "Bu dasturlash tili haqida malumot mavjud emas.")
        query.edit_message_text(text=info, parse_mode='HTML')
    except Exception as e:
        print(f"Nomalum xatolik yuz berdi: {e}")

def send_libraries(update: Update, context: CallbackContext):
    try:
        query = update.callback_query
        query.answer()

        lang_libraries = {
            'libraries_lang_python': "Python Libraries:\n\n- NumPy\n- Pandas\n- Matplotlib\n- Requests",
            'libraries_lang_javascript': "JavaScript Libraries:\n\n- React\n- Angular\n- Vue\n- jQuery",
            'libraries_lang_java': "Java Libraries:\n\n- Spring\n- Hibernate\n- Apache Commons\n- Google Guava",
            'libraries_lang_cpp': "C++ Libraries:\n\n- Boost\n- Eigen\n- Poco\n- Qt",
            'libraries_lang_csharp': "C# Libraries:\n\n- .NET Core\n- Newtonsoft.Json\n- Dapper\n- AutoMapper",
            'libraries_lang_php': "PHP Libraries:\n\n- Laravel\n- Symfony\n- CodeIgniter\n- PHPUnit"
        }

        lang = query.data
        libraries = lang_libraries.get(lang, "Bu dasturlash tilining kitobxonasi haqida malumot mavjud emas.")
        query.edit_message_text(text=libraries)
    except Exception as e:
        print(f"Nomalum xatolik yuz berdi: {e}")

def main():
    try:
        updater = Updater("7036856675:AAHEfwWr1UotxwUYU5UO6JyVppvDOdOPw-o", use_context=True)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CallbackQueryHandler(langs, pattern='langs'))
        dp.add_handler(CallbackQueryHandler(language_info, pattern='^lang_'))
        dp.add_handler(CallbackQueryHandler(send_info, pattern='^info_'))
        dp.add_handler(CallbackQueryHandler(send_libraries, pattern='^libraries_'))

        updater.start_polling()
        updater.idle()
    except Exception as e:
        print(f"Nomalum xatolik yuz berdi: {e}")

if __name__ == '__main__':
    main()
