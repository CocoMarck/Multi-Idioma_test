using System.Collections.Generic;

// Logger
using Microsoft.Extensions.Logging;

// Essentials
using Repositories.LangTags;
using Entities.LangTags;

namespace Controllers.LangTags {
    public class LanguageController : ITableController
    {
        // Variables
        private LanguageRepository _repository;
        private ILogger _logger;
        private LanguageEntity _entity;

        // Constructor
        public LanguageController(
            LanguageRepository repository, LanguageEntity entity, ILogger logger)
        {
            _repository = repository;
            _entity = entity;
            _logger = logger;
        }

        // Methods
        public void Create(string code){
            try {
                bool exists = _repository.ExistsByCode(code);
                if (!exists){
                    _repository.Insert(code, true);
                    _logger.LogInformation($"Code inserted `{code}`");
                }
            } catch (Exception e){
                _logger.LogError(e, $"Error inserted `{code}`");
            }
        }

        public void Update(int id, string code){
            try {
                bool exists = _repository.ExistsById(id);
                if (!exists){
                    _repository.Update(id, code, true);
                    _logger.LogInformation($"Code updated `{code}`");
                }
            } catch (Exception e){
                _logger.LogError(e, $"Error updated `{code}`");
            }
        }

        public void Save(string code, bool isActive=true, int? languageId=null) {
            try {
                _repository.Save(
                    code:code, isActive:isActive, languageId:languageId
                );
            } catch (Exception e){
                _logger.LogError(e, $"Error saving: `{code}`");
            }
        }

        public void Delete(int id){
            try {
                bool exists = _repository.ExistsById(id);
                if (!exists){
                    _repository.Deactivate(id);
                    _logger.LogInformation($"Code deleted `{id}`");
                }
            } catch (Exception e){
                _logger.LogError(e, $"Error deleted `{id}`");
            }
        }

        public void Activate(int id){
            try {
                bool exists = _repository.ExistsById(id);
                if (!exists){
                    _repository.Activate(id);
                    _logger.LogInformation($"Code activated `{id}`");
                }
            } catch (Exception e){
                _logger.LogError(e, $"Error activated `{id}`");
            }
        }
        public string GetCodeById(int id){
            try {
                return _repository.GetCodeById(id);
            } catch {
                return "";
            }
        }
        public int GetIdByCode(string code){
            try {
                return _repository.GetIdByCode(code);
            } catch {
                return -1;
            }
        }

        public bool ExistsById(int id){
            return _repository.ExistsById(id);
        }

        public bool ExistsByCode(string code){
            return _repository.ExistsByCode(code);
        }

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

    }
}
