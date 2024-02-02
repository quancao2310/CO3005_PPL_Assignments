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
        buf.write("\u01a9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\5\3x\n\3\3\4\3\4\5\4|\n\4\3\5\3\5\3\5\3\5\5")
        buf.write("\5\u0082\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\5\t\u0097\n\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\5\f\u00a7\n\f\3\r\3\r\3\r\5\r\u00ac\n\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\5\20\u00ba")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u00c1\n\21\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\5\22\u00ca\n\22\3\23\3\23")
        buf.write("\3\23\3\23\5\23\u00d0\n\23\3\24\3\24\5\24\u00d4\n\24\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\5\25\u00e3\n\25\3\26\3\26\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u00f2\n\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\5\33\u0108")
        buf.write("\n\33\3\34\3\34\3\34\5\34\u010d\n\34\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\5!\u0123\n!\3\"\3\"\3\"\3#\3#\3#")
        buf.write("\3#\3#\3$\3$\3$\3$\5$\u0131\n$\3%\3%\3%\3%\3%\5%\u0138")
        buf.write("\n%\3&\3&\3&\3&\3&\5&\u013f\n&\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\7\'\u0147\n\'\f\'\16\'\u014a\13\'\3(\3(\3(\3(\3(\3(\7")
        buf.write("(\u0152\n(\f(\16(\u0155\13(\3)\3)\3)\3)\3)\3)\7)\u015d")
        buf.write("\n)\f)\16)\u0160\13)\3*\3*\3*\5*\u0165\n*\3+\3+\3+\5+")
        buf.write("\u016a\n+\3,\3,\5,\u016e\n,\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\5-\u017a\n-\3.\3.\3/\3/\3/\3/\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\5\61\u0189\n\61\3\62\3\62\3\62\3\62\3")
        buf.write("\62\3\63\3\63\5\63\u0192\n\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\66\3\66\3\66\5\66\u019d\n\66\3\67\3\67\3\67\5")
        buf.write("\67\u01a2\n\67\38\38\38\58\u01a7\n8\38\2\5LNP9\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<>@BDFHJLNPRTVXZ\\^`bdfhjln\2\b\3\2\35\36\3\2\27\30\3")
        buf.write("\2\31\33\3\2\3\4\3\2\5\7\4\2\37$&&\2\u019e\2p\3\2\2\2")
        buf.write("\4w\3\2\2\2\6{\3\2\2\2\b\u0081\3\2\2\2\n\u0083\3\2\2\2")
        buf.write("\f\u0088\3\2\2\2\16\u008e\3\2\2\2\20\u0096\3\2\2\2\22")
        buf.write("\u0098\3\2\2\2\24\u009e\3\2\2\2\26\u00a6\3\2\2\2\30\u00ab")
        buf.write("\3\2\2\2\32\u00ad\3\2\2\2\34\u00b3\3\2\2\2\36\u00b9\3")
        buf.write("\2\2\2 \u00c0\3\2\2\2\"\u00c9\3\2\2\2$\u00cf\3\2\2\2&")
        buf.write("\u00d3\3\2\2\2(\u00e2\3\2\2\2*\u00e4\3\2\2\2,\u00e6\3")
        buf.write("\2\2\2.\u00f1\3\2\2\2\60\u00f3\3\2\2\2\62\u00fc\3\2\2")
        buf.write("\2\64\u0107\3\2\2\2\66\u010c\3\2\2\28\u010e\3\2\2\2:\u0117")
        buf.write("\3\2\2\2<\u011a\3\2\2\2>\u011d\3\2\2\2@\u0122\3\2\2\2")
        buf.write("B\u0124\3\2\2\2D\u0127\3\2\2\2F\u0130\3\2\2\2H\u0137\3")
        buf.write("\2\2\2J\u013e\3\2\2\2L\u0140\3\2\2\2N\u014b\3\2\2\2P\u0156")
        buf.write("\3\2\2\2R\u0164\3\2\2\2T\u0169\3\2\2\2V\u016d\3\2\2\2")
        buf.write("X\u0179\3\2\2\2Z\u017b\3\2\2\2\\\u017d\3\2\2\2^\u0181")
        buf.write("\3\2\2\2`\u0188\3\2\2\2b\u018a\3\2\2\2d\u0191\3\2\2\2")
        buf.write("f\u0193\3\2\2\2h\u0195\3\2\2\2j\u019c\3\2\2\2l\u01a1\3")
        buf.write("\2\2\2n\u01a6\3\2\2\2pq\5\4\3\2qr\7\2\2\3r\3\3\2\2\2s")
        buf.write("t\5\6\4\2tu\5\4\3\2ux\3\2\2\2vx\5\6\4\2ws\3\2\2\2wv\3")
        buf.write("\2\2\2x\5\3\2\2\2y|\5\b\5\2z|\5\32\16\2{y\3\2\2\2{z\3")
        buf.write("\2\2\2|\7\3\2\2\2}\u0082\5\n\6\2~\u0082\5\f\7\2\177\u0082")
        buf.write("\5\16\b\2\u0080\u0082\5\22\n\2\u0081}\3\2\2\2\u0081~\3")
        buf.write("\2\2\2\u0081\177\3\2\2\2\u0081\u0080\3\2\2\2\u0082\t\3")
        buf.write("\2\2\2\u0083\u0084\5f\64\2\u0084\u0085\7\60\2\2\u0085")
        buf.write("\u0086\5\20\t\2\u0086\u0087\5l\67\2\u0087\13\3\2\2\2\u0088")
        buf.write("\u0089\7\t\2\2\u0089\u008a\7\60\2\2\u008a\u008b\7\26\2")
        buf.write("\2\u008b\u008c\5H%\2\u008c\u008d\5l\67\2\u008d\r\3\2\2")
        buf.write("\2\u008e\u008f\7\n\2\2\u008f\u0090\7\60\2\2\u0090\u0091")
        buf.write("\5\20\t\2\u0091\u0092\5l\67\2\u0092\17\3\2\2\2\u0093\u0094")
        buf.write("\7\26\2\2\u0094\u0097\5H%\2\u0095\u0097\3\2\2\2\u0096")
        buf.write("\u0093\3\2\2\2\u0096\u0095\3\2\2\2\u0097\21\3\2\2\2\u0098")
        buf.write("\u0099\5f\64\2\u0099\u009a\7\60\2\2\u009a\u009b\5\24\13")
        buf.write("\2\u009b\u009c\5\30\r\2\u009c\u009d\5l\67\2\u009d\23\3")
        buf.write("\2\2\2\u009e\u009f\7)\2\2\u009f\u00a0\5\26\f\2\u00a0\u00a1")
        buf.write("\7*\2\2\u00a1\25\3\2\2\2\u00a2\u00a3\7-\2\2\u00a3\u00a4")
        buf.write("\7+\2\2\u00a4\u00a7\5\26\f\2\u00a5\u00a7\7-\2\2\u00a6")
        buf.write("\u00a2\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7\27\3\2\2\2\u00a8")
        buf.write("\u00a9\7\26\2\2\u00a9\u00ac\5\\/\2\u00aa\u00ac\3\2\2\2")
        buf.write("\u00ab\u00a8\3\2\2\2\u00ab\u00aa\3\2\2\2\u00ac\31\3\2")
        buf.write("\2\2\u00ad\u00ae\7\13\2\2\u00ae\u00af\7\60\2\2\u00af\u00b0")
        buf.write("\5\34\17\2\u00b0\u00b1\5$\23\2\u00b1\u00b2\5l\67\2\u00b2")
        buf.write("\33\3\2\2\2\u00b3\u00b4\7\'\2\2\u00b4\u00b5\5\36\20\2")
        buf.write("\u00b5\u00b6\7(\2\2\u00b6\35\3\2\2\2\u00b7\u00ba\5 \21")
        buf.write("\2\u00b8\u00ba\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00b8")
        buf.write("\3\2\2\2\u00ba\37\3\2\2\2\u00bb\u00bc\5\"\22\2\u00bc\u00bd")
        buf.write("\7+\2\2\u00bd\u00be\5 \21\2\u00be\u00c1\3\2\2\2\u00bf")
        buf.write("\u00c1\5\"\22\2\u00c0\u00bb\3\2\2\2\u00c0\u00bf\3\2\2")
        buf.write("\2\u00c1!\3\2\2\2\u00c2\u00c3\5f\64\2\u00c3\u00c4\7\60")
        buf.write("\2\2\u00c4\u00ca\3\2\2\2\u00c5\u00c6\5f\64\2\u00c6\u00c7")
        buf.write("\7\60\2\2\u00c7\u00c8\5\24\13\2\u00c8\u00ca\3\2\2\2\u00c9")
        buf.write("\u00c2\3\2\2\2\u00c9\u00c5\3\2\2\2\u00ca#\3\2\2\2\u00cb")
        buf.write("\u00cc\5n8\2\u00cc\u00cd\5&\24\2\u00cd\u00d0\3\2\2\2\u00ce")
        buf.write("\u00d0\3\2\2\2\u00cf\u00cb\3\2\2\2\u00cf\u00ce\3\2\2\2")
        buf.write("\u00d0%\3\2\2\2\u00d1\u00d4\5> \2\u00d2\u00d4\5D#\2\u00d3")
        buf.write("\u00d1\3\2\2\2\u00d3\u00d2\3\2\2\2\u00d4\'\3\2\2\2\u00d5")
        buf.write("\u00e3\5*\26\2\u00d6\u00e3\5,\27\2\u00d7\u00e3\5\60\31")
        buf.write("\2\u00d8\u00e3\58\35\2\u00d9\u00e3\5:\36\2\u00da\u00e3")
        buf.write("\5<\37\2\u00db\u00dc\5> \2\u00dc\u00dd\5l\67\2\u00dd\u00e3")
        buf.write("\3\2\2\2\u00de\u00e3\5B\"\2\u00df\u00e0\5D#\2\u00e0\u00e1")
        buf.write("\5l\67\2\u00e1\u00e3\3\2\2\2\u00e2\u00d5\3\2\2\2\u00e2")
        buf.write("\u00d6\3\2\2\2\u00e2\u00d7\3\2\2\2\u00e2\u00d8\3\2\2\2")
        buf.write("\u00e2\u00d9\3\2\2\2\u00e2\u00da\3\2\2\2\u00e2\u00db\3")
        buf.write("\2\2\2\u00e2\u00de\3\2\2\2\u00e2\u00df\3\2\2\2\u00e3)")
        buf.write("\3\2\2\2\u00e4\u00e5\5\b\5\2\u00e5+\3\2\2\2\u00e6\u00e7")
        buf.write("\5.\30\2\u00e7\u00e8\7\26\2\2\u00e8\u00e9\5H%\2\u00e9")
        buf.write("\u00ea\5l\67\2\u00ea-\3\2\2\2\u00eb\u00f2\7\60\2\2\u00ec")
        buf.write("\u00ed\7\60\2\2\u00ed\u00ee\7)\2\2\u00ee\u00ef\5j\66\2")
        buf.write("\u00ef\u00f0\7*\2\2\u00f0\u00f2\3\2\2\2\u00f1\u00eb\3")
        buf.write("\2\2\2\u00f1\u00ec\3\2\2\2\u00f2/\3\2\2\2\u00f3\u00f4")
        buf.write("\7\21\2\2\u00f4\u00f5\7\'\2\2\u00f5\u00f6\5H%\2\u00f6")
        buf.write("\u00f7\7(\2\2\u00f7\u00f8\5n8\2\u00f8\u00f9\5(\25\2\u00f9")
        buf.write("\u00fa\5\64\33\2\u00fa\u00fb\5\66\34\2\u00fb\61\3\2\2")
        buf.write("\2\u00fc\u00fd\7\23\2\2\u00fd\u00fe\7\'\2\2\u00fe\u00ff")
        buf.write("\5H%\2\u00ff\u0100\7(\2\2\u0100\u0101\5n8\2\u0101\u0102")
        buf.write("\5(\25\2\u0102\63\3\2\2\2\u0103\u0104\5\62\32\2\u0104")
        buf.write("\u0105\5\64\33\2\u0105\u0108\3\2\2\2\u0106\u0108\3\2\2")
        buf.write("\2\u0107\u0103\3\2\2\2\u0107\u0106\3\2\2\2\u0108\65\3")
        buf.write("\2\2\2\u0109\u010a\7\22\2\2\u010a\u010d\5(\25\2\u010b")
        buf.write("\u010d\3\2\2\2\u010c\u0109\3\2\2\2\u010c\u010b\3\2\2\2")
        buf.write("\u010d\67\3\2\2\2\u010e\u010f\7\f\2\2\u010f\u0110\7\60")
        buf.write("\2\2\u0110\u0111\7\r\2\2\u0111\u0112\5H%\2\u0112\u0113")
        buf.write("\7\16\2\2\u0113\u0114\5H%\2\u0114\u0115\5n8\2\u0115\u0116")
        buf.write("\5(\25\2\u01169\3\2\2\2\u0117\u0118\7\17\2\2\u0118\u0119")
        buf.write("\5l\67\2\u0119;\3\2\2\2\u011a\u011b\7\20\2\2\u011b\u011c")
        buf.write("\5l\67\2\u011c=\3\2\2\2\u011d\u011e\7\b\2\2\u011e\u011f")
        buf.write("\5@!\2\u011f?\3\2\2\2\u0120\u0123\5H%\2\u0121\u0123\3")
        buf.write("\2\2\2\u0122\u0120\3\2\2\2\u0122\u0121\3\2\2\2\u0123A")
        buf.write("\3\2\2\2\u0124\u0125\5^\60\2\u0125\u0126\5l\67\2\u0126")
        buf.write("C\3\2\2\2\u0127\u0128\7\24\2\2\u0128\u0129\5l\67\2\u0129")
        buf.write("\u012a\5F$\2\u012a\u012b\7\25\2\2\u012bE\3\2\2\2\u012c")
        buf.write("\u012d\5(\25\2\u012d\u012e\5F$\2\u012e\u0131\3\2\2\2\u012f")
        buf.write("\u0131\3\2\2\2\u0130\u012c\3\2\2\2\u0130\u012f\3\2\2\2")
        buf.write("\u0131G\3\2\2\2\u0132\u0133\5J&\2\u0133\u0134\7%\2\2\u0134")
        buf.write("\u0135\5J&\2\u0135\u0138\3\2\2\2\u0136\u0138\5J&\2\u0137")
        buf.write("\u0132\3\2\2\2\u0137\u0136\3\2\2\2\u0138I\3\2\2\2\u0139")
        buf.write("\u013a\5L\'\2\u013a\u013b\5h\65\2\u013b\u013c\5L\'\2\u013c")
        buf.write("\u013f\3\2\2\2\u013d\u013f\5L\'\2\u013e\u0139\3\2\2\2")
        buf.write("\u013e\u013d\3\2\2\2\u013fK\3\2\2\2\u0140\u0141\b\'\1")
        buf.write("\2\u0141\u0142\5N(\2\u0142\u0148\3\2\2\2\u0143\u0144\f")
        buf.write("\4\2\2\u0144\u0145\t\2\2\2\u0145\u0147\5N(\2\u0146\u0143")
        buf.write("\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u0146\3\2\2\2\u0148")
        buf.write("\u0149\3\2\2\2\u0149M\3\2\2\2\u014a\u0148\3\2\2\2\u014b")
        buf.write("\u014c\b(\1\2\u014c\u014d\5P)\2\u014d\u0153\3\2\2\2\u014e")
        buf.write("\u014f\f\4\2\2\u014f\u0150\t\3\2\2\u0150\u0152\5P)\2\u0151")
        buf.write("\u014e\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0151\3\2\2\2")
        buf.write("\u0153\u0154\3\2\2\2\u0154O\3\2\2\2\u0155\u0153\3\2\2")
        buf.write("\2\u0156\u0157\b)\1\2\u0157\u0158\5R*\2\u0158\u015e\3")
        buf.write("\2\2\2\u0159\u015a\f\4\2\2\u015a\u015b\t\4\2\2\u015b\u015d")
        buf.write("\5R*\2\u015c\u0159\3\2\2\2\u015d\u0160\3\2\2\2\u015e\u015c")
        buf.write("\3\2\2\2\u015e\u015f\3\2\2\2\u015fQ\3\2\2\2\u0160\u015e")
        buf.write("\3\2\2\2\u0161\u0162\7\34\2\2\u0162\u0165\5R*\2\u0163")
        buf.write("\u0165\5T+\2\u0164\u0161\3\2\2\2\u0164\u0163\3\2\2\2\u0165")
        buf.write("S\3\2\2\2\u0166\u0167\7\30\2\2\u0167\u016a\5T+\2\u0168")
        buf.write("\u016a\5V,\2\u0169\u0166\3\2\2\2\u0169\u0168\3\2\2\2\u016a")
        buf.write("U\3\2\2\2\u016b\u016e\5b\62\2\u016c\u016e\5X-\2\u016d")
        buf.write("\u016b\3\2\2\2\u016d\u016c\3\2\2\2\u016eW\3\2\2\2\u016f")
        buf.write("\u017a\7-\2\2\u0170\u017a\7.\2\2\u0171\u017a\5Z.\2\u0172")
        buf.write("\u017a\5\\/\2\u0173\u017a\5^\60\2\u0174\u017a\7\60\2\2")
        buf.write("\u0175\u0176\7\'\2\2\u0176\u0177\5H%\2\u0177\u0178\7(")
        buf.write("\2\2\u0178\u017a\3\2\2\2\u0179\u016f\3\2\2\2\u0179\u0170")
        buf.write("\3\2\2\2\u0179\u0171\3\2\2\2\u0179\u0172\3\2\2\2\u0179")
        buf.write("\u0173\3\2\2\2\u0179\u0174\3\2\2\2\u0179\u0175\3\2\2\2")
        buf.write("\u017aY\3\2\2\2\u017b\u017c\t\5\2\2\u017c[\3\2\2\2\u017d")
        buf.write("\u017e\7)\2\2\u017e\u017f\5j\66\2\u017f\u0180\7*\2\2\u0180")
        buf.write("]\3\2\2\2\u0181\u0182\7\60\2\2\u0182\u0183\7\'\2\2\u0183")
        buf.write("\u0184\5`\61\2\u0184\u0185\7(\2\2\u0185_\3\2\2\2\u0186")
        buf.write("\u0189\5j\66\2\u0187\u0189\3\2\2\2\u0188\u0186\3\2\2\2")
        buf.write("\u0188\u0187\3\2\2\2\u0189a\3\2\2\2\u018a\u018b\5d\63")
        buf.write("\2\u018b\u018c\7)\2\2\u018c\u018d\5j\66\2\u018d\u018e")
        buf.write("\7*\2\2\u018ec\3\2\2\2\u018f\u0192\7\60\2\2\u0190\u0192")
        buf.write("\5^\60\2\u0191\u018f\3\2\2\2\u0191\u0190\3\2\2\2\u0192")
        buf.write("e\3\2\2\2\u0193\u0194\t\6\2\2\u0194g\3\2\2\2\u0195\u0196")
        buf.write("\t\7\2\2\u0196i\3\2\2\2\u0197\u0198\5H%\2\u0198\u0199")
        buf.write("\7+\2\2\u0199\u019a\5j\66\2\u019a\u019d\3\2\2\2\u019b")
        buf.write("\u019d\5H%\2\u019c\u0197\3\2\2\2\u019c\u019b\3\2\2\2\u019d")
        buf.write("k\3\2\2\2\u019e\u019f\7,\2\2\u019f\u01a2\5l\67\2\u01a0")
        buf.write("\u01a2\7,\2\2\u01a1\u019e\3\2\2\2\u01a1\u01a0\3\2\2\2")
        buf.write("\u01a2m\3\2\2\2\u01a3\u01a4\7,\2\2\u01a4\u01a7\5n8\2\u01a5")
        buf.write("\u01a7\3\2\2\2\u01a6\u01a3\3\2\2\2\u01a6\u01a5\3\2\2\2")
        buf.write("\u01a7o\3\2\2\2!w{\u0081\u0096\u00a6\u00ab\u00b9\u00c0")
        buf.write("\u00c9\u00cf\u00d3\u00e2\u00f1\u0107\u010c\u0122\u0130")
        buf.write("\u0137\u013e\u0148\u0153\u015e\u0164\u0169\u016d\u0179")
        buf.write("\u0188\u0191\u019c\u01a1\u01a6")
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
            self.decl_list()
            self.state = 111
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
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.decl()
                self.state = 114
                self.decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
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
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.variable_decl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
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
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.primitive_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.var_keyword_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.dynamic_keyword_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 126
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
            self.state = 129
            self.primitive_type()
            self.state = 130
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 131
            self.optional_init()
            self.state = 132
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
            self.state = 134
            self.match(ZCodeParser.VAR)
            self.state = 135
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 136
            self.match(ZCodeParser.ASSIGN)
            self.state = 137
            self.expression()
            self.state = 138
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
            self.state = 140
            self.match(ZCodeParser.DYNAMIC)
            self.state = 141
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 142
            self.optional_init()
            self.state = 143
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
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.match(ZCodeParser.ASSIGN)
                self.state = 146
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
            self.state = 150
            self.primitive_type()
            self.state = 151
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 152
            self.array_dimensions()
            self.state = 153
            self.optional_array_init()
            self.state = 154
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
            self.state = 156
            self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
            self.state = 157
            self.dimension_list()
            self.state = 158
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
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(ZCodeParser.NUMBER_LIT)
                self.state = 161
                self.match(ZCodeParser.COMMA)
                self.state = 162
                self.dimension_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
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
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(ZCodeParser.ASSIGN)
                self.state = 167
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
            self.state = 171
            self.match(ZCodeParser.FUNC)
            self.state = 172
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 173
            self.param_decl()
            self.state = 174
            self.optional_impl()
            self.state = 175
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
            self.state = 177
            self.match(ZCodeParser.LEFT_PAREN)
            self.state = 178
            self.param_list()
            self.state = 179
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
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
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
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.param()
                self.state = 186
                self.match(ZCodeParser.COMMA)
                self.state = 187
                self.param_list_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
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
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.primitive_type()
                self.state = 193
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.primitive_type()
                self.state = 196
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 197
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
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.nullable_newline_list()
                self.state = 202
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
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.return_stmt()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
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
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.variable_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.assignment_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 213
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 214
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 215
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 216
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 217
                self.return_stmt()
                self.state = 218
                self.nonempty_newline_list()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 220
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 221
                self.block_stmt()
                self.state = 222
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
            self.state = 226
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
            self.state = 228
            self.lhs_asmt()
            self.state = 229
            self.match(ZCodeParser.ASSIGN)
            self.state = 230
            self.expression()
            self.state = 231
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
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 235
                self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
                self.state = 236
                self.expr_list()
                self.state = 237
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
            self.state = 241
            self.match(ZCodeParser.IF)
            self.state = 242
            self.match(ZCodeParser.LEFT_PAREN)
            self.state = 243
            self.expression()
            self.state = 244
            self.match(ZCodeParser.RIGHT_PAREN)
            self.state = 245
            self.nullable_newline_list()
            self.state = 246
            self.statement()
            self.state = 247
            self.elif_list()
            self.state = 248
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
            self.state = 250
            self.match(ZCodeParser.ELIF)
            self.state = 251
            self.match(ZCodeParser.LEFT_PAREN)
            self.state = 252
            self.expression()
            self.state = 253
            self.match(ZCodeParser.RIGHT_PAREN)
            self.state = 254
            self.nullable_newline_list()
            self.state = 255
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
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.elif_stmt()
                self.state = 258
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
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.match(ZCodeParser.ELSE)
                self.state = 264
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
            self.state = 268
            self.match(ZCodeParser.FOR)
            self.state = 269
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 270
            self.match(ZCodeParser.UNTIL)
            self.state = 271
            self.expression()
            self.state = 272
            self.match(ZCodeParser.BY)
            self.state = 273
            self.expression()
            self.state = 274
            self.nullable_newline_list()
            self.state = 275
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
            self.state = 277
            self.match(ZCodeParser.BREAK)
            self.state = 278
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
            self.state = 280
            self.match(ZCodeParser.CONTINUE)
            self.state = 281
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
            self.state = 283
            self.match(ZCodeParser.RETURN)
            self.state = 284
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
            self.state = 288
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB, ZCodeParser.NOT, ZCodeParser.LEFT_PAREN, ZCodeParser.LEFT_SQUARE_BRACKET, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
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
            self.state = 290
            self.call_expr()
            self.state = 291
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
            self.state = 293
            self.match(ZCodeParser.BEGIN)
            self.state = 294
            self.nonempty_newline_list()
            self.state = 295
            self.stmt_list()
            self.state = 296
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
            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.statement()
                self.state = 299
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
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.expr1()
                self.state = 305
                self.match(ZCodeParser.CONCAT)
                self.state = 306
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
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
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.expr2(0)
                self.state = 312
                self.rel_op()
                self.state = 313
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
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
            self.state = 319
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 326
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 321
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 322
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 323
                    self.expr3(0) 
                self.state = 328
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
            self.state = 330
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 337
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 332
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 333
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 334
                    self.expr4(0) 
                self.state = 339
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
            self.state = 341
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 348
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 343
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 344
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 345
                    self.expr5() 
                self.state = 350
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
            self.state = 354
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.match(ZCodeParser.NOT)
                self.state = 352
                self.expr5()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB, ZCodeParser.LEFT_PAREN, ZCodeParser.LEFT_SQUARE_BRACKET, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
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
            self.state = 359
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.match(ZCodeParser.SUB)
                self.state = 357
                self.expr6()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LEFT_PAREN, ZCodeParser.LEFT_SQUARE_BRACKET, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
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
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.index_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
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
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.match(ZCodeParser.NUMBER_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.match(ZCodeParser.STRING_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 367
                self.boolean_lit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 368
                self.array_lit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 369
                self.call_expr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 370
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 371
                self.match(ZCodeParser.LEFT_PAREN)
                self.state = 372
                self.expression()
                self.state = 373
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
            self.state = 377
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
            self.state = 379
            self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
            self.state = 380
            self.expr_list()
            self.state = 381
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
            self.state = 383
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 384
            self.match(ZCodeParser.LEFT_PAREN)
            self.state = 385
            self.argument_list()
            self.state = 386
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
            self.state = 390
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB, ZCodeParser.NOT, ZCodeParser.LEFT_PAREN, ZCodeParser.LEFT_SQUARE_BRACKET, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
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
            self.state = 392
            self.expr_for_indexing()
            self.state = 393
            self.match(ZCodeParser.LEFT_SQUARE_BRACKET)
            self.state = 394
            self.expr_list()
            self.state = 395
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
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
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
            self.state = 401
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
            self.state = 403
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
            self.state = 410
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.expression()
                self.state = 406
                self.match(ZCodeParser.COMMA)
                self.state = 407
                self.expr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
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
            self.state = 415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.match(ZCodeParser.NEWLINE)
                self.state = 413
                self.nonempty_newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 414
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
            self.state = 420
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.match(ZCodeParser.NEWLINE)
                self.state = 418
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
         




