<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Информация</title>
</head>
<body>
    <h1>Детали тикета</h1>
    <p><strong>ID:</strong> {{ ticket.id }}</p>
    <p><strong>Тема:</strong> {{ ticket.topic }}</p>
    <p><strong>Сообщение:</strong> {{ ticket.message }}</p>
    <a href="{% url 'delete_ticket' pk=ticket.pk %}">Удалить обращение</a>
</body>
</html>
