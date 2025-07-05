# Estilo cabelCase
LANGUAGE_NAME = "language"

LANGUAGES = {
    "en": "en",
    "es": "es",
    "pt": "pt",
    "ru": "ru"
}
DEFAULT_LANGUAGE = LANGUAGES['en']


LANGUAGE_TABLE_NAMES = {
    "table": LANGUAGE_NAME,
    "id": f"{LANGUAGE_NAME}Id",
    "tag": "tag",
}
LANGUAGE_TABLE_NAMES.update( LANGUAGES )

CONFIG_NAME = "config"
LANGUAGE_CONFIG_TABLE_NAMES = {
    "table": CONFIG_NAME,
    "id": f"{CONFIG_NAME}Id",
    "language": LANGUAGE_TABLE_NAMES["table"]
}