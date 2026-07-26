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
    public partial class Languages: UserControl {
        private LanguageController _controller;
        private int _id;
        private string[] _cachedColumns;
        private List<string[]> _cachedRows;
        private object[] _parameters;

        // Constructor
        public Languages(LanguageController controller) {
            InitializeComponent();
            _controller = controller;
            _id = -1;
            _parameters = new object[]{
                TextBoxId, TextBoxCode, CheckBoxIsActive
            };
            LoadCache();
            LoadTable();
        }

        // Methods
        private void LoadCache()
        {
            _cachedColumns = _controller.GetColumnNames();
            _cachedRows = _controller.GetRowValues();
        }
        private void LoadTable()
        {
            // Inicializar columnas en grid
            foreach (string columnName in _cachedColumns) {
                TableGrid.ColumnDefinitions.Add(new ColumnDefinition(GridLength.Auto));
            }
            // Inizializar filas en grid
            TableGrid.RowDefinitions.Add( new RowDefinition(GridLength.Auto) );
            foreach (string[] values in _cachedRows){
                TableGrid.RowDefinitions.Add( new RowDefinition(GridLength.Auto) );
            }

            // Renderizar columnas
            for (int colIndex = 0; colIndex < _cachedColumns.Length; colIndex++) {
                var headerBlock = new TextBlock {
                    Text = _cachedColumns[colIndex],
                    FontWeight = FontWeight.Bold,
                    Margin = new Thickness(12, 6) // Espaciado interno para que no se amontonen
                };
                Grid.SetColumn(headerBlock, colIndex);
                Grid.SetRow(headerBlock, 0); // Fila 0
                TableGrid.Children.Add(headerBlock);
            }

            // Renderizar filas
            for (int rowIndex = 0; rowIndex < _cachedRows.Count; rowIndex++) {
                var rowData = _cachedRows[rowIndex];
                for (int colIndex = 0; colIndex < rowData.Length; colIndex++) {
                    var cellBlock = new TextBlock {
                        Text = rowData[colIndex],
                        Margin = new Thickness(12, 6)
                    };
                    Grid.SetColumn(cellBlock, colIndex);
                    Grid.SetRow(cellBlock, rowIndex + 1); // rowIndex + 1 para brincarse los headers
                    TableGrid.Children.Add(cellBlock);
                }
            }
        }
        private void ClearGrid(){
            TableGrid.Children.Clear();
            TableGrid.RowDefinitions.Clear();
            TableGrid.ColumnDefinitions.Clear();
        }
        private void RefreshTable(){
            ClearGrid();
            LoadCache();
            LoadTable();
        }

        private string GetFilteredTextToAPositiveInteger(string text){
            return TextFilter.IgnoreTextFilter( text: text, filter: "1234567890" );
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
                int id = _controller.GetIdByCode(normalizedCode);
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
                _controller.Save(
                    languageId:_id, code:TextBoxCode.Text, isActive: (bool)CheckBoxIsActive.IsChecked );
                
                if ( goodId == false && _controller.ExistsByCode(TextBoxCode.Text) ) {
                    _id = _controller.GetIdByCode(TextBoxCode.Text);
                }
                if (_controller.ExistsById(_id))
                {
                    RefreshTable();
                    RefreshParameters();
                }
            }
        }
        
        //
    }
}