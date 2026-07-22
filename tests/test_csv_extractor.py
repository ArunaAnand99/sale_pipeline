from src.extract.csv_extractor import *


print("test 1: valid file")

extractor = CsvExtractor('data/raw/sales.csv')
df = extractor.extract()
print(df)
print(f"length:{len(df)}")

print("test 2: large file processing")
extractor = CsvExtractor('data/raw/sales.csv')
# extractor = extractor
for row in extractor.extract_large_file():
    print(row)
    

print("Test 3: Invalid file")


try:
    extractor = CsvExtractor('data/raw/sale.csv')
    df = extractor.extract()
except Exception as e:
    print(f"caught error:{e}")
    
