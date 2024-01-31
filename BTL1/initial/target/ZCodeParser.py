# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write("\u01a8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\5\3z\n\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4")
        buf.write("\u0082\n\4\3\5\3\5\3\5\3\5\5\5\u0088\n\5\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\5\t")
        buf.write("\u009a\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\5\16\u00b1")
        buf.write("\n\16\3\17\3\17\3\17\3\17\3\17\5\17\u00b8\n\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\5\20\u00c1\n\20\3\21\3\21")
        buf.write("\3\21\3\21\5\21\u00c7\n\21\3\22\3\22\5\22\u00cb\n\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\5\23\u00da\n\23\3\24\3\24\3\24\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\26\3\26\3\26\5\26\u00e7\n\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\5\31\u00fd\n\31\3")
        buf.write("\32\3\32\3\32\5\32\u0102\n\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\5\37\u0118\n\37\3 \3 \3 \3!\3!\3")
        buf.write("!\3!\3!\3\"\3\"\3\"\3\"\3\"\5\"\u0127\n\"\3#\3#\3#\3#")
        buf.write("\3#\5#\u012e\n#\3$\3$\3$\3$\3$\3$\7$\u0136\n$\f$\16$\u0139")
        buf.write("\13$\3%\3%\3%\3%\3%\3%\7%\u0141\n%\f%\16%\u0144\13%\3")
        buf.write("&\3&\3&\3&\3&\3&\7&\u014c\n&\f&\16&\u014f\13&\3\'\3\'")
        buf.write("\3\'\5\'\u0154\n\'\3(\3(\3(\5(\u0159\n(\3)\3)\5)\u015d")
        buf.write("\n)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\5*\u0169\n*\3+\3+\3")
        buf.write(",\3,\3,\3,\3-\3-\3.\3.\3.\3.\3.\3/\3/\5/\u017a\n/\3\60")
        buf.write("\3\60\3\60\3\61\3\61\5\61\u0181\n\61\3\62\3\62\3\62\3")
        buf.write("\62\3\62\5\62\u0188\n\62\3\63\3\63\3\63\3\63\5\63\u018e")
        buf.write("\n\63\3\64\3\64\3\64\3\64\5\64\u0194\n\64\3\65\3\65\3")
        buf.write("\65\5\65\u0199\n\65\3\66\3\66\3\66\5\66\u019e\n\66\3\67")
        buf.write("\3\67\38\38\39\39\39\39\39\2\5FHJ:\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhjlnp\2\b\3\2\35\36\3\2\27\30\3\2\31\33\3\2")
        buf.write("\3\4\3\2\5\7\4\2\37$&&\2\u019b\2r\3\2\2\2\4y\3\2\2\2\6")
        buf.write("\u0081\3\2\2\2\b\u0087\3\2\2\2\n\u0089\3\2\2\2\f\u008d")
        buf.write("\3\2\2\2\16\u0092\3\2\2\2\20\u0099\3\2\2\2\22\u009b\3")
        buf.write("\2\2\2\24\u00a1\3\2\2\2\26\u00a5\3\2\2\2\30\u00aa\3\2")
        buf.write("\2\2\32\u00b0\3\2\2\2\34\u00b7\3\2\2\2\36\u00c0\3\2\2")
        buf.write("\2 \u00c6\3\2\2\2\"\u00ca\3\2\2\2$\u00d9\3\2\2\2&\u00db")
        buf.write("\3\2\2\2(\u00de\3\2\2\2*\u00e6\3\2\2\2,\u00e8\3\2\2\2")
        buf.write(".\u00f1\3\2\2\2\60\u00fc\3\2\2\2\62\u0101\3\2\2\2\64\u0103")
        buf.write("\3\2\2\2\66\u010c\3\2\2\28\u010f\3\2\2\2:\u0112\3\2\2")
        buf.write("\2<\u0117\3\2\2\2>\u0119\3\2\2\2@\u011c\3\2\2\2B\u0126")
        buf.write("\3\2\2\2D\u012d\3\2\2\2F\u012f\3\2\2\2H\u013a\3\2\2\2")
        buf.write("J\u0145\3\2\2\2L\u0153\3\2\2\2N\u0158\3\2\2\2P\u015c\3")
        buf.write("\2\2\2R\u0168\3\2\2\2T\u016a\3\2\2\2V\u016c\3\2\2\2X\u0170")
        buf.write("\3\2\2\2Z\u0172\3\2\2\2\\\u0179\3\2\2\2^\u017b\3\2\2\2")
        buf.write("`\u0180\3\2\2\2b\u0187\3\2\2\2d\u018d\3\2\2\2f\u0193\3")
        buf.write("\2\2\2h\u0198\3\2\2\2j\u019d\3\2\2\2l\u019f\3\2\2\2n\u01a1")
        buf.write("\3\2\2\2p\u01a3\3\2\2\2rs\5\4\3\2st\7\2\2\3t\3\3\2\2\2")
        buf.write("uv\5\6\4\2vw\5\4\3\2wz\3\2\2\2xz\5\6\4\2yu\3\2\2\2yx\3")
        buf.write("\2\2\2z\5\3\2\2\2{|\5\b\5\2|}\5j\66\2}\u0082\3\2\2\2~")
        buf.write("\177\5\26\f\2\177\u0080\5j\66\2\u0080\u0082\3\2\2\2\u0081")
        buf.write("{\3\2\2\2\u0081~\3\2\2\2\u0082\7\3\2\2\2\u0083\u0088\5")
        buf.write("\n\6\2\u0084\u0088\5\f\7\2\u0085\u0088\5\16\b\2\u0086")
        buf.write("\u0088\5\22\n\2\u0087\u0083\3\2\2\2\u0087\u0084\3\2\2")
        buf.write("\2\u0087\u0085\3\2\2\2\u0087\u0086\3\2\2\2\u0088\t\3\2")
        buf.write("\2\2\u0089\u008a\5l\67\2\u008a\u008b\7\60\2\2\u008b\u008c")
        buf.write("\5\20\t\2\u008c\13\3\2\2\2\u008d\u008e\7\t\2\2\u008e\u008f")
        buf.write("\7\60\2\2\u008f\u0090\7\26\2\2\u0090\u0091\5B\"\2\u0091")
        buf.write("\r\3\2\2\2\u0092\u0093\7\n\2\2\u0093\u0094\7\60\2\2\u0094")
        buf.write("\u0095\5\20\t\2\u0095\17\3\2\2\2\u0096\u0097\7\26\2\2")
        buf.write("\u0097\u009a\5B\"\2\u0098\u009a\3\2\2\2\u0099\u0096\3")
        buf.write("\2\2\2\u0099\u0098\3\2\2\2\u009a\21\3\2\2\2\u009b\u009c")
        buf.write("\5l\67\2\u009c\u009d\7\60\2\2\u009d\u009e\5\24\13\2\u009e")
        buf.write("\u009f\7\26\2\2\u009f\u00a0\5V,\2\u00a0\23\3\2\2\2\u00a1")
        buf.write("\u00a2\7)\2\2\u00a2\u00a3\5d\63\2\u00a3\u00a4\7*\2\2\u00a4")
        buf.write("\25\3\2\2\2\u00a5\u00a6\7\13\2\2\u00a6\u00a7\7\60\2\2")
        buf.write("\u00a7\u00a8\5\30\r\2\u00a8\u00a9\5 \21\2\u00a9\27\3\2")
        buf.write("\2\2\u00aa\u00ab\7\'\2\2\u00ab\u00ac\5\32\16\2\u00ac\u00ad")
        buf.write("\7(\2\2\u00ad\31\3\2\2\2\u00ae\u00b1\5\34\17\2\u00af\u00b1")
        buf.write("\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00af\3\2\2\2\u00b1")
        buf.write("\33\3\2\2\2\u00b2\u00b3\5\36\20\2\u00b3\u00b4\7+\2\2\u00b4")
        buf.write("\u00b5\5\34\17\2\u00b5\u00b8\3\2\2\2\u00b6\u00b8\5\36")
        buf.write("\20\2\u00b7\u00b2\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\35")
        buf.write("\3\2\2\2\u00b9\u00ba\5l\67\2\u00ba\u00bb\7\60\2\2\u00bb")
        buf.write("\u00c1\3\2\2\2\u00bc\u00bd\5l\67\2\u00bd\u00be\7\60\2")
        buf.write("\2\u00be\u00bf\5\24\13\2\u00bf\u00c1\3\2\2\2\u00c0\u00b9")
        buf.write("\3\2\2\2\u00c0\u00bc\3\2\2\2\u00c1\37\3\2\2\2\u00c2\u00c3")
        buf.write("\5h\65\2\u00c3\u00c4\5\"\22\2\u00c4\u00c7\3\2\2\2\u00c5")
        buf.write("\u00c7\3\2\2\2\u00c6\u00c2\3\2\2\2\u00c6\u00c5\3\2\2\2")
        buf.write("\u00c7!\3\2\2\2\u00c8\u00cb\5:\36\2\u00c9\u00cb\5@!\2")
        buf.write("\u00ca\u00c8\3\2\2\2\u00ca\u00c9\3\2\2\2\u00cb#\3\2\2")
        buf.write("\2\u00cc\u00da\5&\24\2\u00cd\u00da\5(\25\2\u00ce\u00da")
        buf.write("\5,\27\2\u00cf\u00da\5\64\33\2\u00d0\u00da\5\66\34\2\u00d1")
        buf.write("\u00da\58\35\2\u00d2\u00d3\5:\36\2\u00d3\u00d4\5j\66\2")
        buf.write("\u00d4\u00da\3\2\2\2\u00d5\u00da\5> \2\u00d6\u00d7\5@")
        buf.write("!\2\u00d7\u00d8\5j\66\2\u00d8\u00da\3\2\2\2\u00d9\u00cc")
        buf.write("\3\2\2\2\u00d9\u00cd\3\2\2\2\u00d9\u00ce\3\2\2\2\u00d9")
        buf.write("\u00cf\3\2\2\2\u00d9\u00d0\3\2\2\2\u00d9\u00d1\3\2\2\2")
        buf.write("\u00d9\u00d2\3\2\2\2\u00d9\u00d5\3\2\2\2\u00d9\u00d6\3")
        buf.write("\2\2\2\u00da%\3\2\2\2\u00db\u00dc\5\b\5\2\u00dc\u00dd")
        buf.write("\5j\66\2\u00dd\'\3\2\2\2\u00de\u00df\5*\26\2\u00df\u00e0")
        buf.write("\7\26\2\2\u00e0\u00e1\5B\"\2\u00e1\u00e2\5j\66\2\u00e2")
        buf.write(")\3\2\2\2\u00e3\u00e7\7\60\2\2\u00e4\u00e5\7\60\2\2\u00e5")
        buf.write("\u00e7\5p9\2\u00e6\u00e3\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e7")
        buf.write("+\3\2\2\2\u00e8\u00e9\7\21\2\2\u00e9\u00ea\7\'\2\2\u00ea")
        buf.write("\u00eb\5B\"\2\u00eb\u00ec\7(\2\2\u00ec\u00ed\5h\65\2\u00ed")
        buf.write("\u00ee\5$\23\2\u00ee\u00ef\5\60\31\2\u00ef\u00f0\5\62")
        buf.write("\32\2\u00f0-\3\2\2\2\u00f1\u00f2\7\23\2\2\u00f2\u00f3")
        buf.write("\7\'\2\2\u00f3\u00f4\5B\"\2\u00f4\u00f5\7(\2\2\u00f5\u00f6")
        buf.write("\5h\65\2\u00f6\u00f7\5$\23\2\u00f7/\3\2\2\2\u00f8\u00f9")
        buf.write("\5.\30\2\u00f9\u00fa\5\60\31\2\u00fa\u00fd\3\2\2\2\u00fb")
        buf.write("\u00fd\3\2\2\2\u00fc\u00f8\3\2\2\2\u00fc\u00fb\3\2\2\2")
        buf.write("\u00fd\61\3\2\2\2\u00fe\u00ff\7\22\2\2\u00ff\u0102\5$")
        buf.write("\23\2\u0100\u0102\3\2\2\2\u0101\u00fe\3\2\2\2\u0101\u0100")
        buf.write("\3\2\2\2\u0102\63\3\2\2\2\u0103\u0104\7\f\2\2\u0104\u0105")
        buf.write("\7\60\2\2\u0105\u0106\7\r\2\2\u0106\u0107\5B\"\2\u0107")
        buf.write("\u0108\7\16\2\2\u0108\u0109\5B\"\2\u0109\u010a\5h\65\2")
        buf.write("\u010a\u010b\5$\23\2\u010b\65\3\2\2\2\u010c\u010d\7\17")
        buf.write("\2\2\u010d\u010e\5j\66\2\u010e\67\3\2\2\2\u010f\u0110")
        buf.write("\7\20\2\2\u0110\u0111\5j\66\2\u01119\3\2\2\2\u0112\u0113")
        buf.write("\7\b\2\2\u0113\u0114\5<\37\2\u0114;\3\2\2\2\u0115\u0118")
        buf.write("\5B\"\2\u0116\u0118\3\2\2\2\u0117\u0115\3\2\2\2\u0117")
        buf.write("\u0116\3\2\2\2\u0118=\3\2\2\2\u0119\u011a\5Z.\2\u011a")
        buf.write("\u011b\5j\66\2\u011b?\3\2\2\2\u011c\u011d\7\24\2\2\u011d")
        buf.write("\u011e\5j\66\2\u011e\u011f\5f\64\2\u011f\u0120\7\25\2")
        buf.write("\2\u0120A\3\2\2\2\u0121\u0122\5D#\2\u0122\u0123\7%\2\2")
        buf.write("\u0123\u0124\5D#\2\u0124\u0127\3\2\2\2\u0125\u0127\5D")
        buf.write("#\2\u0126\u0121\3\2\2\2\u0126\u0125\3\2\2\2\u0127C\3\2")
        buf.write("\2\2\u0128\u0129\5F$\2\u0129\u012a\5n8\2\u012a\u012b\5")
        buf.write("F$\2\u012b\u012e\3\2\2\2\u012c\u012e\5F$\2\u012d\u0128")
        buf.write("\3\2\2\2\u012d\u012c\3\2\2\2\u012eE\3\2\2\2\u012f\u0130")
        buf.write("\b$\1\2\u0130\u0131\5H%\2\u0131\u0137\3\2\2\2\u0132\u0133")
        buf.write("\f\4\2\2\u0133\u0134\t\2\2\2\u0134\u0136\5H%\2\u0135\u0132")
        buf.write("\3\2\2\2\u0136\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0137")
        buf.write("\u0138\3\2\2\2\u0138G\3\2\2\2\u0139\u0137\3\2\2\2\u013a")
        buf.write("\u013b\b%\1\2\u013b\u013c\5J&\2\u013c\u0142\3\2\2\2\u013d")
        buf.write("\u013e\f\4\2\2\u013e\u013f\t\3\2\2\u013f\u0141\5J&\2\u0140")
        buf.write("\u013d\3\2\2\2\u0141\u0144\3\2\2\2\u0142\u0140\3\2\2\2")
        buf.write("\u0142\u0143\3\2\2\2\u0143I\3\2\2\2\u0144\u0142\3\2\2")
        buf.write("\2\u0145\u0146\b&\1\2\u0146\u0147\5L\'\2\u0147\u014d\3")
        buf.write("\2\2\2\u0148\u0149\f\4\2\2\u0149\u014a\t\4\2\2\u014a\u014c")
        buf.write("\5L\'\2\u014b\u0148\3\2\2\2\u014c\u014f\3\2\2\2\u014d")
        buf.write("\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014eK\3\2\2\2\u014f")
        buf.write("\u014d\3\2\2\2\u0150\u0151\7\34\2\2\u0151\u0154\5L\'\2")
        buf.write("\u0152\u0154\5N(\2\u0153\u0150\3\2\2\2\u0153\u0152\3\2")
        buf.write("\2\2\u0154M\3\2\2\2\u0155\u0156\7\30\2\2\u0156\u0159\5")
        buf.write("N(\2\u0157\u0159\5P)\2\u0158\u0155\3\2\2\2\u0158\u0157")
        buf.write("\3\2\2\2\u0159O\3\2\2\2\u015a\u015d\5^\60\2\u015b\u015d")
        buf.write("\5R*\2\u015c\u015a\3\2\2\2\u015c\u015b\3\2\2\2\u015dQ")
        buf.write("\3\2\2\2\u015e\u0169\7-\2\2\u015f\u0169\7.\2\2\u0160\u0169")
        buf.write("\5T+\2\u0161\u0169\5V,\2\u0162\u0169\5Z.\2\u0163\u0169")
        buf.write("\7\60\2\2\u0164\u0165\7\'\2\2\u0165\u0166\5B\"\2\u0166")
        buf.write("\u0167\7(\2\2\u0167\u0169\3\2\2\2\u0168\u015e\3\2\2\2")
        buf.write("\u0168\u015f\3\2\2\2\u0168\u0160\3\2\2\2\u0168\u0161\3")
        buf.write("\2\2\2\u0168\u0162\3\2\2\2\u0168\u0163\3\2\2\2\u0168\u0164")
        buf.write("\3\2\2\2\u0169S\3\2\2\2\u016a\u016b\t\5\2\2\u016bU\3\2")
        buf.write("\2\2\u016c\u016d\7)\2\2\u016d\u016e\5X-\2\u016e\u016f")
        buf.write("\7*\2\2\u016fW\3\2\2\2\u0170\u0171\5b\62\2\u0171Y\3\2")
        buf.write("\2\2\u0172\u0173\7\60\2\2\u0173\u0174\7\'\2\2\u0174\u0175")
        buf.write("\5\\/\2\u0175\u0176\7(\2\2\u0176[\3\2\2\2\u0177\u017a")
        buf.write("\5b\62\2\u0178\u017a\3\2\2\2\u0179\u0177\3\2\2\2\u0179")
        buf.write("\u0178\3\2\2\2\u017a]\3\2\2\2\u017b\u017c\5`\61\2\u017c")
        buf.write("\u017d\5p9\2\u017d_\3\2\2\2\u017e\u0181\7\60\2\2\u017f")
        buf.write("\u0181\5Z.\2\u0180\u017e\3\2\2\2\u0180\u017f\3\2\2\2\u0181")
        buf.write("a\3\2\2\2\u0182\u0183\5B\"\2\u0183\u0184\7+\2\2\u0184")
        buf.write("\u0185\5b\62\2\u0185\u0188\3\2\2\2\u0186\u0188\5B\"\2")
        buf.write("\u0187\u0182\3\2\2\2\u0187\u0186\3\2\2\2\u0188c\3\2\2")
        buf.write("\2\u0189\u018a\7-\2\2\u018a\u018b\7+\2\2\u018b\u018e\5")
        buf.write("d\63\2\u018c\u018e\7-\2\2\u018d\u0189\3\2\2\2\u018d\u018c")
        buf.write("\3\2\2\2\u018ee\3\2\2\2\u018f\u0190\5$\23\2\u0190\u0191")
        buf.write("\5f\64\2\u0191\u0194\3\2\2\2\u0192\u0194\3\2\2\2\u0193")
        buf.write("\u018f\3\2\2\2\u0193\u0192\3\2\2\2\u0194g\3\2\2\2\u0195")
        buf.write("\u0196\7,\2\2\u0196\u0199\5h\65\2\u0197\u0199\3\2\2\2")
        buf.write("\u0198\u0195\3\2\2\2\u0198\u0197\3\2\2\2\u0199i\3\2\2")
        buf.write("\2\u019a\u019b\7,\2\2\u019b\u019e\5j\66\2\u019c\u019e")
        buf.write("\7,\2\2\u019d\u019a\3\2\2\2\u019d\u019c\3\2\2\2\u019e")
        buf.write("k\3\2\2\2\u019f\u01a0\t\6\2\2\u01a0m\3\2\2\2\u01a1\u01a2")
        buf.write("\t\7\2\2\u01a2o\3\2\2\2\u01a3\u01a4\7)\2\2\u01a4\u01a5")
        buf.write("\5b\62\2\u01a5\u01a6\7*\2\2\u01a6q\3\2\2\2 y\u0081\u0087")
        buf.write("\u0099\u00b0\u00b7\u00c0\u00c6\u00ca\u00d9\u00e6\u00fc")
        buf.write("\u0101\u0117\u0126\u012d\u0137\u0142\u014d\u0153\u0158")
        buf.write("\u015c\u0168\u0179\u0180\u0187\u018d\u0193\u0198\u019d")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'<-'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'not'", "'and'", 
                     "'or'", "'='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'...'", "'=='", "'('", "')'", "'['", "']'", "','", 
                     "'\n'" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "ASSIGN", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "NOT", "AND", "OR", "EQ", "NEQ", "LT", "LTE", "GT", 
                      "GTE", "CONCAT", "STRING_EQ", "LEFT_PAREN", "RIGHT_PAREN", 
                      "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", "COMMA", 
                      "NEWLINE", "NUMBER_LIT", "STRING_LIT", "COMMENT", 
                      "IDENTIFIER", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl_list = 1
    RULE_decl = 2
    RULE_variable_decl = 3
    RULE_primitive_decl = 4
    RULE_var_keyword_decl = 5
    RULE_dynamic_keyword_decl = 6
    RULE_optional_init = 7
    RULE_array_decl = 8
    RULE_array_dimensions = 9
    RULE_function_decl = 10
    RULE_param_decl = 11
    RULE_param_list = 12
    RULE_param_list_sub = 13
    RULE_param = 14
    RULE_optional_impl = 15
    RULE_body = 16
    RULE_statement = 17
    RULE_variable_stmt = 18
    RULE_assignment_stmt = 19
    RULE_lhs_asmt = 20
    RULE_if_stmt = 21
    RULE_elif_stmt = 22
    RULE_elif_list = 23
    RULE_else_stmt = 24
    RULE_for_stmt = 25
    RULE_break_stmt = 26
    RULE_continue_stmt = 27
    RULE_return_stmt = 28
    RULE_return_value = 29
    RULE_call_stmt = 30
    RULE_block_stmt = 31
    RULE_expression = 32
    RULE_expr1 = 33
    RULE_expr2 = 34
    RULE_expr3 = 35
    RULE_expr4 = 36
    RULE_expr5 = 37
    RULE_expr6 = 38
    RULE_expr7 = 39
    RULE_operand = 40
    RULE_boolean_lit = 41
    RULE_array_lit = 42
    RULE_array_element_list = 43
    RULE_call_expr = 44
    RULE_argument_list = 45
    RULE_index_expr = 46
    RULE_expr_for_indexing = 47
    RULE_expr_list = 48
    RULE_number_list = 49
    RULE_stmt_list = 50
    RULE_nullable_newline_list = 51
    RULE_nonempty_newline_list = 52
    RULE_primitive_type = 53
    RULE_rel_op = 54
    RULE_index_op = 55

    ruleNames =  [ "program", "decl_list", "decl", "variable_decl", "primitive_decl", 
                   "var_keyword_decl", "dynamic_keyword_decl", "optional_init", 
                   "array_decl", "array_dimensions", "function_decl", "param_decl", 
                   "param_list", "param_list_sub", "param", "optional_impl", 
                   "body", "statement", "variable_stmt", "assignment_stmt", 
                   "lhs_asmt", "if_stmt", "elif_stmt", "elif_list", "else_stmt", 
                   "for_stmt", "break_stmt", "continue_stmt", "return_stmt", 
                   "return_value", "call_stmt", "block_stmt", "expression", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "operand", "boolean_lit", "array_lit", "array_element_list", 
                   "call_expr", "argument_list", "index_expr", "expr_for_indexing", 
                   "expr_list", "number_list", "stmt_list", "nullable_newline_list", 
                   "nonempty_newline_list", "primitive_type", "rel_op", 
                   "index_op" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    NUMBER=3
    BOOL=4
    STRING=5
    RETURN=6
    VAR=7
    DYNAMIC=8
    FUNC=9
    FOR=10
    UNTIL=11
    BY=12
    BREAK=13
    CONTINUE=14
    IF=15
    ELSE=16
    ELIF=17
    BEGIN=18
    END=19
    ASSIGN=20
    ADD=21
    SUB=22
    MUL=23
    DIV=24
    MOD=25
    NOT=26
    AND=27
    OR=28
    EQ=29
    NEQ=30
    LT=31
    LTE=32
    GT=33
    GTE=34
    CONCAT=35
    STRING_EQ=36
    LEFT_PAREN=37
    RIGHT_PAREN=38
    LEFT_SQUARE_BRACKET=39
    RIGHT_SQUARE_BRACKET=40
    COMMA=41
    NEWLINE=42
    NUMBER_LIT=43
    STRING_LIT=44
    COMMENT=45
    IDENTIFIER=46
    WS=47
    UNCLOSE_STRING=48
    ILLEGAL_ESCAPE=49
    ERROR_CHAR=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_listContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.decl_list()
            self.state = 113
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_list" ):
                return visitor.visitDecl_list(self)
            else:
                return visitor.visitChildren(self)




    def decl_list(self):

        localctx = ZCodeParser.Decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl_list)
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.decl()
                self.state = 116
                self.decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_declContext,0)


        def nonempty_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nonempty_newline_listContext,0)


        def function_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Function_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.variable_decl()
                self.state = 122
                self.nonempty_newline_list()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.function_decl()
                self.state = 125
                self.nonempty_newline_list()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Primitive_declContext,0)


        def var_keyword_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Var_keyword_declContext,0)


        def dynamic_keyword_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Dynamic_keyword_declContext,0)


        def array_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Array_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variable_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_decl" ):
                return visitor.visitVariable_decl(self)
            else:
                return visitor.visitChildren(self)




    def variable_decl(self):

        localctx = ZCodeParser.Variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable_decl)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.primitive_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.var_keyword_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
                self.dynamic_keyword_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 132
                self.array_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(ZCodeParser.Primitive_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def optional_init(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_primitive_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_decl" ):
                return visitor.visitPrimitive_decl(self)
            else:
                return visitor.visitChildren(self)




    def primitive_decl(self):

        localctx = ZCodeParser.Primitive_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_primitive_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.primitive_type()
            self.state = 136
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 137
            self.optional_init()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_keyword_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_keyword_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_keyword_decl" ):
                return visitor.visitVar_keyword_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_keyword_decl(self):

        localctx = ZCodeParser.Var_keyword_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_keyword_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(ZCodeParser.VAR)
            self.state = 140
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 141
            self.match(ZCodeParser.ASSIGN)
            self.state = 142
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dynamic_keyword_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def optional_init(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dynamic_keyword_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDynamic_keyword_decl" ):
                return visitor.visitDynamic_keyword_decl(self)
            else:
                return visitor.visitChildren(self)




    def dynamic_keyword_decl(self):

        localctx = ZCodeParser.Dynamic_keyword_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_dynamic_keyword_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(ZCodeParser.DYNAMIC)
            self.state = 145
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 146
            self.optional_init()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_optional_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_init" ):
                return visitor.visitOptional_init(self)
            else:
                return visitor.visitChildren(self)




    def optional_init(self):

        localctx = ZCodeParser.Optional_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_optional_init)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.match(ZCodeParser.ASSIGN)
                self.state = 149
                self.expression()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(ZCodeParser.Primitive_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_dimensions(self):
            return self.getTypedRuleContext(ZCodeParser.Array_dimensionsContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def array_lit(self):
            return self.getTypedRuleContext(ZCodeParser.Array_litContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl" ):
                return visitor.visitArray_decl(self)
            else:
                return visitor.visitChildren(self)




    def array_decl(self):

        localctx = ZCodeParser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.primitive_type()
            self.state = 154
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 155
            self.array_dimensions()
            self.state = 156
            self.match(ZCodeParser.ASSIGN)
            self.state = 157
            self.array_lit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_dimensionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_SQUARE_BRACKET, 0)

        def number_list(self):
            return self.getTypedRuleContext(ZCodeParser.Number_listContext,0)


        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_SQUARE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_dimensions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_dimensions" ):
                return visitor.visitArray_dimensions(self)
            else:
                return visitor.visitChildren(self)




    def array_dimensions(self):

        localctx = ZCodeParser.Array_dimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_dimensions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
            self.state = 160
            self.number_list()
            self.state = 161
            self.match(ZCodeParser.RIGHT_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def param_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Param_declContext,0)


        def optional_impl(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_implContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_decl" ):
                return visitor.visitFunction_decl(self)
            else:
                return visitor.visitChildren(self)




    def function_decl(self):

        localctx = ZCodeParser.Function_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_function_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(ZCodeParser.FUNC)
            self.state = 164
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 165
            self.param_decl()
            self.state = 166
            self.optional_impl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(ZCodeParser.LEFT_PAREN, 0)

        def param_list(self):
            return self.getTypedRuleContext(ZCodeParser.Param_listContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(ZCodeParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_param_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl" ):
                return visitor.visitParam_decl(self)
            else:
                return visitor.visitChildren(self)




    def param_decl(self):

        localctx = ZCodeParser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_param_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(ZCodeParser.LEFT_PAREN)
            self.state = 169
            self.param_list()
            self.state = 170
            self.match(ZCodeParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_list_sub(self):
            return self.getTypedRuleContext(ZCodeParser.Param_list_subContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = ZCodeParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param_list)
        try:
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.param_list_sub()
                pass
            elif token in [ZCodeParser.RIGHT_PAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_list_subContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def param_list_sub(self):
            return self.getTypedRuleContext(ZCodeParser.Param_list_subContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_list_sub

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list_sub" ):
                return visitor.visitParam_list_sub(self)
            else:
                return visitor.visitChildren(self)




    def param_list_sub(self):

        localctx = ZCodeParser.Param_list_subContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_param_list_sub)
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.param()
                self.state = 177
                self.match(ZCodeParser.COMMA)
                self.state = 178
                self.param_list_sub()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(ZCodeParser.Primitive_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_dimensions(self):
            return self.getTypedRuleContext(ZCodeParser.Array_dimensionsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_param)
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.primitive_type()
                self.state = 184
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.primitive_type()
                self.state = 187
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 188
                self.array_dimensions()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_implContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def body(self):
            return self.getTypedRuleContext(ZCodeParser.BodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_optional_impl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_impl" ):
                return visitor.visitOptional_impl(self)
            else:
                return visitor.visitChildren(self)




    def optional_impl(self):

        localctx = ZCodeParser.Optional_implContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_optional_impl)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.nullable_newline_list()
                self.state = 193
                self.body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = ZCodeParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_body)
        try:
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.return_stmt()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.block_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_stmtContext,0)


        def assignment_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Assignment_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def nonempty_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nonempty_newline_listContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Call_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_statement)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.variable_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.assignment_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 204
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 205
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 206
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 207
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 208
                self.return_stmt()
                self.state = 209
                self.nonempty_newline_list()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 211
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 212
                self.block_stmt()
                self.state = 213
                self.nonempty_newline_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_declContext,0)


        def nonempty_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nonempty_newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variable_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_stmt" ):
                return visitor.visitVariable_stmt(self)
            else:
                return visitor.visitChildren(self)




    def variable_stmt(self):

        localctx = ZCodeParser.Variable_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_variable_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.variable_decl()
            self.state = 218
            self.nonempty_newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs_asmt(self):
            return self.getTypedRuleContext(ZCodeParser.Lhs_asmtContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def nonempty_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nonempty_newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_stmt" ):
                return visitor.visitAssignment_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assignment_stmt(self):

        localctx = ZCodeParser.Assignment_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assignment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.lhs_asmt()
            self.state = 221
            self.match(ZCodeParser.ASSIGN)
            self.state = 222
            self.expression()
            self.state = 223
            self.nonempty_newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lhs_asmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def index_op(self):
            return self.getTypedRuleContext(ZCodeParser.Index_opContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs_asmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs_asmt" ):
                return visitor.visitLhs_asmt(self)
            else:
                return visitor.visitChildren(self)




    def lhs_asmt(self):

        localctx = ZCodeParser.Lhs_asmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_lhs_asmt)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 227
                self.index_op()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LEFT_PAREN(self):
            return self.getToken(ZCodeParser.LEFT_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(ZCodeParser.RIGHT_PAREN, 0)

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_listContext,0)


        def else_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = ZCodeParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(ZCodeParser.IF)
            self.state = 231
            self.match(ZCodeParser.LEFT_PAREN)
            self.state = 232
            self.expression()
            self.state = 233
            self.match(ZCodeParser.RIGHT_PAREN)
            self.state = 234
            self.nullable_newline_list()
            self.state = 235
            self.statement()
            self.state = 236
            self.elif_list()
            self.state = 237
            self.else_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LEFT_PAREN(self):
            return self.getToken(ZCodeParser.LEFT_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(ZCodeParser.RIGHT_PAREN, 0)

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_stmt" ):
                return visitor.visitElif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elif_stmt(self):

        localctx = ZCodeParser.Elif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_elif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(ZCodeParser.ELIF)
            self.state = 240
            self.match(ZCodeParser.LEFT_PAREN)
            self.state = 241
            self.expression()
            self.state = 242
            self.match(ZCodeParser.RIGHT_PAREN)
            self.state = 243
            self.nullable_newline_list()
            self.state = 244
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmtContext,0)


        def elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_list" ):
                return visitor.visitElif_list(self)
            else:
                return visitor.visitChildren(self)




    def elif_list(self):

        localctx = ZCodeParser.Elif_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_elif_list)
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.elif_stmt()
                self.state = 247
                self.elif_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = ZCodeParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_else_stmt)
        try:
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.match(ZCodeParser.ELSE)
                self.state = 253
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = ZCodeParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(ZCodeParser.FOR)
            self.state = 258
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 259
            self.match(ZCodeParser.UNTIL)
            self.state = 260
            self.expression()
            self.state = 261
            self.match(ZCodeParser.BY)
            self.state = 262
            self.expression()
            self.state = 263
            self.nullable_newline_list()
            self.state = 264
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def nonempty_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nonempty_newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = ZCodeParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(ZCodeParser.BREAK)
            self.state = 267
            self.nonempty_newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def nonempty_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nonempty_newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = ZCodeParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(ZCodeParser.CONTINUE)
            self.state = 270
            self.nonempty_newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def return_value(self):
            return self.getTypedRuleContext(ZCodeParser.Return_valueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = ZCodeParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(ZCodeParser.RETURN)
            self.state = 273
            self.return_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_value" ):
                return visitor.visitReturn_value(self)
            else:
                return visitor.visitChildren(self)




    def return_value(self):

        localctx = ZCodeParser.Return_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_return_value)
        try:
            self.state = 277
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB, ZCodeParser.NOT, ZCodeParser.LEFT_PAREN, ZCodeParser.LEFT_SQUARE_BRACKET, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.expression()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Call_exprContext,0)


        def nonempty_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nonempty_newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = ZCodeParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.call_expr()
            self.state = 280
            self.nonempty_newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def nonempty_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nonempty_newline_listContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_listContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = ZCodeParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(ZCodeParser.BEGIN)
            self.state = 283
            self.nonempty_newline_list()
            self.state = 284
            self.stmt_list()
            self.state = 285
            self.match(ZCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr1Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expression)
        try:
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.expr1()
                self.state = 288
                self.match(ZCodeParser.CONCAT)
                self.state = 289
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr2Context,i)


        def rel_op(self):
            return self.getTypedRuleContext(ZCodeParser.Rel_opContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expr1)
        try:
            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.expr2(0)
                self.state = 295
                self.rel_op()
                self.state = 296
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Expr2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 309
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 304
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 305
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 306
                    self.expr3(0) 
                self.state = 311
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 320
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 315
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 316
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 317
                    self.expr4(0) 
                self.state = 322
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 331
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 326
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 327
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 328
                    self.expr5() 
                self.state = 333
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr5)
        try:
            self.state = 337
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(ZCodeParser.NOT)
                self.state = 335
                self.expr5()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB, ZCodeParser.LEFT_PAREN, ZCodeParser.LEFT_SQUARE_BRACKET, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expr6)
        try:
            self.state = 342
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.match(ZCodeParser.SUB)
                self.state = 340
                self.expr6()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LEFT_PAREN, ZCodeParser.LEFT_SQUARE_BRACKET, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Index_exprContext,0)


        def operand(self):
            return self.getTypedRuleContext(ZCodeParser.OperandContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = ZCodeParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expr7)
        try:
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.index_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(ZCodeParser.STRING_LIT, 0)

        def boolean_lit(self):
            return self.getTypedRuleContext(ZCodeParser.Boolean_litContext,0)


        def array_lit(self):
            return self.getTypedRuleContext(ZCodeParser.Array_litContext,0)


        def call_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Call_exprContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(ZCodeParser.LEFT_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(ZCodeParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = ZCodeParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_operand)
        try:
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.match(ZCodeParser.NUMBER_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.match(ZCodeParser.STRING_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 350
                self.boolean_lit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 351
                self.array_lit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 352
                self.call_expr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 353
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 354
                self.match(ZCodeParser.LEFT_PAREN)
                self.state = 355
                self.expression()
                self.state = 356
                self.match(ZCodeParser.RIGHT_PAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_boolean_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_lit" ):
                return visitor.visitBoolean_lit(self)
            else:
                return visitor.visitChildren(self)




    def boolean_lit(self):

        localctx = ZCodeParser.Boolean_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_boolean_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.TRUE or _la==ZCodeParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_SQUARE_BRACKET, 0)

        def array_element_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_element_listContext,0)


        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_SQUARE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = ZCodeParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
            self.state = 363
            self.array_element_list()
            self.state = 364
            self.match(ZCodeParser.RIGHT_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_element_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_element_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element_list" ):
                return visitor.visitArray_element_list(self)
            else:
                return visitor.visitChildren(self)




    def array_element_list(self):

        localctx = ZCodeParser.Array_element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_array_element_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.expr_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFT_PAREN(self):
            return self.getToken(ZCodeParser.LEFT_PAREN, 0)

        def argument_list(self):
            return self.getTypedRuleContext(ZCodeParser.Argument_listContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(ZCodeParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_call_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_expr" ):
                return visitor.visitCall_expr(self)
            else:
                return visitor.visitChildren(self)




    def call_expr(self):

        localctx = ZCodeParser.Call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_call_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 369
            self.match(ZCodeParser.LEFT_PAREN)
            self.state = 370
            self.argument_list()
            self.state = 371
            self.match(ZCodeParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argument_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_list" ):
                return visitor.visitArgument_list(self)
            else:
                return visitor.visitChildren(self)




    def argument_list(self):

        localctx = ZCodeParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_argument_list)
        try:
            self.state = 375
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB, ZCodeParser.NOT, ZCodeParser.LEFT_PAREN, ZCodeParser.LEFT_SQUARE_BRACKET, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.expr_list()
                pass
            elif token in [ZCodeParser.RIGHT_PAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_for_indexing(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_for_indexingContext,0)


        def index_op(self):
            return self.getTypedRuleContext(ZCodeParser.Index_opContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expr" ):
                return visitor.visitIndex_expr(self)
            else:
                return visitor.visitChildren(self)




    def index_expr(self):

        localctx = ZCodeParser.Index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_index_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.expr_for_indexing()
            self.state = 378
            self.index_op()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_for_indexingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def call_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Call_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_for_indexing

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_for_indexing" ):
                return visitor.visitExpr_for_indexing(self)
            else:
                return visitor.visitChildren(self)




    def expr_for_indexing(self):

        localctx = ZCodeParser.Expr_for_indexingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expr_for_indexing)
        try:
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                self.call_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = ZCodeParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_expr_list)
        try:
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.expression()
                self.state = 385
                self.match(ZCodeParser.COMMA)
                self.state = 386
                self.expr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Number_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def number_list(self):
            return self.getTypedRuleContext(ZCodeParser.Number_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_number_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber_list" ):
                return visitor.visitNumber_list(self)
            else:
                return visitor.visitChildren(self)




    def number_list(self):

        localctx = ZCodeParser.Number_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_number_list)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.match(ZCodeParser.NUMBER_LIT)
                self.state = 392
                self.match(ZCodeParser.COMMA)
                self.state = 393
                self.number_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.match(ZCodeParser.NUMBER_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = ZCodeParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_stmt_list)
        try:
            self.state = 401
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.statement()
                self.state = 398
                self.stmt_list()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nullable_newline_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nullable_newline_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullable_newline_list" ):
                return visitor.visitNullable_newline_list(self)
            else:
                return visitor.visitChildren(self)




    def nullable_newline_list(self):

        localctx = ZCodeParser.Nullable_newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_nullable_newline_list)
        try:
            self.state = 406
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.match(ZCodeParser.NEWLINE)
                self.state = 404
                self.nullable_newline_list()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nonempty_newline_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def nonempty_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nonempty_newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nonempty_newline_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonempty_newline_list" ):
                return visitor.visitNonempty_newline_list(self)
            else:
                return visitor.visitChildren(self)




    def nonempty_newline_list(self):

        localctx = ZCodeParser.Nonempty_newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_nonempty_newline_list)
        try:
            self.state = 411
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                self.match(ZCodeParser.NEWLINE)
                self.state = 409
                self.nonempty_newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.match(ZCodeParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = ZCodeParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rel_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(ZCodeParser.EQ, 0)

        def STRING_EQ(self):
            return self.getToken(ZCodeParser.STRING_EQ, 0)

        def NEQ(self):
            return self.getToken(ZCodeParser.NEQ, 0)

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def GT(self):
            return self.getToken(ZCodeParser.GT, 0)

        def LTE(self):
            return self.getToken(ZCodeParser.LTE, 0)

        def GTE(self):
            return self.getToken(ZCodeParser.GTE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_rel_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRel_op" ):
                return visitor.visitRel_op(self)
            else:
                return visitor.visitChildren(self)




    def rel_op(self):

        localctx = ZCodeParser.Rel_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_rel_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQ) | (1 << ZCodeParser.NEQ) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.LTE) | (1 << ZCodeParser.GT) | (1 << ZCodeParser.GTE) | (1 << ZCodeParser.STRING_EQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_SQUARE_BRACKET, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_SQUARE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_index_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_op" ):
                return visitor.visitIndex_op(self)
            else:
                return visitor.visitChildren(self)




    def index_op(self):

        localctx = ZCodeParser.Index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_index_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
            self.state = 418
            self.expr_list()
            self.state = 419
            self.match(ZCodeParser.RIGHT_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[34] = self.expr2_sempred
        self._predicates[35] = self.expr3_sempred
        self._predicates[36] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




