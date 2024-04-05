import asyncio

import sys

from aiogram.client.default import DefaultBotProperties
from aiogram.methods.send_video import SendVideo
from aiogram import F
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardMarkup, ReplyKeyboardBuilder
from tk import API_TOKEN




# Создаем бота и диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="🇷🇺 Русский",
        callback_data="ru")
    )
    builder.add(types.InlineKeyboardButton(
        text="🇰🇿 Қазақша",
        callback_data="kz")
    )
    await message.answer(
        "Выберите язык для общения с меню",
        reply_markup=builder.as_markup()
    )
@dp.callback_query(F.data == "menu")
async def send_ru_menu(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="🇷🇺 Русский",
        callback_data="ru")
    )
    builder.add(types.InlineKeyboardButton(
        text="🇰🇿 Қазақша",
        callback_data="kz")
    )

    await callback.message.answer(
        "На каком языке хотите получить информацию?",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(F.data == "ru")
async def send_ru_menu(callback: types.CallbackQuery):


    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="О компании",
        callback_data="company_ru")
    )

    builder.row(types.InlineKeyboardButton(
        text="Библиотека и контент",
        callback_data="library_ru")
    )

    builder.row(types.InlineKeyboardButton(
        text="Часто задаваемые вопросы",
        callback_data="FAQ_ru")
    )
    # builder.row(types.InlineKeyboardButton(
    #     text="Маркетинг План",
    #     callback_data="marketing_ru")
    # )
    builder.row(types.InlineKeyboardButton(
        text="Адреса филиалов и пунктов выдачи",
        callback_data="locations_ru")
    )


    builder.row(types.InlineKeyboardButton(
        text="О продуктах",
        callback_data="products_ru")
    )

    builder.row(types.InlineKeyboardButton(
        text="Бизнес школа SOLWELL",
        callback_data="school_ru")
    )
    await callback.message.answer(
        """Здесь главное меню👇

😊Я могу тебе рассказать о компании, продукции, маркетинге, о том, как и сколько ты сможешь зарабатывать в компании и многое другое!

⬇️Выбирай с чего начнем:""",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(F.data == "kz")
async def send_kz_menu(callback: types.CallbackQuery):

    builder = InlineKeyboardBuilder()


    builder.row(types.InlineKeyboardButton(
        text="Компания туралы",
        callback_data="company_kz")
    )


    builder.row(types.InlineKeyboardButton(
        text="Кітапхана және контент",
        callback_data="library_kz")
    )

    builder.row(types.InlineKeyboardButton(
        text="Жиі қойылатын сұрақтар",
        callback_data="FAQ_kz")
    )
    # builder.row(types.InlineKeyboardButton(
    #     text="Маркетинг жоспары",
    #     callback_data="marketing_kz")
    # )


    builder.row(types.InlineKeyboardButton(
        text="Филиалдар орындарының мекенжайлары",
        callback_data="locations_kz")
    )




    builder.row(types.InlineKeyboardButton(
        text="Өнімдер туралы",
        callback_data="products_kz")
    )




    builder.row(types.InlineKeyboardButton(
        text="SOLWELL бизнес мектебі",
        callback_data="school_kz")
    )

    
    await callback.message.answer(
        """Мұнда негізгі мәзір👇

😊Мен саған компания, өнімдер, маркетинг, компанияда қалай және қанша таба алатының және басқа да көп нәрсе туралы айтайын!

⬇️Бастаймыз дегенді таңда:""",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(F.data == "company_ru")
async def send_ru_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Компания SOLWELL - это
сообщество людей, своим главным приоритетом в жизни выбрали здоровье.

Мы направили наш опыт, наши знания и умения на то, чтобы помочь себе и другим минимализировать последствия
уже накопившихся проблем со здоровьем, а в каких-то случаях и решить их полностью.
Подробно о нас Вы можете узнать на нашем сайте:
https://solwell.kz/""")

@dp.callback_query(F.data == "company_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""SOLWELL - бұл өмірде басты приоритет ретінде денсаулықты таңдаған адамдардың қоғамы.

Біз тәжірибемізді, білімімізді және дағдыларымызды денсаулық 
мәселелерінің алдын алуға және оларды шешуге, 
кейде тіпті толықтай жоюға көмектесуге бағыттадық.
Біз туралы толығырақ біздің сайттан біле аласыз:
https://solwell.kz/""")


@dp.callback_query(F.data == "library_ru")
async def send_ru_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Отправляю вам краткую информацию о нас ожидайте""")
    agenda = FSInputFile("./files/presentation/SOLWELL.pdf")
    await bot.send_document(callback.message.chat.id, agenda)
@dp.callback_query(F.data == "library_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Сізге біз туралы қысқаша ақпарат жіберемін""")
    agenda = FSInputFile("./files/presentation/SOLWELL.pdf")
    await bot.send_document(callback.message.chat.id, agenda)
# @dp.callback_query(F.data == "marketing_ru")
# async def send_kz_menu(callback: types.CallbackQuery):
#     pass
# @dp.callback_query(F.data == "marketing_kz")
# async def send_kz_menu(callback: types.CallbackQuery):
#     pass
@dp.callback_query(F.data == "locations_ru")
async def send_ru_menu(callback: types.CallbackQuery):
    await callback.message.answer("""ПУНКТЫ ВЫДАЧИ

📍ПВ Алматы 
Калкаман 2, Кабылбаева 78
☑️ Медина +7 778 959 5555

📍ПВ Костанай 
Мкр Береке 52-193
☑️ Хегай Анара +7 777 694 8888

📍 ПВ Астана
Нурмагамбетова 29, подъезд 6, 4 этаж, квартира 175 (между Сдек и Пампушка) Пересечение Байтурсынова.
☑️ Дайана +7 777 681 8170 

📍ПВ-Астана
Левый берег,ЖК «Венский квартал» 
Бокейханова 27
салон красоты Black Diamond 
☑️ Акбике 8 778 6505858 

📍ПВ Астана
ул. Бокейхана, 11
☑️ +77751073266

📍ПВ Шымкент
Мкр Туран-1, дом 18
☑️Айдана +7 771 151 68 28

📍 ПВ Уральск 
А. Хусаинова 157
2подъезд 20кв
☑️ Даметкен  +7 707 586 5164

📍 ПВ Уральск
Пр. Евразия, 61/1
ТРЦ Галактика 4 эт 26 оф
☑️ Айгуль +77013351487

📍ПВ Кульсары
И. Шафиха 3мкр, дом 27
☑️ Куралай+7 701 189 1634
⁩ 
📍 ПВ Усть-Каменогорск
Пр. Казыбек би 5/1
☑️ Мадина 8-776-954-55-15

📍 ПВ Павлодар 
ул. Бекхожина 11-18
☑️ Асемгуль +7 747 279 6264 

📍ПВ Рудный 
Комсомольский 6
☑️ Люся  +7 747 696 0346

📍 ПВ Кокшетау
Микрорайон Старый Аэропорт 13
☑️ Малика   +77077229392

📍ПВ Тараз
Жунусалиева 16
☑️ Багила +7-701-111-26-80

📍 ПВ Ташкент 
Т. Малика 112/1 кв 16
☑️ Лианна  +998975390221

📍ПВ Семей
ул.Новостройка 5, 120 
☑️ Гульдана +77078280292

📍ПВ Туркестан
11-я улица, 35/1
☑️  +77086177680 Асылбек

📍ПВ Орал
Улица Набат Маханова 1Б
Магазин Қуантқан,  
☑️ Сарагүл 87756495535

📍ПВ Бозой (Актюбинская обл.)
Қошқар ата, 7. 
☑️Жаркынай +77774343303

📍ПВ Сайрам
Улица Амира Тимура, 237
☑️ Ирода +77476533636

📍ПВ Кызылорда 
ул.Айтеке би -42/1, 4 этаж,1 офис
☑️Гұлнұр Аблайханқызы  87768539797

📍ПВ Уштобе
участок Фрунзе, Абая 4 
☑️+77081974858

📍ПВ Актау 
14 мкр-н ,61  БЦ “Звезда Актау” 
Правое крыло ,4 этаж 418 офис 
☑️Назым Мырзаевна +77022896869

📍ПВ Омск
ул Масленникова 28
☑️ +7 (923) 692-94-74 Нургуль Кожамбердиевна

📍ПВ Ушарал
Исмаилова, 7
☑️+77771131337 Гулмира

ОФИСЫ SOLLWELL

📍Официальный офис Алматы
Ауэзова 165 А 
☑️ Алена +77071651657

📍Официальный офис Астаны
Алихана Бокейхана, 11 (самый крайний офис, ориентир Китайский спа салон)
☑️ Фариза +7 778 637 0228

📍Офис Solwell Шымкент
Мадели Кожа 65, второй этаж дверь справа
☑️ Зарина +7 778 315 5754

📍Офис Solwell Актобе 
Алия Молдагулова 49/1 
☑️ Еркебулан 8700 333 03 92

📍Офис Solwell Атырау
Мкр. Алмагуль, Ул.Абдрахманова 85Б
Здание Тулпар 2 этаж
☑️СВЕТЛАНА: +7 701 259 91 85

📍Офис Solwell Кызылорда
БЦ БАБАС
☑️Жазира +7 (777) 802-74-72

📍Офис Solwell Караганда
Стройтелей 33, Цокольный этаж (Кабинет 6-7)
☑️Алина +7 775 453 6885

📍 Офис Solwell Орал
Молдагулова 18, 
БЦ Форум
6 этаж, 618 кабинет
☑️ Асхат +7 705 190 69 88

📍Офис Solwell Бишкек
Токтогула 95
☑️ Айгерим +996707929319""")
@dp.callback_query(F.data == "locations_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Орталық кеңсе
Телефондар:
☎️ +7 777 552 94 59 - 🟢 WhatsApp | 🔵 Telegram | 🟣 Viber
📞 +7 702 701 79 68 - байланыс телефоны
Мекен-жайы: Бұқар жырау көшесі 33, кеңсе 1""")

@dp.callback_query(F.data == "FAQ_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""
    **Есть ли рассрочка?**
- Да, сейчас вы можете приобрести набор фульво-гуминовой продукции в рассрочку до 24 месяцев через Halyk market (Халык маркет, приложение Халык Банк).

**Есть ли консультирующий врач?**
- Есть. Контакты: +77071039111

**Ваша продукция ХАЛАЛ? Есть ли сертификат?**
- Да. Коллаген турецкого производства, говяжий, халал. Сертификат можете найти в разделе “Библиотека и контент”.

**Есть ли каталог на английском языке?**
- На данный момент каталог на английском языке в разработке.

**Почему в составе не указано сколько миллиграмм каждого вещества?**
- Состав продукции SOLWELL является органическим. Это связано с тем, что каждый фрукт или овощ уникален, так как обладает своим собственным неповторимым составом.

**Почему мне до сих пор не поступили выплаты?**
- Вам необходимо проверить, сдали ли вы электронную счет-фактуру и акт выполненных работ за прошлый месяц. Без этих закрывающих документов,выплаты будут приостановлены до момента предоставления всех требуемых документов.

**Где я могу посмотреть адреса всех пунктов выдачи и офисов?**
- Вы можете найти адреса и контакты всех пунктов выдачи, а также офисов SOLWELL в разделе “Адреса филиалов и пунктов выдачи”.

**Есть побочные эффекты после приема Anti Age?**
- Биотехнолог - разработчик, Наргиз Омарова: “Очень важно начинать прием с гумата (2 недели), чтобы вывести все накопившиеся вредные вещества, вплоть до камней и тяжелых металлов. Потом только приступить к приему детокса и капсул.”

**Как получить доступ в SOLWELL Business School?**
- Вы можете обратиться в “Горячую линию” или написать личное сообщение по номеру:+77071651655, в Телеграм.

""",parse_mode='Markdown')
@dp.callback_query(F.data == "FAQ_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""
    **Рассрочка бар ма?**
- Иә, қазір сіз фульво-гумин өнімдер жиынтығын 24 айға дейінгі рассрочка арқылы Halyk market арқылы (Халық маркет, Халық Банкінің қосымшасы) сатып ала аласыз.

**Кеңес беретін дәрігер бар ма?**
- Бар. Байланыс: +77071039111

**Сіздің өнімдеріңіз ХАЛАЛ ма? Сертификат бар ма?**
- Иә. Түрік өндірісінің коллагены, сиыр етінен, халал. Сертификатты “Кітапхана және контент” бөлімінен таба аласыз.

**Ағылшын тіліндегі каталог бар ма?**
- Қазіргі уақытта ағылшын тіліндегі каталог жасалу үстінде.

**Құрамында әр заттың неше миллиграмы көрсетілмегенінің себебі неде?**
- SOLWELL өнімінің құрамы органик. Бұл әрбір жеміс немесе көкөніс өзіндік бірегей құрамы бар, сондықтан қайталанбас дегенді білдіреді.

**Неге маған әлі күнге дейін төлемдер түскен жоқ?**
- Сіз өткен айға арналған электрондық шот-фактура және орындалған жұмыстар туралы акті тапсырғаныңызды тексеруіңіз керек. Бұл қорытынды құжаттарсыз, төлемдер барлық қажет құжаттар ұсынылғанға дейін тоқтатылады.

**Барлық тарату пункттерінің және кеңселердің мекенжайларын қайдан көруге болады?**
- SOLWELL тарату пункттерінің және кеңселердің мекенжайлары мен байланыс ақпаратын “Филиалдар мен тарату пункттерінің мекенжайлары” бөлімінен таба аласыз.

**Anti Age қабылдағаннан кейін жанама әсерлері бар ма?**
- Биотехнолог - жобалаушы, Наргиз Омарова: “Гуматпен емдеуді бастау өте маңызды (2 апта), себебі бұл барлық жинақталған зиянды заттарды, тас пен ауыр металдарды шығару үшін қажет. Содан кейін ғана детокс және капсулаларды қабылдауға кірісу керек.”

**SOLWELL Business School-ға қалай қол жеткізуге болады?**
- “Жедел желіге” хабарласуға немесе Телеграм арқылы +77071651655 номеріне жеке хабарлама жіберуге болады.
""",parse_mode='Markdown')
@dp.callback_query(F.data == "products_ru")
async def send_ru_menu(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Men’s Fulvic and Humic Acid detox",
        callback_data="mens_fulvic_humic_acid_detox_ru")
    )

    builder.row(types.InlineKeyboardButton(
        text="Women’s Fulvic and Humic Acid detox",
        callback_data="womens_fulvic_humic_acid_detox_ru")
    )

    builder.row(types.InlineKeyboardButton(
        text="Anti-age Fulvic and Humic Acid detox",
        callback_data="antiage_fulvic_humic_acid_detox_ru")
    )

    builder.row(types.InlineKeyboardButton(
        text="Men’s Fulvic and Humic Acid extract",
        callback_data="mens_fulvic_humic_acid_extract_ru")
    )

    builder.row(types.InlineKeyboardButton(
        text="Women’s Fulvic and Humic Acid extract",
        callback_data="womens_fulvic_humic_acid_extract_ru")
    )

    builder.row(types.InlineKeyboardButton(
        text="Anti-age Fulvic and Humic Acid extract",
        callback_data="antiage_fulvic_humic_acid_extract_ru")
    )
    builder.row(types.InlineKeyboardButton(
        text="Kid’s marmalade",
        callback_data="kids_marmalade_ru")
    )

    builder.row(types.InlineKeyboardButton(
        text="Food Sea Salt",
        callback_data="food_sea_salt_ru")
    )

    builder.row(types.InlineKeyboardButton(
        text="Spirulina Soap",
        callback_data="spirulina_soap_ru")
    )

    builder.row(types.InlineKeyboardButton(
        text="Humic Soap",
        callback_data="humic_soap_ru")
    )

    builder.row(types.InlineKeyboardButton(
        text="Womens spirulina collagen",
        callback_data="womens_spirulina_collagen_ru")
    )

    builder.row(types.InlineKeyboardButton(
        text="Family black cumin biocomplex",
        callback_data="family_black_cumin_biocomplex_ru")
    )
    builder.row(types.InlineKeyboardButton(
        text="Men Fulvic Acid",
        callback_data="men_fulvic_acid_ru")
    )

    builder.row(types.InlineKeyboardButton(
        text="Womens Fulvic Acid",
        callback_data="womens_fulvic_acid_ru")
    )

    builder.row(types.InlineKeyboardButton(
        text="Anti-age Fulvic Acid",
        callback_data="antiage_fulvic_acid_ru")
    )

    builder.row(types.InlineKeyboardButton(
        text="Onco-Protector",
        callback_data="onco_protector_ru")
    )

    builder.row(types.InlineKeyboardButton(
        text="Eye Health",
        callback_data="eye_health_ru")
    )

    builder.row(types.InlineKeyboardButton(
        text="Weight Loss Essentials",
        callback_data="weight_loss_essentials_ru")
    )

    builder.row(types.InlineKeyboardButton(
        text="Anti - Alcohol",
        callback_data="anti_alcohol_ru")
    )

    builder.row(types.InlineKeyboardButton(
        text="High Molecular Weight",
        callback_data="high_molecular_weight_ru")
    )

    await callback.message.answer(
        """Наши продукты""",
        reply_markup=builder.as_markup()
    )
@dp.callback_query(F.data == "products_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()

    builder.row(types.InlineKeyboardButton(
        text="Men’s Fulvic and Humic Acid detox",
        callback_data="mens_fulvic_humic_acid_detox_kz")
    )

    builder.row(types.InlineKeyboardButton(
        text="Women’s Fulvic and Humic Acid detox",
        callback_data="womens_fulvic_humic_acid_detox_kz")
    )

    builder.row(types.InlineKeyboardButton(
        text="Anti-age Fulvic and Humic Acid detox",
        callback_data="antiage_fulvic_humic_acid_detox_kz")
    )

    builder.row(types.InlineKeyboardButton(
        text="Men’s Fulvic and Humic Acid extract",
        callback_data="mens_fulvic_humic_acid_extract_kz")
    )

    builder.row(types.InlineKeyboardButton(
        text="Women’s Fulvic and Humic Acid extract",
        callback_data="womens_fulvic_humic_acid_extract_kz")
    )

    builder.row(types.InlineKeyboardButton(
        text="Anti-age Fulvic and Humic Acid extract",
        callback_data="antiage_fulvic_humic_acid_extract_kz")
    )

    builder.row(types.InlineKeyboardButton(
        text="Kid’s marmalade",
        callback_data="kids_marmalade_kz")
    )

    builder.row(types.InlineKeyboardButton(
        text="Food Sea Salt",
        callback_data="food_sea_salt_kz")
    )

    builder.row(types.InlineKeyboardButton(
        text="Spirulina Soap",
        callback_data="spirulina_soap_kz")
    )

    builder.row(types.InlineKeyboardButton(
        text="Humic Soap",
        callback_data="humic_soap_kz")
    )

    builder.row(types.InlineKeyboardButton(
        text="Womens spirulina collagen",
        callback_data="womens_spirulina_collagen_kz")
    )

    builder.row(types.InlineKeyboardButton(
        text="Family black cumin biocomplex",
        callback_data="family_black_cumin_biocomplex_kz")
    )

    builder.row(types.InlineKeyboardButton(
        text="Men Fulvic Acid",
        callback_data="men_fulvic_acid_kz")
    )

    builder.row(types.InlineKeyboardButton(
        text="Womens Fulvic Acid",
        callback_data="womens_fulvic_acid_kz")
    )

    builder.row(types.InlineKeyboardButton(
        text="Anti-age Fulvic Acid",
        callback_data="antiage_fulvic_acid_kz")
    )

    builder.row(types.InlineKeyboardButton(
        text="Onco-Protector",
        callback_data="onco_protector_kz")
    )

    builder.row(types.InlineKeyboardButton(
        text="Eye Health",
        callback_data="eye_health_kz")
    )

    builder.row(types.InlineKeyboardButton(
        text="Weight Loss Essentials",
        callback_data="weight_loss_essentials_kz")
    )

    builder.row(types.InlineKeyboardButton(
        text="Anti - Alcohol",
        callback_data="anti_alcohol_kz")
    )

    builder.row(types.InlineKeyboardButton(
        text="High Molecular Weight",
        callback_data="high_molecular_weight_kz")
    )

    await callback.message.answer(
         """Біздің өнімдер""",
        reply_markup=builder.as_markup()
    )
@dp.callback_query(F.data == "school_ru")
async def send_ru_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Solwell Business School: Развивайте свои навыки с нами

Solwell Business School - это новый онлайн-образовательный проект, созданный для того, чтобы помочь вам развить ключевые навыки в сфере бизнеса. Наша программа охватывает пять основных блоков обучения, предоставляя участникам полезные знания и навыки для успешной карьеры.

📈Основы маркетинга: Мы расскажем вам о стратегиях привлечения клиентов, создании уникального бренда и эффективном позиционировании на рынке.

💰Искусство продаж: Узнайте, как создавать убедительные предложения, устанавливать контакт с клиентами и заключать успешные сделки.

📱SMM (социальные медиа маркетинг): Погрузитесь в мир социальных сетей и узнайте, как эффективно использовать их для продвижения бизнеса и привлечения аудитории.

🏦Финансовая грамотность: Наши эксперты помогут вам разобраться в финансовых аспектах бизнеса, научат управлять бюджетом и принимать обоснованные финансовые решения.

🗣️Навыки переговоров: Освойте техники ведения успешных переговоров, умение добиваться выгодных условий и разрешать конфликты.

Наши занятия проводят опытные спикеры и профессионалы своего дела, которые поделятся своими знаниями, опытом и лучшими практиками. 

Бизнес-школа доступна на русском и казахском языках, обеспечивая комфортное обучение для всех желающих. Присоединяйтесь к Solwell Business School и откройте для себя новые горизонты в мире бизнеса!""")
@dp.callback_query(F.data == "school_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Solwell Business School: Бізбен бірге өз дағдыларыңызды дамытыңыз

Solwell Business School - бұл сіздің бизнес саласындағы негізгі дағдыларыңызды дамытуға көмектесу үшін құрылған жаңа онлайн-білім беру жобасы. Біздің бағдарламамыз бес негізгі оқу блогын қамтиды, қатысушыларға сәтті мансап құру үшін пайдалы білім мен дағдыларды ұсынады.

📈Маркетингтің негіздері: Біз сізге клиенттерді тарту стратегиялары, бірегей бренд құру және нарықта тиімді орналасу туралы айтып береміз.

💰Сату өнері: Сенімді ұсыныстар жасауды, клиенттермен байланыс орнатуды және сәтті келісімдер жасауды үйреніңіз.

📱SMM (әлеуметтік медиа маркетинг): Әлеуметтік желілер әлеміне батып, оларды бизнесті ілгерілету және аудиторияны тарту үшін қалай тиімді пайдалануға болатынын үйреніңіз.

🏦Қаржы сауаттылығы: Біздің сарапшылар сізге бизнестің қаржы аспектілерін түсінуге, бюджетті басқаруға және негізделген қаржылық шешімдер қабылдауға көмектеседі.

🗣️Келіссөз дағдылары: Табысты келіссөздер жүргізу техникаларын, тиімді шарттарға қол жеткізу қабілетін және келіспеушіліктерді шешу дағдыларын меңгеріңіз.

Біздің сабақтарымызды өз ісінің кәсіби мамандары және тәжірибелі спикерлер жүргізеді, олар өз білімдерімен, тәжірибелерімен және үздік тәжірибелерімен бөліседі.

Бизнес-мектебіміз қазақ және орыс тілдерінде қолжетімді, барлық қалаушылар үшін ыңғайлы оқу мүмкіндігі қамтамасыз етілген. Solwell Business School мектебіне қосылыңыз және өзіңізге бизнес әлемінің жаңа көкжиектерін ашыңыз!""")


## функции для продуктов ru
@dp.callback_query(F.data == "mens_fulvic_humic_acid_detox_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Отправляю описание товара, ожидайте""")
    agenda = FSInputFile("./files/products/ru/final/Mens Fulvic and Humic Acid detoxru.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "womens_fulvic_humic_acid_detox_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Отправляю описание товара, ожидайте""")
    agenda = FSInputFile("./files/products/ru/final/Womens Fulvic and Humic Acid DetoxRu.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "antiage_fulvic_humic_acid_detox_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Отправляю описание товара, ожидайте""")
    agenda = FSInputFile("./files/products/ru/final/Anti-age Fulvic and Humic Acid detoxRU.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "mens_fulvic_humic_acid_extract_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Отправляю описание товара, ожидайте""")
    agenda = FSInputFile("./files/products/ru/final/Mens Fulvic and Humic Acid BioComplexRu.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "womens_fulvic_humic_acid_extract_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Отправляю описание товара, ожидайте""")
    agenda = FSInputFile("./files/products/ru/final/Womens Fulvic and Humic Acid BioComplexRU.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "antiage_fulvic_humic_acid_extract_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Отправляю описание товара, ожидайте""")
    agenda = FSInputFile("./files/products/ru/final/Anti-age Fulvic and Humic Acid BioComplexRU.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "kids_marmalade_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Отправляю описание товара, ожидайте""")
    agenda = FSInputFile("./files/products/ru/final/Kid’s marmaladeRu.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "food_sea_salt_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Отправляю описание товара, ожидайте""")
    agenda = FSInputFile("./files/products/ru/final/Food Sea Salt_ru.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "spirulina_soap_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Отправляю описание товара, ожидайте""")
    agenda = FSInputFile("./files/products/ru/final/Spirulina SoapRu.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "humic_soap_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Отправляю описание товара, ожидайте""")
    agenda = FSInputFile("./files/products/ru/final/Humic SoapRU.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "womens_spirulina_collagen_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Отправляю описание товара, ожидайте""")
    agenda = FSInputFile("./files/products/ru/final/Womens spirulina collagenRU.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "family_black_cumin_biocomplex_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Отправляю описание товара, ожидайте""")
    agenda = FSInputFile("./files/products/ru/final/Family black cumin biocomplexRU.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "men_fulvic_acid_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Отправляю описание товара, ожидайте""")
    agenda = FSInputFile("./files/products/ru/final/Men Fulvic AcidRu.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "womens_fulvic_acid_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Отправляю описание товара, ожидайте""")
    agenda = FSInputFile("./files/products/ru/final/Womens Fulvic AcidRu.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "antiage_fulvic_acid_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Отправляю описание товара, ожидайте""")
    agenda = FSInputFile("./files/products/ru/final/Anti - AlcoholRu.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "onco_protector_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Отправляю описание товара, ожидайте""")
    agenda = FSInputFile("./files/products/ru/final/Onco-ProtectorRu.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "eye_health_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Отправляю описание товара, ожидайте""")
    agenda = FSInputFile("./files/products/ru/final/Eye Healthru.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "weight_loss_essentials_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Отправляю описание товара, ожидайте""")
    agenda = FSInputFile("./files/products/ru/final/Weight Loss EssentialsRu.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "anti_alcohol_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Отправляю описание товара, ожидайте""")
    agenda = FSInputFile("./files/products/ru/final/Anti - AlcoholRu.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "high_molecular_weight_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Отправляю описание товара, ожидайте""")
    agenda = FSInputFile("./files/products/ru/final/High Molecular WeightRU.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

## функции для продуктов kz

@dp.callback_query(F.data == "mens_fulvic_humic_acid_detox_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Тауар сипаттамасын жіберемін, күте тұрыңыз""")
    agenda = FSInputFile("./files/products/kz/final/Men’s Fulvic and Humic Acid detoxKZ.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "womens_fulvic_humic_acid_detox_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Тауар сипаттамасын жіберемін, күте тұрыңыз""")
    agenda = FSInputFile("./files/products/kz/final/Women’s Fulvic and Humic Acid detoxKZ.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "antiage_fulvic_humic_acid_detox_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Тауар сипаттамасын жіберемін, күте тұрыңыз""")
    agenda = FSInputFile("./files/products/kz/final/Anti-age Fulvic and Humic Acid detoxKZ.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "mens_fulvic_humic_acid_extract_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Тауар сипаттамасын жіберемін, күте тұрыңыз""")
    agenda = FSInputFile("./files/products/kz/final/Men’s Fulvic and Humic Acid extractKZ.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "womens_fulvic_humic_acid_extract_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Тауар сипаттамасын жіберемін, күте тұрыңыз""")
    agenda = FSInputFile("./files/products/kz/final/Women’s Fulvic and Humic Acid BioComplexKZ.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "antiage_fulvic_humic_acid_extract_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Тауар сипаттамасын жіберемін, күте тұрыңыз""")
    agenda = FSInputFile("./files/products/kz/final/Anti-age Fulvic and Humic Acid extractKZ.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "kids_marmalade_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Тауар сипаттамасын жіберемін, күте тұрыңыз""")
    agenda = FSInputFile("./files/products/kz/final/Kid’s marmaladeKZ.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "food_sea_salt_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Тауар сипаттамасын жіберемін, күте тұрыңыз""")
    agenda = FSInputFile("./files/products/kz/final/Food Sea Salt_kz.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "spirulina_soap_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Тауар сипаттамасын жіберемін, күте тұрыңыз""")
    agenda = FSInputFile("./files/products/kz/final/Spirulina Soap.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "humic_soap_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Тауар сипаттамасын жіберемін, күте тұрыңыз""")
    agenda = FSInputFile("./files/products/kz/final/Humic SoapKZ.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "womens_spirulina_collagen_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Тауар сипаттамасын жіберемін, күте тұрыңыз""")
    agenda = FSInputFile("./files/products/kz/final/Womens spirulina collagenKZ.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "family_black_cumin_biocomplex_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Тауар сипаттамасын жіберемін, күте тұрыңыз""")
    agenda = FSInputFile("./files/products/kz/final/Family black cumin biocomplexKZ.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "men_fulvic_acid_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Тауар сипаттамасын жіберемін, күте тұрыңыз""")
    agenda = FSInputFile("./files/products/kz/final/Men Fulvic AcidKZ.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "womens_fulvic_acid_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Тауар сипаттамасын жіберемін, күте тұрыңыз""")
    agenda = FSInputFile("./files/products/kz/final/Womens Fulvic AcidKZ.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "antiage_fulvic_acid_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Тауар сипаттамасын жіберемін, күте тұрыңыз""")
    agenda = FSInputFile("./files/products/kz/final/Anti-age Fulvic AcidKZ.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "onco_protector_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Тауар сипаттамасын жіберемін, күте тұрыңыз""")
    agenda = FSInputFile("./files/products/kz/final/Onco-ProtectorKZ.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "eye_health_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Тауар сипаттамасын жіберемін, күте тұрыңыз""")
    agenda = FSInputFile("./files/products/kz/final/Eye HealthKZ.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "weight_loss_essentials_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Тауар сипаттамасын жіберемін, күте тұрыңыз""")
    agenda = FSInputFile("./files/products/kz/final/Weight Loss EssentialsKZ.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "anti_alcohol_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Тауар сипаттамасын жіберемін, күте тұрыңыз""")
    agenda = FSInputFile("./files/products/kz/final/Anti - AlcoholKZ.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

@dp.callback_query(F.data == "high_molecular_weight_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Тауар сипаттамасын жіберемін, күте тұрыңыз""")
    agenda = FSInputFile("./files/products/kz/final/High Molecular WeightKZ.pdf")
    await bot.send_document(callback.message.chat.id, agenda)

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(API_TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
