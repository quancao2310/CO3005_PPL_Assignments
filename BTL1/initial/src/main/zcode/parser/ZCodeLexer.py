# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


# Cao Minh Quan - 2112109
from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u017a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3%\3")
        buf.write("%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\5,\u0119")
        buf.write("\n,\3,\5,\u011c\n,\3-\6-\u011f\n-\r-\16-\u0120\3.\3.\7")
        buf.write(".\u0125\n.\f.\16.\u0128\13.\3/\3/\5/\u012c\n/\3/\6/\u012f")
        buf.write("\n/\r/\16/\u0130\3\60\3\60\7\60\u0135\n\60\f\60\16\60")
        buf.write("\u0138\13\60\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3")
        buf.write("\62\3\63\3\63\3\63\3\63\5\63\u0147\n\63\3\64\3\64\3\64")
        buf.write("\3\64\7\64\u014d\n\64\f\64\16\64\u0150\13\64\3\64\3\64")
        buf.write("\3\65\3\65\7\65\u0156\n\65\f\65\16\65\u0159\13\65\3\66")
        buf.write("\6\66\u015c\n\66\r\66\16\66\u015d\3\66\3\66\3\67\3\67")
        buf.write("\7\67\u0164\n\67\f\67\16\67\u0167\13\67\3\67\5\67\u016a")
        buf.write("\n\67\3\67\3\67\38\38\78\u0170\n8\f8\168\u0173\138\38")
        buf.write("\38\38\39\39\39\2\2:\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y\2[\2]\2_.a\2c\2e\2g/i")
        buf.write("\60k\61m\62o\63q\64\3\2\f\3\2\62;\4\2GGgg\4\2--//\t\2")
        buf.write("))^^ddhhppttvv\6\2\f\f\17\17$$^^\4\2\f\f\17\17\5\2C\\")
        buf.write("aac|\6\2\62;C\\aac|\5\2\n\13\16\17\"\"\4\3\f\f\17\17\2")
        buf.write("\u0181\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2_\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\3s\3\2\2\2\5x\3\2\2\2\7~\3\2\2\2\t\u0085\3\2\2\2\13\u008a")
        buf.write("\3\2\2\2\r\u0091\3\2\2\2\17\u0098\3\2\2\2\21\u009c\3\2")
        buf.write("\2\2\23\u00a4\3\2\2\2\25\u00a9\3\2\2\2\27\u00ad\3\2\2")
        buf.write("\2\31\u00b3\3\2\2\2\33\u00b6\3\2\2\2\35\u00bc\3\2\2\2")
        buf.write("\37\u00c5\3\2\2\2!\u00c8\3\2\2\2#\u00cd\3\2\2\2%\u00d2")
        buf.write("\3\2\2\2\'\u00d8\3\2\2\2)\u00dc\3\2\2\2+\u00df\3\2\2\2")
        buf.write("-\u00e1\3\2\2\2/\u00e3\3\2\2\2\61\u00e5\3\2\2\2\63\u00e7")
        buf.write("\3\2\2\2\65\u00e9\3\2\2\2\67\u00ed\3\2\2\29\u00f1\3\2")
        buf.write("\2\2;\u00f4\3\2\2\2=\u00f6\3\2\2\2?\u00f9\3\2\2\2A\u00fb")
        buf.write("\3\2\2\2C\u00fe\3\2\2\2E\u0100\3\2\2\2G\u0103\3\2\2\2")
        buf.write("I\u0107\3\2\2\2K\u010a\3\2\2\2M\u010c\3\2\2\2O\u010e\3")
        buf.write("\2\2\2Q\u0110\3\2\2\2S\u0112\3\2\2\2U\u0114\3\2\2\2W\u0116")
        buf.write("\3\2\2\2Y\u011e\3\2\2\2[\u0122\3\2\2\2]\u0129\3\2\2\2")
        buf.write("_\u0132\3\2\2\2a\u013c\3\2\2\2c\u013f\3\2\2\2e\u0146\3")
        buf.write("\2\2\2g\u0148\3\2\2\2i\u0153\3\2\2\2k\u015b\3\2\2\2m\u0161")
        buf.write("\3\2\2\2o\u016d\3\2\2\2q\u0177\3\2\2\2st\7v\2\2tu\7t\2")
        buf.write("\2uv\7w\2\2vw\7g\2\2w\4\3\2\2\2xy\7h\2\2yz\7c\2\2z{\7")
        buf.write("n\2\2{|\7u\2\2|}\7g\2\2}\6\3\2\2\2~\177\7p\2\2\177\u0080")
        buf.write("\7w\2\2\u0080\u0081\7o\2\2\u0081\u0082\7d\2\2\u0082\u0083")
        buf.write("\7g\2\2\u0083\u0084\7t\2\2\u0084\b\3\2\2\2\u0085\u0086")
        buf.write("\7d\2\2\u0086\u0087\7q\2\2\u0087\u0088\7q\2\2\u0088\u0089")
        buf.write("\7n\2\2\u0089\n\3\2\2\2\u008a\u008b\7u\2\2\u008b\u008c")
        buf.write("\7v\2\2\u008c\u008d\7t\2\2\u008d\u008e\7k\2\2\u008e\u008f")
        buf.write("\7p\2\2\u008f\u0090\7i\2\2\u0090\f\3\2\2\2\u0091\u0092")
        buf.write("\7t\2\2\u0092\u0093\7g\2\2\u0093\u0094\7v\2\2\u0094\u0095")
        buf.write("\7w\2\2\u0095\u0096\7t\2\2\u0096\u0097\7p\2\2\u0097\16")
        buf.write("\3\2\2\2\u0098\u0099\7x\2\2\u0099\u009a\7c\2\2\u009a\u009b")
        buf.write("\7t\2\2\u009b\20\3\2\2\2\u009c\u009d\7f\2\2\u009d\u009e")
        buf.write("\7{\2\2\u009e\u009f\7p\2\2\u009f\u00a0\7c\2\2\u00a0\u00a1")
        buf.write("\7o\2\2\u00a1\u00a2\7k\2\2\u00a2\u00a3\7e\2\2\u00a3\22")
        buf.write("\3\2\2\2\u00a4\u00a5\7h\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7")
        buf.write("\7p\2\2\u00a7\u00a8\7e\2\2\u00a8\24\3\2\2\2\u00a9\u00aa")
        buf.write("\7h\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac\7t\2\2\u00ac\26")
        buf.write("\3\2\2\2\u00ad\u00ae\7w\2\2\u00ae\u00af\7p\2\2\u00af\u00b0")
        buf.write("\7v\2\2\u00b0\u00b1\7k\2\2\u00b1\u00b2\7n\2\2\u00b2\30")
        buf.write("\3\2\2\2\u00b3\u00b4\7d\2\2\u00b4\u00b5\7{\2\2\u00b5\32")
        buf.write("\3\2\2\2\u00b6\u00b7\7d\2\2\u00b7\u00b8\7t\2\2\u00b8\u00b9")
        buf.write("\7g\2\2\u00b9\u00ba\7c\2\2\u00ba\u00bb\7m\2\2\u00bb\34")
        buf.write("\3\2\2\2\u00bc\u00bd\7e\2\2\u00bd\u00be\7q\2\2\u00be\u00bf")
        buf.write("\7p\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2")
        buf.write("\7p\2\2\u00c2\u00c3\7w\2\2\u00c3\u00c4\7g\2\2\u00c4\36")
        buf.write("\3\2\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7\7h\2\2\u00c7 ")
        buf.write("\3\2\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca\7n\2\2\u00ca\u00cb")
        buf.write("\7u\2\2\u00cb\u00cc\7g\2\2\u00cc\"\3\2\2\2\u00cd\u00ce")
        buf.write("\7g\2\2\u00ce\u00cf\7n\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1")
        buf.write("\7h\2\2\u00d1$\3\2\2\2\u00d2\u00d3\7d\2\2\u00d3\u00d4")
        buf.write("\7g\2\2\u00d4\u00d5\7i\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7")
        buf.write("\7p\2\2\u00d7&\3\2\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da")
        buf.write("\7p\2\2\u00da\u00db\7f\2\2\u00db(\3\2\2\2\u00dc\u00dd")
        buf.write("\7>\2\2\u00dd\u00de\7/\2\2\u00de*\3\2\2\2\u00df\u00e0")
        buf.write("\7-\2\2\u00e0,\3\2\2\2\u00e1\u00e2\7/\2\2\u00e2.\3\2\2")
        buf.write("\2\u00e3\u00e4\7,\2\2\u00e4\60\3\2\2\2\u00e5\u00e6\7\61")
        buf.write("\2\2\u00e6\62\3\2\2\2\u00e7\u00e8\7\'\2\2\u00e8\64\3\2")
        buf.write("\2\2\u00e9\u00ea\7p\2\2\u00ea\u00eb\7q\2\2\u00eb\u00ec")
        buf.write("\7v\2\2\u00ec\66\3\2\2\2\u00ed\u00ee\7c\2\2\u00ee\u00ef")
        buf.write("\7p\2\2\u00ef\u00f0\7f\2\2\u00f08\3\2\2\2\u00f1\u00f2")
        buf.write("\7q\2\2\u00f2\u00f3\7t\2\2\u00f3:\3\2\2\2\u00f4\u00f5")
        buf.write("\7?\2\2\u00f5<\3\2\2\2\u00f6\u00f7\7#\2\2\u00f7\u00f8")
        buf.write("\7?\2\2\u00f8>\3\2\2\2\u00f9\u00fa\7>\2\2\u00fa@\3\2\2")
        buf.write("\2\u00fb\u00fc\7>\2\2\u00fc\u00fd\7?\2\2\u00fdB\3\2\2")
        buf.write("\2\u00fe\u00ff\7@\2\2\u00ffD\3\2\2\2\u0100\u0101\7@\2")
        buf.write("\2\u0101\u0102\7?\2\2\u0102F\3\2\2\2\u0103\u0104\7\60")
        buf.write("\2\2\u0104\u0105\7\60\2\2\u0105\u0106\7\60\2\2\u0106H")
        buf.write("\3\2\2\2\u0107\u0108\7?\2\2\u0108\u0109\7?\2\2\u0109J")
        buf.write("\3\2\2\2\u010a\u010b\7*\2\2\u010bL\3\2\2\2\u010c\u010d")
        buf.write("\7+\2\2\u010dN\3\2\2\2\u010e\u010f\7]\2\2\u010fP\3\2\2")
        buf.write("\2\u0110\u0111\7_\2\2\u0111R\3\2\2\2\u0112\u0113\7.\2")
        buf.write("\2\u0113T\3\2\2\2\u0114\u0115\7\f\2\2\u0115V\3\2\2\2\u0116")
        buf.write("\u0118\5Y-\2\u0117\u0119\5[.\2\u0118\u0117\3\2\2\2\u0118")
        buf.write("\u0119\3\2\2\2\u0119\u011b\3\2\2\2\u011a\u011c\5]/\2\u011b")
        buf.write("\u011a\3\2\2\2\u011b\u011c\3\2\2\2\u011cX\3\2\2\2\u011d")
        buf.write("\u011f\t\2\2\2\u011e\u011d\3\2\2\2\u011f\u0120\3\2\2\2")
        buf.write("\u0120\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121Z\3\2\2")
        buf.write("\2\u0122\u0126\7\60\2\2\u0123\u0125\t\2\2\2\u0124\u0123")
        buf.write("\3\2\2\2\u0125\u0128\3\2\2\2\u0126\u0124\3\2\2\2\u0126")
        buf.write("\u0127\3\2\2\2\u0127\\\3\2\2\2\u0128\u0126\3\2\2\2\u0129")
        buf.write("\u012b\t\3\2\2\u012a\u012c\t\4\2\2\u012b\u012a\3\2\2\2")
        buf.write("\u012b\u012c\3\2\2\2\u012c\u012e\3\2\2\2\u012d\u012f\t")
        buf.write("\2\2\2\u012e\u012d\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u012e")
        buf.write("\3\2\2\2\u0130\u0131\3\2\2\2\u0131^\3\2\2\2\u0132\u0136")
        buf.write("\7$\2\2\u0133\u0135\5e\63\2\u0134\u0133\3\2\2\2\u0135")
        buf.write("\u0138\3\2\2\2\u0136\u0134\3\2\2\2\u0136\u0137\3\2\2\2")
        buf.write("\u0137\u0139\3\2\2\2\u0138\u0136\3\2\2\2\u0139\u013a\7")
        buf.write("$\2\2\u013a\u013b\b\60\2\2\u013b`\3\2\2\2\u013c\u013d")
        buf.write("\7^\2\2\u013d\u013e\t\5\2\2\u013eb\3\2\2\2\u013f\u0140")
        buf.write("\7^\2\2\u0140\u0141\n\5\2\2\u0141d\3\2\2\2\u0142\u0147")
        buf.write("\5a\61\2\u0143\u0144\7)\2\2\u0144\u0147\7$\2\2\u0145\u0147")
        buf.write("\n\6\2\2\u0146\u0142\3\2\2\2\u0146\u0143\3\2\2\2\u0146")
        buf.write("\u0145\3\2\2\2\u0147f\3\2\2\2\u0148\u0149\7%\2\2\u0149")
        buf.write("\u014a\7%\2\2\u014a\u014e\3\2\2\2\u014b\u014d\n\7\2\2")
        buf.write("\u014c\u014b\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c\3")
        buf.write("\2\2\2\u014e\u014f\3\2\2\2\u014f\u0151\3\2\2\2\u0150\u014e")
        buf.write("\3\2\2\2\u0151\u0152\b\64\3\2\u0152h\3\2\2\2\u0153\u0157")
        buf.write("\t\b\2\2\u0154\u0156\t\t\2\2\u0155\u0154\3\2\2\2\u0156")
        buf.write("\u0159\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158\3\2\2\2")
        buf.write("\u0158j\3\2\2\2\u0159\u0157\3\2\2\2\u015a\u015c\t\n\2")
        buf.write("\2\u015b\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015b")
        buf.write("\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015f\3\2\2\2\u015f")
        buf.write("\u0160\b\66\3\2\u0160l\3\2\2\2\u0161\u0165\7$\2\2\u0162")
        buf.write("\u0164\5e\63\2\u0163\u0162\3\2\2\2\u0164\u0167\3\2\2\2")
        buf.write("\u0165\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0169\3")
        buf.write("\2\2\2\u0167\u0165\3\2\2\2\u0168\u016a\t\13\2\2\u0169")
        buf.write("\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016c\b\67\4")
        buf.write("\2\u016cn\3\2\2\2\u016d\u0171\7$\2\2\u016e\u0170\5e\63")
        buf.write("\2\u016f\u016e\3\2\2\2\u0170\u0173\3\2\2\2\u0171\u016f")
        buf.write("\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0174\3\2\2\2\u0173")
        buf.write("\u0171\3\2\2\2\u0174\u0175\5c\62\2\u0175\u0176\b8\5\2")
        buf.write("\u0176p\3\2\2\2\u0177\u0178\13\2\2\2\u0178\u0179\b9\6")
        buf.write("\2\u0179r\3\2\2\2\21\2\u0118\u011b\u0120\u0126\u012b\u0130")
        buf.write("\u0136\u0146\u014e\u0157\u015d\u0165\u0169\u0171\7\3\60")
        buf.write("\2\b\2\2\3\67\3\38\4\39\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    NUMBER = 3
    BOOL = 4
    STRING = 5
    RETURN = 6
    VAR = 7
    DYNAMIC = 8
    FUNC = 9
    FOR = 10
    UNTIL = 11
    BY = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    ASSIGN = 20
    ADD = 21
    SUB = 22
    MUL = 23
    DIV = 24
    MOD = 25
    NOT = 26
    AND = 27
    OR = 28
    EQ = 29
    NEQ = 30
    LT = 31
    LTE = 32
    GT = 33
    GTE = 34
    CONCAT = 35
    STRING_EQ = 36
    LEFT_PAREN = 37
    RIGHT_PAREN = 38
    LEFT_SQUARE_BRACKET = 39
    RIGHT_SQUARE_BRACKET = 40
    COMMA = 41
    NEWLINE = 42
    NUMBER_LIT = 43
    STRING_LIT = 44
    COMMENT = 45
    IDENTIFIER = 46
    WS = 47
    UNCLOSE_STRING = 48
    ILLEGAL_ESCAPE = 49
    ERROR_CHAR = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'<-'", "'+'", "'-'", "'*'", "'/'", "'%'", "'not'", 
            "'and'", "'or'", "'='", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'...'", "'=='", "'('", "')'", "'['", "']'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "ASSIGN", "ADD", "SUB", 
            "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQ", "NEQ", "LT", 
            "LTE", "GT", "GTE", "CONCAT", "STRING_EQ", "LEFT_PAREN", "RIGHT_PAREN", 
            "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", "COMMA", "NEWLINE", 
            "NUMBER_LIT", "STRING_LIT", "COMMENT", "IDENTIFIER", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "ASSIGN", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                  "EQ", "NEQ", "LT", "LTE", "GT", "GTE", "CONCAT", "STRING_EQ", 
                  "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
                  "COMMA", "NEWLINE", "NUMBER_LIT", "INT", "DEC", "EXP", 
                  "STRING_LIT", "ESC_CHAR", "INVALID_ESC_CHAR", "VALID_CHAR", 
                  "COMMENT", "IDENTIFIER", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[46] = self.STRING_LIT_action 
            actions[53] = self.UNCLOSE_STRING_action 
            actions[54] = self.ILLEGAL_ESCAPE_action 
            actions[55] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            if self.text[-1] in ['\r', '\n']:
                raise UncloseString(self.text[1:-1])
            else:
                raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            raise ErrorToken(self.text)

     


