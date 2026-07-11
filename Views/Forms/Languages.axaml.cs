// Avalonia
using Avalonia;
using Avalonia.Controls;
using Avalonia.Media;

// Controllers
using Controllers.LangTags;
using System.Diagnostics;

namespace Views.Forms {
    public partial class Languages: UserControl {
        LanguageController _controller;

        // Constructor
        public Languages(LanguageController controller) {
            InitializeComponent();
            _controller = controller;
            LoadTable();
        }

        // Methods
        private void LoadTable()
        {
            string[] columns = _controller.GetColumnNames();
            List<string[]> rowValues = _controller.GetRowValues();


            // Inicializar columnas en grid
            foreach (string columnName in columns) {
                TableGrid.ColumnDefinitions.Add(new ColumnDefinition(GridLength.Auto));
            }
            // Inizializar filas en grid
            TableGrid.RowDefinitions.Add( new RowDefinition(GridLength.Auto) );
            foreach (string[] values in rowValues){
                TableGrid.RowDefinitions.Add( new RowDefinition(GridLength.Auto) );
            }

            // Renderizar columnas
            for (int colIndex = 0; colIndex < columns.Length; colIndex++) {
                var headerBlock = new TextBlock {
                    Text = columns[colIndex],
                    FontWeight = FontWeight.Bold,
                    Margin = new Thickness(12, 6) // Espaciado interno para que no se amontonen
                };
                Grid.SetColumn(headerBlock, colIndex);
                Grid.SetRow(headerBlock, 0); // Fila 0
                TableGrid.Children.Add(headerBlock);
            }

            // Renderizar filas
            for (int rowIndex = 0; rowIndex < rowValues.Count; rowIndex++) {
                var rowData = rowValues[rowIndex];
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
    }
}