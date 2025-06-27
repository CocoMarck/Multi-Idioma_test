# Estilo cabelCase
LANGUAGE_NAME = "language"
TABLE_LANGUAGE_NAMES = {
    "table": LANGUAGE_NAME,
    "id": f"{LANGUAGE_NAME}Id",
    "tag": "tag",
    "en": "en",
    "es": "es",
    "pt": "pt",
    "ru": "ru"
}

CONFIG_NAME = "config"
TABLE_CONFIG_NAMES = {
    "table": CONFIG_NAME,
    "id": f"{CONFIG_NAME}Id",
    "lang": TABLE_LANGUAGE_NAMES["table"]
}