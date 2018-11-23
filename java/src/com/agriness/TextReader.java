package com.agriness;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.FileReader;

public class TextReader {

    public static final void main(String[] args){
        try {
            String filePath = "/Users/alexandre/tech-day/info.txt";
            BufferedReader buff = new BufferedReader(new FileReader(filePath));
            String line;
            while((line = buff.readLine()) != null){
                System.out.println(line);
            }

        }catch (IOException ioe){
            ioe.printStackTrace();
        }
    }
}
