import asset_downloader_logic as logic

if __name__ == "__main__":
    # file must be in the same place as the script
    # or change to a route
    file_route = "traits.txt"

    # Blacklist: blacklist = ["particles/", "data/"]
    blacklist = []

    # URLs (read from file and filter)
    urls_list = logic.read_urls_from_file(file_route)
    filtered_list = logic.filter_urls(urls_list, blacklist)

    # if filtered
    print("Filtered URLs:")
    for url in filtered_list:
        print(url)

    print("\Downloading assets...")
    logic.download_assets_from_list(filtered_list, "assets_tft")
    print("Finished!")