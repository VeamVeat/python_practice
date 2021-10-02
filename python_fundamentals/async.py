import requests as r
import asyncio


async def get_images_cat():

    header = {'x-api-key': 'bd847905-bc01-4650-ab52- ace3247ee273'}
    img_info = r.get('https://api.thecatapi.com/v1/images/search', headers=header)
    img_url: str = img_info.json()[0]["url"]

    img_file = img_url.split('/')[-1]
    img_name = img_file[:-4]
    img_expansion = img_file[-3:]

    img = r.get(f'{img_url}', headers=header)

    out = open(f"Cats/{img_name}.{img_expansion}", "wb")
    out.write(img.content)
    out.close()


async def main(count_task: int):

    task = [loop.create_task(get_images_cat()) for _ in range(count_task)]
    await asyncio.wait(task)


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(2))

    except:
        pass

