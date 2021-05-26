# Order
**Order** - заказ, который описывает поручение починки мастеру клиентом технику за определенную цену.  

## Поля сущности Order
  - Техника (technique models.ForeignKey(Technique, on_delete=models.CASCADE))
  - Мастер (master models.ForeignKey(Master, on_delete=models.CASCADE))
  - Услуга (price_list models.ForeignKey(PriceList, on_delete=models.CASCADE))
  - Статус выполнения (status_execution models.CharField(max_length=45))
  - Статус виновности (status_guilt models.CharField(max_length=45))
  - Примечание (note models.CharField(max_length=45))
  - Дата заказа (date_receipt models.DateTimeField)
