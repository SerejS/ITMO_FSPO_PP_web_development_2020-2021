# Master
**Master** - мастер, который чинит технику, которую приносит клиент.  

## Поля сущности Master
  - ФИО мастера (master_full_name models.CharField(max_length=45))
  - Номер страховки (insurance_number models.CharField(max_length=45))
  - Телефон мастера (master_phone models.CharField(max_length=45))
  - Номер паспорта (mater_passport models.CharField(max_length=45))
  - Квалификация мастера (master_qualification models.CharField(max_length=45))
  - Опыт работы (work_experience models.IntegerField())
  - Сумма штрафов (sum_amount fine models.IntegerField())
