package wordCountTool;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class WordCount {
    public void fileSize(String filepath) {
        File file = new File(filepath);
        if(file.exists())
            System.out.println(file.length() + " " + filepath);
        else    
            System.out.println("File does not exists");
    }

    public void lineCount(String filePath) throws IOException {
        File file = new File(filePath);
            if(file.exists()) {
                try {
                    BufferedReader reader;
                    reader = new BufferedReader(new FileReader(file.getName()));
                    int lines = 0;
                    while (reader.readLine() != null) 
                        lines++;
                    System.out.println("Line Count: "+ lines +" " +filePath);
                    reader.close();
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                }

            }
            else    
                System.out.println("File does not exists");
    }

    public void wordCount(String filepath) throws IOException {
        File file = new File(filepath);
            if(file.exists()) {
                try {
                    BufferedReader reader;
                    reader = new BufferedReader(new FileReader(file.getName()));
                    int word = 0;
                    String line = reader.readLine();
                    while (line != null) {
                        String[] words = line.split(" ");
                        word = word + words.length;
                        line = reader.readLine();
                    }
                    System.out.println("Word Count: "+ word +" " +filepath);
                    reader.close();
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                }

            }
            else    
                System.out.println("File does not exists");
        }

    public void characterCount(String filepath) throws IOException {
        File file = new File(filepath);
            if(file.exists()) {
                try {
                    BufferedReader reader;
                    reader = new BufferedReader(new FileReader(file.getName()));
                    int character = 0;
                    String line = reader.readLine();
                    while (line != null) {
                        character = character + line.length();
                        line = reader.readLine();
                    }
                    System.out.println("Character Count: "+ character +" " +filepath);
                    reader.close();
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                }

            }
            else    
                System.out.println("File does not exists");
    }
    public static void main(String[] args) {
        if(args[0].equals("-c")) {
            WordCount wc = new WordCount();
            wc.fileSize(args[1]);
        }
        else if(args[0].equals("-l")) {
            WordCount wc = new WordCount();
            try {
                wc.lineCount(args[1]);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        else if(args[0].equals("-w")) {
            WordCount wc = new WordCount();
            try {
                wc.wordCount(args[1]);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        else if(args[0].equals("-m")) {
            WordCount wc = new WordCount();
            try {
                wc.characterCount(args[1]);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        else if (args[0]!="") {
            WordCount wc = new WordCount();
            try {
                wc.fileSize(args[0]);
                wc.lineCount(args[0]);
                wc.wordCount(args[0]);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        else if(args[0]!="")
        {
            System.out.println("Invalid Input");
        }

    }
    
}