from nose.tools import *
from my_tags import *

import re

HTML = "tags.html"
REGEX_STR = r"/tag/(.+)\.html\">.+</a> \((\d+)\)"
REGEX = re.compile(REGEX_STR)

def _get_html_tags():
    # Read the tag counts from the html file to use for testing.
    # Returns a dict of {tag: count,...}
    with open(HTML) as f:
        for line in f.readlines():
            match = REGEX.search(line)
            if match:
                yield (match.group(1), match.group(2))


def get_tags_tests():
    tags = get_tags()
    assert_equal(tags[:2], ["python", "tips"])
    assert_equal(tags[-1], "pybites")
    
    
def get_top_tags_tests():
    tags = get_tags()
    top_tags = get_top_tags(tags)
    assert_equal(top_tags[0], ("python", 10))
    assert_equal(len(top_tags), 10)
    
    
def get_similar_tags_tests():
    tags = get_tags()
    sim_tags = get_similar_tags(set(tags))
    assert {"challenge", "challenges"} in sim_tags