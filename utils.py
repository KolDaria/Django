from http.server import BaseHTTPRequestHandler

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    def do_GET(self) -> None:
        """
        Метод для обработки входящих GET-запросов
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("contacts.html", "r", encoding="utf-8") as file:
            data = file.read()
        self.wfile.write(bytes(data, "utf-8"))
