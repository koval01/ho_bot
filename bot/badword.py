words_list_ = [
    "блять",
    "блядина",
    "блядь",
    "сука",
    "сучара",
    "сучий",
    "мамкин",
    "мамка",
    "мамаша",
    "мамашу",
    "шлюха",
    "шлюхой",
    "ебливый",
    "еблан",
    "ебланище",
    "еблом",
    "ебать",
    "ебаный",
    "ёбаный",
    "ебарь",
    "ёбарь",
    "ебаться",
    "пиздить",
    "пиздиться",
    "пиздится",
    "хуярить",
    "хуй",
    "хуйня",
    "хуйнёй",
    "хуйней",
    "хуем",
    "хуём",
    "выеьыватся",
    "выёбыватся",
    "выёбывается",
    "выебывается",
    "выёбываеться",
    "выебываеться",
    "гавно",
    "гавна",
    "гавнище",
    "гавном",
    "дебил",
    "дебилом",
    "дебилам",
    "дебилов",
    "дебильный",
    "дебильная",
    "дебильным",
    "тупоголовый",
    "тупоголовые",
    "бараны",
    "придурки",
    "мудаки",
    "мудакам",
    "мудаками",
    "мудазвоны",
    "мудазвонам",
    "мудазвонов",
    "Путин",
    "Порошенко",
    "Зеленский",
    "Янукович",
    "Медведев",
    "Навальный",
    "Фапать",
    "фапает",
    "дрочит",
    "дрочил",
    "дрочильня",
    "порно",
    "порнуха",
    "секс",
    "пенис",
    "вагина",
    "пизда",
    "пиздой",
    "пиздец",
    "пиздецом",
    "пиздит",
    "тупой",
    "тупого",
    "дегенират",
    "дегенирата",
    "дегенираты",
    "ебат",
    "ебал",
    "наебал",
    "ебать",
    "пидор",
    "пидораст",
    "петух",
    "петухон",
    "сперма",
    "конча",
    "спермой",
    "кончой",
    "кончей",
    "дилдо",
    "страпон",
    "страпоном",
    "казино",
    "ставки",
    "промокоду",
    "киска",
    "вагину",
    "вагине",
    "жопе",
    "подрочи",
    "жопу",
    "жопа",
    "гомик",
    "гомика",
    "гамасек",
    "гамасека",
    "гамасеку",
    "гомику",
    "дауну",
    "даун",
    "дауна",
    "киску",
    "сиськи",
    "сиськами",
    "пустоголовый",
    "пустоголовому",
    "хую",
    "хер",
    "хером",
    "херня",
    "херней",
    "хернёй",
    "херовый",
    "хервоя",
    "херево",
    "херово",
    "хуйово",
    "хуеплёт",
    "хуиплёт",
    "ахуенно",
    "ахуительно",
    "ахуено",
    "говно",
    "срать",
    "обосраться",
    "обосратся",
    "абасраться",
    "абасратся",
    "сраное",
    "пиздёж",
    "маструбирую",
    "маструбирует",
    "ебаться",
    "ебатся",
    "ебётся",
    "ебёться",
    "ебётся",
    "еба",
    "ибат",
    "йеба",
    "эбат",
    "суча",
    "политический",
    "политические",
    "корупция",
    "корупционер",
    "корупционый",
    "корупцыонная",
    "корумпируваная",
    "донбас",
    "ебалово",
    "луганская",
    "анально",
    "донецкая",
    "анальный",
    "крым",
    "петушки",
    "долбодятлы",
    "долбодятел",
    "ахуе",
    "охуе",
    "охуи",
    "ахуи",
    "зоеби",
    "заеби",
    "трансгендер",
    "гей",
    "геи",
    "транссекусуал",
    "трансвестит",
    "трансвистит",
    "жопой",
    "хуем",
    "охер",
    "ахер",
    "прихуе",
    "прихуи",
    "прихер",
    "ахир",
    "мохнатка",
    "мохнатку",
    "розеб",
    "писичку",
    "писичкой",
    "писечки",
    "вагинальный",
    "инцес",
    "кунилингус",
    "дец",
    "хуеплётсво",
    "матка",
    "курва",
    "курица",
    "курицу",
    "блядки",
    "блядках",
    "гандон",
    "презерватив",
    "контрацептив",
    "сукин",
]

async def badworld_seach_(some_text):
    for i in words_list_:
        some_text = str(some_text.replace(str(i), "(плохое слово)"))
    return some_text
