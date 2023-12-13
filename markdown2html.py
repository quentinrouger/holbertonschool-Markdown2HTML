#!/usr/bin/env python3
"""
Markdown to HTML Converter
Task 0: start a script
"""

import sys
import markdown


def convert_markdown_to_html(input_file, output_file):
    """
    Convert Markdown content to HTML.

    Parameters:
    - input_file (str): Path to the input Markdown file.
    - output_file (str): Path to the output HTML file.
    """
    try:
        with open(input_file, 'r') as md_file:
            md_content = md_file.read()
            html_content = markdown.markdown(md_content)
            with open(output_file, 'w') as html_file:
                html_file.write(html_content)
    except FileNotFoundError:
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_file, output_file)

    sys.exit(0)
