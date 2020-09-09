from summa import keywords
import argparse

parser = argparse.ArgumentParser(description='keyword extractor demo')
parser.add_argument('--file', type=str, default="./test_files/researchpaper.txt", help='dir of txt for testing file')
args = parser.parse_args()

file = args.file
fp = open(file, "r")
text = fp.read()
# print(text)
print(keywords.keywords(text))
