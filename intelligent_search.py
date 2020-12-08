while True:
    n = input("Enter query")
    if n == "EXIT":
        print("Exiting")
        break
    m = input("Enter 2nd query")
    sentence = [n,m]

    print(sentence)

    tokenizer = FullTokenizer(vocab_file="/content/drive/MyDrive/EY_DATA/vocab.txt")

    pred_tokens = map(tokenizer.tokenize, sentence)
    pred_tokens = map(lambda tok: ["[CLS]"] + tok + ["[SEP]"], pred_tokens)
    pred_token_ids = list(map(tokenizer.convert_tokens_to_ids, pred_tokens))
    
    max_seq_len=128

    pred_token_ids = map(lambda tids: tids +[0]*(max_seq_len-len(tids)),pred_token_ids)
    pred_token_ids = np.array(list(pred_token_ids))

    # print(type(pred_token_ids))

    

    predictions = new_model.predict(pred_token_ids).argmax(axis=-1)

    intents_we_came_across = []
    for text, label in zip(sentence, predictions):
        # print("text:", text, "\nintent:", classes[label])
        intents_we_came_across.append(classes[label])
        print()

    for count in range(len(intents_we_came_across)):
        file_loc.append(filename)
        file_name.append(filename.split("/")[-1])
        intent.append(intents_we_came_across[count])
    
    print(intent)

    df = pd.read_csv("/content/test_data_from_crawler.csv", encoding = "utf-8-sig")
    # df = df.drop_duplicates(subset ="File Name") 
    # df.head()
    for word in intents_we_came_across:
        for i in range(len(df['Intent'])):
            if df['Intent'][i]==word:
                print(df["File Name"][i])
                print(df["File Location"][i])
                print()