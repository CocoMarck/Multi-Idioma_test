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

        // Constructor
        public Languages(LanguageController controller) {
            InitializeComponent();
            _languageController = controller;
            _controller = controller;
            _id = -1;
            _parameters = new object[]{
                textBoxId, textBoxCode, checkBoxIsActive
            };
            _tableGrid = tableGrid;
            LoadCache();
            LoadTable();
            RefreshText();
        }

        private void RefreshText(){
            labelCode.Content = App.LangTagsService.GetText("Code");
            labelId.Content = App.LangTagsService.GetText("Id");
            checkBoxIsActive.Content = App.LangTagsService.GetText("Is active");
            buttonRefresh.Content = App.LangTagsService.GetText("Refresh");
            buttonSave.Content = App.LangTagsService.GetText("Save");
        }

        private void RefreshParameters(){
            if (_id > 0 && _id <= _cachedRows.Count)
            {
                string[] rowData = _cachedRows[_id-1];
                textBoxId.Text = rowData[0];
                textBoxCode.Text = rowData[1];
                checkBoxIsActive.IsChecked = rowData[5] == "1";
            } else {
                if ( !string.IsNullOrEmpty(textBoxId.Text) ) {
                    textBoxId.Text = "";}
            }
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
            bool goodCode = string.IsNullOrEmpty(textBoxCode.Text) == false;
            if (_id > 0 || goodCode) {
                _languageController.Save(
                    languageId:_id, code:textBoxCode.Text, isActive: (bool)checkBoxIsActive.IsChecked );
                
                if ( goodId == false && _languageController.ExistsByCode(textBoxCode.Text) ) {
                    _id = _languageController.GetIdByCode(textBoxCode.Text);
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