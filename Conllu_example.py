from conllu import parse_incr
from io import open

path = f"E:\Tokenizer\Efficiency\zh_gsd-ud-train.conllu"

file =  open(path, "r", encoding="utf-8")

# for tokentree in parse_tree(file):
#    print(tokentree)

tokentree = list(parse_incr(file))
length = len(tokentree)
# print(length)
first_tree = tokentree[0]
listt = []
for data in first_tree:
    token = data["form"]
    listt.append(token)

print(listt)
# tree_length = len(first_tree)
# print(tree_length)
print(first_tree.metadata["text"])
# print(tokentree)
