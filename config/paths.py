from utils.resource_loader import ResourceLoader

resource_loader = ResourceLoader()

VIEWS_DIR = resource_loader.base_dir.joinpath( 'views' )
MAIN_WINDOW_UI = VIEWS_DIR.joinpath( 'langtags/xml/main_window.ui' )
BASE_FORM_UI = VIEWS_DIR.joinpath( 'langtags/xml/base_form.ui' )
TRANSLATION_FORM_UI = VIEWS_DIR.joinpath( 'langtags/xml/translation_form.ui' )
GET_TEXT_FORM_UI = VIEWS_DIR.joinpath( 'langtags/xml/get_text_form.ui' )
SETTING_FORM_UI = VIEWS_DIR.joinpath( 'langtags/xml/setting_form.ui' )
