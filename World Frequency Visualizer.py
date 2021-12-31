'''
    Asked to refactor the code
    It was somebody's project

    !!! Old code below !!!
'''

# Word Frequency Visualizer

# Importing
import re
import matplotlib.pyplot as plt # Notice, to use matplotlib library you need first install it

# Input, Create empty dictionary
file_name = input(r'Enter the name of the file (format: C:\Folder_name\file_name.txt): ') # Or if the file in the same directory you can just type it name with the extension(.txt)
dict_of_words = dict()

# Read file
with open(file_name, 'r') as file:
    # Use re module to replace . , ? ! by '' (Nothing)
    clear_text = re.sub('[.?,!]', '', (file.read())) # [.?,!] this regular expression means "If you face any of this elements replace them by '' (Nothing)"

# Create total_words variable
total_words = 0

# Append word in dicteonary
for word in clear_text.split():
    if word.isalpha(): # isalpha() chackes that word consists only of letters
        total_words += 1
        if word in dict_of_words:
            dict_of_words[word] += 1
        else:
            dict_of_words[word] = 1

sort = sorted(dict_of_words.items(), key = lambda x: x[1], reverse=True)[:20] # We sort our dict_of_words by number of repetitions and take only 20 firsts
words, count = [0] * 20, [0] * 20 # We create two static arrays with number of 20 elements
for j, i in enumerate(sort): # j is index, i is value
    words[j], count[j] = i[0], i[1]
        

print(f'The total number of words in the text: {total_words}')

plt.title('The most frequent words in the text')
plt.barh(words, count)
plt.show()

'''-------------------------------------------------------------------------------------------------------------'''

# # Word Frequency Visualizer

# import operator
# import matplotlib.pyplot as plt


# filename = input('Enter the name of the file (example: text.txt): ')
# word_count = dict()
# not_counted_characters = '1234567890`~!@"#№;$%^:&?*()-–_+=[]{}\\|/<>,.\n'


# with open(filename, 'r') as f:
#     lines = f.readlines()

    
# for line in lines:
#     new_line = str()
#     for character in line:
#         if character not in not_counted_characters:
#             new_line += character.lower()
#         else:
#             continue        
#     words = new_line.split()
#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1

# sort = sorted(word_count.items(), key = operator.itemgetter(1))

# filtered_vals = [v for _, v in dict(sort).items() if v != 0]

# total_words = sum(filtered_vals)
# word_y = []
# frequency_x = []
# for y, x in sort:
#     if total_words < 1000000 and total_words > 750000:
#         if x > 4250:
#             word_y.append(y)
#             frequency_x.append(x)
#         else:
#             continue
#     elif total_words < 750000 and total_words > 500000:
#         if x > 2000:
#             word_y.append(y)
#             frequency_x.append(x)
#         else:
#             continue
#     elif total_words < 500000 and total_words > 100000:
#         if x > 1000:
#             word_y.append(y)
#             frequency_x.append(x)
#         else:
#             continue
#     elif total_words < 100000 and total_words > 50000:
#         if x > 500:
#             word_y.append(y)
#             frequency_x.append(x)
#         else:
#             continue
#     elif total_words < 50000 and total_words > 10000:
#         if x > 250:
#             word_y.append(y)
#             frequency_x.append(x)
#         else:
#             continue
#     elif total_words < 10000 and total_words > 5000:
#         if x > 100:
#             word_y.append(y)
#             frequency_x.append(x)
#         else:
#             continue
#     elif total_words < 5000 and total_words > 1000:
#         if x > 50:
#             word_y.append(y)
#             frequency_x.append(x)
#         else:
#             continue
#     elif total_words < 1000 and total_words > 500:
#         if x > 10:
#             word_y.append(y)
#             frequency_x.append(x)
#         else:
#             continue
#     elif total_words < 500 and total_words > 250:
#         if x > 3:
#             word_y.append(y)
#             frequency_x.append(x)
#         else:
#             continue        
#     else:
#         if x > 1:
#             word_y.append(y)
#             frequency_x.append(x)
#         else:
#             continue

        
# print('The total number of words in the text: '+str(total_words)+'')
# plt.style.use('fivethirtyeight')
# plt.barh(word_y, frequency_x)
# plt.title('The most frequent words in the text')
# plt.ylabel('Words')
# plt.xlabel('Frequency')
# plt.tight_layout()
# plt.show()
