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
        private string[] _settingsCodes;

        public Settings(SettingController controller) {
            InitializeComponent();
            _settingController = controller;
            _controller = controller;
            _tableGrid = tableGrid;
            RefreshTable();

            string[] languagesCodes = _settingController.GetLanguageCodes();
            _settingsCodes = new string[2]{"system", "default"};
            var codes = new List<string>();
            codes.AddRange(_settingsCodes);
            codes.AddRange(languagesCodes);
            IEnumerable<string> enumerableCodes = codes;
            comboboxLanguages.ItemsSource = enumerableCodes;
            UpdateComboBoxLanguages();
        }

        private void UpdateComboBoxLanguages(){
            // Establecer lenguaje seleccionado por texto. Dando prioridad al texto "system", que es el ID 0, representando el idioma del sistema.
            string match;
            int selectedId = _settingController.GetSelectedLanguageId();
            string selectedCode = _settingController.GetSelectedLanguageCode();
            
            if (selectedId == 0){
                match = _settingsCodes[selectedId];
            } else {
                match = comboboxLanguages.Items
                    .Cast<string>()
                    .FirstOrDefault(x => x == selectedCode);
            }
                
            comboboxLanguages.SelectedItem = match;
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
                UpdateComboBoxLanguages();
            }
        }
    }
}