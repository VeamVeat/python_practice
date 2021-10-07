import requests as r
import asyncio


async def save_image_cat(img_content_response, img_name):
    print("Сохранение изображения")

    with open(f"Cats/{img_name}", "wb") as file:
        file.write((await img_content_response).content)


async def get_image_cat(img_future):
    img_future = await img_future
    print(img_future, "Получение изображения")

    if img_future.status_code == 200:
        img_url: str = img_future.json()[0]["url"]
        img_name = img_url.split('/')[-1]

        await save_image_cat(loop.run_in_executor(None, r.get, img_url), img_name)


async def main(count_task: int):

    info_img_response = f'https://api.thecatapi.com/v1/images/search'

    task = [loop.create_task(get_image_cat(loop.run_in_executor(None, r.get, info_img_response)))
            for _ in range(count_task)]

    await asyncio.gather(*task)


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(5))

    except:
        pass
