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
    public partial class Settings: TableUserControl {
        private SettingController _settingController;

        public Settings(SettingController controller) {
            InitializeComponent();
            _settingController = controller;
            _controller = controller;
            _tableGrid = tableGrid;
            RefreshTable();

            string[] languagesCodes = _settingController.GetLanguageCodes();
            var settingsCodes = new string[2]{"default", "system"};
            var codes = new List<string>();
            codes.AddRange(settingsCodes);
            codes.AddRange(languagesCodes);
            IEnumerable<string> enumerableCodes = codes;
            comboboxLanguages.ItemsSource = enumerableCodes;
        }

        public void comboBoxLanguageCodeChangedEventHandler(object? sender, SelectionChangedEventArgs args) {
            if (sender is ComboBox comboBox && comboBox.SelectedItem is string code)
            {
                if (code == "system"){
                    _settingController.EstablishSystemLanguage();
                } else if(code == "default") {
                    _settingController.EstablishDefaultLanguage();
                } else {
                    _settingController.UpdateSelectedLanguageCode(code);
                }
                RefreshTable();
            }
        }
    }
}