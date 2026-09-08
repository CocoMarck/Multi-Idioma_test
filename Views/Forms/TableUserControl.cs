// Avalonia
using Avalonia;
using Avalonia.Controls;
using Avalonia.Media;

// Filter
using Utils.Text;

// Controllers
using Controllers.LangTags;

namespace Views.Forms {
    public abstract class TableUserControl : UserControl {
        protected string[] _cachedColumns;
        protected List<string[]> _cachedRows;
        protected ITableController _controller;
        protected Grid _tableGrid; // Referencia a Grid de la vista
        protected object[] _parameters; // Para refrescar parametros

        // Methods
        protected virtual void LoadCache()
        {
            _cachedColumns = _controller.GetColumnNames();
            _cachedRows = _controller.GetRowValues();
        }
        protected virtual bool GoodIndex(int index){
            return index > 0 && index <= _cachedRows.Count;
        }
        protected virtual void LoadTable()
        {
            // Inicializar columnas en grid
            foreach (string columnName in _cachedColumns) {
                _tableGrid.ColumnDefinitions.Add(new ColumnDefinition(GridLength.Auto));
            }
            // Inizializar filas en grid
            _tableGrid.RowDefinitions.Add( new RowDefinition(GridLength.Auto) );
            foreach (string[] values in _cachedRows){
                _tableGrid.RowDefinitions.Add( new RowDefinition(GridLength.Auto) );
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
                _tableGrid.Children.Add(headerBlock);
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
                    _tableGrid.Children.Add(cellBlock);
                }
            }
        }
        protected virtual void ClearGrid(){
            _tableGrid.Children.Clear();
            _tableGrid.RowDefinitions.Clear();
            _tableGrid.ColumnDefinitions.Clear();
        }
        public virtual void RefreshTable(){
            ClearGrid();
            LoadCache();
            LoadTable();
        }
        
        // Repeated specific methods
        protected string GetFilteredTextToAPositiveInteger(string text){
            return TextFilter.IgnoreTextFilter( text: text, filter: "1234567890" );
        }
        protected void ClearParametersWithExceptions( object[] exceptions ){
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
        protected void ClearParameters(){
            ClearParametersWithExceptions( new object[0] );
        }
        

        //
    }
}