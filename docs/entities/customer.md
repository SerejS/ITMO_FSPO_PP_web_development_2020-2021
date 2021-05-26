# Customer
**Customer** - клиент, который приходит в филиал ателье для ремонта своей техники.  

## Поля сущности Customer
  - Телефон клиента (customer_telephone models.CharField(max_length=45))
  - Тип клиента (customer_type models.CharField(max_length=45))
  - ФИО представителя (representative_full_name models.CharField(max_length=45))
  - ФИО начальника клиента (supervisor_full_name models.CharField(max_length=45))
  - ИНН клиента (customer_inn models.CharField(max_length=45))
  - Адрес клиента (customer_address models.CharField(max_length=45))
  - Район клиента (customer_distinct models.CharField(max_length=45))
  - Номер банковсского счета (customer_account_number models.CharField(max_length=45))