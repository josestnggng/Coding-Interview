class StringCompression {
    public static String compress(String str) {
        StringBuilder compressed = new StringBuilder();
        int countConsecutive = 0;
        for (int i = 0; i < str.length(); i++) {
            countConsecutive++;
            // If next character is different than current, append this char to result.
            if (i + 1 >= str.length() || str.charAt(i) != str.charAt(i + 1)) {
                compressed.append(str.charAt(i));
                compressed.append(countConsecutive);
                countConsecutive = 0;
            }
        }

        return (str.length() < compressed.length()) ? str : compressed.toString();
    }

    public static void main(String[] args) {
        System.out.println(compress("aabcccccaaa"));
        System.out.println(compress("ababacccc"));
        System.out.println(compress("aaaaaa"));
        System.out.println(compress("a"));
    }
}