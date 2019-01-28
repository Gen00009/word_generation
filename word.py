from gensim.models import word2vec
import re
model = word2vec.Word2Vec.load('wiki.pkl')

while True:
	input_num = input("入力する語数を1,2,3で入力してください :")
	if input_num == "1":
		youso = input("要素を入力してください: ")
		sim = model.most_similar(positive = [youso])
		sim_text = str(sim)
		result = re.sub(r'[!-~]', "", sim_text)
		print(result)
	elif input_num == "2":
		youso = input("1語目を入力してください: ")
		youso2 = input("2語目を入力してください: ")
		sim = model.most_similar(positive = [youso,youso2])
		sim_text = str(sim)
		result = re.sub(r'[!-~]', "", sim_text)
		print(result)
	elif input_num == "3":
		youso = input("1語目を入力してください: ")
		youso2 = input("2語目を入力してください: ")
		youso3 = input("3語目を入力してください: ")
		sim = model.most_similar(positive = [youso,youso2,youso3])
		sim_text = str(sim)
		result = re.sub(r'[!-~]', "", sim_text)
		print(result)
	else:
		break