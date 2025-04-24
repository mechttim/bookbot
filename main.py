import sys
from stats import make_string
from stats import count_char
from stats import listdic
args =[] 
for i in sys.argv:
    args.append(i)
if len(args) != 2:
    sys.exit("Usage: python3 main.py <path_to_book>")
else:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {args[1]}...")
    def main():
        path = args[1]
        get_book_text(path)

    def get_book_text(path):
        with open (path) as f:
            file_contents = f.read()
        count = make_string(file_contents)
        print("----------- Word Count ----------")
        print(f"Found {count} total words")
        results = count_char(file_contents)
        sorted_list = listdic(results)
        print("--------- Character Count -------")
        for item in sorted_list:
            print(f"{item['char']}: {item['num']}")
    main()