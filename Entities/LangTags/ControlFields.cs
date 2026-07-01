namespace Entities.LangTags {
    public class ControlFields {
        // Propiedades
        public DateTime? CreatedAt { get; protected set; }
        public DateTime? UpdatedAt { get; protected set; }
        public DateTime? DeletedAt { get; protected  set; }
        public bool IsActive { get; protected set; }
    }
}