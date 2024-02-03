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
        buf.write("\u01aa\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\5\3y\n\3\3\4\3\4\5\4}\n\4\3\5\3\5\3\5\3")
        buf.write("\5\5\5\u0083\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\5\t\u0098\n\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\5\f\u00a8\n\f\3\r\3\r\3\r\5\r\u00ad\n\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\5\20")
        buf.write("\u00bb\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u00c2\n\21\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00cb\n\22\3\23")
        buf.write("\3\23\3\23\3\23\5\23\u00d1\n\23\3\24\3\24\5\24\u00d5\n")
        buf.write("\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\5\25\u00e4\n\25\3\26\3\26\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u00f3")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\5\33")
        buf.write("\u0109\n\33\3\34\3\34\3\34\5\34\u010e\n\34\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\5!\u0124\n!\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3#\3#\3$\3$\3$\3$\5$\u0132\n$\3%\3%\3%\3%\3%\5%\u0139")
        buf.write("\n%\3&\3&\3&\3&\3&\5&\u0140\n&\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\7\'\u0148\n\'\f\'\16\'\u014b\13\'\3(\3(\3(\3(\3(\3(\7")
        buf.write("(\u0153\n(\f(\16(\u0156\13(\3)\3)\3)\3)\3)\3)\7)\u015e")
        buf.write("\n)\f)\16)\u0161\13)\3*\3*\3*\5*\u0166\n*\3+\3+\3+\5+")
        buf.write("\u016b\n+\3,\3,\5,\u016f\n,\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\5-\u017b\n-\3.\3.\3/\3/\3/\3/\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\5\61\u018a\n\61\3\62\3\62\3\62\3\62\3")
        buf.write("\62\3\63\3\63\5\63\u0193\n\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\66\3\66\3\66\5\66\u019e\n\66\3\67\3\67\3\67\5")
        buf.write("\67\u01a3\n\67\38\38\38\58\u01a8\n8\38\2\5LNP9\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<>@BDFHJLNPRTVXZ\\^`bdfhjln\2\b\3\2\35\36\3\2\27\30\3")
        buf.write("\2\31\33\3\2\3\4\3\2\5\7\4\2\37$&&\2\u019f\2p\3\2\2\2")
        buf.write("\4x\3\2\2\2\6|\3\2\2\2\b\u0082\3\2\2\2\n\u0084\3\2\2\2")
        buf.write("\f\u0089\3\2\2\2\16\u008f\3\2\2\2\20\u0097\3\2\2\2\22")
        buf.write("\u0099\3\2\2\2\24\u009f\3\2\2\2\26\u00a7\3\2\2\2\30\u00ac")
        buf.write("\3\2\2\2\32\u00ae\3\2\2\2\34\u00b4\3\2\2\2\36\u00ba\3")
        buf.write("\2\2\2 \u00c1\3\2\2\2\"\u00ca\3\2\2\2$\u00d0\3\2\2\2&")
        buf.write("\u00d4\3\2\2\2(\u00e3\3\2\2\2*\u00e5\3\2\2\2,\u00e7\3")
        buf.write("\2\2\2.\u00f2\3\2\2\2\60\u00f4\3\2\2\2\62\u00fd\3\2\2")
        buf.write("\2\64\u0108\3\2\2\2\66\u010d\3\2\2\28\u010f\3\2\2\2:\u0118")
        buf.write("\3\2\2\2<\u011b\3\2\2\2>\u011e\3\2\2\2@\u0123\3\2\2\2")
        buf.write("B\u0125\3\2\2\2D\u0128\3\2\2\2F\u0131\3\2\2\2H\u0138\3")
        buf.write("\2\2\2J\u013f\3\2\2\2L\u0141\3\2\2\2N\u014c\3\2\2\2P\u0157")
        buf.write("\3\2\2\2R\u0165\3\2\2\2T\u016a\3\2\2\2V\u016e\3\2\2\2")
        buf.write("X\u017a\3\2\2\2Z\u017c\3\2\2\2\\\u017e\3\2\2\2^\u0182")
        buf.write("\3\2\2\2`\u0189\3\2\2\2b\u018b\3\2\2\2d\u0192\3\2\2\2")
        buf.write("f\u0194\3\2\2\2h\u0196\3\2\2\2j\u019d\3\2\2\2l\u01a2\3")
        buf.write("\2\2\2n\u01a7\3\2\2\2pq\5n8\2qr\5\4\3\2rs\7\2\2\3s\3\3")
        buf.write("\2\2\2tu\5\6\4\2uv\5\4\3\2vy\3\2\2\2wy\5\6\4\2xt\3\2\2")
        buf.write("\2xw\3\2\2\2y\5\3\2\2\2z}\5\b\5\2{}\5\32\16\2|z\3\2\2")
        buf.write("\2|{\3\2\2\2}\7\3\2\2\2~\u0083\5\n\6\2\177\u0083\5\f\7")
        buf.write("\2\u0080\u0083\5\16\b\2\u0081\u0083\5\22\n\2\u0082~\3")
        buf.write("\2\2\2\u0082\177\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0081")
        buf.write("\3\2\2\2\u0083\t\3\2\2\2\u0084\u0085\5f\64\2\u0085\u0086")
        buf.write("\7\60\2\2\u0086\u0087\5\20\t\2\u0087\u0088\5l\67\2\u0088")
        buf.write("\13\3\2\2\2\u0089\u008a\7\t\2\2\u008a\u008b\7\60\2\2\u008b")
        buf.write("\u008c\7\26\2\2\u008c\u008d\5H%\2\u008d\u008e\5l\67\2")
        buf.write("\u008e\r\3\2\2\2\u008f\u0090\7\n\2\2\u0090\u0091\7\60")
        buf.write("\2\2\u0091\u0092\5\20\t\2\u0092\u0093\5l\67\2\u0093\17")
        buf.write("\3\2\2\2\u0094\u0095\7\26\2\2\u0095\u0098\5H%\2\u0096")
        buf.write("\u0098\3\2\2\2\u0097\u0094\3\2\2\2\u0097\u0096\3\2\2\2")
        buf.write("\u0098\21\3\2\2\2\u0099\u009a\5f\64\2\u009a\u009b\7\60")
        buf.write("\2\2\u009b\u009c\5\24\13\2\u009c\u009d\5\30\r\2\u009d")
        buf.write("\u009e\5l\67\2\u009e\23\3\2\2\2\u009f\u00a0\7)\2\2\u00a0")
        buf.write("\u00a1\5\26\f\2\u00a1\u00a2\7*\2\2\u00a2\25\3\2\2\2\u00a3")
        buf.write("\u00a4\7-\2\2\u00a4\u00a5\7+\2\2\u00a5\u00a8\5\26\f\2")
        buf.write("\u00a6\u00a8\7-\2\2\u00a7\u00a3\3\2\2\2\u00a7\u00a6\3")
        buf.write("\2\2\2\u00a8\27\3\2\2\2\u00a9\u00aa\7\26\2\2\u00aa\u00ad")
        buf.write("\5\\/\2\u00ab\u00ad\3\2\2\2\u00ac\u00a9\3\2\2\2\u00ac")
        buf.write("\u00ab\3\2\2\2\u00ad\31\3\2\2\2\u00ae\u00af\7\13\2\2\u00af")
        buf.write("\u00b0\7\60\2\2\u00b0\u00b1\5\34\17\2\u00b1\u00b2\5$\23")
        buf.write("\2\u00b2\u00b3\5l\67\2\u00b3\33\3\2\2\2\u00b4\u00b5\7")
        buf.write("\'\2\2\u00b5\u00b6\5\36\20\2\u00b6\u00b7\7(\2\2\u00b7")
        buf.write("\35\3\2\2\2\u00b8\u00bb\5 \21\2\u00b9\u00bb\3\2\2\2\u00ba")
        buf.write("\u00b8\3\2\2\2\u00ba\u00b9\3\2\2\2\u00bb\37\3\2\2\2\u00bc")
        buf.write("\u00bd\5\"\22\2\u00bd\u00be\7+\2\2\u00be\u00bf\5 \21\2")
        buf.write("\u00bf\u00c2\3\2\2\2\u00c0\u00c2\5\"\22\2\u00c1\u00bc")
        buf.write("\3\2\2\2\u00c1\u00c0\3\2\2\2\u00c2!\3\2\2\2\u00c3\u00c4")
        buf.write("\5f\64\2\u00c4\u00c5\7\60\2\2\u00c5\u00cb\3\2\2\2\u00c6")
        buf.write("\u00c7\5f\64\2\u00c7\u00c8\7\60\2\2\u00c8\u00c9\5\24\13")
        buf.write("\2\u00c9\u00cb\3\2\2\2\u00ca\u00c3\3\2\2\2\u00ca\u00c6")
        buf.write("\3\2\2\2\u00cb#\3\2\2\2\u00cc\u00cd\5n8\2\u00cd\u00ce")
        buf.write("\5&\24\2\u00ce\u00d1\3\2\2\2\u00cf\u00d1\3\2\2\2\u00d0")
        buf.write("\u00cc\3\2\2\2\u00d0\u00cf\3\2\2\2\u00d1%\3\2\2\2\u00d2")
        buf.write("\u00d5\5> \2\u00d3\u00d5\5D#\2\u00d4\u00d2\3\2\2\2\u00d4")
        buf.write("\u00d3\3\2\2\2\u00d5\'\3\2\2\2\u00d6\u00e4\5*\26\2\u00d7")
        buf.write("\u00e4\5,\27\2\u00d8\u00e4\5\60\31\2\u00d9\u00e4\58\35")
        buf.write("\2\u00da\u00e4\5:\36\2\u00db\u00e4\5<\37\2\u00dc\u00dd")
        buf.write("\5> \2\u00dd\u00de\5l\67\2\u00de\u00e4\3\2\2\2\u00df\u00e4")
        buf.write("\5B\"\2\u00e0\u00e1\5D#\2\u00e1\u00e2\5l\67\2\u00e2\u00e4")
        buf.write("\3\2\2\2\u00e3\u00d6\3\2\2\2\u00e3\u00d7\3\2\2\2\u00e3")
        buf.write("\u00d8\3\2\2\2\u00e3\u00d9\3\2\2\2\u00e3\u00da\3\2\2\2")
        buf.write("\u00e3\u00db\3\2\2\2\u00e3\u00dc\3\2\2\2\u00e3\u00df\3")
        buf.write("\2\2\2\u00e3\u00e0\3\2\2\2\u00e4)\3\2\2\2\u00e5\u00e6")
        buf.write("\5\b\5\2\u00e6+\3\2\2\2\u00e7\u00e8\5.\30\2\u00e8\u00e9")
        buf.write("\7\26\2\2\u00e9\u00ea\5H%\2\u00ea\u00eb\5l\67\2\u00eb")
        buf.write("-\3\2\2\2\u00ec\u00f3\7\60\2\2\u00ed\u00ee\7\60\2\2\u00ee")
        buf.write("\u00ef\7)\2\2\u00ef\u00f0\5j\66\2\u00f0\u00f1\7*\2\2\u00f1")
        buf.write("\u00f3\3\2\2\2\u00f2\u00ec\3\2\2\2\u00f2\u00ed\3\2\2\2")
        buf.write("\u00f3/\3\2\2\2\u00f4\u00f5\7\21\2\2\u00f5\u00f6\7\'\2")
        buf.write("\2\u00f6\u00f7\5H%\2\u00f7\u00f8\7(\2\2\u00f8\u00f9\5")
        buf.write("n8\2\u00f9\u00fa\5(\25\2\u00fa\u00fb\5\64\33\2\u00fb\u00fc")
        buf.write("\5\66\34\2\u00fc\61\3\2\2\2\u00fd\u00fe\7\23\2\2\u00fe")
        buf.write("\u00ff\7\'\2\2\u00ff\u0100\5H%\2\u0100\u0101\7(\2\2\u0101")
        buf.write("\u0102\5n8\2\u0102\u0103\5(\25\2\u0103\63\3\2\2\2\u0104")
        buf.write("\u0105\5\62\32\2\u0105\u0106\5\64\33\2\u0106\u0109\3\2")
        buf.write("\2\2\u0107\u0109\3\2\2\2\u0108\u0104\3\2\2\2\u0108\u0107")
        buf.write("\3\2\2\2\u0109\65\3\2\2\2\u010a\u010b\7\22\2\2\u010b\u010e")
        buf.write("\5(\25\2\u010c\u010e\3\2\2\2\u010d\u010a\3\2\2\2\u010d")
        buf.write("\u010c\3\2\2\2\u010e\67\3\2\2\2\u010f\u0110\7\f\2\2\u0110")
        buf.write("\u0111\7\60\2\2\u0111\u0112\7\r\2\2\u0112\u0113\5H%\2")
        buf.write("\u0113\u0114\7\16\2\2\u0114\u0115\5H%\2\u0115\u0116\5")
        buf.write("n8\2\u0116\u0117\5(\25\2\u01179\3\2\2\2\u0118\u0119\7")
        buf.write("\17\2\2\u0119\u011a\5l\67\2\u011a;\3\2\2\2\u011b\u011c")
        buf.write("\7\20\2\2\u011c\u011d\5l\67\2\u011d=\3\2\2\2\u011e\u011f")
        buf.write("\7\b\2\2\u011f\u0120\5@!\2\u0120?\3\2\2\2\u0121\u0124")
        buf.write("\5H%\2\u0122\u0124\3\2\2\2\u0123\u0121\3\2\2\2\u0123\u0122")
        buf.write("\3\2\2\2\u0124A\3\2\2\2\u0125\u0126\5^\60\2\u0126\u0127")
        buf.write("\5l\67\2\u0127C\3\2\2\2\u0128\u0129\7\24\2\2\u0129\u012a")
        buf.write("\5l\67\2\u012a\u012b\5F$\2\u012b\u012c\7\25\2\2\u012c")
        buf.write("E\3\2\2\2\u012d\u012e\5(\25\2\u012e\u012f\5F$\2\u012f")
        buf.write("\u0132\3\2\2\2\u0130\u0132\3\2\2\2\u0131\u012d\3\2\2\2")
        buf.write("\u0131\u0130\3\2\2\2\u0132G\3\2\2\2\u0133\u0134\5J&\2")
        buf.write("\u0134\u0135\7%\2\2\u0135\u0136\5J&\2\u0136\u0139\3\2")
        buf.write("\2\2\u0137\u0139\5J&\2\u0138\u0133\3\2\2\2\u0138\u0137")
        buf.write("\3\2\2\2\u0139I\3\2\2\2\u013a\u013b\5L\'\2\u013b\u013c")
        buf.write("\5h\65\2\u013c\u013d\5L\'\2\u013d\u0140\3\2\2\2\u013e")
        buf.write("\u0140\5L\'\2\u013f\u013a\3\2\2\2\u013f\u013e\3\2\2\2")
        buf.write("\u0140K\3\2\2\2\u0141\u0142\b\'\1\2\u0142\u0143\5N(\2")
        buf.write("\u0143\u0149\3\2\2\2\u0144\u0145\f\4\2\2\u0145\u0146\t")
        buf.write("\2\2\2\u0146\u0148\5N(\2\u0147\u0144\3\2\2\2\u0148\u014b")
        buf.write("\3\2\2\2\u0149\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a")
        buf.write("M\3\2\2\2\u014b\u0149\3\2\2\2\u014c\u014d\b(\1\2\u014d")
        buf.write("\u014e\5P)\2\u014e\u0154\3\2\2\2\u014f\u0150\f\4\2\2\u0150")
        buf.write("\u0151\t\3\2\2\u0151\u0153\5P)\2\u0152\u014f\3\2\2\2\u0153")
        buf.write("\u0156\3\2\2\2\u0154\u0152\3\2\2\2\u0154\u0155\3\2\2\2")
        buf.write("\u0155O\3\2\2\2\u0156\u0154\3\2\2\2\u0157\u0158\b)\1\2")
        buf.write("\u0158\u0159\5R*\2\u0159\u015f\3\2\2\2\u015a\u015b\f\4")
        buf.write("\2\2\u015b\u015c\t\4\2\2\u015c\u015e\5R*\2\u015d\u015a")
        buf.write("\3\2\2\2\u015e\u0161\3\2\2\2\u015f\u015d\3\2\2\2\u015f")
        buf.write("\u0160\3\2\2\2\u0160Q\3\2\2\2\u0161\u015f\3\2\2\2\u0162")
        buf.write("\u0163\7\34\2\2\u0163\u0166\5R*\2\u0164\u0166\5T+\2\u0165")
        buf.write("\u0162\3\2\2\2\u0165\u0164\3\2\2\2\u0166S\3\2\2\2\u0167")
        buf.write("\u0168\7\30\2\2\u0168\u016b\5T+\2\u0169\u016b\5V,\2\u016a")
        buf.write("\u0167\3\2\2\2\u016a\u0169\3\2\2\2\u016bU\3\2\2\2\u016c")
        buf.write("\u016f\5b\62\2\u016d\u016f\5X-\2\u016e\u016c\3\2\2\2\u016e")
        buf.write("\u016d\3\2\2\2\u016fW\3\2\2\2\u0170\u017b\7-\2\2\u0171")
        buf.write("\u017b\7.\2\2\u0172\u017b\5Z.\2\u0173\u017b\5\\/\2\u0174")
        buf.write("\u017b\5^\60\2\u0175\u017b\7\60\2\2\u0176\u0177\7\'\2")
        buf.write("\2\u0177\u0178\5H%\2\u0178\u0179\7(\2\2\u0179\u017b\3")
        buf.write("\2\2\2\u017a\u0170\3\2\2\2\u017a\u0171\3\2\2\2\u017a\u0172")
        buf.write("\3\2\2\2\u017a\u0173\3\2\2\2\u017a\u0174\3\2\2\2\u017a")
        buf.write("\u0175\3\2\2\2\u017a\u0176\3\2\2\2\u017bY\3\2\2\2\u017c")
        buf.write("\u017d\t\5\2\2\u017d[\3\2\2\2\u017e\u017f\7)\2\2\u017f")
        buf.write("\u0180\5j\66\2\u0180\u0181\7*\2\2\u0181]\3\2\2\2\u0182")
        buf.write("\u0183\7\60\2\2\u0183\u0184\7\'\2\2\u0184\u0185\5`\61")
        buf.write("\2\u0185\u0186\7(\2\2\u0186_\3\2\2\2\u0187\u018a\5j\66")
        buf.write("\2\u0188\u018a\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u0188")
        buf.write("\3\2\2\2\u018aa\3\2\2\2\u018b\u018c\5d\63\2\u018c\u018d")
        buf.write("\7)\2\2\u018d\u018e\5j\66\2\u018e\u018f\7*\2\2\u018fc")
        buf.write("\3\2\2\2\u0190\u0193\7\60\2\2\u0191\u0193\5^\60\2\u0192")
        buf.write("\u0190\3\2\2\2\u0192\u0191\3\2\2\2\u0193e\3\2\2\2\u0194")
        buf.write("\u0195\t\6\2\2\u0195g\3\2\2\2\u0196\u0197\t\7\2\2\u0197")
        buf.write("i\3\2\2\2\u0198\u0199\5H%\2\u0199\u019a\7+\2\2\u019a\u019b")
        buf.write("\5j\66\2\u019b\u019e\3\2\2\2\u019c\u019e\5H%\2\u019d\u0198")
        buf.write("\3\2\2\2\u019d\u019c\3\2\2\2\u019ek\3\2\2\2\u019f\u01a0")
        buf.write("\7,\2\2\u01a0\u01a3\5l\67\2\u01a1\u01a3\7,\2\2\u01a2\u019f")
        buf.write("\3\2\2\2\u01a2\u01a1\3\2\2\2\u01a3m\3\2\2\2\u01a4\u01a5")
        buf.write("\7,\2\2\u01a5\u01a8\5n8\2\u01a6\u01a8\3\2\2\2\u01a7\u01a4")
        buf.write("\3\2\2\2\u01a7\u01a6\3\2\2\2\u01a8o\3\2\2\2!x|\u0082\u0097")
        buf.write("\u00a7\u00ac\u00ba\u00c1\u00ca\u00d0\u00d4\u00e3\u00f2")
        buf.write("\u0108\u010d\u0123\u0131\u0138\u013f\u0149\u0154\u015f")
        buf.write("\u0165\u016a\u016e\u017a\u0189\u0192\u019d\u01a2\u01a7")
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
                     "'...'", "'=='", "'('", "')'", "'['", "']'", "','" ]

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
    RULE_dimension_list = 10
    RULE_optional_array_init = 11
    RULE_function_decl = 12
    RULE_param_decl = 13
    RULE_param_list = 14
    RULE_param_list_prime = 15
    RULE_param = 16
    RULE_optional_impl = 17
    RULE_body = 18
    RULE_statement = 19
    RULE_variable_stmt = 20
    RULE_assignment_stmt = 21
    RULE_lhs_asmt = 22
    RULE_if_stmt = 23
    RULE_elif_stmt = 24
    RULE_elif_list = 25
    RULE_else_stmt = 26
    RULE_for_stmt = 27
    RULE_break_stmt = 28
    RULE_continue_stmt = 29
    RULE_return_stmt = 30
    RULE_return_value = 31
    RULE_call_stmt = 32
    RULE_block_stmt = 33
    RULE_stmt_list = 34
    RULE_expression = 35
    RULE_expr1 = 36
    RULE_expr2 = 37
    RULE_expr3 = 38
    RULE_expr4 = 39
    RULE_expr5 = 40
    RULE_expr6 = 41
    RULE_expr7 = 42
    RULE_operand = 43
    RULE_boolean_lit = 44
    RULE_array_lit = 45
    RULE_call_expr = 46
    RULE_argument_list = 47
    RULE_index_expr = 48
    RULE_expr_for_indexing = 49
    RULE_primitive_type = 50
    RULE_rel_op = 51
    RULE_expr_list = 52
    RULE_nonempty_newline_list = 53
    RULE_nullable_newline_list = 54

    ruleNames =  [ "program", "decl_list", "decl", "variable_decl", "primitive_decl", 
                   "var_keyword_decl", "dynamic_keyword_decl", "optional_init", 
                   "array_decl", "array_dimensions", "dimension_list", "optional_array_init", 
                   "function_decl", "param_decl", "param_list", "param_list_prime", 
                   "param", "optional_impl", "body", "statement", "variable_stmt", 
                   "assignment_stmt", "lhs_asmt", "if_stmt", "elif_stmt", 
                   "elif_list", "else_stmt", "for_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "return_value", "call_stmt", "block_stmt", 
                   "stmt_list", "expression", "expr1", "expr2", "expr3", 
                   "expr4", "expr5", "expr6", "expr7", "operand", "boolean_lit", 
                   "array_lit", "call_expr", "argument_list", "index_expr", 
                   "expr_for_indexing", "primitive_type", "rel_op", "expr_list", 
                   "nonempty_newline_list", "nullable_newline_list" ]

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

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


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
            self.state = 110
            self.nullable_newline_list()
            self.state = 111
            self.decl_list()
            self.state = 112
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
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.decl()
                self.state = 115
                self.decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
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
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.variable_decl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.function_decl()
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
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.primitive_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.var_keyword_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.dynamic_keyword_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
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


        def nonempty_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nonempty_newline_listContext,0)


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
            self.state = 130
            self.primitive_type()
            self.state = 131
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 132
            self.optional_init()
            self.state = 133
            self.nonempty_newline_list()
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


        def nonempty_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nonempty_newline_listContext,0)


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
            self.state = 135
            self.match(ZCodeParser.VAR)
            self.state = 136
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 137
            self.match(ZCodeParser.ASSIGN)
            self.state = 138
            self.expression()
            self.state = 139
            self.nonempty_newline_list()
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


        def nonempty_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nonempty_newline_listContext,0)


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
            self.state = 141
            self.match(ZCodeParser.DYNAMIC)
            self.state = 142
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 143
            self.optional_init()
            self.state = 144
            self.nonempty_newline_list()
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
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(ZCodeParser.ASSIGN)
                self.state = 147
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


        def optional_array_init(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_array_initContext,0)


        def nonempty_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nonempty_newline_listContext,0)


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
            self.state = 151
            self.primitive_type()
            self.state = 152
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 153
            self.array_dimensions()
            self.state = 154
            self.optional_array_init()
            self.state = 155
            self.nonempty_newline_list()
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

        def dimension_list(self):
            return self.getTypedRuleContext(ZCodeParser.Dimension_listContext,0)


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
            self.state = 157
            self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
            self.state = 158
            self.dimension_list()
            self.state = 159
            self.match(ZCodeParser.RIGHT_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimension_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def dimension_list(self):
            return self.getTypedRuleContext(ZCodeParser.Dimension_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dimension_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension_list" ):
                return visitor.visitDimension_list(self)
            else:
                return visitor.visitChildren(self)




    def dimension_list(self):

        localctx = ZCodeParser.Dimension_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_dimension_list)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.match(ZCodeParser.NUMBER_LIT)
                self.state = 162
                self.match(ZCodeParser.COMMA)
                self.state = 163
                self.dimension_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.match(ZCodeParser.NUMBER_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_array_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def array_lit(self):
            return self.getTypedRuleContext(ZCodeParser.Array_litContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_optional_array_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_array_init" ):
                return visitor.visitOptional_array_init(self)
            else:
                return visitor.visitChildren(self)




    def optional_array_init(self):

        localctx = ZCodeParser.Optional_array_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_optional_array_init)
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(ZCodeParser.ASSIGN)
                self.state = 168
                self.array_lit()
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


        def nonempty_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nonempty_newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_decl" ):
                return visitor.visitFunction_decl(self)
            else:
                return visitor.visitChildren(self)




    def function_decl(self):

        localctx = ZCodeParser.Function_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_function_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(ZCodeParser.FUNC)
            self.state = 173
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 174
            self.param_decl()
            self.state = 175
            self.optional_impl()
            self.state = 176
            self.nonempty_newline_list()
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
        self.enterRule(localctx, 26, self.RULE_param_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(ZCodeParser.LEFT_PAREN)
            self.state = 179
            self.param_list()
            self.state = 180
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

        def param_list_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Param_list_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = ZCodeParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_param_list)
        try:
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.param_list_prime()
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


    class Param_list_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def param_list_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Param_list_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_list_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list_prime" ):
                return visitor.visitParam_list_prime(self)
            else:
                return visitor.visitChildren(self)




    def param_list_prime(self):

        localctx = ZCodeParser.Param_list_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_param_list_prime)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.param()
                self.state = 187
                self.match(ZCodeParser.COMMA)
                self.state = 188
                self.param_list_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
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
        self.enterRule(localctx, 32, self.RULE_param)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.primitive_type()
                self.state = 194
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.primitive_type()
                self.state = 197
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 198
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
        self.enterRule(localctx, 34, self.RULE_optional_impl)
        try:
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.nullable_newline_list()
                self.state = 203
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
        self.enterRule(localctx, 36, self.RULE_body)
        try:
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.return_stmt()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
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
        self.enterRule(localctx, 38, self.RULE_statement)
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.variable_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.assignment_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 214
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 215
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 216
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 217
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 218
                self.return_stmt()
                self.state = 219
                self.nonempty_newline_list()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 221
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 222
                self.block_stmt()
                self.state = 223
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


        def getRuleIndex(self):
            return ZCodeParser.RULE_variable_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_stmt" ):
                return visitor.visitVariable_stmt(self)
            else:
                return visitor.visitChildren(self)




    def variable_stmt(self):

        localctx = ZCodeParser.Variable_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_variable_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.variable_decl()
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
        self.enterRule(localctx, 42, self.RULE_assignment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.lhs_asmt()
            self.state = 230
            self.match(ZCodeParser.ASSIGN)
            self.state = 231
            self.expression()
            self.state = 232
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

        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_SQUARE_BRACKET, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_SQUARE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs_asmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs_asmt" ):
                return visitor.visitLhs_asmt(self)
            else:
                return visitor.visitChildren(self)




    def lhs_asmt(self):

        localctx = ZCodeParser.Lhs_asmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_lhs_asmt)
        try:
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 236
                self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
                self.state = 237
                self.expr_list()
                self.state = 238
                self.match(ZCodeParser.RIGHT_SQUARE_BRACKET)
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
        self.enterRule(localctx, 46, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(ZCodeParser.IF)
            self.state = 243
            self.match(ZCodeParser.LEFT_PAREN)
            self.state = 244
            self.expression()
            self.state = 245
            self.match(ZCodeParser.RIGHT_PAREN)
            self.state = 246
            self.nullable_newline_list()
            self.state = 247
            self.statement()
            self.state = 248
            self.elif_list()
            self.state = 249
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
        self.enterRule(localctx, 48, self.RULE_elif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(ZCodeParser.ELIF)
            self.state = 252
            self.match(ZCodeParser.LEFT_PAREN)
            self.state = 253
            self.expression()
            self.state = 254
            self.match(ZCodeParser.RIGHT_PAREN)
            self.state = 255
            self.nullable_newline_list()
            self.state = 256
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
        self.enterRule(localctx, 50, self.RULE_elif_list)
        try:
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.elif_stmt()
                self.state = 259
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
        self.enterRule(localctx, 52, self.RULE_else_stmt)
        try:
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.match(ZCodeParser.ELSE)
                self.state = 265
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
        self.enterRule(localctx, 54, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(ZCodeParser.FOR)
            self.state = 270
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 271
            self.match(ZCodeParser.UNTIL)
            self.state = 272
            self.expression()
            self.state = 273
            self.match(ZCodeParser.BY)
            self.state = 274
            self.expression()
            self.state = 275
            self.nullable_newline_list()
            self.state = 276
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
        self.enterRule(localctx, 56, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(ZCodeParser.BREAK)
            self.state = 279
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
        self.enterRule(localctx, 58, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(ZCodeParser.CONTINUE)
            self.state = 282
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
        self.enterRule(localctx, 60, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(ZCodeParser.RETURN)
            self.state = 285
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
        self.enterRule(localctx, 62, self.RULE_return_value)
        try:
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB, ZCodeParser.NOT, ZCodeParser.LEFT_PAREN, ZCodeParser.LEFT_SQUARE_BRACKET, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
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
        self.enterRule(localctx, 64, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.call_expr()
            self.state = 292
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
        self.enterRule(localctx, 66, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(ZCodeParser.BEGIN)
            self.state = 295
            self.nonempty_newline_list()
            self.state = 296
            self.stmt_list()
            self.state = 297
            self.match(ZCodeParser.END)
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
        self.enterRule(localctx, 68, self.RULE_stmt_list)
        try:
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.statement()
                self.state = 300
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
        self.enterRule(localctx, 70, self.RULE_expression)
        try:
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.expr1()
                self.state = 306
                self.match(ZCodeParser.CONCAT)
                self.state = 307
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
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
        self.enterRule(localctx, 72, self.RULE_expr1)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.expr2(0)
                self.state = 313
                self.rel_op()
                self.state = 314
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 327
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 322
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 323
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 324
                    self.expr3(0) 
                self.state = 329
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 338
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 333
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 334
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 335
                    self.expr4(0) 
                self.state = 340
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 349
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 344
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 345
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 346
                    self.expr5() 
                self.state = 351
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        self.enterRule(localctx, 80, self.RULE_expr5)
        try:
            self.state = 355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.match(ZCodeParser.NOT)
                self.state = 353
                self.expr5()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB, ZCodeParser.LEFT_PAREN, ZCodeParser.LEFT_SQUARE_BRACKET, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
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
        self.enterRule(localctx, 82, self.RULE_expr6)
        try:
            self.state = 360
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.match(ZCodeParser.SUB)
                self.state = 358
                self.expr6()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LEFT_PAREN, ZCodeParser.LEFT_SQUARE_BRACKET, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
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
        self.enterRule(localctx, 84, self.RULE_expr7)
        try:
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.index_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
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
        self.enterRule(localctx, 86, self.RULE_operand)
        try:
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.match(ZCodeParser.NUMBER_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
                self.match(ZCodeParser.STRING_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 368
                self.boolean_lit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 369
                self.array_lit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 370
                self.call_expr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 371
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 372
                self.match(ZCodeParser.LEFT_PAREN)
                self.state = 373
                self.expression()
                self.state = 374
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
        self.enterRule(localctx, 88, self.RULE_boolean_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
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

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


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
        self.enterRule(localctx, 90, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
            self.state = 381
            self.expr_list()
            self.state = 382
            self.match(ZCodeParser.RIGHT_SQUARE_BRACKET)
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
        self.enterRule(localctx, 92, self.RULE_call_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 385
            self.match(ZCodeParser.LEFT_PAREN)
            self.state = 386
            self.argument_list()
            self.state = 387
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
        self.enterRule(localctx, 94, self.RULE_argument_list)
        try:
            self.state = 391
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB, ZCodeParser.NOT, ZCodeParser.LEFT_PAREN, ZCodeParser.LEFT_SQUARE_BRACKET, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
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


        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_SQUARE_BRACKET, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_SQUARE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expr" ):
                return visitor.visitIndex_expr(self)
            else:
                return visitor.visitChildren(self)




    def index_expr(self):

        localctx = ZCodeParser.Index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_index_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.expr_for_indexing()
            self.state = 394
            self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
            self.state = 395
            self.expr_list()
            self.state = 396
            self.match(ZCodeParser.RIGHT_SQUARE_BRACKET)
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
        self.enterRule(localctx, 98, self.RULE_expr_for_indexing)
        try:
            self.state = 400
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 399
                self.call_expr()
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
        self.enterRule(localctx, 100, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
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
        self.enterRule(localctx, 102, self.RULE_rel_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
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
        self.enterRule(localctx, 104, self.RULE_expr_list)
        try:
            self.state = 411
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                self.expression()
                self.state = 407
                self.match(ZCodeParser.COMMA)
                self.state = 408
                self.expr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.expression()
                pass


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
        self.enterRule(localctx, 106, self.RULE_nonempty_newline_list)
        try:
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.match(ZCodeParser.NEWLINE)
                self.state = 414
                self.nonempty_newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
                self.match(ZCodeParser.NEWLINE)
                pass


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
        self.enterRule(localctx, 108, self.RULE_nullable_newline_list)
        try:
            self.state = 421
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.match(ZCodeParser.NEWLINE)
                self.state = 419
                self.nullable_newline_list()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[37] = self.expr2_sempred
        self._predicates[38] = self.expr3_sempred
        self._predicates[39] = self.expr4_sempred
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
         




