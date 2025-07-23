import os
import falcon
import falcon.asgi
import uvicorn


class Index:
    async def on_get(self, req: falcon.Request, resp: falcon.Response):
        resp.content_type = "text/html"
        with open("index.html", "r", encoding="utf-8") as f:
            text = f.read()
            f.close()
        resp.content_length = len(text)
        resp.text = text


app = falcon.asgi.App()
app.add_route("/", Index())
app.add_static_route("/", os.getcwd())

if __name__ == "__main__":
    uvicorn.run("start_server:app", host="127.0.0.1", port=5000, reload=True)
