import asyncio
import uvicorn


async def app(scope, receive, send):
    assert scope['type'] == 'http'
    await send({
        'type': 'http.response.body',
        'body': b'Hello, from neo!',
    })


async def main():
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
