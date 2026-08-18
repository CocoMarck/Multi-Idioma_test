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
        public int GetIdByName(string name) {
            try {
                return _repository.GetIdByName(name);
            } catch {
                return -1;
            }
        }
        public void Delete(int id) {

        }
        public void Activate(int id){

        }
        public string GetNameById(int id){
            try {
                return _repository.GetNameById(id);
            } catch {
                return "";
            }
        }
        public bool ExistsById(int id){
            return _repository.ExistsById(id);
        }

        public bool ExistsByName(string name){
            return _repository.ExistsByName(name);
        }
        public void Save(string name, bool isActive=true, int? tagId=null) {
            try {
                _repository.Save(
                    name:name, isActive:isActive, tagId:tagId
                );
            } catch (Exception e){
                _logger.LogError(e, $"Error saving: `{name}`");
            }
        }
        //
    }
}
