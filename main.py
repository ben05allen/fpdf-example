from fpdf import FPDF
import re


def add_markdown_text(pdf, text_to_parse, font_family="Helvetica", font_size=12):
    pattern = r"(\*\*[^\*]+\*\*|\*[^\*]+\*)"
    parts = re.split(pattern, text_to_parse)

    for part in parts:
        if not part:
            continue

        style = ""
        plain_text = part

        if part.startswith("**") and part.endswith("**"):
            style = "B"
            plain_text = part[2:-2]  # Remove the asterisk
        elif part.startswith("*") and part.endswith("*"):
            style = "I"
            plain_text = part[1:-1]  # Remove the asterisks

        # The 'ln=False' ensures the next text continues on the same line.
        pdf.set_font(font_family, style, font_size)
        pdf.write(5, plain_text)


pdf = FPDF("P", "mm", "A4")
pdf.add_page()
pdf.set_font("Helvetica", size=12)

paragraphs = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "Fusce non lectus sed mauris vehicula ullamcorper. Nam at elit nec sem vestibulum eleifend. Aliquam erat volutpat. Maecenas bibendum libero vel nunc malesuada, a egestas nulla ullamcorper. Praesent ac libero sit amet tortor mollis accumsan. In hac habitasse platea dictumst. Quisque facilisis, orci ac viverra eleifend, felis ipsum faucibus magna, a vulputate nulla mauris vel sapien.",
    "Nulla facilisi. Integer eu felis ut magna fringilla semper. Suspendisse potenti. Nam fringilla sapien vitae velit luctus, vel lacinia ligula semper. Sed vel arcu ac est fermentum ultrices. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec non nibh sed lectus gravida malesuada ut ac quam.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "Fusce non lectus sed mauris vehicula ullamcorper. Nam at elit nec sem vestibulum eleifend. Aliquam erat volutpat. Maecenas bibendum libero vel nunc malesuada, a egestas nulla ullamcorper. Praesent ac libero sit amet tortor mollis accumsan. In hac habitasse platea dictumst. Quisque facilisis, orci ac viverra eleifend, felis ipsum faucibus magna, a vulputate nulla mauris vel sapien.",
    "Nulla facilisi. Integer eu felis ut magna fringilla semper. Suspendisse potenti. Nam fringilla sapien vitae velit luctus, vel lacinia ligula semper. Sed vel arcu ac est fermentum ultrices. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec non nibh sed lectus gravida malesuada ut ac quam.",
]

list_items = [
    "This is the **first** item\n",
    "This is the *next* item\n",
    "XXX This won't be shown\n",
    "This **really** is the *last one*\n",
]


for paragraph in paragraphs:
    with pdf.unbreakable() as para:
        para.multi_cell(0, 10, text=paragraph)
        pdf.ln(5)

filtered_list = [li for li in list_items if "XXX" not in li]
for i, item in enumerate(filtered_list, start=1):
    # note that the list numbers are bold
    add_markdown_text(pdf, f"**{i}.** {item}")


pdf.output("lorem_ipsum.pdf")
