// This file has been modified by me. There is no need to modify it because you do not submit it.
// This file may also be outdated. Please request the latest version of this file from lecturers/TAs.
import java.io.*;
import java.io.IOException;

public class io {
    public static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    public static Writer writer = new BufferedWriter(new OutputStreamWriter(System.out));
    
    /**
     * read a number from the standard input
     * @return the number read from the standard input
     */
    public static float readNumber() {
        String tmp = "";
        try {
            tmp = input.readLine();
            return Float.parseFloat(tmp);
        }
        catch (IOException e) {
            e.printStackTrace();
        }
        catch (NumberFormatException e) {
            e.printStackTrace();
        }
        return 0.0F;
    }
    
    /**
     * print the value of the float n to the standard output
     * @param n the floating-point value to be printed out
     */
    public static void writeNumber(float n) {
        System.out.print(n + "");
    }
    
    /**
     * read a boolean value from the standard input
     * @return the boolean value read from the standard input
     */
    public static boolean readBool() {
        String tmp = "";
        try {
            tmp = input.readLine();
            if (tmp.equalsIgnoreCase("true"))
                return true;
            else
                return false;
        } catch (IOException e) {
            e.printStackTrace();
        }
        return false;
    }
    
    /**
     * print the value of the boolean b to the standard output
     * @param b the boolean value to be printed out
     */
    public static void writeBool(boolean b)  {
        System.out.print(b + "");
    }
    
    /**
     * read a string from the standard input
     * @return the string value read from standard input
     */
    public static String readString() {
        String tmp = "";
        try {
            tmp = input.readLine();
            return tmp;
        }
        catch (IOException e) {
            e.printStackTrace();
        }
        return tmp;
    }
    
    /**
     * print the value of the string s to the standard output
     * @param s the string to be printed out
     */
    public static void writeString(String s) {
        System.out.print(s);
    }
    
    public static void close() {
        try {
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
