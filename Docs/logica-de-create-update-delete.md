```
Insert active:
created_at = now
updated_at = NULL
deleted_at = NULL
is_active = 1

Insert inactive:
created_at = now
updated_at = NULL
deleted_at = now
is_active = 0

Update active:
updated_at = now
deleted_at = NULL
is_active = 1

Update inactive:
updated_at = NULL
deleted_at = now
is_active = 0
```