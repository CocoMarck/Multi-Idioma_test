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
    public partial class Tags: TableUserControl {
        private int _id;
        private TagController _tagController;
        
        // Constructor
        public Tags(TagController controller) {
            InitializeComponent();
            _tagController = controller;
            _controller = controller;
            _id = -1;
            _parameters = new object[]{
                TextBoxId, TextBoxName, CheckBoxIsActive
            };
            _tableGrid = TableGrid;
            LoadCache();
            LoadTable();
        }

        // Methods | Parameters
        private void RefreshParameters(){
            if (_id > 0 && _id <= _cachedRows.Count)
            {
                string[] rowData = _cachedRows[_id-1];
                TextBoxId.Text = rowData[0];
                TextBoxName.Text = rowData[1];
                CheckBoxIsActive.IsChecked = rowData[5] == "1";
            } else {
                if ( !string.IsNullOrEmpty(TextBoxId.Text) ) {
                    TextBoxId.Text = "";}
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

        private void textBoxNameChangedEventHandler(object? sender, TextChangedEventArgs args)
        {
            if (sender is TextBox textBox){
                string normalizedName = TagNameNormalizer.Normalize(
                    textBox.Text);
                int id = _tagController.GetIdByName(normalizedName);
                textBox.Text = normalizedName;
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
            bool goodName = string.IsNullOrEmpty(TextBoxName.Text) == false;
            if (_id > 0 || goodName) {
                _tagController.Save(
                    tagId:_id, name:TextBoxName.Text, isActive: (bool)CheckBoxIsActive.IsChecked );
                
                if ( goodId == false && _tagController.ExistsByName(TextBoxName.Text) ) {
                    _id = _tagController.GetIdByName(TextBoxName.Text);
                }
                if (_tagController.ExistsById(_id))
                {
                    RefreshTable();
                    RefreshParameters();
                }
            }
        }
        //
    }
}

