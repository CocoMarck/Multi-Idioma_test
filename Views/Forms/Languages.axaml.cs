// Avalonia
using Avalonia;
using Avalonia.Controls;
using Avalonia.Media;

// Controllers
using Controllers.LangTags;
using System.Diagnostics;

// Filter
using Utils.Text;

namespace Views.Forms {
    public partial class Languages: UserControl {
        private LanguageController _controller;
        private int _id;
        private string[] _cachedColumns;
        private List<string[]> _cachedRows;

        // Constructor
        public Languages(LanguageController controller) {
            InitializeComponent();
            _controller = controller;
            _id = 0;
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

        private string GetFilteredTextToAPositiveInteger(string text){
            return TextFilter.IgnoreTextFilter( text: text, filter: "1234567890" );
        }

        private void RefreshParameters(){
            if (_id > 0 && _id <= _cachedRows.Count)
            {
                string[] rowData = _cachedRows[_id-1];
                TextBoxId.Text = rowData[0];
                TextBoxCode.Text = rowData[1];
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
        //
    }
}