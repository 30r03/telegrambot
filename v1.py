from telegram.ext import Updater, CommandHandler,MessageHandler,Filters, CallbackContext,CallbackQueryHandler, ConversationHandler
from telegram import Update,InlineKeyboardMarkup,InlineKeyboardButton
from datetime import datetime

updater= Updater("5105491841:AAHoO1tUaEbAE3uNO_uf2TNqpgD-PfXtHas")
dp= updater.dispatcher
list_code=[]
groups=[]
names={}
p= {}
messages=[]
boss={}
n=0
n1=0
code=['66718181','66718182','66718183']
def start_handler(update:Update, context:CallbackContext):
    global n,p
    chat_id = update.message.chat_id
    if chat_id in p:
        update.message.reply_text("شما قبلاً وارد شدید\n"
                              "لطفا کد اختصاصی خود را وارد کنید:\n"
                              "کد اختصاصی را باید از سرگروهتان دریافت کنید\n")
    else:
        p[chat_id]=n
        n=n+1
        counter.append(0), counter1.append(0),counter2.append(0),counter3.append(0),counter4.append(0),counter5.append(0), counter6.append(0)
        counte.append(0),counte1.append(0)
        count.append(0),count1.append(0), count2.append(0), count3.append(0), count4.append(0), count5.append(0),count6.append(0)
        coun.append(0),coun1.append(0), coun2.append(0), coun3.append(0)
        cou.append(0),cou1.append(0),cou2.append(0)
        co.append(0), co1.append(0)
        cu.append(0), cu1.append(0), cu2.append(0),cu3.append(0),cu4.append(0),cu5.append(0),cu6.append(0)
        update.message.reply_text("سلام\n"
                              'به  اتاق فرار مجازی «مثبت کاذب» خوش آمدید.\n'
                              "لطفا کد اختصاصی خود را وارد کنید:\n"
                              "کد اختصاصی را باید از سرگروهتان دریافت کنید\n")
    return 2

def message_handler(update:Update, context:CallbackContext):
    global code, list_code, n1 , boss
    text = str(update.message.text)
    if text in code:
        chat_id = update.message.chat_id
        list_code.append(text)
        number = list_code.index(text)
        code.remove(text)
        groups.insert(number, [chat_id])
        boss [chat_id] = n1
        n1 += 1
        update.message.reply_text(
            'شما سرگروه هستید لطفا بعد از اطمینان از حضور تمام اعضا دستور night/ را وارد کرده تا بازی آغاز شود')
        update.message.reply_text('اسم خود را وارد کنید:')
        return 4

    elif text in list_code:
        number = list_code.index(text)
        chat_id = update.message.chat_id
        groups[number].append(chat_id)
        update.message.reply_text('اسم خود را وارد کنید:')
        update.message.reply_text(
            "منتظر باشید تا سرگروه بازی را شروع کند")
        return 4
    else:
        update.message.reply_text('در وارد کردن رمز دفت کنید')
        return 2

def message_handler2 (update:Update, context:CallbackContext):
    global groups
    chat_id = update.message.chat_id
    name = str(update.message.text)
    names[chat_id]=name
    bot = context.bot

    array = 0
    while array < len(groups):
        array1 = 0
        while array1 < len(groups[array]):
            if groups[array][array1] == chat_id:
                main_array = array
            array1 +=1
        array = array + 1
    for id in groups[main_array]:
        bot.send_message(id,"کلی منتظرت بودیم\n"+
                                  name)
    return 1

a = ['0', 'Fe', 'K', 'Na', 'Cu', '1', '2']
counter = []
counter1 = []
counter2 = []
counter3 = []
counter4 = []
counter5 = []
counter6 = []
def message_handler3 (update:Update, context:CallbackContext):
    global counters, keyboard, p , boss ,groups, message
    bot=context.bot
    chat_id=update.message.chat_id
    if chat_id in boss:
        total = boss.get(chat_id)
        for id in groups[total]:
            m = p.get(id)
            bot.send_message(id,'قوانین و نکات بازی :\n'
                              '(🚨⚠️حتما مطالعه کنید⚠️🚨)\n'
                              '\n'
                              '🎲 مثبت کاذب، یک بازی معمّاییه. شما در قالب یک داستان باید چند چالش معمایی رو پشت سر بذارید تا به انتهای بازی برسید.\n'
                              '\n'
                              '🔒 چالش‌های معمایی در واقع قفل‌هایی هستند که در طول بازی با اونا آشنا میشید. قفل‌ها انواع مختلفی دارن. معمولا با باز کردن یک قفل اطلاعات بیشتری به دست میارید که در ادامه بازی به دردتون میخوره.\n'
                              '\n'
                              '🚨هر قفل یک اسم داره(L1،L2،L3،...). در حین بازی زمانی که به قفلی بر خوردید میتونید روی قفل رمز وارد کنید. با توجّه به زمان محدودی که در کارسوق دارید پیشنهاد می‌کنیم برای هر قفل به صورت میانگین بیشتر از ۳۰ دقیقه وقت نگذارید. در کل مدیریت زمان بسیار نکته مهمّی در این بازی است. بعضی معمّاها سخت هستند و نیاز به زمان بیشتری برای حل دارند و بعضی دیگر آسان‌ترند و سریع‌تر حل می‌شوند🚨. \n'
                              '\n'
                              '🔓 معماها با روش‌های مختلفی حل میشوند. در طول بازی شما اطلاعاتی به شکل تصویر، فایل‌ متنی، صوتی و ... دریافت می‌کنید که حکم سرنخ رو برای شما دارن.\n'
                              'زمانی که پاسخ را وارد کردید بر روی دکمه باز شدن قفل کلیک کند. در صورت درست بودن رمز قفل برای شما باز خواهد شد\n'
                              '\n'
                              '♻️ قبل از هرچیز، تلگرام را به آخرین ورژن بروزرسانی‌ کنید.\n'
                              '\n'
                              '🔎🌐⁩ برای حل بعضی از معماها باید از انواع جستجو در اینترنت و ابزارهای مختلف آنلاین استفاده کنید.\n'
                              '\n'
                              '📱📱 در تمام طول بازی باید همواره در اتاق آنلاین کارسوق حضور داشته باشید. نبود اعضای گروه در اتاق آنلاین به معنای حذف آن گروه از کارسوق است.\n'
                              '\n'
                              '⌛️بازی زمان محدود و مشخصی دارد. دوباره تاکید می‌کنیم که زمانتان را خوب مدیریت کنید.\n'
                              '⚙️ دستگاههای با سیستم عامل ios برای بهره‌مندی از تمام امکانات ربات تگرام، باید به ورژن ۱۳.۲ و یا بالاتر بروزرسانی شده باشند.\n'
                              '⛔️ پس از شروع بازی، لطفا از پاک کردن هرگونه پیام داخل ربات، خودداری کنید.\n'
                              '\n'
                              '🗝 برای گرفتن راهنمایی، به معلم اتاقتان پیام خصوصی بدهید. در پیامتان شماره قفل (L1، L2،L3…) را بنویسید و درخواستتان را مطرح کنید.\n'
                              'گرفتن راهنمایی امتیاز منفی داره. تا جای ممکن سعی کنید راهنمایی نگیرید. در صورت درخواست راهنمایی توسط یکی از اعضای تیم، آن راهنمایی تنها برای فرد درخواست‌کننده ارسال خواهد شد، اما از امتیاز کل تیم کم می‌شود. پس قبل از درخواست راهنمایی حتما با هم هماهنگ کنید و پس از گرفتن راهنمایی آن را در اختیار دیگر دوستانتان نیز قرار دهید.\n'
                              '\n'
                              '✅ اگر یکی از اعضای تیم، پاسخ «درست» را وارد کند، پاسخ تنها برای همان فرد ثبت می‌شود. بنابراین اگر به پاسخ درست دست‌پیدا کردید مطمئن شوید که تمام هم‌گروهی‌هایتان نیز آن پاسخ را وارد کرده و وارد مرحله بعد شده اند.\n'
                              '\n'
                              '❓ هر مشکل و سوالی برایتان پیش آمد به پشتیانی پیام بدهید.\n')
            bot.send_message(id,'🎶 درصورت تمایل، می‌توانید موسیقی زیر را حین انجام بازی پخش کنید.')
            bot.send_audio(id, 'https://www.fesliyanstudios.com/download-link.php?src=i&id=118')
            bot.send_message(id,
        "بیمارستانی که مرکز زایمان بوده و برای اطفال تجهیز شده به دلیل مرگ نوزادان بسیاری در آن کاملا بسته می شود و به یک مکان متروک تبدیل می شود.\n"
        "ژانر بازی اسلشر است.\n"
        "پرستاری به اسم مریم شریفی در این بیمارستان کار میکند و جزو بهترین نیروهای کادر هست . این پرستار پس از ازدواج با یکی از اعضای بیمارستان و چند سالی زندگی مشترک باردار می شود.\n"
        "در همین بیمارستان به مراقبت های دوران بارداری تحت نظر پزشکان می پردازد اما به دلیل فشار کاری زیاد و ضعف جسمانی که پیدا کرده بود فرزندش را در ۵ ماهگی سقط می کند و پس از این حادثه دچار افسردگی و ناراحتی روحی می شود. نزد پزشک روانشناس می رود اما فایده ای ندارد. به دعانویسها و رمالها پناه میبرد اما فایده ای ندارد‌.بیماری روانی او روز به روز شدید تر می شود و او برای تسلی خود شروع به کشتن نوزادان بخش میکند...اما به شکلی که کسی متوجه آن نشود در وقتی که شیفت هست با ترساندن نوزادان بخش مراقبت های ویژه و کم و زیاد کردن اکسیژن آنها باعث ایجاد نوسانات شدید فشار خونی در آنها میشود و در آخر با تزریق دارویی ناشناس که همسرش در انباری خانه برای تحقیقاتش نگهداری میکرد آنها را به کام مرگ میکشاند.\n"
        "در پی شکایت های زیاد و پس از بررسی موضوع پلیس همسر او را مقصر شناخت و او را به اعدام محکوم کرد. همسر او از اعدام جان سالم بدر برد اما بطور کامل دیوانه شده و دائما با وسایل تیز مثل چاقو یا شیشه بدن خود را زخمی میکند. بیمارستان به دلیل این اخبار و عدم اعتماد مردم کاملا بسته شد.\n"
        "حالا دیگر پرستار به خانه نمی رود و اتاقی را در بیمارستان برای خود و همسرش درست کرده ...مخفیانه با همسرش به تنهایی در آنجا زندگی میکنند. الان پرستار و همسرش با صورتی پر از جراحت و زخم سالخورده شده اند. کار پرستار شده مراقبت از همسرش و درمان زخمهایش و البته اگر کسی وارد قلمرو دو نفره آنها شود...\n"
       )
            bot.send_message(id,"میخواهید امتحان کنید...؟")
            bot.send_photo(id,'https://www.uplooder.net/img/image/43/a416e99137964e3bb8b5c02cb399c140/photo-2021-03-23-15-40-53.jpg')
            bot.send_message(id, 'هنوز هوا تاریک نشده بود. وقتی رسیدند دم در مدرسه دیدند که در بازه. همه چراغ‌های مدرسه خاموش بود و مدرسه کاملا ساکت و تاریک بود.\n'
                              '«یه زنگ بهش بزن بگو ما تو مدرسه‌ایم»\n'
                              '«دارم زنگ می‌زنم. جواب نمی‌ده»\n'
                              'آرش و سیروس با نگرانی همدیگر رو نگاه کردند. ناگهان صدای زوزه و فریاد از ساختمان کلاس‌ها بلند شد. آرش و سیروس دویدند به سمت ساختمان. صدا از آزمایشگاه شیمی طبقه پایین می‌آمد\n'
                              'وارد آزمایشگاه شدند. هیچ نور و صدایی نبود. آرش چراغ‌قوه موبایلش رو روشن کرد.\n'
                              '«لعنتی، آنتن هم نمی‌ده. این‌ها چیه روی میز آزمایشگاه؟»\n'
                              'سیروس به تخته خیره شده بود «یه چیزایی این رو نوشته شده»\n'
                              'ناگهان در آزمایشگاه بسته شد. آرش هر چقدر زور زد نتوانست بازش کند «لعنتی قفل شده»\n')
            bot.send_photo(id,'https://www.uplooder.net/img/image/50/03228d85c2aa4e1d26a6325860489345/photo-2021-03-23-17-59-08.jpg')
            bot.send_photo(id,'https://www.uplooder.net/img/image/80/01b03ec6cc982038673b7cb38994b991/photo-2021-03-23-17-59-24.jpg')
            bot.send_photo(id,'https://www.uplooder.net/img/image/31/66e7710c65344e4a54721daedc6c2308/photo-2021-03-23-17-59-29.jpg')
            bot.send_photo(id,'https://www.uplooder.net/img/image/69/449a1e644a982f0587ebf4944ffadf19/photo-2021-03-23-17-59-19.jpg')
            bot.send_photo(id,'https://www.uplooder.net/img/image/16/8a1d939a78c024fdfc055e61c9689a0e/photo-2021-03-23-17-59-13.jpg')
            bot.send_photo(id,'https://www.uplooder.net/img/image/23/2a6a6e8c68e2878c2af1b6bf4df6a4c0/photo-2021-03-23-17-59-34.jpg')
            keyboard = [
            [InlineKeyboardButton(a[counters[0][m]], callback_data='0'),
            InlineKeyboardButton(a[counters[1][m]], callback_data='1'),
            InlineKeyboardButton(a[counters[2][m]], callback_data='2'),
            InlineKeyboardButton(a[counters[3][m]], callback_data='3'),
            InlineKeyboardButton(a[counters[4][m]], callback_data='4'),
            InlineKeyboardButton(a[counters[5][m]], callback_data='5'),
            InlineKeyboardButton(a[counters[6][m]], callback_data='6')],
            [InlineKeyboardButton('باز کردن قفل!🔐', callback_data='7'),
            InlineKeyboardButton('راهنمایی🆘', callback_data='39')]]
            reply_markup= InlineKeyboardMarkup(keyboard)
            message = bot.send_message(id,'🔒 L1 (روی مربع ها کلیک کنید)', reply_markup=reply_markup)
        return 1

counters = [counter, counter1, counter2, counter3, counter4, counter5, counter6]
def allbuttons(update:Update, context:CallbackContext):
    global keyboard, counters, p , message
    for i in range(7):
        query = update.callback_query
        chat_id = query.message.chat_id
        if query.data == str(i):
            m = p.get(chat_id)
            if counters[i][m] < 6:
                counters[i][m] +=1
            else:
                counters[i][m] = 0
            keyboard = [
                [InlineKeyboardButton(a[counters[0][m]], callback_data='0'),
                 InlineKeyboardButton(a[counters[1][m]], callback_data='1'),
                 InlineKeyboardButton(a[counters[2][m]], callback_data='2'),
                 InlineKeyboardButton(a[counters[3][m]], callback_data='3'),
                 InlineKeyboardButton(a[counters[4][m]], callback_data='4'),
                 InlineKeyboardButton(a[counters[5][m]], callback_data='5'),
                 InlineKeyboardButton(a[counters[6][m]], callback_data='6')],
                [InlineKeyboardButton('باز کردن قفل!🔐', callback_data='7'),
                 InlineKeyboardButton('راهنمایی🆘', callback_data='39')]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            bot = context.bot
            message = bot.edit_message_text(chat_id=query.message.chat_id,message_id=query.message.message_id,
                            text="🔒 L1 (روی مربع ها کلیک کنید)",reply_markup=reply_markup)
    return 1

r=0
def button39 (update:Update, context:CallbackContext):
    global r
    if r<5:
        query = update.callback_query
        chat_id = query.message.chat_id
        bot = context.bot
        bot.send_message(chat_id,"تخته چیزی را که می‌خواهی نشانت می‌دهد.\n"
                             "ترتیب واکنش‌پذیری عناصر و تک‌لپه یا دولپه بودن گیاهان را مشخص کن")
        r += 1
    else:
        query = update.callback_query
        chat_id = query.message.chat_id
        bot = context.bot
        bot.send_message(chat_id, 'ای بابا چقدر راهنمایی میخواهید بسه دیگه!')
    return 1


b=['0','1','2','3','4','5','6','7','8','9']
counte =[]
counte1=[]
def button7 (update:Update, context:CallbackContext):
    global keyboard, counters, counte,counte1, p, keyboard2, message
    query = update.callback_query
    chat_id = query.message.chat_id
    bot=context.bot
    m = p.get(chat_id)
    if query.data =='7' and counter[m] ==4 and counter1[m] ==1 and counter2[m] ==3 and counter3[m]==2 and counter4[m]==5 and counter5[m]==6 and counter6[m]==6:
        print (counters)
        array = 0
        nam=names.get(chat_id)
        while array < len(groups):
            array1 = 0
            while array1 < len(groups[array]):
                if groups[array][array1] == chat_id:
                    main_array = array
                array1 += 1
            array = array + 1
        print (main_array)
        for id in groups[main_array]:
            keyboard = [
                [InlineKeyboardButton(a[4], callback_data='0'),
                 InlineKeyboardButton(a[1], callback_data='1'),
                 InlineKeyboardButton(a[3], callback_data='2'),
                 InlineKeyboardButton(a[2], callback_data='3'),
                 InlineKeyboardButton(a[5], callback_data='4'),
                 InlineKeyboardButton(a[6], callback_data='5'),
                 InlineKeyboardButton(a[6], callback_data='6')],
                [InlineKeyboardButton('باز کردن قفل!🔐', callback_data='7'),
                 InlineKeyboardButton('راهنمایی🆘', callback_data='39')]]


            reply_markup = InlineKeyboardMarkup(keyboard)
            bot = context.bot

           bot.edit_message_text ( id , message_id = message.message_id ,
                            text="🔒 L1 (روی مربع ها کلیک کن)" , reply_markup = reply_markup)

            bot.send_message(id, nam+'آفرین\n')
            bot.send_message(id, 'درسته!بازشد.بزن بریم\n'
                                  'آرش و سیروس سریع دویدند به سمت بالا. ترسیده بودند و فقط می‌خواستند از مدرسه خارج شوند. اما در ساختمان قفل شده بود. دنبال راهی بودند برای اینکه قفل در رو بشکنند که صدای توپ‌بازی و فوتبال‌دستی از سالن ورزش مدرسه آمد.\n'
                                  'آرش گفت «من که نمی‌رم اون جا»\n'
                                  '«چیکار کنیم؟ همینجوری بمونیم پشت این در؟ بریم حداقل ببینیم کی تو سالن ورزشه»\n')
            bot.send_photo(id,
                       'https://www.uplooder.net/img/image/30/0ae485c6ed80bc4113b7584b5d60ca00/photo-2021-03-27-16-32-17.jpg')
            bot.send_message(id,
                         'هیچ کس در سالن ورزش نبود اما صدای برخورد توپ به زمین می‌آمد. بازیکن‌های فوتبال‌دستی آرام آرام حرکتشان کند شد و متوقف شدند. یک کاغذ هم روی زمین بود.')
            bot.send_photo(id,
                       'https://www.uplooder.net/img/image/90/18a43e68447206cc08a10ecf207de771/photo-2021-03-27-16-32-27.jpg')
            bot.send_photo(id,
                       'https://www.uplooder.net/img/image/73/e297dfede7e2a51e2807812458ca69c5/photo-2021-03-27-16-32-31.jpg')
            bot.send_photo(id,
                       'https://www.uplooder.net/img/image/87/e815b4663db9ffa18d08898257cc6b21/photo-2021-03-27-16-32-38.jpg')
            bot.send_photo(id,
                       'https://www.uplooder.net/img/image/67/ce576012c34750779d2d89d5b7d0c2cd/photo-2021-03-27-16-32-44.jpg')
            bot.send_photo(id,
                       'https://www.uplooder.net/img/image/40/7a00585522e2e55791beb4eaadacb5be/photo-2021-03-27-16-32-49.jpg')
            bot.send_photo(id,
                       'https://www.uplooder.net/img/image/1/e91d9c8ccc8c35ed29e7c87824d2e13f/photo-2021-03-27-16-33-05.jpg')
            bot.send_photo(id,
                       'https://www.uplooder.net/img/image/73/f8e976b3121d8926e4f17fa501a7c2dd/photo-2021-03-27-16-33-10.jpg')
            keyboard2 = [
                [InlineKeyboardButton(b[counte[m]], callback_data='8'),
                 InlineKeyboardButton(b[counte1[m]], callback_data='9')],
                [InlineKeyboardButton('باز کردن قفل!!🔐', callback_data='10'),
                 InlineKeyboardButton('راهنمایی🆘', callback_data='40')]]
            reply_markup = InlineKeyboardMarkup(keyboard2)
            bot.send_message(id, '🔒 L2(روی مربع ها کلیک کنید)', reply_markup=reply_markup)
        return 3
    else:
        return 1

counters2 = [counte, counte1]
def allbuttons2(update:Update, context:CallbackContext):
    for i in range(8,10):
        global keyboard2, counters2, p
        query = update.callback_query
        chat_id = query.message.chat_id
        if query.data == str(i):
            m = p.get(chat_id)
            if counters2[i-8][m] < 9:
                counters2[i-8][m] +=1
            else:
                counters2[i-8][m] = 0
            keyboard2 [0][i-8] = InlineKeyboardButton(b[counters2[i-8][m]], callback_data=str(i))
            reply_markup = InlineKeyboardMarkup(keyboard2)
            bot = context.bot
            bot.edit_message_text(chat_id=query.message.chat_id,message_id=query.message.message_id,
                            text="🔒 L2 (روی مربع ها کلیک کنید)",reply_markup=reply_markup)
    return 3

def button40 (update:Update, context:CallbackContext):
    global r
    if r < 3:
        query = update.callback_query
        chat_id = query.message.chat_id
        bot = context.bot
        bot.send_message(chat_id, "جهان را برعکس که می‌بینم پاهایم همچنان روی زمین است.\n"
                                  "تعداد بازیکنان برعکس روی فوتبال‌دستی")
        r += 1
    else:
        query = update.callback_query
        chat_id = query.message.chat_id
        bot = context.bot
        bot.send_message(chat_id, 'ای بابا چقدر راهنمایی میخواهید بسه دیگه!')

    return 3
c=['0','1','2','3','4','5','6','7','8','9']
count =[]
count1=[]
count2=[]
count3=[]
count4=[]
count5=[]
count6=[]

def button10 (update:Update, context:CallbackContext):
    global keyboard2 ,keyboard3, counters2, p, count , count1, count2, count3, count4 ,count5 , count6
    query = update.callback_query
    chat_id = query.message.chat_id
    bot = context.bot
    m = p.get(chat_id)
    if counters2 [0][m] ==2 and counters2[1][m] ==8:
        bot.send_message(chat_id,
                         'سیروس گفت «شاید یکی از معلم‌ها در خطره! باید بریم ببینیم کمد شماره ۲۸ برای کدوم معلمه. قضیه جدی‌تر از این حرف‌هاست»\n'
                         '«خودمون رو انداختیم تو چه مخمصه‌ای!»\n'
                         'با هم رفتند اتاق معلم‌ها. کمدها را بررسی کردند و دیدند که کمد شماره ۲۸ درش بازه. کمد ۲۸، کمد مسئول کتابخانه بود. آقای طاهرزاده یک کاغذ توی کمد گذاشته بود.\n')
        bot.send_photo(chat_id,
                       'https://www.uplooder.net/img/image/52/67cc74b7473c2a3b3a704839d8375453/photo-2021-04-02-22-45-12.jpg')
        bot.send_photo(chat_id,
                       'https://www.uplooder.net/img/image/54/5516a7e9f963c680b5eddde7b8771742/photo-2021-04-02-22-45-42.jpg')
        bot.send_photo(chat_id,
                       'https://www.uplooder.net/img/image/41/fb5a64053ace60d86937182218c9b0f0/photo-2021-04-02-22-45-33.jpg')
        bot.send_photo(chat_id,
                       'https://www.uplooder.net/img/image/79/6a35192eb73ef102022df69d0db13957/photo-2021-04-02-22-45-38.jpg')
        bot.send_photo(chat_id,
                       'https://www.uplooder.net/img/image/26/bf958a8d8e241168d7553af705b349d8/photo-2021-04-02-22-45-47.jpg')
        bot.send_message(chat_id, 'آرش گفت «بریم کتابخونه؟»\n'
                                  '«آره دیگه. در ساختمون که قفله. کار دیگه‌ای نمی‌شه کرد.»\n'
                                  'چراغ‌های کتابخانه خاموش و روشن می‌شدند. چند کتاب روی میز کتابخانه بودند.\n'
                                  '«ببین! کامپیوتر واقعا روشنه»\n'
                                  '«خب ببین چی توشه»\n'
                                  '«قفله!»\n'
                                  'قسمتی پاره شده از کتاب شیمی عمومی مورتیمر و یک جلد از کتاب «تکامل چیست» روی میز افتاده بودند.\n'
                                  '«فکر کنم آقای طاهرزاده می‌خواسته اینجوری رمز کامپیوتر رو بهمون بگه»\n')
        bot.send_photo(chat_id, 'https://www.uplooder.net/img/image/87/c5b9b2b0564b4a78224b55710add28b6/photo-2021-04-02-13-02-41.jpg')
        bot.send_photo (chat_id,'https://www.uplooder.net/img/image/55/df3ea605f68eae29b8fb0507676055a4/photo-2021-04-29-11-50-15.jpg')
        bot.send_document(chat_id,'https://files.smallpdf.com/files/0b1feff8b281421d8bd7fe9df4d23248-compressed-401639a1e5cab692ed5164577defac0e.pdf?name=what-evolution-is-compressed.pdf')
        keyboard3 = [[InlineKeyboardButton(c[count[m]], callback_data='11'), InlineKeyboardButton(c[count1[m]], callback_data='12'),
                      InlineKeyboardButton(c[count2[m]], callback_data='13'), InlineKeyboardButton(c[count3[m]], callback_data='14'),
                      InlineKeyboardButton(c[count4[m]], callback_data='15'),
                      InlineKeyboardButton(c[count5[m]], callback_data='16'), InlineKeyboardButton(c[count6[m]], callback_data='17')],
                     [InlineKeyboardButton('باز کردن قفل!!🔐', callback_data='18'),
                      InlineKeyboardButton('راهنمایی🆘', callback_data='41')]]
        reply_markup = InlineKeyboardMarkup(keyboard3)
        bot.send_message(chat_id, '🔒 L3(روی مربع ها کلیک کنید)', reply_markup=reply_markup)
        return 5
    else:
        return 3
counters3 = [count, count1, count2, count3, count4, count5, count6]
def allbuttons3(update:Update, context:CallbackContext):
    for i in range(11, 18):
        global keyboard3, counters3, p
        query = update.callback_query
        chat_id = query.message.chat_id
        if query.data == str(i):
            m = p.get(chat_id)
            if counters3[i-11][m] < 9:
                counters3[i-11][m] +=1
            else:
                counters3[i-11][m] = 0
            keyboard3 [0][i-11] = InlineKeyboardButton(c[counters3[i-11][m]], callback_data=str(i))
            reply_markup = InlineKeyboardMarkup(keyboard3)
            bot = context.bot
            bot.edit_message_text(chat_id=query.message.chat_id,message_id=query.message.message_id,
                            text="🔒 L3 (روی مربع ها کلیک کنید)",reply_markup=reply_markup)
    return 5

def button41 (update:Update, context:CallbackContext):
    global r
    if r < 3:
        query = update.callback_query
        chat_id = query.message.chat_id
        bot = context.bot
        bot.send_message(chat_id, "جهان را برعکس که می‌بینم پاهایم همچنان روی زمین است.\n"
                                  "تعداد بازیکنان برعکس روی فوتبال‌دستی")
        r += 1
    else:
        query = update.callback_query
        chat_id = query.message.chat_id
        bot = context.bot
        bot.send_message(chat_id, 'ای بابا چقدر راهنمایی میخواهید بسه دیگه!')
    return 5

d = ['➡', '⬅', '⬆', '⬇', '↗', '↘', '↙','↖']
coun = []
coun1 = []
coun2 = []
coun3 = []

def button18 (update:Update,context:CallbackContext):
    global keyboard4, coun, coun1, coun2, coun3, counters3
    query = update.callback_query
    chat_id = query.message.chat_id
    bot = context.bot
    m=p.get(chat_id)
    if counters3[0][m] ==1 and counters3[1][m] ==3 and counters3[2][m] == 3 and counters3[3][m]==8 and counters3[4][m]==8 and counters3[5][m] ==0 and counters3[6][m] == 2:
        bot.send_message(chat_id, '«درسته! قفل باز شد!» \n'
                                  '«این چیه؟ وبلاگ آقای طاهرزادست؟» \n'
                                  '«آره احتمالا. چه علایق جالبی هم داره! نجوم و زنبورها!»')
        bot.send_photo(chat_id,
                       'https://www.uplooder.net/img/image/97/7db077ff06914d15d9f272eb50c0590a/photo-2021-04-02-15-26-18.jpg')
        bot.send_message(chat_id, 'ناگهان صدای زوزه و فریاد از طبقه بالا آمد. سیروس و آرش دویدند به سمت راه پله‌ها\n'
                                  '«صدا از پشت بوم میاد!»\n'
                                  'وقتی به پشت بوم رسیدند پشت در برگه‌ای را دیدند. آرش گفت «فکر کنم این نقشه پشت بومه. انگار یکی می‌خواد بهمون یه جای خاصی رو نشون بده» \n'
                                  '«از کدوم مسیر باید بریم؟» \n'
                                  'آرش کمی فکر کرد. «ساعت چنده؟»\n'
                                  '«۹ شده…»\n')
        bot.send_photo(chat_id,
                       'https://www.uplooder.net/img/image/68/c1aeb8fedf8cd5657c4dbe6442cb7e1d/photo-2021-04-03-22-45-37.jpg')
        keyboard4 = [
            [InlineKeyboardButton(d[coun[m]], callback_data='19'), InlineKeyboardButton(d[coun1[m]], callback_data='20'),
             InlineKeyboardButton(d[coun2[m]], callback_data='21'), InlineKeyboardButton(d[coun3[m]], callback_data='22')],
            [InlineKeyboardButton('باز کردن قفل!!🔐', callback_data='23'),
             InlineKeyboardButton('راهنمایی🆘', callback_data='42')]]
        reply_markup = InlineKeyboardMarkup(keyboard4)
        bot.send_message(chat_id, '🔒 L4(روی مربع ها کلیک کنید)', reply_markup=reply_markup)
        return 7
    else:
        return 5
counters4 = [coun, coun1, coun2, coun3]
def allbuttons4(update:Update, context:CallbackContext):
    for i in range(19, 23):
        global keyboard4, counters4, p
        query = update.callback_query
        chat_id = query.message.chat_id
        if query.data == str(i):
            m = p.get(chat_id)
            if counters4[i-19][m] < 7:
                counters4[i-19][m] +=1
            else:
                counters4[i-19][m] = 0
            keyboard4 [0][i-19] = InlineKeyboardButton(d[counters4[i-19][m]], callback_data=str(i))
            reply_markup = InlineKeyboardMarkup(keyboard)
            bot = context.bot
            bot.edit_message_text(chat_id=query.message.chat_id,message_id=query.message.message_id,
                            text="🔒 L4 (روی مربع ها کلیک کنید)",reply_markup=reply_markup)
            return 7

def button42 (update:Update, context:CallbackContext):
    global r
    query = update.callback_query
    chat_id = query.message.chat_id
    bot = context.bot
    bot.send_message(chat_id,"برو سراغ استاد راهنما!")
    r +=1
    return 7
e = ['A', 'V', 'B', 'C', 'K', 'D', 'F','H']
cou = []
cou1 = []
cou2 = []
def button23 (update:Update, context:CallbackContext):
    global keyboard5,cou,cou1,cou2
    query = update.callback_query
    chat_id = query.message.chat_id
    bot = context.bot
    m = p.get(chat_id)
    if coun ==3 and coun1 ==1 and coun2 == 2 and coun3==4:
        bot.send_message(chat_id, '«درسته! اونجا یه پنجرست!»\n'
                                  'سیروس داشت فکر می‌کرد. «خب که چی؟ الان یه پنجره بهمون نشون داده شده» \n'
                                  'آرش که رفته بود به سمت پنجره با ترس و لرز سرش رو به سمت سیروس برگردوند «بیا نگاه کن!»\n'
                                  '«این که آزمایشگاه شیمیه!  کی تو آزمایشگاهه؟»\n'
                                  '«باید بریم اونور» \n'
                                  '«چجوری؟ در ساختمون قفل شده»\n'
                                  '«پیدا می‌کنیم قفلش رو، باید بفهمیم داستان چیه» \n'
                                  'هر دو از پله‌ها پایین آمدند تا به در ساختمان کلاس‌ها رسیدند.\n'
                                  'آرش گفت «این دفعه قفلش فرق داره. عددی نیست. حرفیه. اونم انگلیسی!»\n'
                                  'سیروس غرق در فکر بود. چه کسی اون ساعت توی آزمایشگاه شیمیه؟\n')
        bot.send_video(chat_id,
                       'https://hajifirouz3.cdn.asset.aparat.com/aparat-video/d31d981ecc357fea55f8d49bd94c435831968004-480p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6ImI3YTQ4YzZlYTQwZDMzZWY0YWQ3NDdhNTU5ZmYxMjUzIiwiZXhwIjoxNjE3ODc2MzkxLCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.gfBqnHwznGdl888YAGInSN4kg384t2cj5QJyigmS9UY')
        keyboard5 = [
            [InlineKeyboardButton(e[cou[m]], callback_data='24'), InlineKeyboardButton(e[cou1[m]], callback_data='25'),
             InlineKeyboardButton(e[cou2[m]], callback_data='26')],
            [InlineKeyboardButton('باز کردن قفل!!🔐', callback_data='27'),
             InlineKeyboardButton('راهنمایی🆘', callback_data='43')]]

        reply_markup = InlineKeyboardMarkup(keyboard5)
        bot.send_message(chat_id, '🔒 L5(روی مربع ها کلیک کنید)', reply_markup=reply_markup)
        return 9
    else:
        return 7

counters5 = [cou, cou1, cou2]

def allbuttons5(update:Update, context:CallbackContext):
    for i in range(24, 27):
        global keyboard5, counters5, p
        query = update.callback_query
        chat_id = query.message.chat_id
        if query.data == str(i):
            m = p.get(chat_id)
            if counters5[i-24][m] < 7:
                counters5[i-24][m] +=1
            else:
                counters5[i-24][m] = 0
            keyboard5 [0][i-24] = InlineKeyboardButton(e[counters5[i-24][m]], callback_data=str(i))
            reply_markup = InlineKeyboardMarkup(keyboard)
            bot = context.bot
            bot.edit_message_text(chat_id=query.message.chat_id,message_id=query.message.message_id,
                            text="🔒 L5 (روی مربع ها کلیک کنید)",reply_markup=reply_markup)
            return 9

def button43 (update:Update, context:CallbackContext):
    global r
    query = update.callback_query
    chat_id = query.message.chat_id
    bot = context.bot
    bot.send_message(chat_id,"برو سراغ استاد راهنما!")
    r +=1
    return 9

f=['Li','Na','H','He']
co=[]
co1=[]
def button27 (update:Update, context:CallbackContext):
    global keyboard6, co1, co
    if cou ==2 and cou1 ==0 and cou2 == 3 :
        query = update.callback_query
        chat_id = query.message.chat_id
        bot = context.bot
        bot.send_message(chat_id, 'قفل در را باز کردند. و وارد حیاط شدند. هوا انقدر تاریک بود که تقریبا هیچ چیز را نمی‌دیدند. حیاط با وقتی که وارد مدرسه شده بودند تفاوت کرده بود. جای ناخن روی دیوارها و زمین افتاده بود. صدایی از گوشی سیروس بلند شد. \n'
                                 '«چی نوشته؟»\n'
                                  '«یه متن عجیبه. از آقای افشار!»\n'
                                  '«آقای افشار؟»\n'
                                  '«نوشته که نور ستاره‌ها خیلی حرف‌ها برای گفتن داره. حتی ترکیبات توی ستاره‌ها رو هم می‌شه با نورشون فهمید.»\n'
                                  'آرش بی‌اراده آسمون رو نگاه کرد. پر از ستاره‌های چشمک‌زن. هیچ‌وقت آسمون مدرسه به این قشنگی نشده بود.\n'
                                  '«یه عکس هم برام فرستاده. جالبه»\n'
                                  '«نکنه آقای افشار هم تو خطر باشه؟ سریع بریم آزمایشگاه شیمی!»\n'
                                  'هر دو نفر دویدند و به سمت ساختمان آزمایشگاه‌ها رفتند. اما باز هم در قفل بود.\n'
                                  'آرش عصبانی شده بود «دوباره؟»\n'
                                  'سیروس به عکسی که آقای افشار فرستاده بود نگاه می‌کرد.\n')
        bot.send_photo(chat_id,
                       'https://www.uplooder.net/img/image/58/37804678ebd24418f5b70f77a02bf2a0/e97a9sdcj2pz.png')
        keyboard6 = [
            [InlineKeyboardButton(f[co[m]], callback_data='28'), InlineKeyboardButton(f[co1[m]], callback_data='29')],
            [InlineKeyboardButton('باز کردن قفل!!🔐', callback_data='30'),
             InlineKeyboardButton('راهنمایی🆘', callback_data='44')]]
        reply_markup = InlineKeyboardMarkup(keyboard6)
        bot.send_message(chat_id, '🔒 L6(روی مربع ها کلیک کنید)', reply_markup=reply_markup)
        return 11
    else:
        return 9

counters6 = [co, co1]
def allbuttons6(update:Update, context:CallbackContext):
    for i in range(28, 30):
        global keyboard6, counters6, p
        query = update.callback_query
        chat_id = query.message.chat_id
        if query.data == str(i):
            m = p.get(chat_id)
            if counters6[i-28][m] < 2:
                counters6[i-28][m] +=1
            else:
                counters6[i-28][m] = 0
            keyboard6 [0][i-28] = InlineKeyboardButton(f[counters6[i-28][m]], callback_data=str(i))
            reply_markup = InlineKeyboardMarkup(keyboard6)
            bot = context.bot
            bot.edit_message_text(chat_id=query.message.chat_id,message_id=query.message.message_id,
                            text="🔒 L6 (روی مربع ها کلیک کنید)",reply_markup=reply_markup)
            return 11

def button44 (update:Update, context:CallbackContext):
    global r
    query = update.callback_query
    chat_id = query.message.chat_id
    bot = context.bot
    bot.send_message(chat_id,"برو سراغ استاد راهنما!")
    r +=1
    return 11

g=['1','0','C','H','8','V','D','4','5']
cu=[]
cu1=[]
cu2=[]
cu3=[]
cu4=[]
cu5=[]
cu6=[]

def button30 (update:Update, context:CallbackContext):
    global keyboard7 , cu,cu1,cu2,cu3,cu4,cu5,cu6
    if co ==2 and co1 ==3:
        query = update.callback_query
        chat_id = query.message.chat_id
        bot = context.bot
        bot.send_message(chat_id,
                         'بالاخره در ساختمان آزمایشگاه‌ها را باز کردند. ترسیده بودند. آرام از پله‌ها بالا رفتند.\n'
                         'در کمال تعجب دیدند که در آزمایشگاه زیست و شیمی باز است.\n'
                         'آرش گفت «من می‌رم آزمایشگاه زیست رو ببینم. تو برو شیمی رو ببین.» \n'
                         '«باشه، مراقب باش»\n'
                         'آرش و سیروس از هم جدا شدند و هر کدام وارد یکی از آزمایشگاه‌ها شدند.\n'
                         'آزمایشگاه‌ها تاریک بود و نمی‌شد چراغ‌ها را روشن کرد. ناگهان درِ هر دو آزمایشگاه بسته شد.\n'
                         '«چی شد؟ سیروس خوبی؟»\n'
                         '«آره من خوبم. در آزمایشگاه قفل شده»\n'
                         'ناگهان صدای ترسناکی از راهرو آمد.\n')
        bot.send_video(chat_id,
                       'https://hw7.cdn.asset.aparat.com/aparat-video/300c67f5018548e8ec5f8eb58e0f4afd32770689-240p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6ImY4MGE3ZmQ5Mzk2MWYzNjIxYmIyMzE2MmVlMmNmZjk3IiwiZXhwIjoxNjE5NzE0MDQ1LCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.J0UJFF1dDNON1SvGXLq1Yt6HmDIX6wXm45kg30SZ-5M')
        bot.send_message(chat_id,
                         'آرش ترسیده بود، عرق کرده بود. توی آزمایشگاه زیست دنبال هر چیزی می‌گشت تا بتونه رمز آزمایشگاه زیست رو پیدا کنه. روی یکی از میزها یک خفاش بود. کنار خفاش هم یک متن انگلیسی بود و چند لام میکروسکوپ که نمونه خون خفاش روشون بود. باید هر چه زودتر قفل آزمایشگاه زیست رو پیدا می‌کرد')
        bot.send_photo(chat_id,
                       'https://www.uplooder.net/img/image/61/d5ed542ec39f9a64ea2467e810a91f67/photo-2021-04-09-16-42-01.jpg')
        bot.send_photo(chat_id,
                       'https://www.uplooder.net/img/image/55/843d860ab4ee2513bd0b5b11e1279c3c/photo-2021-04-09-16-42-06.jpg')
        bot.send_photo(chat_id,
                       'https://www.uplooder.net/img/image/92/225f32c14a885041e7b1c0a9435859f0/photo-2021-04-09-16-41-57.jpg')
        bot.send_photo(chat_id,
                       'https://www.uplooder.net/img/image/54/1353f968983b72fcf2b4a77d47883484/photo-2021-04-09-16-42-12.jpg')
        bot.send_photo (chat_id,'https://www.uplooder.net/img/image/37/10f0bd8d2bbbbc2c5e222e8a1622aa21/download.png')


        bot.send_message(chat_id,'همزمان سیروس در آزمایشگاه شیمی سردرگم شده. همه جای آزمایشگاه را می‌گشت. برق آزمایشگاه رفته بود و همه جا را خاک گرفته بود. بوی تندی به مشامش می‌رسید. جسد کبوتری را هم در آزمایشگاه پیدا کرد.  به ذهنش آمد «نکنه سرنوشت ما هم مثل همین کبوتره بشه! نکنه واقعا یه موجودی توی مدرسه وجود داره!»\n'
                                 'غرق در همین افکار بود که برگه‌ای را کف آزمایشگاه دید. تمام فکر و ذکرش این بود که قفل را باز کند.\n')
        bot.send_photo(chat_id,'https://www.uplooder.net/img/image/81/70a5c454da344e9514c4c0d50c9e2bfc/photo-2021-04-29-11-50-15.jpg')
        bot.send_photo(chat_id,'https://www.uplooder.net/img/image/38/97dc750002bf537fbdd6e88803c1dbbd/photo-2021-04-29-12-07-04.jpg')
        bot.send_photo(chat_id,'https://www.uplooder.net/img/image/94/3b44b0f31017dcd09544cbae5f2cddb6/photo-2021-04-29-12-13-56.jpg')
        bot.send_photo(chat_id,'https://www.uplooder.net/img/image/58/b23ddd5d6271d82b08a3af9cd16b4a52/photo-2021-04-29-12-14-00.jpg')
        bot.send_photo(chat_id,'https://www.uplooder.net/img/image/37/28c25a7b217274fa6d193e1eee02c8f9/photo-2021-04-29-12-14-05.jpg')
        bot.send_photo(chat_id, 'https://www.uplooder.net/img/image/91/8749908321c4f5dac0303d74e524c0dd/0001.jpg')
        bot.send_photo(chat_id, 'https://www.uplooder.net/img/image/23/9ee75ec524d82339075b8db971a21ae7/0002.jpg')
        bot.send_message(chat_id, 'صدای آرش در راهرو پیچید «این قفل جای ۷تا رمز داره  ولی من فقط چهارتای اوّل رو می‌تونم بزنم»\n'
                                  'سیروس گفت «من هم فقط سه‌تای دوم رو می‌تونم بزنم»\n'
                                  'با خودشان فکر می‌کردند. واضح است، ۴ رمز اول برای معمای آزمایشگاه زیست و ۳تای بعدی برای معمای آزمایشگاه شیمی است…\n')
        keyboard7 = [[InlineKeyboardButton(g[cu[m]], callback_data='31'), InlineKeyboardButton(g[cu1[m]], callback_data='32'),
                      InlineKeyboardButton(g[cu2[m]], callback_data='33'),
                      InlineKeyboardButton(g[cu3[m]], callback_data='34'),
                      InlineKeyboardButton(g[cu4[m]], callback_data='35'),
                      InlineKeyboardButton(g[cu5[m]], callback_data='36'),
                      InlineKeyboardButton(g[cu6[m]], callback_data='37')],
                     [InlineKeyboardButton('باز کردن قفل!!🔐', callback_data='38'),
                      InlineKeyboardButton('راهنمایی🆘', callback_data='45')]]
        reply_markup = InlineKeyboardMarkup(keyboard7)
        bot.send_message(chat_id, '🔒 L7(روی مربع ها کلیک کنید)', reply_markup=reply_markup)
        return 13
    else:
        return 11
counters7 = [cu, cu1, cu2, cu3, cu4, cu5, cu6]
def allbuttons7(update:Update, context:CallbackContext):
    for i in range(31, 37):
        global keyboard7, counters7, p
        query = update.callback_query
        chat_id = query.message.chat_id
        if query.data == str(i):
            m = p.get(chat_id)
            if counters7[i-31][m] < 6:
                counters7[i-31][m] +=1
            else:
                counters7[i-31][m] = 0
            keyboard7 [0][i-31] = InlineKeyboardButton(g[counters7[i-31][m]], callback_data=str(i))
            reply_markup = InlineKeyboardMarkup(keyboard)
            bot = context.bot
            bot.edit_message_text(chat_id=query.message.chat_id,message_id=query.message.message_id,
                            text="🔒 L7 (روی مربع ها کلیک کنید)",reply_markup=reply_markup)
            return 13

def button45 (update:Update, context:CallbackContext):
    global r
    query = update.callback_query
    chat_id = query.message.chat_id
    bot = context.bot
    bot.send_message(chat_id,"برو سراغ استاد راهنما!")
    r +=1
    return 13


def button38 (update:Update, context:CallbackContext):
    global r
    if cu ==0 and cu1 ==4 and cu2==1 and cu3==0 and cu4==2 and cu5==3  and cu6==0 :
        query = update.callback_query
        w = query.message.chat_id
        chat_id = query.message.chat_id
        bot = context.bot
        bot.send_message(chat_id,'قفل‌ها باز  شد و هر دو از آزمایشگاه‌ها بیرون آمدند. سایه‌ای را دیدند که از پلّه‌ها پایین رفت. دویدند و دنبالش کردند. اما وقتی وارد حیاط شدند کسی در حیاط نبود.\n '
                                 'تنها راه ممکن خروج از مدرسه بود. چه اتّفاقی افتاده بود؟ در مدرسه چه شده بود؟ آن صدا از کی بود؟\n'
                                 'آرش گفت «بریم. سریع‌تر از مدرسه بریم بیرون.»\n'
                                 '«آره فقط بریم. باید زنگ بزنم و حال آقای افشار رو هم بپرسم.»\n'
                                 'از مدرسه رفتند بیرون. هیچ‌کدامشان تا چند شب خوابشان نبرده بود. تمام فکر و ذکرشان این شده بود که شب‌ها در مدرسه چه می‌شود؟ از آن به بعد در اتاق معلّمان هر وقت بحثی در این مورد می‌شد سکوت می‌کردند. حتی نمی‌خواستند به همدیگر نگاه کنند\n'
                                 'هنوز هیچ‌کس نمی‌داند که چه شده بود. چرا آن شب آن اتّفاقات افتاد و آیا باز هم تکرار می‌شود یا نه.\n'
                                 'چند ماه بعد تلفن آرش زنگ خورد. ساعت ۹ شب بود «سلام سیروس. چی شده؟»\n'
                                 '«سلام. یکی از معلّم‌ها بهم زنگ زده. می‌گه صدای غرّش و خرناس از توی آزمایشگاه فیزیک می‌شنوه…»\n'
                                 '\n'
                                 '\n'
                                    'پایان')
        v= str (r+123)
        now = datetime.now()
        z = str(now.strftime('%d/%m/%y , %H:%M:%S'))
        bot.send_message(chat_id,
                         'تبریک می‌گوییم! شما اتاق فرار شبی در مدرسه را تمام کردید.\n'
                         'کد زیر را به معلّم اتاق‌تان تحویل دهید تا امتیازات شما ثبت شود.')
        bot.send_message(chat_id, z)
        bot.send_message(chat_id,v )

    else:
        return 13


handler = ConversationHandler(entry_points=[CommandHandler('start',start_handler)],
                            states={
                                    2:[MessageHandler (Filters.text, message_handler)],
                                    4:[MessageHandler (Filters.text, message_handler2)],
                                    1:[CommandHandler('night',message_handler3),
                                        CallbackQueryHandler(allbuttons,pattern='^'+str(0)+'$'),
                                       CallbackQueryHandler(allbuttons,pattern='^'+str(1)+'$'),
                                       CallbackQueryHandler(allbuttons,pattern='^'+str(2)+'$'),
                                       CallbackQueryHandler(allbuttons,pattern='^'+str(3)+'$'),
                                       CallbackQueryHandler(allbuttons,pattern='^'+str(4)+'$'),
                                       CallbackQueryHandler(allbuttons,pattern='^'+str(5)+'$'),
                                       CallbackQueryHandler(allbuttons,pattern='^'+str(6)+'$'),
                                       CallbackQueryHandler(button7,pattern='^'+str(7)+'$'),
                                       CallbackQueryHandler(button39,pattern='^'+str(39)+'$'),
                                       ],
                                    3:[CallbackQueryHandler(allbuttons2,pattern='^'+str(8)+'$'),
                                       CallbackQueryHandler(allbuttons2,pattern='^'+str(9)+'$'),
                                       CallbackQueryHandler(button10,pattern='^'+str(10)+'$'),
                                       CallbackQueryHandler(button40,pattern='^'+str(40)+'$'),
                                       ],
                                    5:[CallbackQueryHandler(allbuttons3,pattern='^'+str(11)+'$'),
                                       CallbackQueryHandler(allbuttons3,pattern='^'+str(12)+'$'),
                                       CallbackQueryHandler(allbuttons3,pattern='^'+str(13)+'$'),
                                       CallbackQueryHandler(allbuttons3,pattern='^'+str(14)+'$'),
                                       CallbackQueryHandler(allbuttons3,pattern='^'+str(15)+'$'),
                                       CallbackQueryHandler(allbuttons3,pattern='^'+str(16)+'$'),
                                       CallbackQueryHandler(allbuttons3,pattern='^'+str(17)+'$'),
                                       CallbackQueryHandler(button18,pattern='^'+str(18)+'$'),
                                       CallbackQueryHandler(button41,pattern='^'+str(41)+'$'),
                                       ],
                                    7:[CallbackQueryHandler(allbuttons4,pattern='^'+str(19)+'$'),
                                       CallbackQueryHandler(allbuttons4,pattern='^'+str(20)+'$'),
                                       CallbackQueryHandler(allbuttons4,pattern='^'+str(21)+'$'),
                                       CallbackQueryHandler(allbuttons4,pattern='^'+str(22)+'$'),
                                       CallbackQueryHandler(button23,pattern='^'+str(23)+'$'),
                                       CallbackQueryHandler(button42,pattern='^'+str(42)+'$')
                                       ],
                                    9:[CallbackQueryHandler(allbuttons5,pattern='^'+str(24)+'$'),
                                        CallbackQueryHandler(allbuttons5,pattern='^'+str(25)+'$'),
                                        CallbackQueryHandler(allbuttons5,pattern='^'+str(26)+'$'),
                                        CallbackQueryHandler(button27,pattern='^'+str(27)+'$'),
                                       CallbackQueryHandler(button43,pattern='^'+str(43)+'$')
                                        ],
                                    11:[CallbackQueryHandler(allbuttons6,pattern='^'+str(28)+'$'),
                                       CallbackQueryHandler(allbuttons6,pattern='^'+str(29)+'$'),
                                       CallbackQueryHandler(button30,pattern='^'+str(30)+'$'),
                                        CallbackQueryHandler(button44,pattern='^'+str(44)+'$')
                                        ],
                                    13:[CallbackQueryHandler(allbuttons7,pattern='^'+str(31)+'$'),
                                       CallbackQueryHandler(allbuttons7,pattern='^'+str(32)+'$'),
                                       CallbackQueryHandler(allbuttons7,pattern='^'+str(33)+'$'),
                                       CallbackQueryHandler(allbuttons7,pattern='^'+str(34)+'$'),
                                       CallbackQueryHandler(allbuttons7,pattern='^'+str(35)+'$'),
                                       CallbackQueryHandler(allbuttons7,pattern='^'+str(36)+'$'),
                                       CallbackQueryHandler(allbuttons7,pattern='^'+str(37)+'$'),
                                       CallbackQueryHandler(button38,pattern='^'+str(38)+'$'),
                                        CallbackQueryHandler(button45,pattern='^'+str(45)+'$')
                                       ],
                                    },

                            fallbacks=[CommandHandler('cancel',start_handler)]
                              )

dp.add_handler(handler)
updater.start_polling()
updater.idle()