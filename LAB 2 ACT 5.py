#ACT 5
def classify_age():
    age = int(input("Attach an age: "))

    if age < 0:
        print("Age cannot be negative(Bakit may nakita kana bang age na negative?, kupal!")
    elif age <= 12:
        print("You are a Child.")
    elif age <= 19:
        print("You are a Teen.")
    elif age <= 64:
        print("You are an Adult.")
    else:
        print("You are a Senior.")

classify_age()
#Ian Dave Ching