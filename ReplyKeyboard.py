
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🤲 Namoz vaqtlarini bilish 🤲")
        ],
        [
            KeyboardButton(text="Duolar")
        ]
    ],
    resize_keyboard=True
)
menushahar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Toshkent"),
            KeyboardButton(text="Namangan"),
            KeyboardButton(text="Andijon")
        ],
        [
            KeyboardButton(text="Buxoro"),
            KeyboardButton(text="Farg'ona"),
            KeyboardButton(text="Samarqand")
        ],
        [
            KeyboardButton(text="Navoiy"),
            KeyboardButton(text="Nukus"),
            KeyboardButton(text="Qarshi")
        ],
        [
            KeyboardButton(text="Menu")
        ]
    ],
    resize_keyboard=True
)
menuduo = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1. Uyqudan uygonganda"),
            KeyboardButton(text="2. Juma tongida")
        ],
        [
            KeyboardButton(text="3. Uxlash uchun toshakka yotganda"),
            KeyboardButton(text="4. Bezovta bolib, uxlay olmaganda")
        ],
        [
            KeyboardButton(text="5. Uyquda qorqqanda"),
            KeyboardButton(text="6. Tushida yoqtirmagan narsani korganda")
        ],
        [
            KeyboardButton(text="7. Qon oldirganda"),
            KeyboardButton(text="8. Tahorat qilganda")
        ],
        [
            KeyboardButton(text="9. Masjidga ketayotganda"),
            KeyboardButton(text="10. Masjidga kirayotganda va undan chiqayotganda")
        ],
        [
            KeyboardButton(text="11. Namozdagi ruku'zikrlarini aytadi"),
            KeyboardButton(text="12. Namoz boshlaganda")
        ],
        [
            KeyboardButton(text="13. Ruku'dan bosh kotarganda va tik turganda"),
            KeyboardButton(text="14. Sajda paytida")
        ],
        [
            KeyboardButton(text="15. Hojatxonaga kirayotganda"),
            KeyboardButton(text="16. Hojatxonadan chiqayotganda")
        ],
        [
            KeyboardButton(text="17. Kiyim kiyishda"),
            KeyboardButton(text="18. Kiyim yechilganda")
        ],
        [
            KeyboardButton(text="19. Uydan chiqayotganda"),
            KeyboardButton(text="20. Qiyinchilik va Gamginlikda")
        ],
        [
            KeyboardButton(text="Ortga qaytish")
        ]
    ],
    resize_keyboard=True
)