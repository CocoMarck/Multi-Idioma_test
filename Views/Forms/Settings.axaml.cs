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
            LoadCache();
            LoadTable();
        }
    }
}