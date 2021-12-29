//package project;

import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

public class javaProject {
    public static void readFile(String RFname, ArrayList<String> str) throws IOException{   //read data from file
        try {
            FileReader in = new FileReader(RFname + ".txt");
            BufferedReader buff = new BufferedReader(in);
            String line = "";

            while((line=buff.readLine())!=null){
                str.add(line);
            }
            buff.close();

        } catch (FileNotFoundException e) {         //exit if file not found
            System.out.println("Open failed.");
            System.exit(0);
        }
    }

    public static void writeFile(String WFname, ArrayList<String> str) throws IOException{  //output data into a new file
        FileWriter out = new FileWriter(WFname + ".txt");
        for(String s: str) {
            out.write(s);
            out.write("\r\n");
        }
        out.close();
        System.out.println("File saved.");
    }

    public static void LSDsort(ArrayList<String> str, int x) {      //perform LSD sorting algo
        int ascii = 128;                            //total number of ASCII
        int size = str.size();                      //total number of string in the file(array list)
        String[] newList = new String[size];        //array for sorted string

        for(int i = x - 1; i >= 0; i--) {           //loop for sorting string from last letter to the first
            int[] count = new int[ascii + 1];       //array for frequency of letter

            for(int j = 0; j < size; j++)           //get frequency
                count[str.get(j).charAt(i) + 1]++;

            for(int j = 0; j < ascii; j++)          //compute cumulates
                count[j + 1] += count[j];

            for(int j = 0; j < size; j++)           //move data
                newList[count[str.get(j).charAt(i)]++] = str.get(j);

            for(int j = 0; j < size; j++)           //copy back sorted string
                str.set(j, newList[j]);
        }
    }

    public static void main(String[] args) throws IOException{      //main
        ArrayList<String> str = new ArrayList<>();
		long startTime = 0;
        long endTime = 0;
        long timeElapsed;
		
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter text file name to read data: ");
        String RFname = sc.nextLine();

        readFile(RFname, str);          //read data from file

        System.out.println("\nDo you want to proceed LSD sorting? (YES/NO)");
        String choice = sc.nextLine();
        if(choice.toUpperCase().equals("YES") || choice.toUpperCase().equals("Y")) {
            startTime = System.nanoTime();                          //execution starts
            LSDsort(str, 5);                                     	//perform LSD sorting algo
            endTime = System.nanoTime();                            //execution ends
        }
        else
            System.exit(0);

        System.out.println("\nEnter a new text file name for sorted list: ");
        String WFname = sc.nextLine();

        writeFile(WFname, str);         //output data into a new file
        sc.close();
		
		timeElapsed = endTime - startTime;							//print execution time
        System.out.println("Execution time in nanoseconds: " + timeElapsed);   
    }
}

