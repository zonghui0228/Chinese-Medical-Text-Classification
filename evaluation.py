#! python3
# *_* coding: utf-8 *_*

# a script to evaluate the performance of criteria classification model results.

# >>input
	# test_file, predict_file

# >>output
	# macro f1 score

import codecs

class evaluation:
	def __init__(self, test_file, predict_file):
		self.test_results = []
		with codecs.open(test_file, 'r', encoding="utf-8") as f1:
			for line in f1:
				self.test_results.append(line.strip().split('\t')[1])
		self.predict_results = []
		with codecs.open(predict_file, 'r', encoding="utf-8") as f2:
			for line in f2:
				self.predict_results.append(line.strip().split('\t')[1])

		self.category = sorted(list(set(self.test_results)))
		self.get_tp_tn_fp_fn()
		self.caculate_precision_recall_f1()
		self.caculate_macrof1()
		self.print_result()

	def get_tp_tn_fp_fn(self):
		# count tp, tn, fp, fn for each category.
		self.evaluation_results = {c:{} for c in self.category}
		for c in self.category:
			self.evaluation_results[c]["tp"] = 0
			self.evaluation_results[c]["tn"] = 0
			self.evaluation_results[c]["fp"] = 0
			self.evaluation_results[c]["fn"] = 0
		for c in self.category:
			for i in range(len(self.test_results)):
				c1 = self.test_results[i]
				c2 = self.predict_results[i]
				if c1 == c and c2 == c:
					self.evaluation_results[c]["tp"] += 1
				if c1 != c and c2 != c:
					self.evaluation_results[c]["tn"] += 1
				if c1 == c and c2 != c:
					self.evaluation_results[c]["fn"] += 1
				if c1 != c and c2 == c:
					self.evaluation_results[c]["fp"] += 1

	def caculate_precision_recall_f1(self):
		# caculate precision, recall, f1 for each category
		for c in self.category:
			try:
				precision = float(self.evaluation_results[c]["tp"]) / (self.evaluation_results[c]["tp"] + self.evaluation_results[c]["fp"])
			except ZeroDivisionError:
				precision = 0.0
			try:
				recall = float(self.evaluation_results[c]["tp"]) / (self.evaluation_results[c]["tp"] + self.evaluation_results[c]["fn"])
			except ZeroDivisionError:
				recall = 0.0
			try:
				f1 = (2 * precision * recall) / (precision + recall)
			except ZeroDivisionError:
				f1 = 0.0
			self.evaluation_results[c]["precision"] = precision
			self.evaluation_results[c]["recall"] = precision
			self.evaluation_results[c]["f1-score"] = f1

	def caculate_macrof1(self):
		self.precision_macro = sum([self.evaluation_results[c]["precision"] for c in self.evaluation_results]) / len(self.category)
		self.recall_macro = sum([self.evaluation_results[c]["recall"] for c in self.evaluation_results]) / len(self.category)
		self.F_macro = sum([self.evaluation_results[c]["f1-score"] for c in self.evaluation_results]) / len(self.category)

	def print_result(self):
		print("{0:<40s} {1:<10s} {2:<10s} {3:<10s}".format("category", "precision", "recall", "F1"))
		for c in self.category:
			print("{0:<40s} {1:<10f} {2:<10f} {3:<10f}".format(c, self.evaluation_results[c]["precision"], self.evaluation_results[c]["recall"], self.evaluation_results[c]["f1-score"]))
		print("{0:s} {1:<10f} {2:s} {3:<10f} {4:s} {5:<10f}".format("macro_precision:", self.precision_macro, "macro_recall:", self.recall_macro, "macro_F1:", self.F_macro))

if __name__ == "__main__":
	import sys
	test_gold = sys.argv[1]
	test_predict = sys.argv[2]
	
	# test_gold = "./data/test.gold"
	# test_predict = "./data/test.predict"
	eva = evaluation(test_gold, test_predict)
	evaluation_results = eva.evaluation_results
