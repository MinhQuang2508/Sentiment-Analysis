vnese_stop_words_list = [
    "ai",
    "anh",
    "cha",
    "bố",
    "bà",
    "bác",
    "bạn",
    "tao",
    "mẹ",
    "con",
    "mày",
    "em",
    "mình",
    "tớ",
    "tôi",
    "nó",
    "hắn",
    "cụ",
    "chú",
    "cậu",
    "mợ",
    "dì",
    "thím",
    "anh", 
    "con",
    "cháu",
    "lão",
    "huynh",
    "đệ",
]
emotion_dist = {
    "Enjoyment": 0,
    "Fear": 1,
    "Anger": 2,
    "Sadness": 3,
    "Disgust": 4,
    "Surprise": 5,
    "Other": 6,
}
emoticon_dist = {
    ":)": ":smiling_face:",
    "☻": ":smiling_face:",
    "☺": ":smiling_face:",
    "=)": ":smiling_face:",
    ":‑)": ":smiling_face:",
    ":)": ":smiling_face:",
    ":-]": ":smiling_face:",
    ":]": ":smiling_face:",
    ":->": ":smiling_face:",
    ":>": ":smiling_face:",
    "8-)": ":smiling_face:",
    "8)": ":smiling_face:",
    ":-}": ":smiling_face:",
    ":}": ":smiling_face:",
    ":o)": ":smiling_face:",
    ":c)": ":smiling_face:",
    ":^)": ":smiling_face:",
    "=]": ":smiling_face:",
    "=)": ":smiling_face:",
    ":-)": ":smiling_face:",
    ":(": ":frowning_face:",
    ":c": ":frowning_face",
    "-.-": ":shaming_face:",
    "- _ -": ":shaming_face:",
    "xD": ":smiling_face:",
    "XD": ":smiling_face:",
    "@@": ":surprise_face:",
    ':">': ":tears_of_happiness:",
    ":v": ":surprise_face:",
    ":V": ":surprise_face:",
    ":3": ":playful_face:",
    ":<": ":frowning_face:",
    ">:(": ":angry_face:",
    ">:[": ":angry_face",
    ":'(": ":crying_face:",
    "• 3 •": ":cute_face:",
    "xd": ":shaming_face:",
    "uwu": ":cute_face:",
    "UwU": ":cute_face:",
    "owo": ":cute_face:",
    "OwO": ":cute_face:",
    "<\3": ":broken_heart:",
    "<3": ":heart:",
}
emoji_vietnamese_dist = {
    ":crying_face:": "khóc",
    ":thumbs_down:": "không thích", 
    ":kissing_face_with_closed_eyes:": "cảm ơn",
    ":confounded_face:": "xấu hổ",
    ":woman_facepalming_light_skin_tone:": "bất lực",
    ":frowning_face_with_open_mouth:": "thất vọng",
    ":two_hearts:": "yêu",
    ":sad_but_relieved_face:": "căng thẳng",
    ":beaming_face_with_smiling_eyes:": "vui sướng",
    ":cloud_with_rain:": "mưa",
    ":new_moon_face:": "mỉa mai",
    ":broken_heart:": "buồn",
    ":fearful_face:": "sợ hãi",
    ":face_with_hand_over_mouth:": "im lặng",
    ":thumbs_up:": "thích",
    ":star-struck:": "ngưỡng mộ",
    ":spider_web:": "mạng nhện",
    ":angry_face:": "tức giận",
    ":weary_face:": "mệt mỏi",
    ":face_with_open_mouth:": "ngạc nhiên",
    ":neutral_face:": "bình thường",
    ":man_facepalming_light_skin_tone:": "bất lực",
    ":smiling_face_with_hearts:": "niềm vui",
    ":ghost:": "dễ thương",
    ":dog:": "chó",
    ":pile_of_poo:": "đống phân",
    ":smiling_face_with_open_hands:": "cởi mở",
    ":crying_cat:": "khóc",
    ":sleepy_face:": "buồn ngủ",
    ":expressionless_face:": "vô cảm",
    ":money-mouth_face:": "giàu có",
    ":red_heart:": "yêu",
    ":grinning_face_with_big_eyes:": "vui vẻ",
    ":face_with_monocle:": "tìm hiểu",
    ":slightly_frowning_face:": "buồn rầu",
    ":kiss_mark:": "hôn",
    ":upside-down_face:": "mỉa mai",
    ":relieved_face:": "nhẹ nhõm",
    ":clapping_hands:": "vỗ tay",
    ":frowning_face:": "buồn bã",
    ":grinning_face:": "rất vui",
    ":face_with_tears_of_joy:": "vui phát khóc",
    ":face_screaming_in_fear:": "sợ hãi",
    ":grimacing_face:": "lo lắng",
    ":persevering_face:": "khó chịu",
    ":thinking_face:": "đắn đo",
    ":beating_heart:": "yêu thích",
    ":heart_suit:": "tình yêu",
    ":rolling_on_the_floor_laughing:": "cưới lăn lộn",
    ":shushing_face:": "im lặng",
    ":woman_facepalming:": "bất lực",
    ":squinting_face_with_tongue:": "vui vẻ",
    ":woman_pouting_light_skin_tone:": "tức giận",
    ":pensive_face:": "trầm ngâm",
    ":smiling_face_with_heart-eyes:": "tình yêu",
    ":full_moon_face:": "chế giễu",
    ":enraged_face:": "rất tức giận",
    ":anxious_face_with_sweat:": "lo sợ",
    ":zany_face:": "hài hước",
    ":face_with_raised_eyebrow:": "nghi ngờ",
    ":tired_face:": "mệt mỏi",
    ":smirking_face:": "tinh nghịch",
    ":sleeping_face:": "buồn ngủ",
    ":winking_face:": "hài hước",
    ":face_with_steam_from_nose:": "tức giận",
    ":face_with_symbols_on_mouth:": "tức giận",
    ":flushed_face:": "xấu hổ",
    ":kissing_face:": "hôn",
    ":confused_face:": "bối rối",
    ":face_with_rolling_eyes:": "buồn chán",
    ":smiling_cat_with_heart-eyes:": "tình yêu",
    ":winking_face_with_tongue:": "hài hước",
    ":loudly_crying_face:": "khóc to",
    ":face_without_mouth:": "im lặng",
    ":slightly_smiling_face:": "cười mỉm",
    ":smiling_face_with_smiling_eyes:": "vui vẻ",
    ":OK_hand:": "được thôi",
    ":face_vomiting:": "kinh tởm",
    ":clapping_hands_light_skin_tone:": "vỗ tay",
    ":anguished_face:": "tức giận",
    ":cat_with_tears_of_joy:": "bất lực",
    ":nauseated_face:": "buồn nôn",
    ":hot_face:": "gợi cảm",
    ":flexed_biceps:": "cơ bắp",
    ":downcast_face_with_sweat:": "căng thẳng",
    ":disappointed_face:": "thất vọng",
    ":smiling_face_with_horns:": "nham hiểm",
    ":index_pointing_up:": "ngón trỏ",
    ":folded_hands:": "cảm ơn",
    ":smiling_face_with_sunglasses:": "tự tin",
    ":exploding_head:": "khó chịu",
    ":drooling_face:": "khát khao",
    ":grinning_face_with_smiling_eyes:": "vui vẻ",
    ":victory_hand:": "chiến thắng",
    ":sneezing_face:": "hắt xì",
    ":grinning_squinting_face:": "hài hước",
    ":grinning_face_with_sweat:": "khó xử",
    ":woman_dancing:": "nhảy múa",
    ":cherry_blossom:": "hoa anh đào",
    ":dog_face:": "chó",
    ":surprise_face:": "ngạc nhiên",
    ":shaming_face:": "xấu hổ",
    ":playful_face:": "vui đùa",
    ":tears_of_happiness:": "mừng sắp khóc",
    ":smiling_face:": "cười vui",
    ":face_blowing_a_kiss:": "yêu đương",
    ":unamused_face:": "khó chịu",
    ":face_with_head-bandage:": "đau đớn",
    ":face_savoring_food:": "thèm thuồng",
    ":cute_face:": "dễ thương",
    ":heart:": "yêu",
    ":broken_heart:": "buồn",
    ":love-you_gesture:": "mình yêu bạn",
    ":face_with_crossed-out_eyes:": "bất ngờ",
    ":astonished_face:": "kinh ngạc",
    ":hushed_face:": "bất ngờ há mồm",
    ":weary_cat:": "mèo ngạc nhiên",
    ":face_with_tongue:":"hài hước",
    ":zipper-mouth_face:": "Tôi không thể nói gì về điều đó",
    ":pleading_face:":"buồn bã",
    ":wilted_flower:":"hoa hồng buồn bã",
    ":worried_face:":"mặt lo lắng",
    ":face_with_spiral_eyes:":"ghê tởm",
    ":skull:": "đầu lâu tiêu cực",
    ":woozy_face:": "buồn bã",
    ":snake:": "con rắn",
    " ‍:fire:":"lửa",
    " :tomato:":"cà chua",
    ":face_with_thermometer:" : "buồn",
    
    
    
}
spell_correct_dist = {
    "zui": "vui",
    "thw": "thương",
    "đéo": "không",
    "mng": "mọi người",
    "dể": "dễ",
    "đmm": "địt mẹ mày",
    "duới": "dưới",
    "đỉ": "đĩ",
    "đuỹ": "đĩ",
    "tuỳ": "tùy",
    "klk": "haha",
    "skil": "skill",
    "trog": "trong",
    "ko": "không",
    "per": "bạn",
    "trất": "chốt",
    "hs": "học sinh",
    "pạt": "phạt",
    "t": "tao",
    "sgk": "sách giáo khoa",
    "cv": "công việc",
    "kq": "kết quả",
    "dzầy": "vậy",
    "mj": "mặt dày",
    "c": "chị",
    "ad": "admin",
    "ah": "à",
    "z": "vậy",
    "nhìu": "nhiều",
    "cta": "chúng ta",
    "đm": "địt mẹ",
    "v": "vậy",
    "ks": "khách sạn",
    "àk": "à",
    "k": "không",
    "m": "mày",
    "ngulon": "ngu lồn",
    "vkl": "vãi cả lồn",
    "dume": "đụ mẹ",
    "hoà": "hòa",
    "nyc": "người yêu cũ",
    "nge": "nghe",
    "zi": "vậy",
    "chẳn": "chẳng",
    "bos": "boss",
    "sứng": "xứng",
    "of": "của",
    "kip": "kịp",
    "g": "gì",
    "volum": "volume",
    "chowi": "chơi",
    "dlm": "đĩ lồn má",
    "ghêe": "ghê",
    "gane": "game",
    "fải": "phải",
    "or": "hoặc",
    "zời": "trời",
    "viẹc": "việc",
    "vler": "vãi lồn",
    "giớ": "giới",
    "zo": "vào",
    "tr": "trước",
    "nta": "người ta",
    "thậc": "thật",
    "lsao": "là sao",
    "mặp": "mập",
    "hàg": "hàng",
    "vcb": "vãi cả buồi",
    "tý": "tí",
    "time": "thời gian",
    "mink": "mình",
    "nv": "nhân viên",
    "thuờg": "thường",
    "loai": "loại",
    "dõ": "rõ",
    "vl": "vãi lồn",
    "thuoc": "thuộc",
    "bat": "bắt",
    "kiem": "kiếm",
    "chời": "trời",
    "shiper": "shipper",
    "quáa": "quá",
    "del": "đéo",
    "dcm": "địt con mẹ",
    "hoạ": "họa",
    "th": "thằng",
    "vn": "việt nam",
    "ng": "người",
    "phia": "khuya",
    "lìn": "lồn",
    "ntnay": "từ nay",
    "cm": "con mẹ",
    "lun": "luôn",
    "trol": "troll",
    "cf": "cafe",
    "cở": "cởi",
    "thg": "thằng",
    "dth": "dễ thương",
    "hjxhjx": "hic hic",
    "ngta": "ngươi ta",
    "hloz": "hãm lồn",
    "ac": "anh chị",
    "hâha": "haha",
    "zai": "trai",
    "đựoc": "được",
    "híc": "hic",
    "rhì": "thì",
    "zay": "vậy",
    "zoe": "xoe",
    "záy": "váy",
    "diển": "diễn",
    "hlv": "huấn luyện viên",
    "đbh": "không bình thường",
    "tno": "tụi nó",
    "dùm": "giùm",
    "độg": "động",
    "cs": "cuộc sống",
    "hoả": "hỏa",
    "hp": "hạnh phúc",
    "gê": "ghê",
    "bth": "bình thường",
    "cẩng": "cẳng",
    "sời": "giởi",
    "kara": "karaoke",
    "loz": "lồn",
    "facebok": "facebook",
    "mừn": "mình",
    "rùi": "rồi",
    "chuc": "chúc",
    "toà": "tòa",
    "inter": "internet",
    "kau": "tao",
    "dt": "điện thoại",
    "xog": "xong",
    "doạ": "dọa",
    "hoc": "học",
    "dg": "đang",
    "dap": "đáp",
    "rat": "rất",
    "tuyet": "tuyệt",
    "saolol": "xạo lồn",
    "bn": "bạn",
    "troét": "trét",
    "ak": "à",
    "đzai": "đẹp trai",
    "iêu": "yêu",
    "thíu": "thiếu",
    "ukm": "ừm",
    "rỡi": "rời",
    "caphe": "cà phê",
    "tn": "thế này",
    "sg": "sài gòn",
    "bep": "không",
    "kbh": "không bình thường",
    "xĩu": "xỉu",
    "mềnh": "mình",
    "ĩa": "ỉa",
    "toau": "tao",
    "íu": "không",
    "bankon": "ban công",
    "đag": "đang",
    "rmit": "miết",
    "vcd": "vãi cả đái",
    "xh": "xã hội",
    "đếu": "không",
    "đỹ": "đĩ",
    "cmt": "comment",
    "đcm": "địt con mẹ",
    "mịa": "má",
    "ctay": "chia tay",
    "tuôi": "tôi",
    "qtrong": "quan trọng",
    "nghr": "nghe",
    "hoá": "hóa",
    "ds": "dễ sợ",
    "khoẻ": "khỏe",
    "đg": "đường",
    "hã": "hả",
    "cíu": "cứu",
    "xomg": "xong",
    "sx": "sản xuất",
    "hơm": "không",
    "shits": "shit",
    "lien": "liên",
    "fre": "free",
    "móe": "má",
    "đíu": "không",
    "hỉu": "hiểu",
    "godbye": "goodbye",
    "ây": "ấy",
    "ez": "dễ",
    "dme": "đụ mẹ",
    "thẳg": "thẳng",
    "ml": "mặt lồn",
    "niếm": "nếm",
    "xời": "trời",
    "đame": "sát thương",
    "nguối": "cúi",
    "đhs": "không hiểu sao",
    "giốg": "giống",
    "nhưg": "nhưng",
    "tưởg": "tưởng",
    "toè": "tòe",
    "tưong": "tương",
    "sug": "sung",
    "lám": "lắm",
    "vẫ": "vẫn",
    "post": "facebook",
    "màt": "mày",
    "xò": "sò",
    "dma": "đụ má",
    "gv": "giáo viên",
    "vid": "video",
    "doume": "đụ mẹ",
    "qcao": "quảng cáo",
    "hj": "hi",
    "nghờ": "ngờ",
    "xiền": "tiền",
    "thạ": "thả",
    "halo": "zalo",
    "hoy": "thôi",
    "cũnh": "cũng",
    "chữi": "chửi",
    "thiì": "thì",
    "dm": "địt mẹ",
    "kím": "kiếm",
    "cũg": "cũng",
    "ngưỡn": "ngưỡng",
    "oy": "rồi",
    "chj": "chị",
    "vướn": "vướng",
    "pê": "mang",
    "dkm": "địt con mẹ",
    "uoc": "ước",
    "duoc": "được",
    "top1": "top 1",
    "mat": "mà",
    "đúi": "đuối",
    "hịt": "hệt",
    "comt": "comment",
    "oke": "ok",
    "chổ": "chỗ",
    "xãy": "xảy",
    "nhât": "nhất",
    "cừi": "cười",
    "đọan": "đoạn",
    "phảu": "phải",
    "hix": "hic",
    "daklak": "đắc lắk",
    "chiêc": "chiếc",
    "đh": "đại học",
    "quâ": "quá",
    "qa": "quá",
    "đũy": "đĩ",
    "sat": "sát",
    "klq": "không liên quan",
    "bằg": "bằng",
    "nghệt": "nghệ",
    "đki": "đăng kí",
    "chúg": "chúng",
    "ngổng": "ngỗng",
    "cmnl": "con mẹ nó lồn",
    "quad": "quá",
    "vailon": "vãi lồn",
    "nhg": "nhưng",
    "truỵên": "truyện",
    "tks": "cảm ơn",
    "roai": "rồi",
    "đaumoa": "đụ má",
    "bit": "biết",
    "ngiu": "người yêu",
    "dv": "diễn viên",
    "virut": "virus",
    "7nam": "7 năm",
    "thặc": "thật",
    "cungz": "cũng",
    "maiz": "mãi",
    "lm": "làm",
    "choét": "trét",
    "màa": "mà",
    "gdinh": "gia đình",
    "stk": "số tài khoản",
    "nhiếu": "nhiều",
    "nhma": "nhưng mà",
    "đển": "đến",
    "ônc": "ông",
    "csong": "cuộc sống",
    "disme": "địt mẹ",
    "ngĩ": "nghĩ",
    "tq": "trung quốc",
    "tữn": "khùng",
    "xiaolon": "xạo lồn",
    "đcđ": "không chịu được",
    "thoả": "thỏa",
    "csgt": "cảnh sát giao thông",
    "xạolin": "xạo lồn",
    "blod": "blood",
    "kil": "kill",
    "xiaolin": "xạo lồn",
    "thiệc": "thật",
    "hịn": "xịn",
    "nãn": "nản",
    "mịe": "mẹ",
    "huỷ": "hủy",
    "hiuhiu": "huhu",
    "bt": "biết",
    "thíck": "thích",
    "cã": "cả",
    "àh": "à",
    "dis": "địt",
    "gvien": "giáo viên",
    "đma": "đụ má",
    "rược": "rượt",
    "chộm": "trộm",
    "céc": "cặc",
    "đkm": "địt con mẹ",
    "cđv": "cổ động viên",
    "cại": "lại",
    "chậy": "chị",
    "quí": "quý",
    "hêtd": "hết",
    "piza": "pizza",
    "kv": "khu vực",
    "hjhj": "hihi",
    "ful": "full",
    "hnua": "hôm nữa",
    "sốn": "sống",
    "bcs": "bao cao su",
    "sag": "sang",
    "mìh": "mình",
    "moẹ": "mẹ",
    "từg": "từng",
    "ngheng": "nhen",
    "xún": "xuống",
    "đx": "được",
    "mọe": "mẹ",
    "kphai": "không phải",
    "fr": "friend",
    "mod": "mood",
    "nũa": "nữa",
    "bede": "bê đê",
    "rồu": "rồi",
    "helo": "hello",
    "dống": "giống",
    "đựu": "đụ",
    "nguoi": "người",
    "đoá": "đóa",
    "ẳm": "ẳm",
    "nghia": "nghĩa",
    "het": "hết",
    "liết": "liếc",
    "hỏg": "hỏng",
    "đep": "đẹp",
    "sn": "sinh nhật",
    "dòg": "dòng",
    "mxh": "mạng xã hội",
    "chg": "chẳng",
    "thằg": "thằng",
    "bổg": "bổng",
    "karaok": "karaoke",
    "thoy": "thôi",
    "xl": "xạo lồn",
    "qá": "quá",
    "cừng": "cũng",
    "mều": "mèo",
    "vlon": "vãi lồn",
    "troai": "trai",
    "ava": "avatar",
    "qúa": "quá",
    "folow": "follow",
    "thât": "thật",
    "đuợc": "được",
    "ngừoi": "người",
    "càrôt": "cà rốt",
    "kô": "không",
    "vửa": "vừa",
    "clm": "con lồn má",
    "xink": "xinh",
    "xoè": "xòe",
    "tg": "thời gian",
    "nhoà": "nhòa",
    "valungtung": "lung tung",
    "hoạng": "hoảng",
    "đaklak": "đắk lắk",
    "hk": "không",
    "ỏo": "ồ",
    "nghiêp": "nghiệp",
    "ju": "giữ",
    "jin": "gìn",
    "mlz": "mặt lồn",
    "matlon": "mặt lồn",
    "haizx": "vãi",
    "ny": "người yêu",
    "cug": "cũng",
    "gío": "gió",
    "bđ": "bóng đá",
    "bthg": "bình thường",
    "vliz": "vãi lồn",
    "đág": "đáng",
    "ngỗg": "ngỗng",
    "hịu": "hiệu",
    "đúg": "đúng",
    "rụg": "rụng",
    "trg": "trường",
    "vks": "vãi cả lồn",
    "chẹ": "chọe",
    "mis": "miss",
    "zị": "vị",
    "dzậy": "vậy",
    "khôg": "không",
    "dhs": "không hiểu sao",
    "gvcn": "giáo viên chủ nhiệm",
    "coá": "quá",
    "hqua": "hôm qua",
    "géc": "ghét",
    "nhaỷ": "nhảy",
    "lổi": "lỗi",
    "thik": "thích",
    "noá": "nó",
    "chuân": "chuẩn",
    "chụy": "chị",
    "mòa": "mà",
    "hnao": "hôm nào",
    "galang": "ga lăng",
    "giay": "giây",
    "nthe": "như thế",
    "douma": "đụ má",
    "đẹo": "đẹp",
    "gheê": "ghê",
    "nuôn": "luôn",
    "gét": "ghét",
    "chêu": "trêu",
    "buf": "buff",
    "vcl": "vãi cả lồn",
    "síu": "xíu",
    "zồi": "giời",
    "mừ": "mà",
    "trym": "chim",
    "adim": "admin",
    "nhình": "nhìn",
    "cofe": "coffee",
    "loat": "loạt",
    "hc": "học",
    "zại": "dạy",
    "moij": "mọi",
    "cườ": "cười",
    "hiếmk": "hiếm",
    "cng": "con người",
    "masage": "massage",
    "ngọai": "ngoại",
    "cđcm": "cái địt con mẹ",
    "êi": "ơi",
    "tml": "thằng mặt lồn",
    "oimeoi": "ôi mẹ ơi",
    "ron": "rôn",
    "chyện": "chuyện",
    "ngẵn": "ngắn",
    "thõa": "xõa",
    "ụa": "ủa",
    "lôz": "lồn",
    "truong": "trường",
    "hop": "hợp",
    "thuong": "thương",
    "khac": "khác",
    "riền": "riêng",
    "ae": "anh em",
    "biet": "biết",
    "tiep": "tiếp",
    "tnao": "thế nào",
    "mợt": "mệt",
    "chetme": "chết mẹ",
    "pải": "phải",
    "nhưnh": "nhưng",
    "thix": "thích",
    "gơm": "gớm",
    "găp": "gặp",
    "ùi": "rồi",
    "suong": "sướng",
    "bjt": "biết",
    "tôgn": "tồn",
    "củng": "cũng",
    "oto": "ô tô",
    "haiz": "thở dài",
    "ẻ": "ỉa",
    "ay": "này",
    "ok": "đồng ý",
    "móa": "má",
    "moá": "má",
    "giởi": "trời",
    "ự": "hự",
    "ừm": "ừ",
    "mổi": "mỗi",
    "haiza": "buồn",
    "ưi": "ơi",
    "tiển": "triển",
    "kỉu": "kiểu",
    "ghệ": "người yêu",
    "col": "coi",
    "nhãm": "nhảm",
    "chuỵ": "chị",
    "iem": "em",
    "phìm": "phim",
    "ỏ": "ồ",
    "ẻm": "em ấy",
    "ôtô": "ô tô",
    "chỉa": "chìa",
    "mớinxem": "mới xem",
    "chs": "chả hiểu sao",
    'uớc': 'ước',
    'fa': 'cô đơn',
    'clgt': 'cái lồn gì thế',
    'khùm': 'khùng',
    'ak': 'à',
    'đin': 'điên',
    'mài': 'mày',
    'xèm': 'xàm',
    'dui': 'vui',
    'hông': 'không',
    'bùn': 'buồn',
    'bít': 'biết',
    'nma': 'nhưng mà',
    'mún': 'muốn',
    'bỉn': 'biển',
    'mớ': 'mới',
    'nhén': 'nhắn',
    'dịt': 'việt',
    'chít': 'chết',
    'mịa': 'mẹ',
    'dị': 'vậy',
    'đel': 'không',
    'del': 'không',
    'nhma': 'nhưng mà',
    'quớ': 'quá',
    'try': 'trai',
    'mọe': 'mẹ',
    'zãi': 'vãi',
    'dìa': 'về',
    'lém': 'lắm',
    'lừi': 'lười',
    'cbi': 'chuẩn bị',
    'ngèo': 'nghèo',
    'chóa': 'chó',
    'qué': 'quá',
    'mún': "muốn",
    'nch': 'nói chuyện',
    'lìn': 'lồn',
    'ik': 'đi',
    'éo': 'không',
    'thứk': 'thức',
    'mịt': "mệt",
    'pek': 'biết',
    'quãi': 'vãi',
    'hok': 'không',
    'mey': 'may',
    'đún': 'đúng',
    'gùi': 'rồi',
    'hỏ': 'hở',
    'hum': 'hôm',
    'm': 'mày',
    'đc': 'được',
    'tr': 'trời',
    'j': 'gì',
    'z': 'vậy',
    'r': 'rồi',
    'b': 'biết',
    'h': 'giờ',
    'k': 'không',
    'l': "lồn"
}