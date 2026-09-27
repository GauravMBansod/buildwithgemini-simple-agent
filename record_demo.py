import asyncio
import os
import time
from playwright.async_api import async_playwright

async def record_demo():
    output_dir = "/config/Desktop/Session1/simple-agent/assets"
    os.makedirs(output_dir, exist_ok=True)
    video_path = os.path.join(output_dir, "demo_recording.webm")

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            executable_path="/usr/bin/google-chrome",
            headless=True,
            args=["--no-sandbox", "--disable-setuid-sandbox"]
        )
        context = await browser.new_context(
            viewport={"width": 1280, "height": 800},
            record_video_dir=output_dir,
            record_video_size={"width": 1280, "height": 800}
        )
        page = await context.new_page()

        print("Navigating to http://localhost:8080...")
        await page.goto("http://localhost:8080/", wait_until="networkidle")
        await asyncio.sleep(2)

        # 1. First Prompt: Core pantry inventory check
        prompt_1 = "List my pantry inventory"
        print(f"Sending Prompt 1: '{prompt_1}'")
        await page.fill("#input", prompt_1)
        await page.click("button[type='submit']")

        # Wait for agent response
        await page.wait_for_selector(".msg.agent .bubble:not(:has-text('Thinking…'))", timeout=30000)
        await asyncio.sleep(4)

        # 2. Second Richer Prompt: Recipe suggestion + generated food image
        prompt_2 = "Suggest a recipe for dinner using my pantry items and generate a photo of the dish"
        print(f"Sending Prompt 2: '{prompt_2}'")
        await page.fill("#input", prompt_2)
        await page.click("button[type='submit']")

        # Wait for agent response & generated image card
        await page.wait_for_selector(".msg.agent .bubble:not(:has-text('Thinking…'))", timeout=45000)
        await asyncio.sleep(5)

        # Close context to finalize video recording
        await context.close()
        await browser.close()

        # Rename recorded video file to demo_recording.webm
        recorded_files = [f for f in os.listdir(output_dir) if f.endswith(".webm")]
        if recorded_files:
            latest_file = max([os.path.join(output_dir, f) for f in recorded_files], key=os.path.getmtime)
            print(f"Recorded video saved at: {latest_file}")
            return latest_file

if __name__ == "__main__":
    asyncio.run(record_demo())
