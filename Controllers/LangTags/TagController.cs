using System.Collections.Generic;

// Logger
using Microsoft.Extensions.Logging;

// Essentials
using Repositories.LangTags;
using Entities.LangTags;

namespace Controllers.LangTags {
    public class TagController : ITableController
    {
        // Variables
        private TagRepository _repository;
        private ILogger _logger;
        private TagEntity _entity;

        // Constructor
        public TagController(
            TagRepository repository, TagEntity entity, ILogger logger)
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
