#%%
from PIL import Image, ImageGrab
# from IPython.display import display
from sensei import sensei

workingImg = "screen.png"
tlator = sensei()
dim = (0,25,819,760)

def main():
    options = ["Check Kanji", "Full Translation", "Exit"]

    while True:
        print("\nMenu:")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        choice = input("\nEnter your choice: ")

        try:
            choice = int(choice)
            if 1 <= choice <= len(options):
                image = ImageGrab.grab(dim)
                image.save(workingImg)
                if choice == len(options):
                    print("Exiting...")
                    exit()
                    break
                if choice == 1:
                    prompt = "Translate all kanji in the image. Only respond with kanji, the kanji's hiragana reading, and english translation"
                    print(f"You selected: {options[choice-1]}")
                if choice == 2:
                    prompt = "Translate all the japanese in the image. only respond with the original text and english translation"
                    
                result = tlator.parseImage(workingImg,prompt) 
                print(result)
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

main()
