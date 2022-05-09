import os
import requests
import asyncio

os.makedirs(os.path.dirname('Cats/'), exist_ok=True)


async def download_img():
    image_json = loop.run_in_executor(None, requests.get, 'https://api.thecatapi.com/v1/images/search')
    url_img = (await image_json).json()[0]['url']
    print(f'Получение {url_img}')
    return url_img


async def save_img(url_img, img_name, img_extension):
    response = loop.run_in_executor(None, requests.get, url_img)
    img = (await response).content
    print(f'Сохранение {img_name}.{img_extension}')
    with open(f"Cats/{img_name}.{img_extension}", "wb+") as f:
        f.write(img)


async def get_cat_img():
    url_img = await download_img()

    img = url_img.split('/')[-1]
    img_name = img.split('.')[0]
    img_extension = img.split('.')[-1]

    await save_img(url_img, img_name, img_extension)


async def create_tasks_func(count_img: int):
    tasks = [asyncio.create_task(get_cat_img()) for _ in range(count_img)]
    await asyncio.wait(tasks)


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(create_tasks_func(10))
        loop.close()
    except:
        pass

