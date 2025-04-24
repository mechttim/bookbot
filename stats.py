def make_string(file_content):
    words = file_content.split()
    count = 0 
    for word in words:
        count += 1
    return count

def count_char(file_content):
    chart = {}
    words = file_content.lower()
    letters = ''.join([word for word in words if word.isalpha()])
    for i in letters:
        if i in chart:
            chart[i] += 1
        else:
            chart[i] = 1
    return chart

def sort_on(dict):
    return dict["num"] 

def listdic(results):
    little_list = []
    for char, count in results.items():
        little_list.append({"char": char, "num": count})
    
    little_list.sort(reverse=True, key=sort_on)
    
    return little_list
     



   