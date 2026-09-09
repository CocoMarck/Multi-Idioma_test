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
            _tableGrid = tableGrid;
            LoadCache();
            LoadTable();
            RefreshText();
        }
        private void RefreshText(){
            labelTagName.Content = App.LangTagsService.GetText("Tag name");
            labelLanguageCode.Content = App.LangTagsService.GetText("Language code");
            labelValue.Content = App.LangTagsService.GetText("Value");
            labelId.Content = App.LangTagsService.GetText("Id");
            buttonRefresh.Content = App.LangTagsService.GetText("Refresh");
            buttonSave.Content = App.LangTagsService.GetText("Save");
            checkBoxIsActive.Content = App.LangTagsService.GetText("Is active");
        }
        private void RefreshParameters(){
            if (_id > 0 && _id <= _cachedRows.Count)
            {
                string[] rowData = _cachedRows[_id-1];
                textBoxId.Text = rowData[0];
                textBoxTagName.Text = _translationController.GetTagNameById(
                    TextNumber.ReadInt(rowData[1]) );
                textBoxLanguageCode.Text = _translationController.GetLanguageCodeById(
                    TextNumber.ReadInt(rowData[2]) );
                textBoxValue.Text = rowData[3];
                checkBoxIsActive.IsChecked = rowData[7] == "1";
            } else {
                if ( !string.IsNullOrEmpty(textBoxId.Text) ) {
                    textBoxId.Text = "";}
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
        private void ChangeIdByTagNameAndLanguageCode(string tagName, string languageCode){
            // Establecer nombre por tag name y language code.
            if (string.IsNullOrEmpty(tagName) || string.IsNullOrEmpty(languageCode)){
                return;
            }
            string normalizedName = TagNameNormalizer.Normalize(tagName);
            string normalizedCode = LanguageCodeNormalizer.Normalize(languageCode);
            int id = _translationController.GetIdByTagNameAndLanguageCode(
                normalizedName, normalizedCode);
            textBoxId.Text = ""; // Para meter custom ID si es que se requiere.
            if (id > 0){
                _id = id;
                RefreshParameters();
            }
        }
        private void textBoxTagNameChangedEventHandler(object? sender, TextChangedEventArgs args)
        {
            if (sender is TextBox textBox){
                ChangeIdByTagNameAndLanguageCode(textBox.Text, textBoxLanguageCode.Text);
            }
        }
        private void textBoxLanguageCodeChangedEventHandler(object? sender, TextChangedEventArgs args)
        {
            if (sender is TextBox textBox){
                ChangeIdByTagNameAndLanguageCode(textBoxTagName.Text, textBox.Text);
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
            bool goodValue = string.IsNullOrEmpty(textBoxValue.Text) == false;
            if (goodValue) {
                if (goodId){
                    Console.WriteLine(_id);
                    string[] rowData = _cachedRows[_id-1];
                    int tagId = TextNumber.ReadInt(rowData[1]);
                    int languageId = TextNumber.ReadInt(rowData[2]);
                    _translationController.SaveByTagIdAndLanguageId(
                        tagId: tagId, languageId: languageId, translationId: _id, value: textBoxValue.Text, isActive:(bool)checkBoxIsActive.IsChecked);
                } else {
                    _translationController.SaveByTagNameAndLanguageCode(
                        tagName: textBoxTagName.Text, languageCode: textBoxLanguageCode.Text, translationId: null, value: textBoxValue.Text, isActive:(bool)checkBoxIsActive.IsChecked
                    );
                    _id = _translationController.GetIdByTagNameAndLanguageCode(
                        textBoxTagName.Text, textBoxLanguageCode.Text);
                }
                RefreshTable();
                RefreshParameters();
            }
        }
        //
    }
}