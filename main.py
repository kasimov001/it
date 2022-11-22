from aiogram import executor
from datetime import *
from translate import Translator
import requests
from aiogram.types import Message, CallbackQuery
from config import *
from inline import *
from ReplyKeyboard import *


@dp.message_handler(commands="start")
async def start(msg: Message):
    txt = f"Assalomu alaykum {msg.from_user.full_name}. Namoz vaqtlari botga xush kelibsiz!"
    await msg.answer_photo(open("Image/images (2).jpg", "rb"), caption=txt, reply_markup=menuStart)
    await msg.delete()


@dp.message_handler(commands="help")
async def help(msg: Message):
    txt = f"Yordam uchun https://t.me/Hello_this_isAbdurrohman profiliga bog'laning."
    await msg.answer_photo(open("Image/Без названия.jpg", "rb"), caption=txt, reply_markup=menuStart)
    await msg.delete()


@dp.message_handler(text="Duolar")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/images.jpg", "rb"), caption="Bismillahir rohmanir rohiym.", reply_markup=menuduo)
    await msg.delete()

@dp.message_handler(text="1. Uyqudan uygonganda")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/images.jpg", "rb"), caption="Huzayfa ibn Yamon roziyallohu anhu va Abu Zarr roziyallohu anhudan rivoyat qilinadi. Rasululloh sollallohu alayhi vasallam to'shaklariga yotsalar,\n\n  بِاسْمِكَ اللهمَّ أَحْيَا وَأَمُوتُ\n\n    «Bismikallohumma ahya va amutu», deb aytganlar. (Ma'nosi: Ey Rabbim, Sening isming bilan tirilaman va o'laman.)\n Uyg'onganlarida:\n\n الْحَمْدُ للهِ الَّذِي أَحْيَانَا بَعْدَ مَا أَمَاتَنَا وَإِلَيْهِ النُّشُورُ\n\n  «Alhamdu lillahillaziy ahyana ba'da ma amatana va ilayhin nushur», deb aytar edilar. (Ma'nosi: Bizni o'ldirgandan keyin tiriltirgan Allohga hamd bo'lsin.  \n Va biz Ungagina qaytamiz.) Imom Buxoriy rivoyatlari"
                                                                   , reply_markup=menuduo)
    await msg.delete()

@dp.message_handler(text="2. Juma tongida")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/images.jpg", "rb"), caption="Anas roziyallohu anhudan rivoyat qilinadi: Rasululloh sollallohu alayhi vasallam: «Kim juma kuni bomdod namozidan oldin:\n\n أسْتَغْفِرُ اللهَ الَّذِي لاَ إِلَهَ إِلاَّ هُوَ الْحَيُّ القَيُّومُ وَأَتُوبُ إِلَيْهِ \n\n «Astag'firullohallaziy la ilaha illa huval hayyul qoyyum va atubu ilayh», deb uch marta aytsa, Alloh taolo uning gunohlarini dengiz ko'pigicha bo'lsa ham, kechirib yuboradi», dedilar.\n \n(Ma'nosi: Hay va qayyum sifatli Zotdan boshqa iloh yo'q va Unga istig'for aytaman, Unga tavba qilaman.) Ibn Sunniy rivoyatlari.", reply_markup=menuduo)
    await msg.delete()

@dp.message_handler(text="3. Uxlash uchun toshakka yotganda")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/images.jpg", "rb"), caption="Abu Hurayra roziyallohu anhudan rivoyat qilinadi: Rasululloh sollallohu alayhi vasallam: «Kishi to'shakka yotayotganida ko'rpa va izorini qoqib tashlasin. Chunki uning orasida nima borligini bilmaydi. So'ng:\n\n بِاسْمِكَ رَبِّي وَضَعْتُ جَنْبِي وَبِكَ أَرْفَعُهُ إِنْ أَمْسَكْتَ نَفْسِي فَارْحَمْهَا وَإِنْ أرْسَلْتَهَا فَاحْفَظْهَا بِمَا تَحْفَظُ بِهِ عِبَادَكَ الصَّالِحِينَ \n\n «Bismika robbiy vazo'tu jambiy va bika arfa'uhu, in amsakta nafsiy farhamha va in arsaltaha fahfazha bima tahfazu bihi 'ibadakas solihiyn», deb aytsin», dedilar. \n\n(Ma'nosi: Ey Rabbim, Sening isming bilan yotdim va Sening isming bilan turaman. Agar mening ruhimni olsang, unga rahm qil. Agar uni qo'yib yuborsang, xuddi solih bandalaringni saqlaganingdek, uni ham hifzu himoyangga ol.) Imom Buxoriy va Muslim rivoyatlari. \n\nOisha roziyallohu anho aytadilar: «Rasululloh sollallohu alayhi vasallam to'shaklariga yotsalar, qo'llariga suflab, ikkita «Qul a'uzu»ni o'qir, so'ng tanalariga surtar edilar». Imom Buxoriy va Muslim rivoyatlari.", reply_markup=menuduo)
    await msg.delete()

@dp.message_handler(text="4. Bezovta bolib, uxlay olmaganda")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/images.jpg", "rb"), caption="Zayd ibn Sobit roziyallohu anhu aytadilar: «Rasululloh sollallohu alayhi vasallamga uyqusizlikdan shikoyat qildim, u zot:\n\n اللهُمaَّ غَارَتِ النُّجُومُ وَهَدَأَتِ العُيُونُ وَأَنْتَ حَيٌّ قَيُّوم لاَ تَأْخُذُكَ سِنَةٌ وَلاَ نَومٌ يَا حَيُّ يَا قَيُّومُ أهْدِي لَيْلِي وَأنِمْ عَيْنِي \n\n «Allohumma g'orotin nujumu va hadaatil 'uyunu va anta hayyun qoyyum, la taxuzuka sinatun va la navm, ya hayyu, ya qoyyumu, ahdiy layliy va anim 'ayniy, deb ayt», dedilar. Shu duoni aytgan edim, Alloh mendan uyqusizlikni ketkazdi». \n\n(Ma'nosi: Allohim, yulduzlar botdi, ko'zlar tindi. Sen tirik, qoimdirsan. Seni mudroq ham, uyqu ham olmaydi. Ey Hay va Qayyum sifatli Zot, kechamni tinch qilib, ko'zimga uyqu ber.) Ibn Sunniy rivoyatlari.", reply_markup=menuduo)
    await msg.delete()

@dp.message_handler(text="5. Uyquda qorqqanda")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/images.jpg", "rb"), caption="Amr ibn Shuayb otalaridan, otalari bobolaridan rivoyat qiladilar. Rasululloh sollallohu alayhi vasallam uyqusida qo'rqqanlarga:\n\n أعُوsaُ بِكَلِمَاتِ اللهِ التَّامَّةِ مِنْ غََضَبِهِ وَشَرِّ عِبَادِهِ وَمِنْ هَمَزَاتِ الشَّيَاطِينِ وَأنْ يَحْضُرُونِ \n\n «A'uzu bikalimatillahit tammah min g'ozabihi va sharri 'ibadihi va min hamazatish shayatiyni va an yahzuruni», deb aytishni o'rgatganlar. \n\n(Ma'nosi: Allohning mukammal kalimalari bilan Uning g'azabidan, bandalarining yomonligidan, shayton hozir bo'lib, vasvasa qilishidan panoh tilayman.) Abu Dovud, Termiziy va Ibn Sunniylar rivoyatlari.", reply_markup=menuduo)
    await msg.delete()

@dp.message_handler(text="6. Tushida yoqtirmagan narsani korganda")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/images.jpg", "rb"), caption="Ibn Sunniyning rivoyatlarida Abu Hurayra roziyallohu anhu bunday deganlar: «Agar birortangiz o'zi yoqtirmagan tush ko'rsa, uch marta tuflab:\n\n إِنِّي أعُوذُ بِكَ مِنْ عَمَلِ الشَّيْطَانِ وَسَيِّئَاتِ الأَحْلاَمِ \n\n«Inniy a'uzu bika min 'amalish shaytoni va sayyiatil ahlami», desa, unga hech narsa bo'lmaydi». \n\n(Ma'nosi: Men shaytonning amalidan va bulg'angan tushdan Sening isming ila panoh  tilayman.)", reply_markup=menuduo)
    await msg.delete()

@dp.message_handler(text="7. Qon oldirganda")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/images.jpg", "rb"), caption="Ali roziyallohu anhudan rivoyat qilinadi: Rasululloh sollallohu alayhi vasallam: «Kimki qon oldirayotgan paytda «Oyatal kursi»ni o'qisa, o'sha oldirayotgan qoni manfaatli bo'ladi», dedilar. Ibn Sunniy rivoyatlari.", reply_markup=menuduo)
    await msg.delete()

@dp.message_handler(text="8. Tahorat qilganda")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/images.jpg", "rb"), caption="Umar ibn Xattob roziyallohu anhudan rivoyat qilinadi: Rasululloh sollallohu alayhi vasallam: «Kim tahorat qilib bo'lib:\n"
                                                                   "\n أَشْهَ أَنْ لاَ إِلَهَ إِلاَّ الله وَحْدَهُ لاَ شَرِيكَ لَهُ وَأَشْهَدُ أَنَّ مُحَمَّدًا عَبْدُهُ وَرَسُولُهُ"
                                                                   " \n\n «Ashhadu anla ilaha illallohu vahdahu la shariyka lahu va ashhadu anna Muhammadan 'abduhu va rosuluhu», desa, unga jannatning sakkizta eshigi ochilib, xohlaganidan kiraveradi», dedilar. Imom Muslim rivoyatlari.", reply_markup=menuduo)
    await msg.delete()

@dp.message_handler(text="9. Masjidga ketayotganda")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/images.jpg", "rb"), caption="Anas roziyallohu anhudan rivoyat qilinadi: Rasululloh sollallohu alayhi vasallam hojatxonaga kirayotganlarida:\n\n اللهُمَّ إِنَّي أَعُوذُ بِكَ مِنَ الْخُبْثِ وَالْخَبَائِثِ \n\n«Allohumma inniy a'uzu bika minal xubsi val xobais» duosini o'qir edilar». \n\n(Ma'nosi: Ey Rabbim, erkak va ayol shaytonning yomonligidan panoh tilayman.) Imom Buxoriy va Muslim rivoyatlari.", reply_markup=menuduo)
    await msg.delete()

@dp.message_handler(text="10. Masjidga kirayotganda va undan chiqayotganda")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/images.jpg", "rb"), caption="Abu Humayd yoki Abu Usaydlardan rivoyat qilinadi: “Rasululloh sollallohu alayhi vasallam aytdilar: «Agar birortangiz masjidga kirsa, Rasululloh sollallohu alayhi vasallamga salom aytib, so'ng:\n"
                                                                   "\n اللهُمَّ افْتَحْ لِي أبْوَابَ رَحْمَتِكَ \n\n «Allohummaftah liy abvaba rohmatik», deb aytsin. \n\n(Ma'nosi: Ey Rabbim, bizga rahmat eshiklarini ochgin) \n\nChiqqanida esa:\n\n اللهُمَّ إِنِّي أَسْأَلُكَ مِنْ فَضْلِكَ \n\n «Allohumma inniy as`aluka min fazlik», desin». \n\n(Ma'nosi: Ey Rabbim, Sening fazlingni so'rayman.) /n/nBu hadisni Imom Muslim rivoyat qilganlar. Lekin u zotning rivoyatlarida «Rasulullohga salom aytsin», degan lafz yo'q.", reply_markup=menuduo)
    await msg.delete()

@dp.message_handler(text="11. Namozdagi ruku'zikrlarini aytadi")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/images.jpg", "rb"), caption="Namoz o'qiyotgan kishi ruku'ga to'la egilsa;\n\n سُبْحَانَ رَبِّيَ العَظِيمِ، سُبْحَانَ رَبِّيَ العَظِيمِ، سُبْحَانَ رَبِّيَ العَظِيمِ \n\n«Subhana robbiyal 'aziym», deb ruku' zikrlarini aytadi. \n\n(Ma'nosi: Ulug' Rabbim nuqsonlardan pokdir.)", reply_markup=menuduo)
    await msg.delete()

@dp.message_handler(text="12. Namoz boshlaganda")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/images.jpg", "rb"), caption="Oisha onamiz roziyallohu anhodan rivoyat qilinadi: Rasululloh sollallohu alayhi vasallam namozni boshlasalar:\n\n سُبْحَانَكَ اللهُمَّ وَبِحَمْدِكَ وَتَبَارَكَ اسْمُكَ وَتَعَالى جَدُّكَ وَلاَ إِلَهَ غَيْرُكَ \n\n «Subhanakallohumma va bihamdika va tabarokasmuka va ta'ala jadduka va la ilaha g'oyruk», der edilar. \n\n(Ma'nosi: Ey Rabbim, Senga hamd aytish bilan Seni aybu nuqsonlardan poklayman. Sening isming muborakdir. Azamating oliydir. Sendan boshqa iloh yo'qdir.)", reply_markup=menuduo)
    await msg.delete()

@dp.message_handler(text="13. Ruku'dan bosh kotarganda va tik turganda")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/images.jpg", "rb"), caption="Abu Hurayra roziyallohu anhudan rivoyat qilinadi: Rasululloh sollallohu alayhi vasallam ruku'dan qomatlarini ko'targanlarida:\n\n سَمِعَ اللهُ لِمَنْ حَمِدَهُ رَبَّنَا لَكَ الْحَمْدُ  \n\n«Sami'allohu liman hamidah» (Kim hamd aytsa, Alloh uni eshitadi), tik bo'lganlarida esa, «Robbana lakal hamd» (Rabbimiz, Senga hamd bo'lsin), deb aytar edilar. (Ba'zi rivoyatlarda: «Robbana va lakal hamd» bo'lib kelgan). Imom Buxoriy va Muslim rivoyatlari.", reply_markup=menuduo)
    await msg.delete()

@dp.message_handler(text="14. Sajda paytida")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/images.jpg", "rb"), caption="Rasululloh alayhissalom: «Agar birortangiz sajda qilsa, kamida uch marta:\n\n سُبْحَانَ رَبِّيَ الأَعْلَى، سُبْحَانَ رَبِّيَ الأَعْلَى، سُبْحَانَ رَبِّيَ الأَعْلَى \n\n«Subhana robbiyal a'la, Subhana robbiyal a'la, Subhana robbiyal a'la», deb aytsin», dedilar. Sunan kitoblarida rivoyat qilingan.", reply_markup=menuduo)
    await msg.delete()

@dp.message_handler(text="15. Hojatxonaga kirayotganda")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/images.jpg", "rb"), caption="Anas roziyallohu anhudan rivoyat qilinadi: Rasululloh sollallohu alayhi vasallam hojatxonaga kirayotganlarida:\n\n  اللهُمَّ إِنَّي أَعُوذُ بِكَ مِنَ الْخُبْثِ وَالْخَبَائِثِ \n\n«Allohumma inniy a'uzu bika minal xubsi val xobais» duosini o'qir edilar». \n\n(Ma'nosi: Ey Rabbim, erkak va ayol shaytonning yomonligidan panoh tilayman.) Imom Buxoriy va Muslim rivoyatlari.", reply_markup=menuduo)
    await msg.delete()

@dp.message_handler(text="16. Hojatxonadan chiqayotganda")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/images.jpg", "rb"), caption="Rasululloh sollallohu alayhi vasallam hojatxonadan chiqqanlarida:\n\n غُفْرَانَكَ، الْحَمْدُ للهِ الَّذِي أَذْهَبَ عَنِّي الأَذَى وَعَافَانِي \n\n«g'ufronaka» (Sening mag'firatingni so'rayman) va «alhamdu lillahillaziy azhaba 'annil aza va 'afaniy» (mendan aziyatlarni ketkazib, ofiyatda qilgan Allohga hamd bo'lsin), deb aytar edilar. Avvalgisini Abu Dovud va Termiziy, keyingisini Nasaiy va Ibn Mojalar rivoyat qilishgan.", reply_markup=menuduo)
    await msg.delete()

@dp.message_handler(text="17. Kiyim kiyishda")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/images.jpg", "rb"), caption="Abu Said Xudriy roziyallohu anhudan rivoyat qilinadi: Rasululloh sollallohu alayhi vasallam ko'ylak, rido yoki salla kiysalar, bismillohni aytib, so'ng:\n\n اللهمَّ إِنِّي أَسْأَلُكَ مِنْ خَيْرِهِ وَخَيْرِ مَا هُوَ لَهُ وَأَعُوذُ بِكَ مِنْ شَرِّهِ وَشَرِّ مَا هُوَ لَهُ \n\n«Allohumma inniy as`aluka min xoyrihi va xoyri ma huva lahu va a'uzu bika min sharrihi va sharri ma huva lahu», deb o'qir edilar. \n\n(Ma'nosi: Ey Rabbim, Sendan uning yaxshisini va unga beriladigan narsaning yaxshisini so'rayman. Va uning yomonidan hamda unga beriladigan narsaning yomonidan panoh tilayman.) Ibn Sunniy rivoyatlari.", reply_markup=menuduo)
    await msg.delete()

@dp.message_handler(text="18. Kiyim yechilganda")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/images.jpg", "rb"), caption="Anas roziyallohu anhudan rivoyat qilinadi: Rasululloh sollallohu alayhi vasallam: «Musulmon kishi kiyimini yechmoqchi bo'lsa:\n\n بِسْمِ اللهِ الَّذِي لاَ إِلَهَ إِلاَّ هُوَ \n\n«Bismillahillaziy la ilaha illa huva», deb aytsin, shu so'z odam bolasi avrati bilan jin ko'zi orasida pardadir», dedilar.     \n\n(Ma'nosi: Undan boshqa iloh yo'q bo'lgan Allohning ismi bilan.) Ibn Sunniy rivoyatlari.", reply_markup=menuduo)
    await msg.delete()

@dp.message_handler(text="19. Uydan chiqayotganda")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/images.jpg", "rb"), caption="Ummu Salama onamiz roziyallohu anhodan rivoyat qilinadi: Rasululloh sollallohu alayhi vasallam uydan chiqayotib:\n\n بِاسْمِ اللهِ تَوَكَّلْتُ عَلَى اللهِ، اللهُمَّ إِنِّي أَعُوذُ بِكَ أَنْ أَضِلَّ أَوْ أُضَلَّ أَوْ أَزِلَّ أَوْ أُزَلَّ أَوْ أَظْلِمَ أَوْ أُظْلَمَ أَوْ أَجْهَلَ أَوْ يُجْهَلَ عَلَيَّ \n\n«Bismillahi, tavakkaltu 'alallohi. Allohumma inniy a'uzu bika an adilla av udalla av azilla av uzalla av azlima av uzlama av ajhala av yujhala 'alayya», degan duoni o'qir edilar». \n\n(Ma'nosi: Alloh nomi bilan. Allohga tavakkal qildim. Ey Rabbim, adashish va adashtirilishdan, toyilish va toyiltirilishdan, zulm qilish va zulm ko'rishdan, johillik qilish va menga nisbatan johillik qilinishidan Sendan panoh so'rayman.) Abu Dovud, Termiziy, Nasaiy, Ibn Moja rivoyatlari.", reply_markup=menuduo)
    await msg.delete()

@dp.message_handler(text="20. Qiyinchilik va Gamginlikda")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/images.jpg", "rb"), caption="Ali roziyallohu anhudan rivoyat qilinadi: Rasululloh sollallohu alayhi vasallam agar menga biror qiyinchilik yoki xafachilik yetsa, quyidagi kalimalarni aytishni buyurdilar:\n\n لاَ إِلَهَ إِلاَّ اللهُ الكَرِيْمُ العَظِيمُ، سُبْحَانَهُ تَبَارَكَ اللهُ رَبُّ العَرْشِ العَظِيمِ، الْحَمْدُ للهِ رَبِّ العَالَمِينَ \n\n«La ilaha illallohu karimul 'aziym. Subhanahu tabarokallohu robbul 'arshil 'aziym. Alhamdu lillahi robbil 'alamiyn». (Ma'nosi: Ulug' va karim sifatli Allohdan boshqa iloh yo'q. Ulug' arsh Rabbi Alloh barakotli va pokdir. Olamlar rabbi Allohga hamd bo'lsin.) Nasaiy va Ibn Sunniy rivoyatlari.", reply_markup=menuduo)
    await msg.delete()

@dp.message_handler(text="Ortga qaytish")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/images.jpg", "rb"), caption="Bismillahir rohmanir rohiym.", reply_markup=menuStart)
    await msg.delete()

















@dp.message_handler(text="🤲 Namoz vaqtlarini bilish 🤲")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/images.jpg", "rb"), caption="Shaxarni tanlang!", reply_markup=menushahar)
    await msg.delete()


@dp.message_handler(text="Toshkent")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/Без названия.jpg", "rb"), "Tanlang!", reply_markup=menuTosh)


@dp.message_handler(text="Namangan")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/Без названия.jpg", "rb"), "Tanlang!", reply_markup=menuNam)


@dp.message_handler(text="Andijon")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/Без названия.jpg", "rb"), "Tanlang!", reply_markup=menuAnd)


@dp.message_handler(text="Buxoro")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/Без названия.jpg", "rb"), "Tanlang!", reply_markup=menuBux)


@dp.message_handler(text="Farg'ona")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/Без названия.jpg", "rb"), "Tanlang", reply_markup=menuFarg)


@dp.message_handler(text="Xiva")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/Без названия.jpg", "rb"), "Tanlang", reply_markup=menuXiva)


@dp.message_handler(text="Guliston")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/Без названия.jpg", "rb"), "Tanlang", reply_markup=menuGul)


@dp.message_handler(text="Samarqand")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/Без названия.jpg", "rb"), "Tanlang", reply_markup=menuSam)


@dp.message_handler(text="Navoiy")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/Без названия.jpg", "rb"), "Tanlang", reply_markup=menuNav)


@dp.message_handler(text="Jizzax")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/Без названия.jpg", "rb"), "Tanlang", reply_markup=menuJizzakh)


@dp.message_handler(text="Nukus")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/Без названия.jpg", "rb"), "Tanlang", reply_markup=menuNuk)


@dp.message_handler(text="Qarshi")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/Без названия.jpg", "rb"), "Tanlang", reply_markup=menuQar)


@dp.callback_query_handler(text_contains="b1")
async def namoz(call: CallbackQuery):
    await call.message.answer_photo(open("Image/Без названия.jpg", "rb"), caption="Shaxarni tanlang!", reply_markup=menushahar)
    await call.message.delete()


@dp.callback_query_handler(text_contains="menu")
async def start(call: CallbackQuery):
    txt = f"Assalomu alaykum. Namoz vaqtlari botga xush kelibsiz!"
    await call.message.answer_photo(open("Image/Без названия.jpg", "rb"), caption=txt, reply_markup=menuStart)
    await call.message.delete()


@dp.callback_query_handler(text_contains="t1")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    today_time = datetime.today().now()
    p = open("Image/Без названия.jpg", "rb")
    today = today_time + timedelta(minutes=15)
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/toshkent").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"Bomdod: {bomdod} 🌑    "
                                 f"|Quyosh: {quyosh_ch} 🌒\nPeshin: {peshin} 🌕       "
                                 f"|Asr: {asr} 🌔\nShom: {shom} 🌑 "
                                 f"        |Xufton: {xufton} 🌚")


@dp.callback_query_handler(text_contains="t2")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    today_time = datetime.today().now()
    p = open("Image/Без названия.jpg", "rb")
    today = today_time + timedelta(minutes=15)
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/toshkent").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"Bomdod: {bomdod} 🌑    "
                                 f"|Quyosh: {quyosh_ch} 🌒\nPeshin: {peshin} 🌕       "
                                 f"|Asr: {asr} 🌔\nShom: {shom} 🌑 "
                                 f"        |Xufton: {xufton} 🌚")


@dp.callback_query_handler(text_contains="n1")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    today_time = datetime.today().now()
    p = open("Image/Без названия.jpg", "rb")
    today = today_time + timedelta(minutes=15)
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/namangan").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"Bomdod: {bomdod} 🌑    "
                                 f"|Quyosh: {quyosh_ch} 🌒\nPeshin: {peshin} 🌕       "
                                 f"|Asr: {asr} 🌔\nShom: {shom} 🌑 "
                                 f"        |Xufton: {xufton} 🌚")


@dp.callback_query_handler(text_contains="n2")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    today_time = datetime.today().now()
    p = open("Image/Без названия.jpg", "rb")
    today = today_time + timedelta(minutes=15)
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/namangan").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"Bomdod: {bomdod} 🌑    "
                                 f"|Quyosh: {quyosh_ch} 🌒\nPeshin: {peshin} 🌕       "
                                 f"|Asr: {asr} 🌔\nShom: {shom} 🌑 "
                                 f"        |Xufton: {xufton} 🌚")


@dp.callback_query_handler(text_contains="a1")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    today_time = datetime.today().now()
    p = open("Image/Без названия.jpg", "rb")
    today = today_time + timedelta(minutes=15)
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/andijon").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"Bomdod: {bomdod} 🌑    "
                                 f"|Quyosh: {quyosh_ch} 🌒\nPeshin: {peshin} 🌕       "
                                 f"|Asr: {asr} 🌔\nShom: {shom} 🌑 "
                                 f"        |Xufton: {xufton} 🌚")


@dp.callback_query_handler(text_contains="a2")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    today_time = datetime.today().now()
    p = open("Image/Без названия.jpg", "rb")
    today = today_time + timedelta(minutes=15)
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/andijon").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"Bomdod: {bomdod} 🌑    "
                                 f"|Quyosh: {quyosh_ch} 🌒\nPeshin: {peshin} 🌕       "
                                 f"|Asr: {asr} 🌔\nShom: {shom} 🌑 "
                                 f"        |Xufton: {xufton} 🌚")


@dp.callback_query_handler(text_contains="f1")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    today_time = datetime.today().now()
    p = open("Image/Без названия.jpg", "rb")
    today = today_time + timedelta(minutes=15)
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/farg'ona").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"Bomdod: {bomdod} 🌑    "
                                 f"|Quyosh: {quyosh_ch} 🌒\nPeshin: {peshin} 🌕       "
                                 f"|Asr: {asr} 🌔\nShom: {shom} 🌑 "
                                 f"        |Xufton: {xufton} 🌚")


@dp.callback_query_handler(text_contains="f2")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    today_time = datetime.today().now()
    p = open("Image/Без названия.jpg", "rb")
    today = today_time + timedelta(minutes=15)
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/farg'ona").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"Bomdod: {bomdod} 🌑    "
                                 f"|Quyosh: {quyosh_ch} 🌒\nPeshin: {peshin} 🌕       "
                                 f"|Asr: {asr} 🌔\nShom: {shom} 🌑 "
                                 f"        |Xufton: {xufton} 🌚")


@dp.callback_query_handler(text_contains="b2")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    today_time = datetime.today().now()
    p = open("Image/Без названия.jpg", "rb")
    today = today_time + timedelta(minutes=15)
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/buxoro").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"Bomdod: {bomdod} 🌑    "
                                 f"|Quyosh: {quyosh_ch} 🌒\nPeshin: {peshin} 🌕       "
                                 f"|Asr: {asr} 🌔\nShom: {shom} 🌑 "
                                 f"        |Xufton: {xufton} 🌚")


@dp.callback_query_handler(text_contains="b3")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    today_time = datetime.today().now()
    p = open("Image/Без названия.jpg", "rb")
    today = today_time + timedelta(minutes=15)
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/buxoro").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"Bomdod: {bomdod} 🌑    "
                                 f"|Quyosh: {quyosh_ch} 🌒\nPeshin: {peshin} 🌕       "
                                 f"|Asr: {asr} 🌔\nShom: {shom} 🌑 "
                                 f"        |Xufton: {xufton} 🌚")


@dp.callback_query_handler(text_contains="s1")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    today_time = datetime.today().now()
    p = open("Image/Без названия.jpg", "rb")
    today = today_time + timedelta(minutes=15)
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/samarqand").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"Bomdod: {bomdod} 🌑    "
                                 f"|Quyosh: {quyosh_ch} 🌒\nPeshin: {peshin} 🌕       "
                                 f"|Asr: {asr} 🌔\nShom: {shom} 🌑 "
                                 f"        |Xufton: {xufton} 🌚")


@dp.callback_query_handler(text_contains="s2")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    today_time = datetime.today().now()
    p = open("Image/Без названия.jpg", "rb")
    today = today_time + timedelta(minutes=15)
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/samarqand").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"Bomdod: {bomdod} 🌑    "
                                 f"|Quyosh: {quyosh_ch} 🌒\nPeshin: {peshin} 🌕       "
                                 f"|Asr: {asr} 🌔\nShom: {shom} 🌑 "
                                 f"        |Xufton: {xufton} 🌚")


@dp.callback_query_handler(text_contains="m1")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    today_time = datetime.today().now()
    p = open("Image/Без названия.jpg", "rb")
    today = today_time + timedelta(minutes=15)
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/navoiy").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"Bomdod: {bomdod} 🌑    "
                                 f"|Quyosh: {quyosh_ch} 🌒\nPeshin: {peshin} 🌕       "
                                 f"|Asr: {asr} 🌔\nShom: {shom} 🌑 "
                                 f"        |Xufton: {xufton} 🌚")


@dp.callback_query_handler(text_contains="m2")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    today_time = datetime.today().now()
    p = open("Image/Без названия.jpg", "rb")
    today = today_time + timedelta(minutes=15)
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/navoiy").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"Bomdod: {bomdod} 🌑    "
                                 f"|Quyosh: {quyosh_ch} 🌒\nPeshin: {peshin} 🌕       "
                                 f"|Asr: {asr} 🌔\nShom: {shom} 🌑 "
                                 f"        |Xufton: {xufton} 🌚")


@dp.callback_query_handler(text_contains="o1")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    today_time = datetime.today().now()
    p = open("Image/Без названия.jpg", "rb")
    today = today_time + timedelta(minutes=15)
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/nukus").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"Bomdod: {bomdod} 🌑    "
                                 f"|Quyosh: {quyosh_ch} 🌒\nPeshin: {peshin} 🌕       "
                                 f"|Asr: {asr} 🌔\nShom: {shom} 🌑 "
                                 f"        |Xufton: {xufton} 🌚")


@dp.callback_query_handler(text_contains="o2")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    today_time = datetime.today().now()
    p = open("Image/Без названия.jpg", "rb")
    today = today_time + timedelta(minutes=15)
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/nukus").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"Bomdod: {bomdod} 🌑    "
                                 f"|Quyosh: {quyosh_ch} 🌒\nPeshin: {peshin} 🌕       "
                                 f"|Asr: {asr} 🌔\nShom: {shom} 🌑 "
                                 f"        |Xufton: {xufton} 🌚")


@dp.callback_query_handler(text_contains="q1")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    today_time = datetime.today().now()
    p = open("Image/Без названия.jpg", "rb")
    today = today_time + timedelta(minutes=15)
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/qarshi").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"Bomdod: {bomdod} 🌑    "
                                 f"|Quyosh: {quyosh_ch} 🌒\nPeshin: {peshin} 🌕       "
                                 f"|Asr: {asr} 🌔\nShom: {shom} 🌑 "
                                 f"        |Xufton: {xufton} 🌚")


@dp.callback_query_handler(text_contains="q2")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    today_time = datetime.today().now()
    p = open("Image/Без названия.jpg", "rb")
    today = today_time + timedelta(minutes=15)
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/qarshi").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"Bomdod: {bomdod} 🌑    "
                                 f"|Quyosh: {quyosh_ch} 🌒\nPeshin: {peshin} 🌕       "
                                 f"|Asr: {asr} 🌔\nShom: {shom} 🌑 "
                                 f"        |Xufton: {xufton} 🌚")


if __name__ == '__main__':
    executor.start_polling(dp)