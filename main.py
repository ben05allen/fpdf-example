from fpdf import FPDF

pdf = FPDF("P", "mm", "A4")
pdf.add_page()
pdf.set_font("Helvetica", size=12)

paragraph1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
paragraph2 = "Fusce non lectus sed mauris vehicula ullamcorper. Nam at elit nec sem vestibulum eleifend. Aliquam erat volutpat. Maecenas bibendum libero vel nunc malesuada, a egestas nulla ullamcorper. Praesent ac libero sit amet tortor mollis accumsan. In hac habitasse platea dictumst. Quisque facilisis, orci ac viverra eleifend, felis ipsum faucibus magna, a vulputate nulla mauris vel sapien."
paragraph3 = "Nulla facilisi. Integer eu felis ut magna fringilla semper. Suspendisse potenti. Nam fringilla sapien vitae velit luctus, vel lacinia ligula semper. Sed vel arcu ac est fermentum ultrices. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec non nibh sed lectus gravida malesuada ut ac quam."
paragraph4 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
paragraph5 = "Fusce non lectus sed mauris vehicula ullamcorper. Nam at elit nec sem vestibulum eleifend. Aliquam erat volutpat. Maecenas bibendum libero vel nunc malesuada, a egestas nulla ullamcorper. Praesent ac libero sit amet tortor mollis accumsan. In hac habitasse platea dictumst. Quisque facilisis, orci ac viverra eleifend, felis ipsum faucibus magna, a vulputate nulla mauris vel sapien."
paragraph6 = "Nulla facilisi. Integer eu felis ut magna fringilla semper. Suspendisse potenti. Nam fringilla sapien vitae velit luctus, vel lacinia ligula semper. Sed vel arcu ac est fermentum ultrices. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec non nibh sed lectus gravida malesuada ut ac quam."

for paragraph in [
    paragraph1,
    paragraph2,
    paragraph3,
    paragraph4,
    paragraph5,
    paragraph6,
]:
    with pdf.unbreakable() as para:
        para.multi_cell(0, 10, text=paragraph)
        pdf.ln(5)


pdf.output("lorem_ipsum.pdf")
