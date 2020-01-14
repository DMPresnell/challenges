from collections import Counter
from difflib import SequenceMatcher
import nltk
import re

RSS_FEED = "rss.xml"
TOP_COUNT = 10
REGEX = re.compile(r"<category>(.+?)</category>")
SIMILAR = 0.87

def get_tags():
    # Reads RSS_FEED file and returns a list of all tags found in it.
    tags = []
    with open(RSS_FEED) as f:
        return REGEX.findall(f.read())
        
        
def get_top_tags(tags):
    # Counts passed list of tags and returns a new list of len TOP_COUNT.
    # Returned list is ordered most common first.  List elements are tuples:
    # (tag, count).
    counter = Counter(tags)
    return counter.most_common(10)
    
    
def get_similar_tags(tags_set):
    # Uses SequenceMatcher to compare each element of tags_set to all other
    # elements of tags_set.  Returns a 
    sim_tags_set = set()
    for tag1 in tags_set:
        for tag2 in tags_set:
            if tag1 != tag2 and tag1[0] == tag2[0]:
                ratio = SequenceMatcher(None, tag1, tag2).ratio()
                if 1 > ratio >= SIMILAR:
                    sim_tags_set.add(frozenset([tag1, tag2]))
    return sim_tags_set
    
    
def main():
    tags = get_tags()
    print()
    print(f"  Top {TOP_COUNT} tags:")
    for tag in get_top_tags(tags):
        print(f"{tag[0]:<20} {tag[1]}")
    
    print()
    for tag_set in get_similar_tags(set(tags)):
        tag_list = list(tag_set)
        print(f"{tag_list[0]:<20} {tag_list[1]}")
    
    
if __name__ == "__main__":
    
    main()