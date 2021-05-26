# Technique
**Technique** - техника, которую приносит клиент и чинит Мастер.  

## Поля сущности Technique
  - Модель техники (model_technique models.ForeignKey(ModelTechnique, on_delete=models.CASCADE))
  - Хозяин техники (customer models.ForeignKey(Customer, on_delete=models.CASCADE))
  - Дата создания (date_create models.DateField(null=True))
  - Дата окончания гарантии (date_end_guarantee models.DateField(null=True))
  - Фото техники (technique_photo models.ImageField)
