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
        public string GetLanguageCodeById(int id){
            return _repository.GetLanguageCodeById(id);
        }
        public string GetTagNameById(int id){
            return _repository.GetTagNameById(id);
        }
        public int GetTagIdByName(string name){
            try {
                return _repository.GetTagIdByName(name);
            } catch {
                return -1;
            }
        }
        public int GetLanguageIdByCode(string code){
            try {
                return _repository.GetLanguageIdByCode(code);
            } catch {
                return -1;
            }
        }
        public int GetIdByTagNameAndLanguageCode(string tagName, string languageCode){
            try {
                return _repository.GetIdByTagNameAndLanguageCode(tagName, languageCode);
            } catch {
                return -1;
            }
        }
        public void SaveByTagIdAndLanguageId(
            int tagId, int languageId, string value, bool isActive=true, int? translationId=null){
            try{
                _repository.SaveByTagIdAndLanguageId(tagId, languageId, value, isActive, translationId);
            } catch {
                return;
            }
        }
        public void SaveByTagNameAndLanguageCode(
            string tagName, string languageCode, string value, bool isActive=true, int? translationId=null){
            try{
                _repository.SaveByTagNameAndLanguageCode(tagName, languageCode, value, isActive, translationId);
            } catch {
                return;
            }
        }
        //
    }
}
