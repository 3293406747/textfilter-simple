class TextFilter:
	""" 敏感词过滤 """
	def __init__(self):
		self.array = []

	def parse(self, fileName):
		with open(fileName, encoding="utf-8") as f:
			for keyword in f.readlines():
				self.add(keyword.strip())

	def add(self,keyword):
		if isinstance(keyword,str):
			return self.array.append(keyword)
		raise ValueError

	def filter(self,message:str,repl="*"):
		if isinstance(message,str):
			message = message.lower()
			for i in self.array:
				message = message.replace(i,repl*len(i))
			return message
		raise ValueError


if __name__ == '__main__':
	tf = TextFilter()
	tf.parse("keywords")
	print(tf.filter("拒绝法论功，拒绝黄赌毒"))