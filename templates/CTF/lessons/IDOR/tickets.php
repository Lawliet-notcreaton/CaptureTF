<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Обращение в тех. поддержку</title>
</head>
<body>
    <body>
    <div align="center">
    <h3> Создать обращение </h3>
    <hr style="width: 80%">
    <form method="POST">
        {% csrf_token %}
        {{form.topic}}<br>
        {{form.message}}<br>
        <button class='btn btn-success' type="submit">Отправить</button>
    </form>
    </div>
    <span>{{error}}</span>
    </body>
</body>
</html>




