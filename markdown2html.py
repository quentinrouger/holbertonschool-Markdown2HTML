#!/usr/bin/python3
"""
Markdown to HTML Converter
Task 1: convert heading
"""

import sys
import markdown


def convert_markdown_to_html(input_file, output_file):
    """function that converts a Markdown file to an HTML file."""
    try:
        with open(input_file, 'r') as md_file:
            md_content = md_file.read()
            html_content = markdown.markdown(md_content)
            with open(output_file, 'w') as html_file:
                html_file.write(html_content)
    except FileNotFoundError:
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)


def parse_headings(md_content):
    """Parse Markdown headings and generate corresponding HTML."""
    lines = md_content.split('\n')
    html_lines = []

    for line in lines:
        if line.startswith('#'):
            # Extract heading level and text
            heading_level = line.count('#')
            heading_text = line.lstrip('#').strip()
            # Generate HTML for the heading
            html_line = f"<h{heading_level}>{heading_text}</h{heading_level}>"
            html_lines.append(html_line)
        else:
            html_lines.append(line)

    return '\n'.join(html_lines)


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
