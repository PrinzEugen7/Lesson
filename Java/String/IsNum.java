// 方法1
public boolean isNum1(String s) {
    return Pattern.compile("^-?[0-9]+$").matcher(s).find();
}

// 方法2
public boolean isNum2(String s) {
    try {
        Integer.parseInt(s);
        return true;
    } catch (NumberFormatException e) {
        return false;
    }
}

System.out.println(isNum1("fgo")); // false
System.out.println(isNum2("10"));  // true
