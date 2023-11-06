from PIL import Image, ImageDraw, ImageFont

print("Генератор мемов запущен!")
while True:
    text_type = int(input("Введите 1, если нужен только нижний текст, и 2, если и верхний, и нижний: "))
    top_text = ""
    bottom_text = ""
    if text_type == 1:
        bottom_text = input("Введите нижний текст: ")
        print(bottom_text)
    elif text_type == 2:
        top_text = input("Введите верхний текст: ")
        bottom_text = input("Введите нижний текст: ")
    else:
        quit(print("Неверный ввод!"))


    letters = "abcdefghijklmnopqrstuvwxyz"

    for i in letters:
        top_text = top_text.replace(i, "")
        top_text = top_text.replace(i.upper(), "")
        bottom_text = bottom_text.replace(i, "")
        bottom_text = bottom_text.replace(i.upper(), "")

    memes = [" Деньги"," Рукопожатие"," Удивление"]
    for i in range(len(memes)):
        print(i + 1, memes[i])

    user_image = int(input("Выбери картинку:"))
    if user_image == 3:
        image = Image.open("memejpg(1).jpg")
    elif user_image == 2:
        image = Image.open("memejpg(2).jpg")
    elif user_image == 1:
        image = Image.open("memejpg(3).jpg")
    else:
        quit(print("Неверный ввод!"))

    width,height = image.size
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("arial.ttf", size = 70)

    text = draw.textbbox((0,0), top_text, font)
    draw.text(((width - text[2])/ 2, 10), top_text, font=font, fill="black")

    draw.text(((width - text[2])/ 2, height - text[3]-10), bottom_text, font=font, fill="black")
    user_meme_name = input("Назовите мем: ") + ".jpg"

    image.save(user_meme_name)
    ask = input("Введите 1, чтобы закрыть программу. 2 чтобы создать еще один мем.")

    if ask == "1":
        break
    elif ask == "2":
        continue
    else:
        quit(print("Неверный ввод!"))
    

  
   
    
