namespace Controllers.LangTags {
    public interface ITableController{
        string[] GetColumnNames();
        List<string[]> GetRowValues();
        bool ExistsById(int id);
        void Delete(int id);
        void Activate(int id);
    }
}