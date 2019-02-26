class StringCompression {
    public static String compress(String str) {
        int final_length = countCompression(str);
        if (final_length > str.length())
            return str;

        StringBuilder compressed = new StringBuilder(final_length);
        int count_consecutive = 0;
        for (int i = 0; i < str.length(); i++) {
            count_consecutive++;
            // If next character is different than current, append this char to result.
            if (i + 1 >= str.length() || str.charAt(i) != str.charAt(i + 1)) {
                compressed.append(str.charAt(i));
                compressed.append(count_consecutive);
                count_consecutive = 0;
            }
        }

        return (str.length() < compressed.length()) ? str : compressed.toString();
    }

    public static int countCompression(String str) {
        int count_consecutive = 0;
        int compressed_length = 0;
        for (int i = 0; i < str.length(); i++) {
            count_consecutive++;
            // If next character is different than current, append this char to result.
            if (i + 1 >= str.length() || str.charAt(i) != str.charAt(i + 1)) {
                compressed_length += 1 + String.valueOf(count_consecutive).length();
                count_consecutive = 0;
            }
        }
        return compressed_length;
    }

    public static void main(String[] args) {
        System.out.println(compress("aabcccccaaa"));
        System.out.println(compress("ababacccc"));
        System.out.println(compress("aaaaaa"));
        System.out.println(compress("a"));
    }
}