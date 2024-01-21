#!/usr/bin/python3

import sys
import markdown

# Check the number of arguments
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

# Get the input and output file names from command-line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    # Read the content of the input Markdown file
    with open(input_file, 'r') as f:
        markdown_content = f.read()
except FileNotFoundError:
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

# Convert the Markdown content to HTML
html_content = markdown.markdown(markdown_content)

# Write the HTML content to the output file
with open(output_file, 'w') as f:
    f.write(html_content)

sys.exit(0)
