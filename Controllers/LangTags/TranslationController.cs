using System.Collections.Generic;

// Logger
using Microsoft.Extensions.Logging;

// Essentials
using Repositories.LangTags;
using Entities.LangTags;

namespace Controllers.LangTags {
    public class TranslationController : ITableController
    {
        // Variables
        private TranslationRepository _repository;
        private ILogger _logger;
        private TranslationEntity _entity;

        // Constructor
        public TranslationController(
            TranslationRepository repository, TranslationEntity entity, ILogger logger)
        {
            _repository = repository;
            _entity = entity;
            _logger = logger;
        }

        // Interface Methods
        public string[] GetColumnNames() {
            try {
                return _repository.Table.GetColumnNames();
            } catch
            {
                return new string[0];
            }
        }
        public List<string[]> GetRowValues(){
            try {
                return _repository.Table.GetRowValues();
            } catch
            {
                return new List<string[]>();
            }
        }
        public bool ExistsById(int id){
            return true;
        }
        public void Delete(int id) {

        }
        public void Activate(int id){

        }
    }
}
