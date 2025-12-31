class ChaiUtils:
    @staticmethod
    def clean_ingred(text):
        return [item.strip() for item in text.split(",")]


raw="  water, milk, ginger , honey"

print(ChaiUtils.clean_ingred(raw))