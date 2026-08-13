using System.Linq;

// Avalonia
using Avalonia;
using Avalonia.Controls;
using Avalonia.Media;

// Controllers
using Controllers.LangTags;
using System.Diagnostics;

// Filter
using Utils.Text;

// Normalizer text
using Core.LangTags;

namespace Views.Forms {
    public partial class Languages: TableUserControl {
        private int _id;
        private LanguageController _languageController;
        private object[] _parameters;

        // Constructor
        public Languages(LanguageController controller) {
            InitializeComponent();
            _languageController = controller;
            _controller = controller;
            _id = -1;
            _parameters = new object[]{
                TextBoxId, TextBoxCode, CheckBoxIsActive
            };
            _tableGrid = TableGrid;
            LoadCache();
            LoadTable();
        }

        private void RefreshParameters(){
            if (_id > 0 && _id <= _cachedRows.Count)
            {
                string[] rowData = _cachedRows[_id-1];
                TextBoxId.Text = rowData[0];
                TextBoxCode.Text = rowData[1];
                CheckBoxIsActive.IsChecked = rowData[5] == "1";
            } else {
                if ( !string.IsNullOrEmpty(TextBoxId.Text) ) {
                    TextBoxId.Text = "";}
            }
        }

        private void ClearParametersWithExceptions( object[] exceptions ){
            for (int i = 0; i < _parameters.Length; i++){
                object widget = _parameters[i];
                if ( exceptions.Contains(widget) == false){
                    if (widget is TextBox textBox){
                        textBox.Text = "";
                    }
                    else if (widget is CheckBox checkBox){
                        checkBox.IsChecked = true;
                    }
                }
            }
        }
        private void ClearParameters(){
            ClearParametersWithExceptions( new object[0] );
        }
        
        // EventHandlers
        private void textBoxIdChangedEventHandler(object? sender, TextChangedEventArgs args) 
        {
            if (sender is TextBox textBox){
                string filteredText = GetFilteredTextToAPositiveInteger(textBox.Text);
                textBox.Text = filteredText;
                _id = TextNumber.ReadInt(filteredText);
                RefreshParameters();
            }
        }

        private void textBoxCodeChangedEventHandler( object? sender, TextChangedEventArgs args)
        {
            if (sender is TextBox textBox){
                string normalizedCode = LanguageCodeNormalizer.Normalize(
                    textBox.Text);
                int id = _languageController.GetIdByCode(normalizedCode);
                textBox.Text = normalizedCode;
                if (id > 0) {
                    _id = id;
                    RefreshParameters();
                }
                else {
                    ClearParametersWithExceptions( 
                        new object[]{ textBox } );
                }
            }
        }

        private void OnSaveClick(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
        {
            bool goodId = _id > 0;
            bool goodCode = string.IsNullOrEmpty(TextBoxCode.Text) == false;
            if (_id > 0 || goodCode) {
                _languageController.Save(
                    languageId:_id, code:TextBoxCode.Text, isActive: (bool)CheckBoxIsActive.IsChecked );
                
                if ( goodId == false && _languageController.ExistsByCode(TextBoxCode.Text) ) {
                    _id = _languageController.GetIdByCode(TextBoxCode.Text);
                }
                if (_languageController.ExistsById(_id))
                {
                    RefreshTable();
                    RefreshParameters();
                }
            }
        }
        //
    }
}