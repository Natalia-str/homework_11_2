def get_high_letter(arg: str) -> str:
    """принимает строку и возвращает их со всеми заглавными буквами"""
    high_letter = arg.upper()
    return high_letter


def get_title_letter(arg: str) -> str:
    """принимает на вход строку и возвращает ее с заглавными первыми буквами каждого слова"""
    title_letter = arg.title()
    return title_letter