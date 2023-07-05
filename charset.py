# generate charset based on the language

def get_charset(language='en_36'):

    if language == 'en_36':
        return '0123456789abcdefghijklmnopqrstuvwxyz'

    elif language == 'en_62':
        return '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    elif language == 'en_94':
        return '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '

    elif language == 'hindi_128':
        unicode_min = 0x0900
        unicode_max = 0x097F
        printable_glyphs = [ chr(x) for x in range(unicode_min, unicode_max+1) if chr(x).isprintable() ]
        s1 = ""
        for i in printable_glyphs:
            s1 += i
        charset  = s1
        return charset

    elif language == 'hindi_142':
        unicode_min = 0x0900
        unicode_max = 0x097F
        printable_glyphs = [ chr(x) for x in range(unicode_min, unicode_max+1) if chr(x).isprintable() ]
        s1 = ""
        for i in printable_glyphs:
            s1 += i
        charset  = s1
        charset += '0123456789./,-'
        return charset

    elif language == 'hindi_161':
        unicode_min = 0x0900
        unicode_max = 0x097F
        printable_glyphs = [ chr(x) for x in range(unicode_min, unicode_max+1) if chr(x).isprintable() ]
        s1 = ""
        for i in printable_glyphs:
            s1 += i
        charset  = s1
        charset += '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
        return charset

    elif language == 'gujarati':
        unicode_min = 0x0A80
        unicode_max = 0x0AFF
        printable_glyphs = [ chr(x) for x in range(unicode_min, unicode_max+1) if chr(x).isprintable() ]
        s1 = ""
        for i in printable_glyphs:
            s1 += i
        charset  = s1
        return charset

    elif language == 'kannada':
        unicode_min = 0x0C80
        unicode_max = 0x0CFF
        printable_glyphs = [ chr(x) for x in range(unicode_min, unicode_max+1) if chr(x).isprintable() ]
        s1 = ""
        for i in printable_glyphs:
            s1 += i
        charset  = s1
        return charset

    elif language == 'odia':
        unicode_min = 0x0B00
        unicode_max = 0x0B7F
        printable_glyphs = [ chr(x) for x in range(unicode_min, unicode_max+1) if chr(x).isprintable() ]
        s1 = ""
        for i in printable_glyphs:
            s1 += i
        charset  = s1
        return charset

    elif language == 'bengali':
        unicode_min = 0x0980
        unicode_max = 0x09FF
        printable_glyphs = [ chr(x) for x in range(unicode_min, unicode_max+1) if chr(x).isprintable() ]
        s1 = ""
        for i in printable_glyphs:
            s1 += i
        charset  = s1
        return charset
    
    # elif language == 'assamese':
    #     unicode_min = 0x0980
    #     unicode_max = 0x09FF
    #     printable_glyphs = [ chr(x) for x in range(unicode_min, unicode_max+1) if chr(x).isprintable() ]
    #     s1 = ""
    #     for i in printable_glyphs:
    #         s1 += i
    #     charset  = s1
    #     charset += ' '
    #     return charset

    elif language == 'as97':
        unicode_min = 0x0980
        unicode_max = 0x09FF
        printable_glyphs = [ chr(x) for x in range(unicode_min, unicode_max+1) if chr(x).isprintable() ]
        s1 = ""
        for i in printable_glyphs:
            if (ord(i) != 2551):
                s1 += i
        charset  = s1
        charset += '-।'
        return charset