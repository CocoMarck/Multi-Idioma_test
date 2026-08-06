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
        //
    }
}