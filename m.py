# # import re
# # import pickle
# # from collections import defaultdict
# # from hazm import Normalizer

# # def read_corpus(corpus_path):
# #     with open(corpus_path, 'r', encoding='utf-8') as file:
# #         return file.read()

# # def read_stop_words(stop_words_path):
# #     with open(stop_words_path, 'r', encoding='utf-8') as file:
# #         return file.read().splitlines()

# # def remove_stop_words(text, stop_words):
# #     return ' '.join([word for word in text.split() if word not in stop_words])

# # def normalize(text):
# #     normalizer = Normalizer()
# #     return normalizer.normalize(text)

# # def create_inverted_index(corpus, stop_words):
# #     inverted_index = defaultdict(list)
# #     terms = set()
# #     for i, line in enumerate(corpus.splitlines()):
# #         line = normalize(line)
# #         for term in re.findall(r'\b\w+\b', line):
# #             if term not in stop_words:
# #                 inverted_index[term].append((i, line.find(term)))
# #                 terms.add(term)
# #     return sorted(terms), inverted_index

# # def print_inverted_index(inverted_index):
# #     for term, postings in inverted_index.items():
# #         print(f'Term: {term}')
# #         for posting in postings:
# #             print(f'Document ID: {posting[0]}, Position: {posting[1]}')
# #         print('-------------------')

# # corpus_path = 'Urdu Corpus/Current Affairs1.txt'
# # stop_words_path = '/home/hp/Desktop/IR/A1/urdu_stopwords.txt'
# # index_path = 'term_list.txt'
# # postings_path = 'postings.bin'

# # corpus = read_corpus(corpus_path)
# # stop_words = read_stop_words(stop_words_path)
# # corpus_without_stop_words = remove_stop_words(corpus, stop_words)
# # terms, inverted_index = create_inverted_index(corpus_without_stop_words, stop_words)


# # # Print the inverted index before saving to disk
# # print_inverted_index(inverted_index)

# # # Save the index to disk
# # # save_index_to_disk(terms, inverted_index, index_path, postings_path)

# import os
# import re
# import pickle
# from collections import defaultdict
# from hazm import Normalizer

# def read_corpus(corpus_path):
#     with open(corpus_path, 'r', encoding='utf-8') as file:
#         return file.read()

# def read_stop_words(stop_words_path):
#     with open(stop_words_path, 'r', encoding='utf-8') as file:
#         return file.read().splitlines()

# def remove_stop_words(text, stop_words):
#     return ' '.join([word for word in text.split() if word not in stop_words])

# def normalize(text):
#     try:
#         normalizer = Normalizer()
#         return normalizer.normalize(text)
#     except Exception as e:
#         print(f"Error normalizing text: {e}")
#         return text

# def create_inverted_index(corpus_folder, stop_words):
#     inverted_index = defaultdict(list)
#     terms = set()

#     for filename in os.listdir(corpus_folder):
#         file_path = os.path.join(corpus_folder, filename)
#         with open(file_path, 'r', encoding='utf-8') as file:
#             document = file.read()
#             document_without_stop_words = remove_stop_words(document, stop_words)
#             for i, line in enumerate(document_without_stop_words.splitlines()):
#                 line = normalize(line)
#                 for term in re.findall(r'\b\w+\b', line):
#                     if term not in stop_words:
#                         inverted_index[term].append((filename, i, line.find(term)))
#                         terms.add(term)

#     return sorted(terms), inverted_index

# def save_index_to_disk(terms, inverted_index, index_path, postings_path):
#     with open(index_path, 'w', encoding='utf-8') as index_file, open(postings_path, 'wb') as postings_file:
#         for term in terms:
#             index_file.write(f'{term}\t{len(inverted_index[term])}\n')
#             pickle.dump(inverted_index[term], postings_file)

# def print_inverted_index(inverted_index):
#     for term, postings in inverted_index.items():
#         print(f'Term: {term}')
#         for posting in postings:
#             print(f'Document ID: {posting[0]}, Line: {posting[1]}, Position: {posting[2]}')
#         print('-------------------')

# corpus_folder = 'Urdu Corpus'
# stop_words_path = '/home/hp/Desktop/IR/A1/urdu_stopwords.txt'
# index_path = 'term_list.txt'
# postings_path = 'postings.bin'

# stop_words = read_stop_words(stop_words_path)
# terms, inverted_index = create_inverted_index(corpus_folder, stop_words)

# # Print the inverted index before saving to disk
# print_inverted_index(inverted_index)

# # Save the index to disk
# save_index_to_disk(terms, inverted_index, index_path, postings_path)
