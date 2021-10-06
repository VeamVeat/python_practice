import requests as r
import asyncio


async def get_images_cat(img_future):
    img_future = await img_future

    if img_future.status_code == 200:
        img_url: str = img_future.json()[0]["url"]

        img_name = img_url.split('/')[-1]

        img_content = r.get(img_url).content

        with open(f"Cats/{img_name}", "wb") as file:
            file.write(img_content)


async def main(count_task: int):

    task = [loop.create_task(get_images_cat(loop.run_in_executor(None,
                                                                 r.get,
                                                                 f'https://api.thecatapi.com/v1/images/search')))
            for _ in range(count_task)]

    await asyncio.gather(*task)


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(5))

    except:
        pass
