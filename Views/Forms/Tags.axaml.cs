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
        private object[] _parameters;
        
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

        // EventHandlers
        private void textBoxIdChangedEventHandler(object? sender, TextChangedEventArgs args)
        {
        }

        private void textBoxNameChangedEventHandler(object? sender, TextChangedEventArgs args)
        {
        }
        
        private void OnSaveClick(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
        {
        }
        //
    }
}

