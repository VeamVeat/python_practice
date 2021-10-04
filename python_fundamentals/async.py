import requests as r
import asyncio


async def get_images_cat(img_info):
    img_info = await img_info

    if img_info.status_code == 200:
        img_url: str = img_info.json()[0]["url"]

        img_file = img_url.split('/')[-1]
        img_name = img_file[:-4]
        img_expansion = img_file[-3:]

        img = r.get(f'{img_url}')

        with open(f"Cats/{img_name}.{img_expansion}", "wb") as o:
            o.write(img.content)


async def main(count_task: int):

    task = [loop.create_task(get_images_cat(loop.run_in_executor(None, r.get, f'https://api.thecatapi.com/v1/images/search'))) for _ in range(count_task)]
    await asyncio.gather(*task)


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(5))

    except:
        pass