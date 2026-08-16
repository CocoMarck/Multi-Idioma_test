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
        private object[] _parameters;

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
        private void textBoxValueChangedEventHandler(object? sender, TextChangedEventArgs args)
        {
        }
        //
    }
}