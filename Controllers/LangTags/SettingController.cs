using System.Collections.Generic;

// Logger
using Microsoft.Extensions.Logging;

// Essentials
using Repositories.LangTags;
using Entities.LangTags;

namespace Controllers.LangTags {
    public class SettingController: ITableController {
        // Variables
        private SettingRepository _repository;
        private ILogger _logger;
        private SettingEntity _entity;

        // Constuctor
        public SettingController(
            SettingRepository repository, SettingEntity entity, ILogger logger){
            _repository = repository;
            _entity = entity;
            _logger = logger;
        }

        // ITableController IMethods
        public string[] GetColumnNames() {
            try {
                return _repository.Table.GetColumnNames();
            } catch {
                return new string[0];
            }
        }
        public List<string[]> GetRowValues(){
            try {
                return _repository.Table.GetRowValues();
            } catch {
                return new List<string[]>();
            }
        }
        public bool ExistsById(int id){
            return _repository.ExistsById(id);
        }
        public void Delete(int id){
            // No se necesita
        }
        public void Activate(int id){
            // No se necesita
        }
        // --------------------
    }
}