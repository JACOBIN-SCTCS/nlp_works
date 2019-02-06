import parser.tokenizer as tk 


def main():
    print("\tELIZA LIKE CHATBOT\n")
    print("Enter exit at any time to quit the program")

    while(1):
        user_input = raw_input("\n>>")
        tokens = tk.word_tokenize(user_input)

        if 'EXIT' in tokens or 'exit' in tokens:
            break 
        
        print(tokens)
        

            

        

if __name__ == "__main__":
    main()
