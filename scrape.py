import asyncio
from playwright.async_api import async_playwright

seeds = list(range(82, 92))
base_url = "https://sanand0.github.io/tdsdata/js_table/?seed="

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        grand_total = 0
        per_seed_totals = {}
        
        for seed in seeds:
            url = f"{base_url}{seed}"
            await page.goto(url)
            await page.wait_for_selector("#table table td")
            
            cell_texts = await page.eval_on_selector_all("#table table td", "elements => elements.map(el => el.textContent.trim())")
            numbers = [int(text) for text in cell_texts if text.isdigit()]
            seed_sum = sum(numbers)
            per_seed_totals[seed] = seed_sum
            grand_total += seed_sum
            print(f"Seed {seed} sum: {seed_sum}")
            
        await browser.close()
        
        print("\n==========================================")
        print("SUMMARY RESULTS PER SEED:")
        for seed, ssum in per_seed_totals.items():
            print(f"Seed {seed}: {ssum}")
        print(f"\nGRAND TOTAL SUM: {grand_total}")
        print("==========================================")

if __name__ == "__main__":
    asyncio.run(main())
