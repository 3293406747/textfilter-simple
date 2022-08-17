class TextFilter:

	def __init__(self):
		self.seq = list()

	def parse(self,path):
		with open(path, encoding="utf-8") as f:
			for keyword in f.readlines():
				self.add(keyword.strip())

	def add(self,keyword):
		if isinstance(keyword,str):
			self.seq.append(keyword)

	def filter(self,message:str,repl="*"):
		if isinstance(message,str):
			message = message.lower()
			for i in self.seq:
				message = message.replace(i,repl*len(i))
		return message


if __name__ == '__main__':
	t = TextFilter()
	t.parse("keywords")
	print(t.filter("过滤:法论功"))