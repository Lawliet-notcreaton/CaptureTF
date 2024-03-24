<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Тех. поддержка | Вход</title>
</head>
<body>
    <div align="center">
    <h3>Войти в личный кабинет</h3>

<form method="post" action="../">
    {% csrf_token %}

<div class="form-error">{{ form.non_field_errors }}</div>

{% for f in form %}
<p><label class="form-label" for="{{ f.id_for_label }}">{{f.label}}: </label>{{ f }}</p>
<div class="form-error">{{ f.errors }}</div>
{% endfor %}

    <button type="submit">Войти</button>
</form>
</div>
</body>
</html>



