

with open(r"C:/Users/Alean/TurtleArt/Input/Names/invited_names.txt") as names:
    list_names_unprocessed=names.readlines()
    list_names=list(list_names_unprocessed)
    for n in range(len(list_names)):
        list_names[n]=list_names[n].strip()


a=0
print(list_names)
with open(r"C:/Users/Alean/TurtleArt/Input/Letters/starting_letter.txt",mode='r+') as file:
    conteudo_original=file.readlines(0)
    conteudo=conteudo_original
    correct_entry=[[] for n in range(len(list_names))]

    for n in range(len(list_names)):
        correct_entry[n].append(conteudo[0].replace('[name]',list_names[n]))
    carta_correta=''
    list_with_all_letters=[]
    for documentos in range(len(correct_entry)):
        conteudo_original[0]=conteudo_original[0].replace(conteudo_original[0],correct_entry[documentos][0])
        carta_correta=''.join(conteudo_original)
        list_with_all_letters.append(carta_correta)
    for cartas in range(len(list_with_all_letters)):
        list_with_all_letters[cartas]=list_with_all_letters[cartas].replace("\n",'')
    for documentos in range(len(list_names)):
        with open(r'C:\Users\Alean\TurtleArt\Input\Letters\Letter_for_'+list_names[documentos],mode='w')as new_letters:
            new_letters.write(list_with_all_letters[documentos])




