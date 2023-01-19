PLACEHOLDER="[name]"
with open("Input/names") as file:
    names= file.readlines()

with open("Input/reference_letter.txt") as file:
    content= file.read()
    for name in names:
        strip_name=name.strip()
        new_letter=content.replace(PLACEHOLDER, strip_name)
        with open(f"../{strip_name}_letter.txt", "w") as completed_letter:
            completed_letter.write(new_letter)




