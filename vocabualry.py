# def prefix_un(word1):
#     return ("un"+word1)
# def add_prefix_to_word_group(vocab_words):
#     return("::",vocab_words[0].join(vocab_words))
# def remove_suffix(word):
#     return
#     suffix="ness"
#     res=(word.removesuffix(suffix))
#     if res.endswith("i"):
#         print(res.replace(res[-1],"y"))
#     else:
#         print(res)
# def adjective_to_verb(sentence,index):
#     return sentence.split()[index].strip(".")+'en'
# while True:

#     word1=str(input("enter the word:"))
#     print(prefix_un(word1))
#     break
#     vocab_words=str(input("enter the word :"))
#     print(vocab_words)
#     break
#     word=str(input("enter the word:"))
#     print(remove_suffix)
#     break
#     sentence=str(input("enter the sentence"))
#     index=int(input("enter its index"))
#     print(adjective_to_verb)
# name=input("enter the name: ")
# if name==" ":
#     print("one for you, one for me")
# else:
#     print(f"one for {name}, one for me")
# def two_fer(name):
#     return f"one for {name}, one for me"
# def two_fer1(name=None):
#     return f"one for you, one for me"

# name=input("enter the name")
# if name==" ":
#     print(two_fer1())
# else:
#     print(two_fer(name))
# def convert(number):
#     for i in range(1,number+1):
#         factor=number%i
#         if factor==0:
#             if i==3 and i==5:
#                 print("plingplang")
#             if i==3:
#                 print("pling")
#             if i==5:
#                 print("plang")
#             if i==7:
#                 print("plong")
# convert(15)
def convert(number):
    output = ""

    if number % 3 == 0:
        output += "pling"
    if number % 5 == 0:
        output += "plang"
    if number % 7 == 0:
        output += "plong"
    if output== "":
        return str(number)
    
    return output
print(convert(105))
