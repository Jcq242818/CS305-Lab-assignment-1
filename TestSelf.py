"""
Author: Harry Wang
Date: 11/4/2022
"""

# creat a http request and send it to server
import random
import string
import socket
from collections import namedtuple
from typing import *
HTTPHeader = namedtuple('HTTPHeader', ['name', 'value'])
Host = '127.0.0.1:8080'

def resolveHeader(HTTPHeader):
    return HTTPHeader.name + ": " + HTTPHeader.value
def resolveAllHeader(HTTPHeaders):
    message = ""
    for header in HTTPHeaders:
        message = message + resolveHeader(header) + "\r\n"
    return message

def random_string(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

class HTTPClient():
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(('127.0.0.1', 8080))
        self.method = ''
        self.headers: List[HTTPHeader] = list()
        self.body: bytes = b''
        self.path = '/'
    def init_post_request(self):
        self.method = 'POST'
        content = random_string(10240) # 这里发一个超长的报文

        # # conner case body部分以\r\n\r\n 开头,取消注释测试
        content = "\r\n\r\n" + content


        self.body = content.encode()

        startline = f'{self.method} {self.path} HTTP/1.1\r\n'
        self.headers.append(HTTPHeader('Host', Host))
        self.headers.append(HTTPHeader('Content-Length', str(len(self.body))))
        self.headers.append(HTTPHeader('Content-Type', 'application/json'))
        Info = startline + resolveAllHeader(self.headers) + '\r\n' + content
        return Info.encode()

    def init_get_request(self):
        self.method = 'GET'
        startline = f'{self.method} {self.path} HTTP/1.1\r\n'
        self.headers.append(HTTPHeader('Host', Host))



    def send(self, request):
        self.socket.sendall(request)


client = HTTPClient('127.0.0.1',12345)
post_request = client.init_post_request()
client.send(post_request)
# client.socket.close()

# 这么长就是没收完
#SXRXSJKBT1LR0HYSAA4C8WA31CUICFZ4N7IW11YXIWXEHPT0KORPXEIMJFT3QHPQS81CG38LFA31XVBVKY2ZSWDTRMVLWIKQ1MBVLFW3HW1RRZSW39E36PICTMA5LXD7C0YVBUXXDHH681WR8CKONI209F1DSZO3WYV6B5AIRGAJUYCNQHEOZV7W5KSP9AFTVMPW5OUW6SHUQFIE5YB4HM11DRJ9Y2JF8G103S87IN4JPU70SQYBFLDSYCZLOMKG87G8DKAVXUADHLMKYP1QODOQ79SOWXGIVLSF6FFUHTTNTLSIYTV5K3GBGYLTK393VMV31K52V4TYHKGZGFUVEBXQ5DJG1I2KB55L5V20QP0TE8WBNH1O1Q084NEAASGGRK4SF9K3WOOBIM0D00KKM7F3RZE4V05J2WD3RBD5OFS68JD5APRBIQNC87OYJ84PEE1CNEQU9AAWB2MLJZ39CHMIUFR9G3O5TKXIETNO86K04CSCLTWUS7UWRHNYEK30GTSC6BAPRXDSESOJ3FXK8DBNSMEYRR49BR8HTWH9QIARTZY9WSQWBF3NZIBMT4DR1UW1D0KF0VRDU58ADHXKUL91GP7OUYP85J3MM8RG8QSURHZ5EY0MS46NQ7EYMBCL5CAANEKWQ4Q67HD01ONNYOLR3AEP6YTUUTSZQAJO1MF4A3LL4RBB5LKQQJQNYQZ550OADL0TJ49L2H66WJ6QQ8M0BO5R2X6L2KB4DU0K9YC7NGO0BFDKSYCAT97JQUA0CMIAP0G6LRCHB0S2Z0BV5V3JY2W3ERUV9IPFG8XPHPFZCXLRGO8K0Q1FPM2WMWZ25D6C3PFB2YJ482BOQOIOWXXBQ83SY9FSV4J8RBW8RGTV4OIFBR59AA5GOS3VUY97NFFS0A6DK4AS7L6WFJN810TWQ881ALORPO4OM75A37FG5B6EU71O136X4LWES9ZXUJ40B3ZG6WIO15WTNIL3K9OGJ12ANLNU9QMI8UNKGA2J6BEJG82DXG9G6CRFIFVW

# 这么长就是收完了
#5TANBT84RRLZ1EKTEQH738AQ5JK25XGFT3AEY7T038T96A5N7TKI0MM9EXM2EXX7GD6D706ITZN6V8YQVTRFKS555WKLB06AP57AMKUFTGZ63BG82S7ZUD3G2OHM0VNEMUH6GS685BA0C2ZOGGK6BFZRODNLLZLXDXAZCU7B63686GAEHU5TWR1M52C1CMR8ERZTOLW7B40LM9RNPTVBWARNK50I6KE8DLZ3DFIK5L93H20STU9TFKGALPPSN8ZJC1WK9HD21XEVEPX24OOT54QHJWI5UJIZ4L9VOERD1QBWLND3Z3BUQBOL89SQ0MCVCK2BQPR63N73GVWPWNPEDCF5TC3DFWOVCLXTHHXYF8MBINCN1X7PGTB1CF950Y1J6GQIKU0ETXLB9XEGWGWLZC8H13YIP1A9V5A77QWL98GAD2MTZHQ0IO6NXUYMM9HXSMORQQQNIUREFY0HDWZYV3OWP7LNPJOO9BT1NGLVCG94RBFSXFEI3S76OYG15703Q2K3FIRTI254URQU3K2XUS02RFYILP41B6GTTNF5CEAO2E7COOIX7EVEFFLMV58HH8GQFOLF7D396JTYNTPHNT1IUARLCKXNPKKSKODI8ANR2Q52UJ2KBB6CKC21JIZQ2HVJNH7DGRWXTB7M3XHARJ5PSLMEC848CRBLERAWEHE3WZDSPHJW32K4S310849EU8OI3YNUFIOUNMDLT1BO7IIO3H5ECMIS08ZY6L5O4NRY8IP4U2CBE9JD3ATBS6NFRF1ZYTHP2B54YOFGFSA7FUAR7ZIMQNL0AV9TNIVHOCCSX0RQR85YLFQHMYEJOPGUIRW8BSF88M6WHRU22Z9KNAP9KW2YRCCGTQYLAMYGJ90BUFO8PFWBGRI9J0LB5BFJNITSV2TAJLG6VAI9EPVOXW4I4SOUPXIYAYH4V6MXXSLKM8Q5F30MON5F7S1XSZ0RIBUS347OIRW9M2YPGY189ZLFIGVGC6AN7UMM2XGPHH0POEWVAESULXLI9E5CSXU9WSH54GWMYNRRYXKIC0AOJFB8PWCH7CUXJDT3A94MJJ9L1G12XVR57ZZORNX0ASE02SC3S7VGXMR9Z003CFREPFC76VGUBQGPBNJKOF7YTFW3FZMWISYWKWSDVCR8P2A8A1SH5PA2BOCV14AOI9GVN6YFUKKO5FK8IOFA87DZ5ALQRZWRS2U2RUH53M9JMNGARP0MU0VJT2GHRDNJGB4ODYJ0LBAEII7BQKUFVNFKN5LDF3R28QWLGCK27EX240TX7E0N5Z12D6UETDU3IA9SGCHOQK6KIZZD8UZWLZ81M0YP2OMWLW9ZA75C0SAOYK0U7B5RIF6DBLAMNV60LVFGG92YRJKD5GDDZTNP3PJAMDCBZYWNE1396QVIR5VX19O6L0CDBYCCWUZYT4HYYA77UDYG3P36ZCHOT5CFZ4I9DMX07YSK5ZIC2XPDXKQTEJM7XI2BNH5O5MTXV4KR91T7RO6BWWS9GHYICEMRONZUA9IA2VT6Y2BNIFH2ZNKABZZ197L5SME4XRSXIPK80NFBH3LXZ57VVQKTCRT6LVEPM5NAWLVXKYT784WS4ZQ32O4HWNERYMR51D8R0ZNG0NK2MAZCKLLXUG18BAQN3VNA0KALXI105V0LYNDMHBM63V2TJNO2IQ70ZI077AE3ID09B5FZR87WSCP2WI6IKQ3YQFF7RCKW3QSW6IBPK71S5YUIHR7Z4NWCKNQRNHY4S2WAOBZEFVMY6RCF5RZ48GO746AEOL7M0N0MVLT3KHEUXFU97HVH5WRLI72UMBLGM8368TI2LRH1TPYI22RJW7F88MWPL20V7ZXX6YQRPPGNBI8NA08LEZTILPCBIX5552A7I95HGLLWZET2H5TIRVP321AHZCL2FUPEA58XQ7BKNP189OCSADF907J1UYS1GVCT99MWYOTGA6NQDM3GRBZ7XCEV6XYSZ7FC4LFUS9CHGZEVI55JDKRJVZAMO79VW9WWPTCCO5TIQGR4A4V6P14LWS834MUUWJDK3TA2LYTJB32TFJSHSF95ESW1BR4UEM5RYP19PJLLFC3W1SWW1DO3S6XMYTSVQUDGVNO0RFCDV909SHSBOGRFKJUCBS36DFH0UB4ZXEIT4FTZYZJQYG3E1ZTAGK0THAL9J2W1FJMJK8DETPUXUZIL2X1N0K0Z4QOVSJJF0QMXKQH8HFITKTE8FP2ZC2MJSM42V9VJ4RTEIVH53IX6FMOB6C8L3TIFSVKGTLGTGD2IMCAXFGHQRQD2985TF20WJBEVO03IZ3WYZ0SFI9PEK229WI8YD48SKSFANA18E668ODZD7AT41IYAD2QW19ZGKTT0IZZQL8EKKQ3UIOADECP9GV3DS1A2QCYCK59USDOWK4VTFZVI0TOSSFUSQ656UNNA21KTGPMVMUHL89EEK3658KO1ZXGZE3U66P6GLRGPTX1HLYI1AGTEARP70AMEUVP8TJZ24G7H7YMX6XMBVGWRL6BTTFU9KBUR0BRWE6A2O6NFHS3F6IXCGVI289Z9ALS3J0XZXGVPY4WQF6G5QAZNHQJUZ91OV8A7RBBYG2YX3AISX38ZXPOVY9ZJ51YNXY5Q0FWFSLRXJNRV7LURR79UKC1BO4SUFOCRW3FTPXJ7ZD1YC61WAH4OS7D1IW6RKNAKB3FOW2YC0WETZK9ULGUPZH6TB46J2AQWGCIBJX51343TADFZ44Y74QXYTN6S8VYUW5U69WYDRRW2E0J969N4BGUYJEMD12498P0E0QUX2C4OLYTQN6KKVX5A0HZ41WLU97MJ97W1WL3TRHB18WWAY9OHJECUN7YJ000RHQTA4YAAE3B9XGKSQGGXPLP0H2BKVPV58B513F6336SFD0LOINGUN3QSGAT1IQSEUF9BFTB33Z0UW56HN4O4S9D2NRUCCU9W1MC78XO7NXWZ5I8PFYAWXLC753C9LF8M4KF3YLOV34F71SY4JWGCF5MVL8I757RPP0HEOWMUUUX9L1J8VBMMQ0W3WEJLZ7XUBMNXGCBFX7OIJZE86IBZIWZCJY6XFZLGHY6CPBF0CHR0VVLLWZBOBESAHUZEVX3NEJLZYURHRPT2TP41PG59I03JLNI5D1S1292KAJMPE5U1WEWNZR6300IQKKJ60BQXPNUY0VWW1KQJIZ7L5TF30VGJ6LMI31UY5R389XMXCCV6L6IZUN4UE3IVN2TX72NAS3ZKPZAVGPIQV67WCJQQ0AOWYDIRRDS8L1RFZ7IYTEZTW1PIQPXD91LAE6YB9KX6ZPELIBPMT54G6QZQC5GG3HV4W5UJA8U56KLS4Q7WA6GWIRT5H2ZR0VNOFBBPJ8EZA3HIMA33E8W5E4G2MNF5OMKQ3DCA3CKCJ2DQITOZOK7CAU5QOCMAIWZFRCFUXXTLANQUPUO1QAIAJW4WIHW8DOXHUUUMTP8MUJAFJQDCTXL3PHQZ73WIH6299YF4RGF5HN0BDMD89FPGF6JC244C1FIRO9EKX435D45W8XRGND4WGQLYENLEM05RTWSZVECF6YRSHHVO6B3EIPNE8WFCN5W7N4OA0K8C6UI3HWWP7Q8DJCKJQPOJ3ROF80SNWU9XWD8EJFZ0FCKP8WM2IGGY51EKMN2R4KRJEQDXOZSSQ52X5DWUT19P5D8XR7RNPGB9L56K22T3CHK405UW5VBKA50JGLDRENZ6UAYZLIJ7F5K4QL6KSVQZHGSBD1U69A3ORXANHUGIWXC8W1ZEPUZEAR9DBRZAORW22ARA3H2A1LU2RHTS1ZMMOVIWKZE7Z28ZEXUW81U0R7FC08B70HPOEC6E7CVR77LYW6WDYSR6C40UQ1EOLIKZASL386FNHVLZNCQHYOZZ88INACH9FIE3ULFZCFEV5TWWFKQ2ZX27KPHONSIM54G2C6ONAL1SXIZOY4M35806EBAE4LFV1I9H8XGMAB7Q5SKZQ0UE190E98C3OV29M1USVXSB65KJK256SLQ1SI4M8IFZ12TECU2XO2OZVPDKGFA76BEUGKHAEI21O0JP21NIB5KEFZG9IEZTI46NS5EV92TTHBKK96R07SRRU92MWH601ZD5EID9I51T8UH0SFVH27QBJKRSXVKHZQA19WGG6OPF2RQZQJ9XFCVTJ65ZPXN1KRON3C2ZBG187789LULZ4Z6Z4NR3L3XLKZ3ZJSZWK9FJ9CRM9N32RMHOWTTANBAIK9Q42DI8XPQYQFZNRC4DN74CT2HFEVLHIRB7C3R4OLL81DQ42IDBI0AND2FEYTXRHWHRJOHSJ01EC2FN923W2PEIDAJC8BEG6SVB1UVCEBMNZ4HY2GRLTL4AGQ5XF7FFXFERP8SXQ8KQS669PDH2KY9Z7XIUYH8BM8RZZDD59WTQOVL0P7KME143G76TFQMH3TVLM9TL0Z9GH5VSU7YXN2GFNZW0TQ452M9P0WH9A0AMA692AZ48S8FGWWDF6OGMHG8KORHJ2SA4JK2I912OIBG36UHSCR0KX5A126XPM3YRN1OMVTT1JB075DYDKQV9MJUHU0E5KW0Q5JVUW0MFHU71BDLPI3OBUSCQFM9WRV2W6UZY2PKLCMCW62ZIDV1LL866BCCORSSX3N01PPMQYS8MSXW83DHAM0G03OX9X94HAXFRB5FZ00MC9FA8DPJGOM6ZNC6YUSPTUU5WBA583ZB0ZZZTU7O5HGPPUQZZ9F5G8965QBHO67YVHME8JRUREH30LF70S1J8GD2MLIGXDVPTK68O1QFKH2WQVR1E9GH03JTJUQYR6Z70NKFXCLWFL9Q2YUOR0KDY2EHXSMDOH1Y9O7LUACGXBB2GFQY3TS9YW2FJAS6F80303DI0O0X4L0U1FSY4R2HUKI8KU4FVTF4AL70IKCJQ6LVD84X2BNV2QNOTTOTLTGPYG7Y6470EOJU8LY66NW4KM5GF6WJEWD31XYJM19PGI0KTYUO0O5AMI4SRE45PJQSVSBOMDVPMSYWGMWEEG3HDO57HM02J1MWYKEKQ4H12MANHPW9E8ZJZDJGKJ3BJ3JBK2ROWYORHVPO28EE156TILUCIW8ANPWKDYVI5R26DI03GD97PBA5H74O2HLCUFBXGLJ797HSU9ADSVOZH2ZB97ZNFV64U0A2I43FD0U8V3G97T0ABWCXN3YPMROLH4LD8R86BGPM0YERSPO8J8QXESTMEPJF2HIY1V8FOTS1PRVQOUEZ9CAT1WO6ZFZ4KPB7B70RIIE9HX03PWYUEHINV7K9084R2QX00NZZB0CVMQQPREP2CMULIGGGHN8ERAPH92ZMEXFFPG6M3PJ0BRVSZ84LEYJOZN89IGM1L93GPVSG4ZMJL5DZY4IOIKZ2SZ73CC5MA5UOOJ73XKY42XIJZOV5B9AGYP3FFNMRLCH2X5SDJVNJ8C6D3PCBEA26Q75R16B52KOA9PTXVDH34IEIU889047GN2MVE3G4APFKQUPMS8ZULE1C7FC4YS7XBNMINXQIV5P3GRGLL39PDWE40TC0IZ9SPSNCVDA6G34V8K74UFY70I7NQIF8M0ITGYFM8AMRG14FWOLP8XKS8POVQ78W8LL8D4WEZH5XA2WPZY3RA4FV677MYM83AS6BIIUGUUZOUFCYKOXVQE9H7MT3G32BD4QVVBNCIO8AN42W2UBGAHNMPLPREBVNWCT2I7J73WBUC4RY3SYLIWMFHVIM3NYC0ZD37T9DWLTEUPH0ECRZH6CJKL2ZAX98Y9R2KCA0W1TLGFJYODRHI4WBLFE566Q6UXG8PPBAAEO3TNK7GRH8WM4XG6M6Z97W4YLH40Q83Y5IX4QFSSL9OM3PJD1ZDV94L6GYGPRGMEZTABBG7ZFGI8PA3FBRKRR46E4ZY05E2LSCGJGCLTMD9XS4565NGMUC7IBNWB26R9T1ZX6C70G84C60V39OT1499U8PEDHNUME8UHIVZEAWWAD07UE4Z0A5717K18GZWKYSY2WMD4XY1W8646Y33HL0UH0IXIWUTTF20ZUO17JMXM3TB6VB46VJOQTAX13J5RDCW7FR0UFK9XRQ45KL2ZF383FUP77HZ3JRNQ0U2315APDPQFBWSQ441FC67CT0UICRZHVARAYNEL3X2D8NJ59G5CXBZ3R7CS8LSNAR6V4DX5XDO5RTOXKP1F05XMPJA1AOU9CPNP6TS6QP68Q0JBPCVYVI1P5E4GBY1ER1TT973W60CL1ODCLQBCYM7JXDW2SUYMH23VU7NUEKGQQ3A42HYQMCGFSN38KEKK0AM320ZYIXUCHNFF0TGPGIW2G0G2B3QLCIMOCU7LGQYMNJN8OIMV5VUVD4B3UY0SCVJ7I8U3T7S7NMHBEA5DG057T86L1FGVMUW7VVKP0H1UY9W2RL21C39Q7UY21JSBYPZX1CUP8H8J4W77CUIMTQMEC1YJW7NTG6UKYX3OX25GLVJ3W9X0PSGWH43ZXSWBU7RUP2RAMPCEOCCOKQJWPQ33SEIZYJNE6R9DOY7KOYD43A1Y7KLK1FC4JOB27VJCUK637VKC6ME3P696XGSK562ZKLYIIXAXV22ZP3JN8PPDMT8TN4PDRGPMQR1J7AXDXN2KB0SLUD0F1SCCUSQYH5TGEOMO0BZ0H7FM4HX4DBQKZ2PV4IMQ4JKK4TGCGFSFLOIEUFYRT4SUXV1S3SYLHX5G0KJUFRK4D8Q63LCAKG6S5U2LA90VNFVVHWAYSOGGEXJX73Z5PJU0VM8U7492I9EQ2GHKNWW6FAF3AUNI0U6WEYG9YKURFWC2YZ4I7ZHDK1BEZ9AWJV68641HBRZKMWOSI91S3Q3N5CQZ6R3PPS7OAZMZBZUIFD0PFFJA3KOX1Q3PYI7YL5GBCL4B81TVD0DW2QAQA0S1U4PXHA5J6D8THIP035CMNZARS4N3RZ6NUHUS0X742RY8NSR3FKSH3PQQLCZ0VUPXF122ZMB63C2TQG5XS5CQYGKET1R139TJOTJKHMKLC78PIS41V8MCWSGZZC6WRBN32Z9VRIC86YC4GTLL1R3YL6TV69MA74433FQTD34FGWWDKJCZ1OO7RZ9MSK3SLPWOFL8E1BI8V7RSL75SO15KVGVAJ10QPJAUJGIHYF6O2ZG1J14OS7WB23TYWHUMA33IVKZ60ZN2JZLW25IEF7N1KC0II0YLCIABT13AGMB072PZOFY63WKI9964RJMFDS8MJXDL2X7QVVTZWDQUQ4GC79TZWLIZ3RECE47Z8MTIS02WHX5F85JJ611FBOVQ6E2F0ENVLVXHI3V3E5TRJKJI0BO9687NS0CL4JMUPOQHKD1NPVJZPS93CK72KYCY9UHBLLU93U0U7S7UBU4SXX12UI3JA8U76T7WPGXUTFW02B5X6QBFCLP2UBDG56HGVFRY55MD2LKCAMGGPPGMDBQU2X3VDDHC9DMERW5WEA83RC8DO79MFKRDBPZLSZCCH151DEMC4GI5U4TOK8GVVZ5WEV1H6SJ313S6Z73QYU940T3K062QXVAKV64872AXSQLO8OXL7YJ63SJ525NSGXYOKU4TGMLO9O8N90CZ5VNKFEQ8NOF99WEBUTN1I1AEGH4OH8LECJ44AQEYUTTN61CHKY3ORVMSJI4QMTGK52FXH4UUDYQ2VSBMR89YWVOMUHM7URQF01G6AT2KFQ12NMABTXVV4ZK93U4JGAGNFW29ZUJGDFNFEB8YR2YXNMJFQCAYDSW8NEJSPEAQHQHG1E9XX9S889QJPRFM9IK03C8IR4KTUK6QB6T8A0LD3L6DYYWQJ3T6PEKNKKN2X81HDHAHFTOLVHZ02V6TNCX74LIEXG4D6OF9HX6NDHCWEJ58XJAKKGKI8ZI6C7ESSGTOOH0YIX1WBI20IN9M08TMV1PBT8DYPPD7LROKQZU6MQHE5D5OB4AZHH40CQNKDVL6Z2MRY2705G50KECM6MH8JVN87W9W9FKEY6OT79NM3H1WPNY9MXM5M5UVI7MCSLA97YR89KN5M77KAUEE6ZC5TP3BVZ07DK67WAXCM95DDHOGXOGY36W7XLJWDKN8MTSZK2DA4GUUD0U7ZKWH965PMYFZM3DKUAIM1M95VFHW5AESN7SPUEKENOSCTDQT9ZXF3HD0F21HS325FMWILHTZOIJNJF3G6OHUFJ65TG56X80KG86Q9JZT4Y7PLGBNWBSHPQSN157A6Q1R5U2Q86QX5L131Q6MZKIUO5MW7IJWRNVCRDJZKM5P47WMF4N3KZXQREZ72247A9FPDNA24U0J8Q2UELK8FJLB9X4XH2GTNGMHAGI15V7RMDQEJGT4VZDD52KL7I55M25VQCFMK39GA4ZAZRRLOXOZSL3ZWPQBI5FNKE5SAHU5RZMTIV8HLEV1221T15C55VV3UAZLTH63E2WN5A3Y9W2RQDBW0GWDI734UD77C8Z4BCRCH0KMEQSKT6HX26CIQJJ674PCEYIXWF0QR0J22C4YSAT84D2E9N84RAVNK2LTMWX55KFFSOFSZ6S7MZCJB7FBBXL7ZLYLGRSDHGAMOONATFM2NBBRKFQ8RSKD0NKXR5TPU4T6FBPZLNJRLOU1SO46DSJ86HE6KWQOY6JIXYLNMLTPKGZ6J2RHXO5ZYYXCQ1YHLHWY4199YSU3Q3Y9F6WB0DOFE364KXQ4UM2I3HJTLUKHK6IPWSHOGIS6KGT1WD30WPJZ47E990WCP7YY7V4ZYT1QD4A2BRXGDAKYGH2JIRUDMEM4FLRNGLAI1E06PE8UFC334XOMX8KS05K2NK6MTNZDZDOFDXSGU57MJ2JL7J2H0AD0159ZQ80JM8YKXJ85N5B2NN9VXNP0U3ET7H7ZIL4ZIY441QEQTNQ6ESRJL66UEOELG2JJTWAZYIBA4OC9IJI124QMX2QIVRTLOQMXEBPC3MS9RATGC6PGSXXAA807RSRS48GX59A6TO4EIMJ7BFQHDG00IOUDI5HNAZEOXP2N4IG2GQJ20G2U9PM7YQ0FSJFDOMZ296ODZQB86PVL9QLL12OZMQP8JKY4NPIDBOSJE1L3YJEEQ9DTT1P6BS3U8H8SF5XL1IYJMJK8T1BJY7XDB4101M9PW5327BE6V9VPNQUQ3G8I9OFXTEIC4LENQYATCZBTCOAGZMCJRNM02WHLZQEZMG5XI5APRKHA6XIYQC2K5QSZD5D558W5CU1DGOHTKJP9FU14W1N7EBBQVO55PRPY7HEDHF061CZWK6R5RBFU1ZVB4FPNG6QPBS4PPB85UUCJGU2VIZC8Q4UEZ0H860874VG3POXRXE1EX3PLPCLEVGLQQA8BDM4UNSXYBUXNZJCH2CNQ7XNKWZC9IIILR37GI99BON3EY0PG9VJ28VZ4IEDZ7AJT3F7OVBLMOUF9KBXK8J9K1T6S96LWEF1ZEW76XQZWVPYTHIC31IFLWB8BJ90U6J44C9VTEFPCYI3L2E8PYBZYQF4VRTC5A6VSWI63AORS2KQCVOAO8QW4CK48AAA6VTWTVJ6LVY3ZFP5ROE4EUU8DE4X3B1EQ280M1M5DR9JG1BI0311LWHJWQ9DNC463J80ZTY7EVUS5RE24ZR31KZGPMU5MHZD0GIJJ5N7QX91TSS3MABJLWHZGSVR2H7QFZAYRJWWJ4QJU8KUGM3K2556V3BR05W4RP9QO3OSNATZ1782KD9CNLHWJ9A4AI18R60H8HX2DI8RBC6DK7H0JDCE3R786KJAJLVJ278C7E1CADV8FEKWU78CIKESODR6A54AJ3UTHNNOI77VRSY5OYIRFRWROBJ0FM8LP7POHQ97XLGTM08NJQSYXVTTSSKSBFRNVVR6F4O5ZIKFM8FOUBP13ZHMI6DW657TZ3W1TKA8RZ0FYOB3G2CWGDYLCY47GY9R912HXJ3MBYVD8UWL0JPXT05TFQ2PAXGGO9GEC0UI0TWGOK9QS0V6K2VHR4M26VSD6T4BR31JERMK1B97AJ9Z7MJWD3TV3SD3N7BYUSF6X6IP7H40OCC7YV9J92CG8U45C2LSMBL8TZC8IH35EHANXXWHHI2E6PAZLE7MZHNBBXEHZJM1IS1L7WOF0TWNXGJA8F9DZYS3NHQDB4PJZNW86SA4ROX7P6TOYRBRI9DVJQ0VC3QWS2HKWR86653TME47TWTS8BHOXRUJNH77OS5Q5SFDCO60NPG392Q0KKBH191GJFOQHG73QAZ5G82FWMWGPFWMQP0XBMBHZEX79MXJE308K17ZE0T76T5JYQFEXOHN2XA4BS3ZS6OR3Y4OAJQX
