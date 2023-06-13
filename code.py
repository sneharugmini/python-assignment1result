#This code will count the frequency of each word in the sample.txt file in the directory. I will do so by using the code to first split the entire content of the file into words after which I will count the frequency of each word. The code will then arrange each word with its frequency side by side which you can find after running the code which will display a message in the terminal to show that it worked and you can find a file called word_count in the directory with is newly made after you run the code.
from collections import Counter

def count_word_frequency(file_path):
    
    with open(file_path, 'r') as file: #file being opened in read mode.
        words = file.read().split() #splitting the content into words
        word_count = Counter(words) #counting how many times a word occurs.
    return word_count

def save_word_frequency_report(word_count, report_file):
    with open(report_file, 'w') as file: #file being opened in write mode.
        file.write("Word\t\tFrequency\n") #heading
        for word, count in word_count.most_common():
            file.write(f"{word}\t|\t{count}\n") #each word with its frequency 

            #printing message to show that it worked and where to find the result.
    print("Word count recorded successfully in a file called word_count located in the directory.")

file_path = "sample.txt"  #showing path of the sample text
report_file = "word_count.txt"  #path of the result

word_count = count_word_frequency(file_path) #counting frequency
save_word_frequency_report(word_count, report_file) #saving it to file



