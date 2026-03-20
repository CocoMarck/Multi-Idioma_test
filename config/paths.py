from utils.resource_loader import ResourceLoader

resource_loader = ResourceLoader()

VIEWS_DIR = resource_loader.base_dir.joinpath( 'views' )
MAIN_WINDOW_UI = VIEWS_DIR.joinpath( 'langtags/xml/main_window.ui' )
BASE_FORM_UI = VIEWS_DIR.joinpath( 'langtags/xml/base_form.ui' )
TRANSLATION_FORM_UI = VIEWS_DIR.joinpath( 'langtags/xml/translation_form.ui' )

SCHEMAS_DIR = resource_loader.base_dir.joinpath( 'schemas' )
SCHEMAS_LANGTAGS_DIR = SCHEMAS_DIR.joinpath( 'langtags' )
SCHEMAS_LANGTAGS_DIR_TREE = resource_loader.get_recursive_tree( SCHEMAS_LANGTAGS_DIR )
SCHEMAS_LANGTAGS_FILES = SCHEMAS_LANGTAGS_DIR_TREE['file']
