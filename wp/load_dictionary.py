import pickle
import dictionary_trie

English = dictionary_trie.Dictionary()
source = open('words.txt','r')
count = 0
for line in source:
	count += 1
	line = line.strip()
	English.addWord(line)
	#print(line, count)

english = open('english.chow','wb')
english_struct = open('english_struct.chow','wb')
marker = open('marker.chow','wb')
pickle.dump(dictionary_trie.marker,marker)
pickle.dump(dictionary_trie.table,english)
pickle.dump(English,english_struct)
english_struct.close()
english.close()
marker.close()