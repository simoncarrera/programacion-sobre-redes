import _mysql_connector

datos = {
    "mail" : ""
}

conn = _mysql_connector.connect(
    host = "localhost",
    user = "",
    password = "",
    database = "chat",
)


cursor = conn.cursor()

query = "INSERT INTO users (email, power, created_at, update_at, deleted_at) VALUES ()"