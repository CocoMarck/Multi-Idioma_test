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
    public partial class Translations: TableUserControl {
        private int _id;
        private TranslationController _translationController;

        public Translations(TranslationController controller) {
            InitializeComponent();
            _translationController = controller;
            _controller = controller;
            _id = -1;
            _tableGrid = TableGrid;
            LoadCache();
            LoadTable();
        }
        private void RefreshParameters(){
            if (_id > 0 && _id <= _cachedRows.Count)
            {
                string[] rowData = _cachedRows[_id-1];
                TextBoxId.Text = rowData[0];
                TextBoxTagName.Text = _translationController.GetTagNameById(
                    TextNumber.ReadInt(rowData[1]) );
                TextBoxLanguageCode.Text = _translationController.GetLanguageCodeById(
                    TextNumber.ReadInt(rowData[2]) );
                TextBoxValue.Text = rowData[3];
                CheckBoxIsActive.IsChecked = rowData[7] == "1";
            } else {
                if ( !string.IsNullOrEmpty(TextBoxId.Text) ) {
                    TextBoxId.Text = "";}
            }
        }
        private void textBoxIdChangedEventHandler(object? sender, TextChangedEventArgs args)
        {
            if (sender is TextBox textBox){
                string filteredText = GetFilteredTextToAPositiveInteger(textBox.Text);
                textBox.Text = filteredText;
                _id = TextNumber.ReadInt(filteredText);
                RefreshParameters();
            }
        }
        private void changeIdByTagNameAndLanguageCode(string tagName, string languageCode){
            // Establecer nombre por tag name y language code.
            if (string.IsNullOrEmpty(tagName) || string.IsNullOrEmpty(languageCode)){
                return;
            }
            string normalizedName = TagNameNormalizer.Normalize(tagName);
            string normalizedCode = LanguageCodeNormalizer.Normalize(languageCode);
            int id = _translationController.GetIdByTagNameAndLanguageCode(
                normalizedName, normalizedCode);
            if (id > 0){
                _id = id;
                RefreshParameters();
            }
        }
        private void textBoxTagNameChangedEventHandler(object? sender, TextChangedEventArgs args)
        {
            if (sender is TextBox textBox){
                changeIdByTagNameAndLanguageCode(textBox.Text, TextBoxLanguageCode.Text);
            }
        }
        private void textBoxLanguageCodeChangedEventHandler(object? sender, TextChangedEventArgs args)
        {
            if (sender is TextBox textBox){
                changeIdByTagNameAndLanguageCode(TextBoxTagName.Text, textBox.Text);
            }
        }
        private void textBoxValueChangedEventHandler(object? sender, TextChangedEventArgs args)
        {
            // Esto no seguramente no se necesita.
        }
        private void OnSaveClick(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
        {
            // Guardar solo si id, tagName, languageCode, y value, están bien.
            bool goodId = GoodIndex(_id);
            bool goodValue = string.IsNullOrEmpty(TextBoxValue.Text) == false;
            if (goodValue) {
                if (goodId){
                    Console.WriteLine(_id);
                    string[] rowData = _cachedRows[_id-1];
                    int tagId = TextNumber.ReadInt(rowData[1]);
                    int languageId = TextNumber.ReadInt(rowData[2]);
                    _translationController.SaveByTagIdAndLanguageId(
                        tagId: tagId, languageId: languageId, translationId: _id, value: TextBoxValue.Text, isActive:(bool)CheckBoxIsActive.IsChecked);
                } else {
                    _translationController.SaveByTagNameAndLanguageCode(
                        tagName: TextBoxTagName.Text, languageCode: TextBoxLanguageCode.Text, translationId: null, value: TextBoxValue.Text, isActive:(bool)CheckBoxIsActive.IsChecked
                    );
                    _id = _translationController.GetIdByTagNameAndLanguageCode(
                        TextBoxTagName.Text, TextBoxLanguageCode.Text);
                }
                RefreshTable();
                RefreshParameters();
            }
        }
        //
    }
}