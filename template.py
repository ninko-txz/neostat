ADMIN_CONSOLE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    table { border-spacing: .5rem }
    th { text-align: left }
    </style>
    <title>Neostat</title>
</head>
<body>
    <table>
        <tr>
            <th>Id</th>
            <th>Timestamp</th>
            <th>Path</th>
            <th>Address</th>
            <th>UserAgent</th>
            <th>Language</th>
        </tr>

        {% for log in access_logs %}
        <tr>
            <td>{{ log.id }}</td>
            <td>{{ log.created_at }}</td>
            <td>{{ log.path }}</td>
            <td>{{ log.x_forwarded }}</td>
            <td>{{ log.user_agent }}</td>
            <td>{{ log.languages }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""
